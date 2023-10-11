from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
    def save(self):
        user = User(username=self.validated_data['username'],first_name=self.validated_data['first_name'],last_name=self.validated_data['last_name'],email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']
    def update(self,instance,validated_data):
        instance.title = validated_data.get('first_name', instance.first_name)
        instance.code = validated_data.get('last_name', instance.last_name)
        instance.linenos = validated_data.get('email', instance.email)
        instance.save()
        return instance
