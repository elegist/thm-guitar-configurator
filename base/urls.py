from django.urls import path
from base import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('add-to-cart/<str:item_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<str:item_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('order-summary/', views.order_summary, name='order-summary'),
    path('category/', views.category_list),
    path('model/', views.model_list),
    path('item/', views.item_list),
    path('order/', views.order_list),
    path('orderItem/', views.orderItem_list),
    path('configuration/', views.configuration_list),
] 

##urlpatterns = format_suffix_patterns(urlpatterns)
