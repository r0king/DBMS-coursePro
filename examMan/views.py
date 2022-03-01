from datetime import datetime
from django.http import HttpResponse
from .models import Exam
from django.shortcuts import render  

import pytz
def index(request):
    exams = Exam.objects.filter(time__gte=datetime(2013, 11, 20, 20, 9, 26, 423063,tzinfo=pytz.UTC))
    context = {
        "data":exams
    }
    return render(request,"index.html",context)