from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('configurator/', views.configurator, name='configurator'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('add-to-cart/<str:item_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<str:item_id>/', views.remove_from_cart, name='remove-from-cart')
]