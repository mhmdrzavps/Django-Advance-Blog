from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    #path('fbv-index', views.indexView, name = 'fbv-index'),
    #path('cbv-index', TemplateView.as_view(template_name = 'index.html', extra_context = {'name': 'mhmdrza'}))
    path('cbv-index', views.IndexView.as_view(), name = 'cbv-index'),
    path('go-to-maktabkhooneh', RedirectView.as_view(url='https://maktabkhooneh.org/'), name = 'Redirect-to-maktabkhooneh'),
    path('go-to-index', RedirectView.as_view(pattern_name ='blog:cbv-index'), name = 'Redirect-to-maktabkhooneh'),
    path('go-maktabkhooneh/<int:pk>', views.RedirectToMaktabkhooneh.as_view(), name = 'RedirectMaktabkhooneh'),
    path('post/', views.PostList.as_view(), name = 'post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post-detail'),
    path('post/create/', views.postCreateView.as_view(), name=  'post-create')

    ]