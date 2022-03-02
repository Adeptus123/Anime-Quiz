from django.http import HttpResponse
from  django.shortcuts import render

def index(request):
    return render(request,'index.html')
def result(request):
    name=request.POST.get('name',"no name")
    a1=request.POST.get('q1correct','no')
    a2=request.POST.get('q2correct','no')
    a3=request.POST.get('q3correct','no')
    a4=request.POST.get('q4correct','no')
    a5=request.POST.get('q5correct','no')
    correcta=[a1,a2,a3,a4,a5]
    score=0
    for char in correcta:
        if char=='on':
            score=score+1
    params={'name':name,'score':score}
    return render(request,'result.html',params)