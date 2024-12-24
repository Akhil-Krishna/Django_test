from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import sign_up, sign_in, profile,notifications, mark_as_read

urlpatterns = [
    path('', views.index, name='index'),
    
   path('explore/', views.explore, name='explore'),
    path('explore/<int:person_id>/', views.person_detail, name='person_detail'),

   path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', profile, name='profile'),
    path('notifications/', notifications, name='notifications'),
    path('notifications/read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
   
]
