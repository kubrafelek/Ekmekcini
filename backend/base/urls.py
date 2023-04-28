from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("products/", views.getProducts, name="products"),
    path("products/<str:pk>", views.getProduct, name="product"),
    path("users/profile/", views.getUserProfile, name="users-profile"),
    path("users/profile/update/", views.updateUserProfile, name="user-profile-update"),
    path("users/", views.getUsers, name="users"),
    path("users/<str:pk>/", views.getUserById, name="user"),
    path("users/update/<str:pk>/", views.updateUser, name="user-update"),
    path("users/delete/<str:pk>/", views.deleteUser, name="user-delete"),
    path("users/register/", views.registerUser, name="register"),
    path("users/login/", views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
