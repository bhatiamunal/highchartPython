from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path("",views.index,name='home'),
   path("about",views.about,name='about'),
   path('database', views.database),
   path('table', views.table),
   path('analyze', views.analyze),
   path('dashboard', views.dashboard),
   path('setting',views.setting)
]
