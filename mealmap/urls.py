from django.urls import path
from . import views

app_name = 'mealmap'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('category/', views.CategoryIndexView.as_view(), name='category_index'),
    path('<int:pk>/category/', views.CategoryTemplateView.as_view(), name='category_detail'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('category_create/', views.CategoryCreateView.as_view(), name='category_create'),
]