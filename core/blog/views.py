from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from blog.models import Post
from blog.form import ContactForm, PostForm
from  datetime import datetime
# Create your views here.

#Function Base View for show a template
'''
def indexView(request):
    """
    a function base view for show index page
    """
    context = {'name': 'mhmdrza'}
    return render(request, 'index.html', context)
'''

class IndexView(TemplateView):
    """ 
    a class base view for show index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context

#Function Base View for show a template
'''
from django.shortcuts import redirect
def RedirectMaktabkhooneh(request):
    return redirect('https://maktabkhooneh.org/')
'''

class RedirectToMaktabkhooneh(RedirectView):

    #url = 'https://maktabkhooneh.org/'
    pattern_name = 'blog:cbv-index'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        #return super().get_redirect_url(*args, **kwargs)
        return super().get_redirect_url()

class PostList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    permission_required = 'blog.view_post'
    # queryset = Post.objects.all()
    context_object_name = 'posts'
    #paginate_by = 2
    ordering = 'id'

    #def get_queryset(self):
        #posts = Post.objects.filter(status = True).orderby('-id')
        #return posts
    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(status = True)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        contex =  super().get_context_data(**kwargs)
        contex['now'] = datetime.now()
        return contex

class postCreateView(LoginRequiredMixin, FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    #fields = ['author', 'title', 'content', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'