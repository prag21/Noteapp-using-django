
from django.http.response import HttpResponse
from note import models
from django.http import request
from django.shortcuts import redirect, render
from django.views import View

class sign(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        error=''
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        c1=models.Customer(username=username,password=password,email=email)
        if c1.get1():
            error="Username already exists"
        if c1.get2():
            error="Email already exists"
        if len(password)<8:
            error="Weak Password"
        if error=='':
            c1.save()
            return redirect('base')  
        else:
            return render(request,'signup.html',{'error':error})
def base(request):
    return render(request,'home.html')
class login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        error=None
        email=request.POST.get('email')
        password=request.POST.get('password')
        c=models.Customer.get3(email,password)
        if c:
            request.session['id']=c.id;
            print(request.session.get('email'))
            return redirect('base')
        else:
            error="Email and password doesnot match"
            return render(request,'login.html',{'error':error})
def logout(request):
    request.session.clear()
    return redirect('base')
class note(View):
    def get(self,request):
        user=request.session.get('id')
        c=models.Todo.get5(user=user)
        return render(request,'note.html',{'c':c})
       
    def post(self,request):
     
        user=request.session.get('id')
        c=models.Todo.get5(user=user)
        title=request.POST.get('title')
        status=request.POST.get('status')
        priority=request.POST.get('priority')
        i=request.POST.get('id1')
        i1=request.POST.get('id2')
        if i:
            n=models.Todo.get6(i)
            n.delete()
            return redirect('note')
        if i1:
            n=models.Todo.get6(i1)
            return render(request,'edit.html',{'n':n})
        error=None
        if not title:
            error="No Title"
        if not status:
            error="No Status"
        if not priority:
            error="No Priority"
        if error:
            return render(request,'note.html',{'c':c,'error':error})
        else:
            t=models.Todo(user=models.Customer(user),title=title,status=status,priority=priority)
            t.save()
            return redirect('note')
class edit(View):
    def get(self,request):
        return render(request,'edit.html')
    def post(self,request):
        user=request.session.get('id')
        title=request.POST.get('title')
        status=request.POST.get('status')
        priority=request.POST.get('priority')
        w=request.POST.get('id2')
        t=models.Todo.get6(w)
        t1=models.Todo(user=models.Customer(user),title=title,priority=priority,status=status)
        t1.save()
        t.delete()
       
   
        return redirect('note')

        






