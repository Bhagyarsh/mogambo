from django.db import models
from django.contrib.auth import get_user_model 
from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()
class platform(models.Model):
    platform = models.CharField(max_length=250)

    def __str__(self):
        return self.platform


class PackageManager(models.Model):
    name = models.CharField(max_length=250)
    downloads = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name


class Linux(models.Model):
    BaseDistro = models.ForeignKey(PackageManager, on_delete=models.CASCADE)
    OsName = models.CharField(max_length=250)

    def __str__(self):
        return self.OsName


class OsVersion(models.Model):
    osandversion = ''
    OsName = models.ForeignKey(Linux, on_delete=models.CASCADE)
    Osversion = models.CharField(max_length=250)

    def __str__(self):
        osandversion = str(self.OsName) + str(self.Osversion)
        return osandversion


class Error(models.Model):
    BaseDistro = models.ForeignKey(
        OsVersion, on_delete=models.CASCADE, related_name="errors")
    error = models.TextField()


class ErrorComment(MPTTModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    os = models.ForeignKey(Linux, on_delete=models.CASCADE)
    software = models.ForeignKey('SoftwareData.Software', on_delete=models.CASCADE,
                                 blank=True)
    html_comment = models.TextField(blank=True)
    error = models.TextField()
    offical = models.BooleanField(default=False)
    Spam = models.BooleanField(default=False, blank=True)
    helpfull = models.BooleanField(default=False, blank=True)
    unHelpfull = models.BooleanField(default=False, blank=True)
    reply = models.ManyToManyField("self",  blank=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.html_comment


class Command(models.Model):
    OsVersion = models.ForeignKey(OsVersion, on_delete=models.CASCADE)
    PackageManager = models.ForeignKey(PackageManager,on_delete=models.CASCADE)

    working = models.BooleanField(blank=True)
    command = models.TextField()
    command2 = models.TextField(blank=True)
    success = models.IntegerField(default=0, blank=True)
    verified = models.BooleanField()
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    fails = models.IntegerField(default=0, blank=True)
    downloads = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.command
