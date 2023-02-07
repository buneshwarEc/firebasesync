from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
import json
import pyrebase


config = {
  "apiKey": "AIzaSyBsKZp6f3oJoqkBKVd2X15reohrfQrbsss",
  "authDomain": "fir-sync-a3379.firebaseapp.com",
  "databaseURL": "https://fir-sync-a3379-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "fir-sync-a3379",
  "storageBucket": "fir-sync-a3379.appspot.com",
  "messagingSenderId": "139882003184",
  "appId": "1:139882003184:web:6bd92db1645a5dbbbf6035",
  "measurementId": "G-8TSYGWRE3G"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()





# Create your views here.

#create update delete patch using genric api viewset







class StudentView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'
  

    def get_queryset(self):
       return Student.objects.all()


    def get(self, request, id=None):

        if id:
            return self.retrieve(request, id)
        else:
            fetchResponse=db.child("Student").get()
            print(fetchResponse.val())
            return self.list(request)

    def delete(self, request, id=None):
        return self.destroy(request, id)

    def post(self, request):
        data= self.create(request)
        firebaseRepsonse=json.dumps(db.child("Student").push(data.data))
        print(firebaseRepsonse)

        return Response({"data":data.data,})


    def put(self, request, id=None):
        return self.update(request, id)

    def patch(self,request, id =None):
        return self.partial_update(request,id)


