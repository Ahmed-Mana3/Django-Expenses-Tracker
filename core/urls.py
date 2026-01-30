from django.contrib import admin
from django.urls import path
from expenses.views import index, add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add/', add, name='add'),
]
