
from django.shortcuts import render ,redirect
#from django.http import HttpResponse
# Create your views here.
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

from .forms import ProfilesForm

def home(request):
    form = CreateUserForm()
    if request.method == 'POST':  
        form = CreateUserForm(request.POST)  
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            print(user,email)
            messages.info(request,'Account created try log in')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user1 = authenticate(request, username = username , password = password)

        if user1 is not None:
            login(request , user1)
            return redirect('challenges')


    context = {'form':form}
    return render(request, 'home_page/submain.html',context)
    
@login_required(login_url = 'home')
def logoutUser(request):
    logout(request)
    return redirect('home')

def nav(request):
    return render(request, 'home_page/navigation.html')

@login_required(login_url = 'home')
def challenges(request):
    return render(request, 'challenge_page/challenges.html')

@login_required(login_url = 'home')
def profile(request):
  
    return render(request, 'profile_page/profile.html') 

@login_required(login_url = 'home')
#@allowed_user(allowed_roles=['profiles'])
def editprofile(request):
    profile = request.user.profiles
    form = ProfilesForm(instance=profile)
    if request.method == "POST":
        form = ProfilesForm(request.POST ,request.FILES, instance=request.user.profiles)
        if form.is_valid():
            form.save() 
            return render(request, 'profile_page/profile.html')
        else:
            return render(request, 'profile_page/editprofile.html')
    context = {'form':form}
    return render(request, 'profile_page/editprofile.html',context)

@login_required(login_url = 'home')
def unsubs(request):
    dic=[]
    dic1=[]
    task=profiles.objects.get(user=request.user)
    task1=task.sublist
    # print(task1)
    for i in range(len(task1)):
        dic=subbrand.objects.filter(id=task1[i])
        dic1.append(dic[0])
    print(dic1)
    if request.method == 'POST':
        var = request.POST.get('in1') 
        task1=profiles.objects.get(user=request.user)
        if var in task1.sublist: 
            task1.sublist.remove(var)                                                 
            task1.save()  
        else:
            pass 
    return render(request, 'profile_page/unsubs.html',{"list":dic1})
    return render(request, 'profile_page/unsubs.html')

@login_required(login_url = 'home')
def creward(request):
    return render(request, 'profile_page/creward.html')

@login_required(login_url = 'home')
def brand(request):
    task = subbrand.objects.all()
    print(task)
    task2=profiles.objects.get(user=request.user)
    if request.method == 'POST':
        var = request.POST.get('in1')
        task1=profiles.objects.get(user=request.user)
        if var not in task1.sublist: 
            task1.sublist.append(var)                                                 
            task1.save()     
        else:
            pass
    return render(request, 'brand_page/brand.html',{'task':task,'list':task2.sublist})

@login_required(login_url = 'home')
def products(request):
    return render(request, 'products_page/products.html')
