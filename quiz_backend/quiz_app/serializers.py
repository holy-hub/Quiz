from rest_framework import serializers # , viewsets
from .models        import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'date_joined']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'desc', 'time',]

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Quiz
        fields = ['id', 'creator', 'category', 'question', 'proposition', 'proposition1', 'proposition2', 'response', 'level', 'valeur']

    def create(self, validated_data):
        quiz = Quiz.objects.create(**validated_data)
        return quiz

    def update(self, instance, validated_data):
        instance.creator      = validated_data.get('creator', instance.creator)
        instance.category     = validated_data.get('category', instance.category)
        instance.question     = validated_data.get('question', instance.question)
        instance.proposition  = validated_data.get('proposition', instance.proposition)
        instance.proposition1 = validated_data.get('proposition1', instance.proposition1)
        instance.proposition2 = validated_data.get('proposition2', instance.proposition2)
        instance.response     = validated_data.get('response', instance.response)
        instance.level        = validated_data.get('level', instance.level)
        instance.valeur       = validated_data.get('valeur', instance.valeur)
        instance.created_at   = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Score
        fields = ['id', 'Player', 'category', 'level', 'score', 'created',]
    
    def create(self, validated_data):
        score = Score.objects.create(**validated_data)
        return score
    
    def update(self, instance, validated_data):
        instance.Player   = validated_data.get('Player', instance.Player)
        instance.category = validated_data.get('category', instance.category)
        instance.level    = validated_data.get('level', instance.level)
        instance.score    = validated_data.get('score', instance.score)
        instance.created  = validated_data.get('created', instance.created)
        instance.save()
        return instance
    
""" 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
"""