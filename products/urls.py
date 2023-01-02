from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
]