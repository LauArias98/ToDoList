from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path('list/<int:id>/', views.list_detail_view, name='list-detail'),
    path('create/', views.list_create_view, name='create'),
    path('update/<int:id>/', views.list_update_view, name='update'),
    path('delete/<int:id>/', views.list_delete_view, name='delete'),
    path('all/', views.list_list_view, name='all'),
    path('completed/', views.completed_view, name='complete'),
    path('incomplete/', views.incomplete_view, name='incomplete'),
]