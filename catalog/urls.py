from django.urls import path, include
from catalog.views import UserRegistrationView, UserLoginView, UserLogoutView, ProductListCreateView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/logout/', UserLogoutView.as_view(), name='user-logout'),

    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/create-product/', ProductCreateView.as_view(), name='create-product'),

]
