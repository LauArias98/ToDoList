from django.urls import path
from list import views

app_name = 'list'
urlpatterns = [
    path('list/<int:id>/', views.list_detail_view, name='list-detail'),
    path('create/', views.list_create_view),
    path('update/<int:id>/', views.list_update_view),
    path('delete/<int:id>/', views.list_delete_view),
    path('all/', views.list_list_view),
]