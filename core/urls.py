from django.contrib import admin
from django.urls import path
from expenses.views import index, add, history
from accounts.views import login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('history/', history, name='history'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
