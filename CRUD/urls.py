from django.urls import path
from .import views
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    # path('', views.home, name='crud-home'),
    path('create', views.create, name='create'),
    path('', ProductListView.as_view(), name='crud-home'),
    path('product/new/', ProductCreateView.as_view(), name='crud-add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='crud-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='crud-delete'),
]