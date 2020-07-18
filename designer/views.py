from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import designerProfile
from .forms import ProfilesForm


# Create your views here.
def log(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        
        user1 = authenticate(request, username = username , password = password)
        if user1 is not None:
            return render(request,"designer/index.html")
        else:
            print("fail")

    return render(request,"designer/login.html")

def registration(request):
    usrname=request.POST.get("username")
    firname=request.POST.get("firstname")
    lasname=request.POST.get("lastname")
    password=request.POST.get("password")
    confirmpassword=request.POST.get("confirmpassword")
    mail=request.POST.get("mail")
    categ=request.POST.get("category")
    brandname=request.POST.get("brandname")
    about=request.POST.get("about")
    # print("username:"usrname)
    return render(request,"designer/success.html",{'username':usrname,'category':categ,'firstname':firname,'lastname':lasname,'password':password,'confirmpassword':confirmpassword,'mail':mail,'brandname':brandname,'about':about})


def reqregister(request):
    dic={}
    print("inside reqregister method")
    form = CreateUserForm()
    context = {'form':form}
    if request.method == 'POST':  
        form = CreateUserForm(request.POST)
        print("252")  
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            print(user,email)
            return redirect('createprofile')
        else:
            print("epty")
            
            # context.update({"value":"fail"})
            # return render(request,"designer/register.html",context)
            #check whether its printing in console
             
            messages.info(request,'Failed')
       
    
    print(context)
    return render(request,"designer/register.html",context)#change here spelling pothum run pannu phone off call panrem 


def indexreq(request):
    return render(request,"designer/index.html")

def profilereq(request):
    return render(request,"designer/profile.html")

def createprofile(request):
    # username=request.user
    form = ProfilesForm()
    if request.method == 'POST':
        
        print("inside create if")
        print(request.POST.get("FirstName"))
        print(request.POST.get("LastName"))
        print(request.user)
        #print(form)
        designerProfile.objects.create(user=request.user,FirstName=request.POST.get("FirstName"),LastName=request.POST.get("LastName"))
        # # if form.is_valid():
        #     print("inside form valid")
        #     designerProfile.objects.create(form)
        # else:
        #     print("bbbbbb")
    context = {'form':form}
    print(context)
    return render(request,"designer/editprofile.html",context)    

def editprofilereq(request):
    print("inside editprofilereq")
    print(request.user)
    
    profile = designerProfile.objects.get(user=request.user)
    form = ProfilesForm(instance=profile)
    
    if request.method == 'POST':  
        fname=request.POST.get("FirstName","")
        lname=request.POST.get("LastName")
        mob=request.POST.get("Mobile")
        print("////////////////////",fname,lname,mob)
        form = ProfilesForm(request.POST,request.FILES,instance=request.user.profiles)
        if form.is_valid():
            form.save()
            firname = form.cleaned_data.get('FirstName')
            categ = form.cleaned_data.get('Category')
            print("////////////////////",firname,categ)
            return redirect('indexreq')
        else:
            print("not a valid form")

    context = {'form':form}
    print(context)
    return render(request,"designer/editprofile.html",context)

def samplereq(request):
    return render(request,"designer/sample.html")

def timelinereq(request):
    return render(request,"designer/timeline.html")

def logoutreq(request):
    return render(request,"designer/logout.html")

def base(request):
    return render(request,"designer/base.html")

