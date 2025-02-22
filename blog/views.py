from django.shortcuts import render, redirect
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


def post_category(request, category_name):
    category= Category.objects.get(name=category_name)
    posts = category.post_set.all()

    category_number = category.post_set.count()

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    category_post_page = paginator.get_page(page_number)

    return render(request, 'blog/post_category.html', {'category': category, 'category_number': category_number, 'category_post_page': category_post_page})