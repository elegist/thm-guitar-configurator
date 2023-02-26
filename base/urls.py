from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_view, name="register"), 
    path('category/', views.category_list),
    path('item/', views.item_list),
    path('cart/', views.cart_list),
    path('cartItem/', views.cartItem_list),
    path('staffPick/', views.staffPick_list),
    path('staffPickItem/', views.staffPickItem_list),
]