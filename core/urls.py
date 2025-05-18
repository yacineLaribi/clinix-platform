from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('challenges/', views.challenges, name='challenges'),
    path('challenges/<int:pk>/', views.challenge_details, name='challenge_details'),
]
