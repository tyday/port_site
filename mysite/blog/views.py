from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import Post
from .forms import PostForm
from sendemail.forms import ContactForm

# Create your views here.
def index(request):
    # posts = reversed(Post.objects.exclude(published_date__isnull=True).order_by('published_date'))
    if request.method == 'GET':
        form = ContactForm()
        posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')[:2]
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_name = form.cleaned_data['from_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message = f"""Name: {from_name}
                        Sender: {from_email}
                        Subject:{subject}
                        {message}"""
            try:
                send_mail('tylerday.net: contact message', message, 'admin@tylerday.net', ['tyrday@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, 'blog/index.html', {'posts': posts, 'form':form})
    
def post_list(request):
    posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})