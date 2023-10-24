from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('product_list/',
         views.product_list,
         name='product_list'),
    path('account/', views.account, name='account'),
    path('edit/', views.edit, name='edit'),
    path('<int:product_id>/review/',
         views.product_review,
         name='product_review'),
    path('<int:id>/<slug:slug>/',
         views.product_detail,
         name='product_detail'),
]
