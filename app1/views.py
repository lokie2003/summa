from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import table1
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def sample(request):

    return HttpResponse("ram loki")
def sample2(request):
    data=table1.objects.all()
    return render(request,'index.html',{'data':data})
def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render())
@csrf_exempt
def addrecord(request):
    x=request.POST["first"]
    y=request.POST["last"]
    t=table1(firstname=x,lastnmae=y)
    t.save()
    return HttpResponseRedirect(reverse('sample2'))
def delete(request,id):
    t=table1.objects.get(id=id)
    t.delete()
    return HttpResponseRedirect(reverse('sample2'))
