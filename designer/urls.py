from django.urls import path
from . import views

urlpatterns=[

     path('',views.log,name='login'),
     path('base',views.base),
     path('registback',views.registration,name='registration'),
     path('registerreq',views.reqregister,name='reqregister'),
     path('loginreq',views.loginreq,name='loginreq'),
     path('profilereq',views.profilereq,name='profilereq'),
     path('editprofilereq',views.editprofilereq,name='editprofilereq'),
     path('samplereq',views.samplereq,name='samplereq'),
     path('timelinereq',views.timelinereq,name='timelinereq'),
     path('logoutreq',views.logoutreq,name='logoutreq'),
     path('indexreq',views.indexreq,name='indexreq'),

]