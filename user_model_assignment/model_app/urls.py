# from django.urls import path, include
# from . import views
# urlpatterns = [
#     path('create/', views.CreateUser.as_view(), name='create_user'),
#     path('read/', views.ReadUser.as_view(), name='read_user'),
#     path('update/<int:pk>/', views.UpdateUser.as_view(), name='update_user'),
#     path('delete/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
# ]
# users/urls.py
# from django.urls import path, include
# from . import views
# urlpatterns = [
#     path('create/', views.CreateUser.as_view(), name='create_user'),
#     path('read/', views.ReadUser.as_view(), name='read_user'),
#     path('update/<int:pk>/', views.UpdateUser.as_view(), name='update_user'),
#     path('delete/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
# ]

# users/urls.py
from django.urls import path
from .views import CustomUserListView, CustomUserDetailView
urlpatterns = [
    path('', CustomUserListView.as_view()),
    path('<int:pk>/', CustomUserDetailView.as_view()),
]