from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, User
from django.core.paginator import Paginator
from django.db.models import Count

def blog(request):
    posts= Post.objects.all().order_by('-created_date')
    five= Post.objects.all()

    if len(five) > 5:
        five_posts = five[len(Post.objects.all()) - 1:len(Post.objects.all()) - 6:-1]

    categories = Category.objects.annotate(article_count=Count('post'))
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    blog_page = paginator.get_page(page_number)

    if not request.user.is_authenticated:
        return redirect('account:login')

    try:
        return render(request, 'blog/blog.html', {'Posts': posts, 'categories': categories, 'blog_page': blog_page, 'five_posts': five_posts})
    except:
        return render(request, 'blog/blog.html', {'Posts': posts, 'categories': categories, 'blog_page': blog_page})
