from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
)

# Create your views here.

class ArticleListView(ListView):
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Article.objects.all()
    def get_success_url(self):
        return reverse('blog:article_list')


class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()