from rest_framework import serializers
from SoftwareData.models import Software,Tag,ScreenShot,Category
from Platforms.api.serializers import CommandSerializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.api.jwt.serializers import UserPublicSerializer


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'


class ScreenShotSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScreenShot
        lookup_field = 'pk'


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        lookup_field = 'pk'
        fields = [
            "name"
        ]
class SoftwareSerializers(serializers.ModelSerializer):

    Tag = TagSerializers(many=True)
    category = CategorySerializers()
    user = UserPublicSerializer()
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

            "Tag",
            "slug",

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

class SoftwareRUDSerializers(serializers.ModelSerializer):
    Tag =  serializers.PrimaryKeyRelatedField(queryset = Tag.objects.all(),
                                                many=True)
    category =  serializers.SlugRelatedField(queryset = Category.objects.all(),
                        slug_field='sname')
    # user = serializers.PrimaryKeyRelatedField(queryset = User.objects.get(pk),
    #                                             many=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        depth = 4
        model = Software
        lookup_field = 'slug'
        fields = [
            "name" ,
            "user",
            "version",
            "weburl",
            "description" ,
            "icon", 
            "width_field" ,
            "height_field",
            "offical" ,
            "total_downloads" ,
            "verified", 
            "category",
            "ratings" ,
            "whats_new" ,
            "Tag" ,

            ]
        extra_kwargs = {
                "category":{'validators': []}, 
                "ScreenShot":{'validators': []},
                
            }

    # def get_result(self, obj):
    #     print(obj)
    #     return "some result"