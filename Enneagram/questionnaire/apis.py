from django.shortcuts import render,HttpResponse
import json

def save(request):
    if request.method=="POST":
        ops = dict(request.POST)
        csrfmiddlewaretoken = ops.pop('csrfmiddlewaretoken')
        current = ops.pop('current')[0]
        print (ops)
        
    return HttpResponse(json.dumps({"m":"debug"}))
    