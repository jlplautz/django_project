from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    # function views
    # path('', views.home, name='blog-home'),
    # ListViews
    path('', PostListView.as_view(), name='blog-home'),  # templates => <app>/<model>_viewtype>.html
    # DetailView
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # CreateView
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    # UpdateView
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # DeleteView
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
