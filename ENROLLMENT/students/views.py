from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
  return HttpResponse("DIS THE STUDENTS")

def BSTI(request):
  return HttpResponse('BSIT')

def BSPA(request):
  return HttpResponse('BSPA')

def BSA(request):
  return HttpResponse('BSA')

def BSE(request):
  return HttpResponse('BSE')
