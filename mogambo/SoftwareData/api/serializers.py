from rest_framework import serializers
from SoftwareData.models import Software,Tag,ScreenShot,Category
from Platforms.api.serializers import CommandSerializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        lookup_field = 'pk'
        fields = [
            "name",
            "parent"
        ]


class ScreenShotSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScreenShot
        lookup_field = 'pk'
        fields = [
            "icon"
        ]

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        lookup_field = 'pk'
        fields = [
            "name"
        ]
class SoftwareSerializers(serializers.ModelSerializer):
    Command = CommandSerializers(many=True)
    Tag = TagSerializers(many=True)
    category = CategorySerializers()
    ScreenShot = ScreenShotSerializers(many=True)
    class Meta:
        model = Software
        lookup_field = 'slug'
        fields = [
            "name",
            "user",
            "version",
            "weburl",
            "description",
            "icon",
            "timestamp",
            "updated",
            "offical",
            "total_downloads",
            "verified",
            "category",
            "whats_new",
            "ScreenShot",
            "Tag",
            "slug",
            "Command",
        ]

class SoftwareListSerializers(serializers.ModelSerializer):
    Tag = TagSerializers(many=True)
    category = CategorySerializers()
    class Meta:
        model = Software
        lookup_field = 'slug'
        fields = [
            "name",
            "version",
            "weburl",
            "description",
            "offical",
            "total_downloads",
            "category",
            "whats_new",
            "Tag",
            "slug",
        ]
