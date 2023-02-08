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
from .fire import fire

""" send to firebase""" 

import firebase_admin
from firebase_admin import credentials

# cred = credentials.Certificate("./fir-sync-a3379-firebase-adminsdk-m10u0-ce74ad8e70.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()



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
            fetchResponse=db.child("Student").child(id).get()
            data=fetchResponse.val()
            jdata=json.dumps(data)
            print("data from Firebase using id",id)
            print(jdata,type(jdata))
            return self.retrieve(request, id)
        else:
            fetchResponse=db.child("Student").get()
            data=fetchResponse.val()
            jdata=json.dumps(data)
            print("data from Firebase using all")
            print(jdata,type(jdata))
            return self.list(request)

    def delete(self, request, id=None):
        responsefirebase=db.child("Student").child(id).remove()
        print("Record Deleted in firebase",responsefirebase)
        return self.destroy(request, id)

    def post(self, request):
        data= self.create(request)
        id=data.data['id']
        #firebaseRepsonse=json.dumps(db.child("Student").child(id).push(data.data))
        firebaseRepsonse=json.dumps(db.child("Student").child(id).set(data.data))
        #frdbb=db.collection('Student').document(id).create(data.data)
        #print(frdbb)
        print("Record Created from firebase",firebaseRepsonse)
        fire()
        return Response({"data":data.data,})


    def put(self, request, id=None):
        data=self.update(request, id)
        print(data.data)
        updatefirebase=db.child("Student").child(id).update(data.data)
        print("update response from firebase",updatefirebase)
        return data

    def patch(self,request, id =None):
        data=self.partial_update(request, id)
        print(data.data)
        updatefirebase=db.child("Student").child(id).update(data.data)
        print("patch response from firebase",updatefirebase)
        return data


