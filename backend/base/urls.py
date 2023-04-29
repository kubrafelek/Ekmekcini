from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),

    # users
    path("users/profile/", views.getUserProfile, name="users-profile"),
    path("users/profile/update/", views.updateUserProfile, name="user-profile-update"),
    path("users/", views.getUsers, name="users"),
    path("users/<str:pk>/", views.getUserById, name="user"),
    path("users/update/<str:pk>/", views.updateUser, name="user-update"),
    path("users/delete/<str:pk>/", views.deleteUser, name="user-delete"),
    path("users/register/", views.registerUser, name="register"),
    path("users/login/", views.TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # products
    path("products/", views.getProducts, name="products"),
    path("products/<str:pk>", views.getProduct, name="product"),
    path("products/create/", views.createProduct, name="product-create"),
    path("products/upload/", views.uploadImage, name="image-upload"),
    path("products/<str:pk>/reviews/", views.createProductReview, name="create-review"),
    path("products/top/", views.getTopProducts, name='top-products'),
    path("products/<str:pk>/", views.getProduct, name="product"),
    path("products/update/<str:pk>/", views.updateProduct, name="product-update"),
    path("products/delete/<str:pk>/", views.deleteProduct, name="product-delete"),

    # orders
    path("orders/", views.getOrders, name="orders"),
    path("orders/add/", views.addOrderItems, name="orders-add"),
    path("orders/myorders/", views.getMyOrders, name="myorders"),
    path("orders/<str:pk>/deliver/", views.updateOrderToDelivered, name="order-delivered"),
    path("orders/<str:pk>/", views.getOrderById, name="user-order"),
    path("orders/<str:pk>/pay/", views.updateOrderToPaid, name="pay"),
]
