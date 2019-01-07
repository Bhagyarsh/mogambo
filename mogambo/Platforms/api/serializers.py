from rest_framework import serializers
from Platforms.models import Command,PackageManager,OsVersion,Linux



class PackageManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = PackageManager
        fields = [
            "name",
            "downloads"
        ]

class Linuxserializers():

    class Meta:
        model = Linux
        lookup_field = 'pk'
        fields = [
            "OsName",
            "BaseDistro"
        ]

class OsVersionSerializers(serializers.ModelSerializer):
    OsName = Linuxserializers()

    class Meta:
        lookup_field = 'pk'
        model = OsVersion
        fields = [
            "OsName",
            "Osversion"
        ]


class CommandSerializers(serializers.ModelSerializer):
    PackageManager = PackageManagerSerializers()
    OsVersion = OsVersionSerializers()
    class Meta:
        model = Command

        lookup_field = 'pk'
        fields = [
            'pk',
            'OsVersion',
            'PackageManager',
            "working",
            "command",
            "command2",
            "success",
            "verified",
            "timestamp",
            "fails",
            "downloads"

        ]
