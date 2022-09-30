from django.shortcuts import render
from django.http import HttpResponse

def link(request):
  return render(request, 'linktree.html') 


