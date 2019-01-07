# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework_jwt.settings import api_settings
import datetime
from django.utils import timezone
from rest_framework.views import exception_handler
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# payload = jwt_payload_handler(user)
# token = jwt_encode_handler(payload)


expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'firstname','lastname')

class UserRegisterSerializer(serializers.ModelSerializer):
    expires= serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(
        style={'input_type':'password'},
        write_only=True
    )
    # password2 = serializers.CharField(
    #     style={'input_type':'password'},
    #     write_only=True
    # )
    class Meta:
        model = User
        fields = ('email', 'firstname','lastname' ,'password','token','expires')
        extra_kwargs = {'password':{'write_only':True}}
    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token
    def get_expires(self,obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    # def validate(self,data):
    #     pw = data.get("password")
    #     pw2 = data.pop("password2")

    #     if pw != pw2:
    #         raise serializers.ValidationError("Password must match ")
    #     return data
    # def validate_email(self,value):
    #     qs = User.objects.filter(email__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("Password must match ")
    #     return data
