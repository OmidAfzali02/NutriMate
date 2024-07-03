from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', userRegister, name='register'),
    path('logout/', userLogout, name='logout'),

    # path('profile/<int:pk>/', userProfile, name='profile'),
    
    path('calculate/', food_calorie_view, name='calculate'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)