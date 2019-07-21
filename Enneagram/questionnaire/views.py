from django.shortcuts import render,HttpResponse
from .models import Question

def index(request):
    questions = Question.objects.order_by('qid')[:3]
    completed = {"current":2,"questions":['q1a','q2b']} ## 已完成
    return render(request,'qindex.html',{"questions":questions,"completed":completed})