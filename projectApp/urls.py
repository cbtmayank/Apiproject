from .views import projectDetailsViewset
from . import views
from django.urls import path

#LINK YOUR VIEWS FUNCTIONS HERE .

urlpatterns = [
    
    path('data-create/', views.projectDetailsViewset.as_view({'post':'createData'}),name='data-create'),
    path('data-update/', views.projectDetailsViewset.as_view({'post':'updateData'}),name='data-update'),
    path('data-delete/', views.projectDetailsViewset.as_view({'post':'deleteData'}),name='data-delete'),
    path('data-view/', views.projectDetailsViewset.as_view({'post':'viewData'}),name='data-view'),
    path('data-list/', views.projectDetailsViewset.as_view({'post':'listData'}), name='data-list'),

]
