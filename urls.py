from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('quiz/<int:category_id>/', views.quiz_page, name='quiz_page'),
]
