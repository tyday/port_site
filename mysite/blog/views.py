from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import Post, Project
from .forms import PostForm
from sendemail.forms import ContactForm

# Create your views here.
def index(request):
    # posts = reversed(Post.objects.exclude(published_date__isnull=True).order_by('published_date'))
    if request.method == 'GET':
        form = ContactForm()
        posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')[:2]
        projects = Project.objects.filter(display=True).order_by('-importance')
        print(posts,projects)
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
                messages.add_message(request, messages.SUCCESS, 'Thank you, your information was submitted.')
            return redirect('index')
        else:
            # Form isnt valid. Set posts and projects and move on
            posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')[:2]
            projects = Project.objects.filter(display=True).order_by('-importance')
            messages.add_message(request, messages.ERROR, 'The contact form failed to send.')
    return render(request, 'blog/index.html', {'posts': posts, 'projects':projects, 'form':form})
    
def post_list(request):
    posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required(login_url='/admin/login/')
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

@login_required(login_url='/admin/login/')
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
def project_list(request):
    project = Project.objects.all()
    return render(request, 'blog/project_list.html', {'project': project})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/project_detail.html', {'project':project})