from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="bhome"),
    path('dashboard/', views.dashboard,name="bdashboard"),
    path('products/', views.products,name="bproducts"),
    path('products/addproduct/', views.addproduct,name="baddproduct"),
    path('designers/', views.designers,name="bdesigners"),
    path('market/', views.market,name="bmarket"),
    path('challenges/', views.view_chal,name="bchallenges"),
    path('challenges/create_challenge/',views.create_chal,name="bcreate_challenge"),
    #path('challenges/status/',views.view_status,name="view_status"),
    path('settings/', views.settings,name="bsettings"),
    path('register/', views.register,name="bregister"),
    path('designers/profile/', views.profile,name="bprofile"),
    path('designers/dregister/', views.dregister,name="bdregister"),
    
]