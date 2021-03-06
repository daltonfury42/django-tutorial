from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	print(latest_question_list)
	context = {
		latest_question_list : 'latest_question_list'
	}
	return render(request, 'polls/index.html', context)		

def detail(request, question_id):
	return HttpResponse("You are looking at the details of %s." % question_id)

def results(request, question_id):
	return HttpResponse("You are looking at the results of %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on %s." % question_id)