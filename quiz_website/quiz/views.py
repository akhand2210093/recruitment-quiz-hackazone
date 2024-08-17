from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import User, Question, Answer, UserResponse, Leaderboard
from .serializers import (
    UserSerializer, QuestionSerializer, AnswerSerializer, 
    UserResponseSerializer, LeaderboardSerializer
)

# Login API (or Create User)
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        student_number = data.get('student_number')
        email = data.get('email')
        name = data.get('name')

        user, created = User.objects.get_or_create(
            student_number=student_number,
            defaults={'email': email, 'name': name}
        )
        if not created and user.email != email:
            return Response({'detail': 'Invalid email.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View to add questions and answers
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        question_data = request.data.get('question')
        answers_data = request.data.get('answers')

        question = Question.objects.create(**question_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)

        serializer = self.get_serializer(question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# View all questions
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Submit all responses at once
class SubmitResponseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        responses = request.data.get('responses', [])
        user = request.user
        score = 0
        
        for response in responses:
            question = get_object_or_404(Question, id=response['question_id'])
            answer = get_object_or_404(Answer, id=response['answer_id'])
            
            UserResponse.objects.create(user=user, question=question, answer=answer)
            
            if answer.is_correct:
                score += 4
            else:
                score -= 1

        leaderboard, created = Leaderboard.objects.get_or_create(user=user)
        leaderboard.score = score
        leaderboard.save()

        return Response({'score': score}, status=status.HTTP_200_OK)

# View user score
class UserScoreView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LeaderboardSerializer

    def get_object(self):
        return get_object_or_404(Leaderboard, user=self.request.user)

# View leaderboard
class LeaderboardView(generics.ListAPIView):
    queryset = Leaderboard.objects.all().order_by('-score')
    serializer_class = LeaderboardSerializer

