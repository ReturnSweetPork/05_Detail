from django.shortcuts import render,redirect
from django.template import RequestContext
# Create your views here.
def list(request):
    return render(request,"detail/list.html")
    
def mypage(request):
    return render(request,"detail/mypage.html")
    
def qna(request):
    return render(request,"detail/qna.html")
    
def signup(request):
    return render(request,"detail/signup.html")
    
def page(request, not_found):
    return render(request,"detail/page.html", {'not_found':not_found})    
    
    
    

    