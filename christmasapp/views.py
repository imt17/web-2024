from datetime import datetime

from django.shortcuts import render

def index(request):
    today = datetime.now()
    answer = today.month == 12 and today.day == 25
    return render(request, "index.html", {'answer':answer})
