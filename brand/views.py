from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ProductForm , logs ,Design,BrandReg
import paho.mqtt.client as mqtt
from datetime import *
# Create your views here.

def home(request):

    if request.method == 'POST':
        #print("printing brand login : ",request.POST)
        bname=request.POST.get('bname')
        password=request.POST.get('password')
        dbrandn=Registerpage.objects.get(bname=bname)
        dpwd=dbrandn.password
        dbrandid=dbrandn.id
        #print("dbrandn",dbrandn)
        #print("dpwd",dpwd)
        #print("dbrandid",dbrandid)
        if password == dpwd:
            #login(request,bname)
            #return redirect('dashboard')
            bname=request.POST.get('bname')
            prds = Product.objects.all()
            # l=[]
            # for i in prds:
            #     if(i.brand == bname):
            #         l.append(i.brand)
            # print(l)
            total_products = prds.count()
            context = {'bname':bname,'total_products':total_products,'prds':prds}
            
            return render(request, 'brand/home_page/dashboard.html',context)
        else:
            messages.info(request,'Brand name or Password is incorrect')
        
        
    
    return render(request, 'brand/home_page/index.html')


def dashboard(request):
    bname=request.POST.get('bname')
    prds = Product.objects.all()
    total_products = prds.count()
    context = {'total_products':total_products,'prds':prds}
    return render(request, 'brand/home_page/dashboard.html',context)


def products(request):
    prds = Product.objects.all()
    context ={'prds':prds}
    return render(request, 'brand/product_page/products.html',context)



def addproduct(request):
    if request.method == 'POST':
        print("printing product:",request.POST)
        name=request.POST.get('name')
        designer=request.POST.get('designer')
        quantity=request.POST.get('quantity')
        date=request.POST.get('date')
        category=request.POST.get('gender')
        description=request.POST.get('description')
        size=request.POST.get('size')
        price=request.POST.get('cost')
        images=request.POST.get('inpFile')

        add=Product(name=name,designer=designer,quantity=quantity,price=price,description=description,category=category,date=date,size=size,images=images)
        add.save()
        return redirect('products')

    
    
   
    # form=ProductForm()
    # if request.method == 'POST':
    #     #print("printing product:",request.POST.get('images'))
    #     #images=request.POST.get('images')
    #     form = ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('products')
    #     else:
    #         form.save()
    #         return redirect('addproduct')

    # context ={'form':form}   
    # 
    return render(request, 'brand/product_page/addproduct.html')


def register(request):
    form = BrandReg()
    if request.method =='POST':
        form = BrandReg(request.POST)
        if form.is_valid():
            form.save()
            print('DONE>>>>>>>>>>>')
            print(request.POST.get('email'))
    # if request.method == 'POST':
    #     #print("printing product:",request.POST)
    #     name=request.POST.get('name')
    #     password=request.POST.get('password')
    #     repeatpwd=request.POST.get('re_password')
    #     email=request.POST.get('email')
    #     TandC=request.POST.get('agree-term')
    #     logo=request.POST.get('logo')
    #     certificate=request.POST.get('certificate')
    #     if(password == repeatpwd):
    #         if(TandC == 'on'):
    #             log=Registerpage(bname=name,bemail=email,password=password,logo=logo,certificate=certificate)
    #             log.save()
    #             return redirect('home')
    #         else:
    #             messages.info(request,'Please check the Tearms and Conditions ')
    #     else:
    #         messages.info(request,'Passwords does not match')
    context ={'form':form}
    return render(request, 'brand/home_page/register.html',context)


def designers(request):
    membs = Designer.objects.all()
    return render(request, 'brand/designer_page/designers.html',{'membs': membs})


def view_chal(request):
    if request.method =='POST':
        n=request.POST.get('name')
        data=challenges.objects.get(cname=n)
        return render(request,'brand/challenge_page/stat.html',{'datas':data})  
    else:
        val=challenges.objects.all()
        return render(request, 'brand/challenge_page/challenges.html',{'vals':val})
'''
def view_status(request):
    if request.method =='POST':
        n=request.POST.get('name')
        print(n)
    return render(request,'brand/challenge_page/stat.html')  
'''
def create_chal(request):
    if request.method =='POST':
        print("REQUEST"+str(request.POST))
        ch_name=request.POST.get('challege_name')
        ch_desc=request.POST.get('challege_desc')
        ch_participants=request.POST.get('participants')
        ch_designers=request.POST.get('Designers')
        ch_date=request.POST.get('date')
        ch_sme=request.POST.get('sme')
        y,m,d=[int(x) for x in ch_date.split('-')]
        select_date=date(y,m,d)
        today_date=date.today()
        #flag=0
        if(select_date>=today_date):
            print("done............... ")
            form1=challenges(cname=ch_name,cdesc=ch_desc,csme=ch_sme,cparticipants=ch_participants,cdesigners=ch_designers,cdobegin=ch_date)
            form1.save()
            messages.info(request,'challenge created successfully')
            broker_ad="127.0.0.1"
            client = mqtt.Client("P1") #create new instance
            client.connect(broker_ad)
            print('here')
            #client.publish("brand"," challenge name:"+str(ch_name)+"\n description:"+str(ch_desc)+"\n Total participants:"+str(ch_participants))
            #client.publish("brand","create rooms for "+str(ch_sme)+" SME's and a total "+str(ch_participants)+" participants (icludes "+str(ch_designers)+" designers)")
            client.publish("brand","create rooms for a challenge of name"+str(ch_name)+"containing"+str(ch_sme)+" SME's and a total "+str(ch_participants)+" customers and "+str(ch_designers)+" designers")
            return redirect('/challenges')
        else:
            messages.info(request,'select a valid date')            
        
    return render(request,'brand/challenge_page/create_challenge.html')




def settings(request):
    return render(request, 'brand/settings_page/settings.html')


def market(request):
    return render(request, 'brand/market_page/market.html')


def profile(request):
    return render(request, 'brand/settings_page/profile.html')


def dregister(request):
    form=Design()
    if request.method == 'POST':
        form = Design(request.POST, request.FILES)
        print("printing designer:",request.POST)
        name = request.POST.get('name')
        desc = request.POST.get('designation')
        mail = request.POST.get('email')
        pic = request.POST.get('img')
        phn = request.POST.get('phone')
        insta = request.POST.get('insta')
        fb = request.POST.get('fb')

        form = Designer(name=name, designation=desc, images=pic, email=mail, phone=phn, facebook=fb, insta=insta)
        form.save()
        return redirect('designers')
        

    return render(request, 'brand/designer_page/dregister.html')