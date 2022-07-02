
from . import views
from django.contrib import admin
# from django.urls import path
# add include to your imports from django.urls
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('project/', views.project, name='project'),
    path('demo/', views.demo, name='demo'),
    path('', views.home, name='home'),
]