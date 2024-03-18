from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',views.homepage,name='homepage'),
  path('fillform/',views.fillform,name='fillform'),
  path('fetchdetail/',views.fetchdetail,name="fetchdetail"),
   path('update/<int:id>/',views.update,name="update"),
  path('delete/<int:id>/',views.delete,name="delete"),
]