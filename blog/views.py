from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    
    return render(request,'blog/index.html')

def Post(request):
    if request.session.has_key('blogid'):
        posts=post.objects.all()
        return render(request, 'blog/post.html' ,{'posts':posts})
    else:
        return redirect('login')
    
def addpost(request):
    if request.session.has_key('blogid'):
        if request.method == "POST" :
            form = postForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/blog')
        else :
            form = postForm() 
            return render(request,'blog/addpost.html',{'form':form})
    else:
        return redirect('login')


def login(request):
    if request.session.has_key('blogid'):
        return redirect('blog')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['blogid'] = user.id
                return redirect('blog')
            else:
                msg = "username or password invalide"
                return render(request,'blog/login.html',{'msg':msg})
        else:
            return render(request,'blog/login.html')
# Create your views here.
def logout(request):
    if not request.session.has_key('blogid'):
        return redirect('login')
    try:
        del request.session['blogid']
        return redirect('login')
    except:
        pass
    
def register(request):
    if request.session.has_key('blogid'):
        return redirect('blog')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user  = User.objects.filter(username=username)
            if user:
                msg = "Username already in use"
                return render(request, 'blog/signup.html',{'msg':msg})
            else:
                user = User()
                user.username = username
                user.password = password
                user.save()
                request.session['blogid'] = user.id
                return redirect('blog')
        else:
            return render(request,'blog/signup.html',)