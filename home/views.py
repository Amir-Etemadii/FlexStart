from django.shortcuts import render
from .models import *
from blog.models import Post

def index(request):

    posts = Post.objects.all()

    if len(posts)>3:
        posts= posts[len(Post.objects.all())-1:len(Post.objects.all())-4:-1]

    context = {
        'Home': Home.objects.all(),
        'About': About.objects.all(),
        'OurValue': OurValue.objects.all(),
        'WorkStatus': WorkStatus.objects.all(),
        'Features': Feature.objects.all(),
        'Features2': Feature2.objects.all(),
        'Services': Service.objects.all(),
        'Price': Price.objects.all(),
        'Frequently': Frequently.objects.all(),
        'Team': Team.objects.all(),
        'Contact': Contact.objects.all(),
        'ContactUs': ContactUs.objects.all(),

        'Post': posts
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message= request.POST.get('message')

        Contact.objects.create(name=name,email=email,subject=subject,body=message)


    return render(request, 'home/index.html',context= context)