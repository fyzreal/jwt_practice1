from rest_framework import serializers 
from .models import Student, Category, Book
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'
        # exclude = ['id']

    def validate(self, data):
        if data['age']<18 :
            raise serializers.ValidationError({'error':'age cannot be less then 18'})
        if data['name']:
            for n in  data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'name cannot contain numbers'})
        # if data['fathers_name']
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category_name = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'

