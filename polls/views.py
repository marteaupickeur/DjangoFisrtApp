from django.shortcuts import render
from django.http import HttpResponse

from .serializers import ChoiceSerializer, QuestionSerializer
from .models import Choice, Question
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


def index(request):
    latest_question_list = Question.objects.all()
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("you are looking at questions: {}".format(question_id))

def results(request, question_id):
    return HttpResponse("you are looking at results of qustion: {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("you are voting at questions: {}".format(question_id))


class QuestionViewSet(viewsets.ModelViewSet):
    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated, )
    

class ChoiceViewSet(viewsets.ModelViewSet):
    
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (IsAuthenticated, )
