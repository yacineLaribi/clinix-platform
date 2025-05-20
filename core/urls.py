from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('challenges/', views.challenges, name='challenges'),
    path('challenges/<int:pk>/', views.challenge_details, name='challenge_details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
