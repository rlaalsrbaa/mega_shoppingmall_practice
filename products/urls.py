from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('<int:products_id>/', views.detail, name='detail'),
    path('<int:products_id>/question/create', views.question_create, name='question_create'),
]