from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # No se usa login/ porque se ha añadido la funcionalidad de registro en el home
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
]