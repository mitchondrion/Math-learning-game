from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Question, Result
from .serializers import QuestionSerializer, ResultSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer