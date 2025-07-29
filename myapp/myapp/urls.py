
from django.contrib import admin
from django.urls import path
from myauth.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', login_view, name="login"),
    
]
