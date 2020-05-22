from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# this is Home function views
def home(request):
    # from views -> is routing a response to user
    # return HttpResponse('<h1>Blog Home</h1>')

    # context to receive de posts (dummy data)
    context = {'posts': Post.objects.all()}
    # from views -> is routing to a tempĺate, with context information
    return render(request, 'blog/home.html', context)


# this Home List Views => class-Based Views
class PostListView(ListView):
    model = Post
    # templates => <app>/<model>_viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


# This is a view for individual Post => as Detail View => import DetailView
class PostDetailView(DetailView):
    model = Post


# This is a create New Post => import CreateView
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# This is an Update to  Post => import UpdateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # function to verify id user is the same of the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# This is a DeleteView Post => import DeleteView
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # for a success delete post the redirect pages
    success_url = '/'

    # function to verify id user is the same of the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
