from rest_framework import serializers
from .models import User, Question, Answer, UserResponse, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['student_number', 'email', 'name']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'section', 'text', 'correct_answer']  # Only include the correct answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'text', 'is_correct']

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['user', 'question', 'answer']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Leaderboard
        fields = ['user', 'score']
