from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class MypjApiView(APIView):
    serializer_project= MypjSerializer
    def get(self,request):
        info  = Mypj.objects.all().values()
        return Response({"Your Account Info": info})

    def post(self,request):
        serializer_post_project=MypjSerializer(data=request.data)
        if(serializer_post_project.is_valid()):
            Mypj.objects.create(
                            name=serializer_post_project.data.get("name"),
                            age=serializer_post_project.data.get("age"),
                            )

        project = Mypj.objects.all().filter(name=request.data["name"]).values()
        return Response({"Notification": "Your information is Added!", "Project": project})