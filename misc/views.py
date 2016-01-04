from django.shortcuts import render, redirect

# Create your views here.

def app_download(request):
    return redirect("/media/download/app/latest.apk")
