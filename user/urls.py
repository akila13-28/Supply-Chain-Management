from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    
    path('nav/', views.nav,name="navigation"),
    path('logout/', views.logoutUser,name="logout"),
    path('challenges/', views.challenges,name="challenges"),
    path('profile/', views.profile,name="userprofile"),
    path('editprofile/', views.editprofile,name="editprofile"),
    path('unsubs/', views.unsubs,name="unsubs"),
    path('creward/', views.creward,name="creward"),
    path('brand/', views.brand,name="brand"),
    path('products/',views.products,name="products"),
   
    
]