from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from home.models import Blogpost
from home.serializers import BlogpostSerializer


def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return render(request,'login.html')


def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request,'blogpage.html')
        else:
            return render(request, 'login.html')

def insert(request):
    if request.method=='POST':

        a=request.POST.get('date')
        b=request.POST.get('blog')
        Blogpost.objects.create(date=a,post=b)
        return render(request,'blogpage.html')


@csrf_exempt
def blogposts(request):
    if request.method=='GET':
        obj=Blogpost.objects.all()
        serializerobj=BlogpostSerializer(obj,many=True)
        return JsonResponse(serializerobj.data,safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=BlogpostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@api_view(['GET','PUT'])
def blogpst(request,id):
    # try:
    #     blg=Blogpost.objects.get(id=id)
    # except blg.DoesNotExists:
    #     return HttpResponse(status=404)
    blg = Blogpost.objects.get(id=id)
    if request.method=='GET':
        serializer=BlogpostSerializer(blg)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=BlogpostSerializer(blg,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)