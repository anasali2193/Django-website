from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question
# Create your views here.

#note 
#request is pass whenever you do anything

#this function will display whatever in the index()
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#in this case the id is the PK
def details(request, question_id):
    return HttpResponse("you are looking at question %s." %question_id)

def results(request, question_id):
    response = "you are looking at results of qstn %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you are waiting on qstn %s. " % question_id)

