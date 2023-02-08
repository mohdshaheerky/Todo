from django.shortcuts import render,redirect
from. models import *
from.form import PostForm

# Create your views here.

def home(request):
    return render(request,'index.html')


def home(request):
    todo=Todo.objects.all()
    context={'Todo':todo}
    return render(request,'index.html',context)

def createpost(request):
    form =PostForm()
    if request.method == 'POST':
        form =PostForm(request.POST)
        if form.is_valid():
            post =form.save()
            post.save()
            return redirect ('home')
    context={'form':form}
    return render (request,'createpost.html',context)

def deletepost(request,pk):
    todo=Todo.objects.get(id=pk)   
    todo.delete()
    return redirect('home')

def updatepost(request,pk):
    post = Todo.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form =PostForm(request.POST,instance=post)
        if form.is_valid():
            post =form.save()
            post.save()
            return redirect ('home')
    context={'form':form}
    return render (request,'createpost.html',context)