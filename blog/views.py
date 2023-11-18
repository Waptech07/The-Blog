from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def index(request):
    title = "The Blog"
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    search_query = request.GET.get('search')

    if search_query:
        posts = Post.objects.filter(title__icontains=search_query).order_by('-id')
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
        if search_query:
            next_url += f'&search={search_query}'
    else:
        next_url = ''

    if page.has_previous():
        previous_url = f'?page={page.previous_page_number()}'
        if search_query:
            previous_url += f'&search={search_query}'
    else:
        previous_url = ''

    # Pass only the posts for the current page to the template
    current_posts = page.object_list

    # Retrieve distinct categories
    categories = Post.objects.values_list('category', flat=True).distinct()

    return render(request, 'index.html', {'title': title, 'posts': current_posts, 'page': page, 'next_url': next_url, 'previous_url': previous_url, 'search_query': search_query, 'categories': categories})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password=password)
        # If user is authenticated then login user
        if user is not None:
            auth.login(request, user)

            # Redirect to home page
            return redirect("/")
        else:

            # If user is not authenticated then show error message
            # and redirect to login page
            messages.info(request, "Invalid Credential")
            return redirect("login")
    else:
        return render (request, 'login.html')

# Register Page
def register(request):

    # If request is post then get user details from request
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Check if password and confirm password matches
        if password == confirm_password:

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect("register")

            # Check if email already exists
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect("register")

            # If username and email does not exists then create user
            else:

                # Create user
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )

                # Save user
                user.save()

                # Redirect to login page
                return redirect("login")
        else:

            # If password and confirm password does not matches then show error message
            messages.info(request, "Password does not match")
            return redirect("register")
    else:

        # If request is not post then render register page
        return render(request, "register.html")


# Logout view to logout user
def logout(request):
    # Logout user and redirect to home page
    auth.logout(request)
    return redirect("/login")


def read(request, id, title):

    post = get_object_or_404(Post, id=id, title=title)
    return render(request, 'read_more.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {"projects" : projects})

def newsletter(request):
    posts = Post.objects.order_by('-id')[:6]
    return render(request, 'newsletter.html', {'posts': posts})

@login_required(login_url="login")
def view_profile(request):
    user = User.objects.all().values()
    return render(request, 'profile/view_profile.html', {"user": user})

@login_required(login_url="login")
def add_post(request):
    post = Post.objects.all()

    if request.method == 'POST':

        # Create post
        post = Post.objects.create(
            title = Post.title,
        )

        post.save()

    return render(request, 'add_post.html', {'post' : post})