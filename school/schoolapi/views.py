from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FormParser
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#login Page in HTML
def LoginPage(request):
        return render(request , 'studentapi/login.html')

class Login(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        # import pdb; pdb.set_trace()
        if user is not None:
            login(request, user)
            return Response({'message':'success'}, status=status.HTTP_200_OK)

        return Response({'message': 'login failed'}, status=status.HTTP_400_BAD_REQUEST)


#DepartmentApi()
def departmentApi(request):
	if request.method == 'GET':
		department = Department.objects.all()
		serializer = DepartmentSerializer(department, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = DepartmentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
#End departmentApi

#courseApi()
def courseApi(request):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	if request.method == 'GET':
		if request.GET.get('name'):
			print(request.GET.get('name'))
			course = Course.objects.filter(name=request.GET.get('name'))
		elif request.GET.get('duration'):
			print(request.GET.get('duration'))
			course = Course.objects.filter(duration__gte=request.GET.get('duration'))
		else:
			course = Course.objects.all()
		serializer = CourseSerializer(course, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		print(data)
		serializer = CourseSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
#End courseApi
