from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from Platforms.models import  Command
from django.contrib.auth import get_user_model 
User = get_user_model()

def upload_location(instance, filename):
    filebase, ext = filename.split('.')
    return "media/{}/{}/{}.{}".format(instance.name, 'icon', instance.name, ext)


def upload_location_ss(instance, filename):
    filebase, ext = filename.split('.')
    return "media/{}/{}/{}.{}".format(instance.Software, 'ScreenShot', instance.Software, ext)





class ScreenShot(models.Model):
    Software = models.CharField(max_length=100,blank=False,null=True)
    icon = models.ImageField(
        width_field="width_field",
        height_field="height_field",
        upload_to=upload_location_ss)
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.Software



class Category(MPTTModel):
    sname = models.CharField(max_length=100, blank=False, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE
            ,related_name='children', db_index=True)
    slug = models.SlugField(blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['sname']

    class Meta:
        verbose_name_plural = u"Categories"

    def __str__(self):
        return self.sname

    @property
    def title(self):
        return self.sname


class Comment(MPTTModel):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Developer = models.ForeignKey('SoftwareData.Developer',on_delete=models.CASCADE, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    Software = models.ForeignKey('SoftwareData.Software', on_delete=models.CASCADE)
    html_comment = models.TextField(blank=True)
    offical = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.html_comment


class Developer(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.URLField()
    email = models.EmailField()
    address = models.TextField(blank=True)
    Software = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class SoftwareQuerySet(models.query.QuerySet):
    pass


class SoftwareManager(models.Manager):
    pass


class platform(models.Model):
    platform = models.CharField(max_length=250)
    def __str__(self):
        return self.platform


class Software(models.Model):

    name = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    version = models.CharField(max_length=250)
    weburl = models.URLField()
    description = models.TextField()
    icon = models.ImageField(
        width_field="width_field",
        height_field="height_field",
        upload_to=upload_location)

    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    offical = models.BooleanField(default=False)
    total_downloads = models.IntegerField(default=0, blank=True)
    verified = models.BooleanField(default=False)
    category = TreeForeignKey('Category', on_delete=models.CASCADE,null=True, blank=True, db_index=True)
    ratings = models.IntegerField(blank=True,null=True)
    whats_new = models.TextField(null=True, blank=True,)
    
    Tag = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(null=True, blank=True)
    objects = SoftwareManager()
    # Command = models.ManyToManyField(Command,blank=True,null=True)
    # class Meta:
    #     ordering = ('-ratings__average',)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        print('software/' + self.slug)
        return ('software/' + self.slug)


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def rl_post_save_receiver(sender, instance, *args, **kwargs):
    pass


pre_save.connect(rl_pre_save_receiver, sender='SoftwareData.Software')
pre_save.connect(rl_pre_save_receiver, sender='SoftwareData.Category')
post_save.connect(rl_post_save_receiver, sender='SoftwareData.Software')
