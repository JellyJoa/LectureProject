
from django.urls import path
from bbs import views

urlpatterns = [
    path('list/', views.b_list, name='b_list'),
]
