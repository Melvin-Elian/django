from django.urls import panth

from . import views
urlpatterns=[
    path('',views.home,name='home')
    path('add',views.add,name='add')
]