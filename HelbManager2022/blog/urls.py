from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views
from contact.views import icontact


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),     # localhost:8000/
    path('about/', views.about, name='blog-about'),  # localhost:8000/about
    path('contact/', icontact, name='blog-contact'),  # localhost:8000/contact

    path('status/', views.status , name='blog-status'),  # localhost:8000/status
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),  # localhost:8000/user/<str:username>

    path('post/new/', PostCreateView.as_view(), name='post-create'),  # localhost:8000/post/new
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   # localhost:8000/post/pk
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),   # localhost:8000/post/pk/update
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),   # localhost:8000/post/pk/delete

    path('task/<int:pk>/new/', views.task_create, name='task-create'),
    path('task/list/', views.task_list, name='task-list'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task-delete'),
    path('task/<int:task_id>/', views.task_detail, name='task-detail'),


    path('subtask/<int:pk>/new/', views.subtask_create, name='subtask-create'),
    path('subtask/list/', views.subtask_list, name='subtask-list'),
    path('subtask/<int:subtask_id>/delete/', views.subtask_delete, name='subtask-delete'),
    path('subtask/<int:subtask_id>/', views.subtask_detail, name='subtask-detail'), 


    
]



