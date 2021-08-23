from django.db.models import query
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page_obj = paginate_query(request, posts, settings.PAGE_PER_ITEM)
    newer_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/post_list.html', {'page_obj' : page_obj, 'posts' : posts, 'newer_posts' : newer_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    newer_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/post_detail.html', {'post' : post, 'newer_posts' : newer_posts})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def category(request, category):
    category = Category.objects.get(name=category)
    blog = Post.objects.filter(category=category).order_by('-published_date')
    newer_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/post_list.html',
                   {'category': category, 'blog': blog, 'newer_posts' : newer_posts})
'''
def tag(request, tag):
    tag = Tag.objects.get(name=tag)
    blog = Post.objects.filter(tag=tag)
    newer_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/post_list.html',
                  {'tag': tag, 'blog': blog, 'newer_posts' : newer_posts})
'''


def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return page_obj


def aboutme(request):
    newer_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/aboutme.html', {'newer_posts' : newer_posts})

def contact(request):
    newer_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/contact.html', {'newer_posts' : newer_posts})

def search(request):
    newer_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    keyword = request.GET.get('keyword')
    return render(request, 'blog/search.html', {'keyword' : keyword, 'newer_posts': newer_posts})
