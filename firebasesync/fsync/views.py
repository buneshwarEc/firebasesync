from django.shortcuts import render

import pyarbase


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


