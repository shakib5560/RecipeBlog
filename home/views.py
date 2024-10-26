
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.db.models import Q
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        images = request.FILES.get('images')
        user_id = data.get('user')
        tags = data.get('tags')

        # Fetch the user object
        user = User.objects.get(id=user_id)

        # Create the Recipe object
        Recipe.objects.create(title=title, description=description, images=images, user=user, tags=tags)
        messages.success(request, "Post created successfully!")
        return redirect('allrecipe')

    # Fetch users for the dropdown and recent posts for display
    users = User.objects.all()
    recent_posts = Recipe.objects.all().order_by('-created_date')[:4]  # Latest 4 posts
    return render(request, 'home.html', {'recData': users, 'recent_posts': recent_posts})



def blog(request):
    
    return render(request, 'blog.html')

def contect(request):
    return render(request, 'contect.html')

def allrecipe(request):
    recent_posts = Recipe.objects.all()
    
    search_query = request.GET.get('search')
    if search_query:
        # Filter by title or tags that contain the search term
        recent_posts = recent_posts.filter(
            Q(title__icontains=search_query) | Q(tags__icontains=search_query)
        )

    return render(request, 'allrecipe.html', {'recent_posts': recent_posts})


def about(request):
    return render(request, 'about.html')

def delectitem(request, id):
    Recipe.objects.get(id=id).delete()
    messages.success(request, "Recipe deleted successfully!")
    return redirect('allrecipe')

def edititem(request, id):
    recData = get_object_or_404(Recipe, id=id)
    users = User.objects.all()  # Get all users for the author dropdown

    if request.method == 'POST':
        recData.title = request.POST['title']
        recData.description = request.POST['description']
        recData.tags = request.POST['tags']

        # Handling image update
        if 'images' in request.FILES:
            recData.images = request.FILES['images']

        # Update the selected author
        author_id = request.POST['user']
        if author_id:
            recData.user = User.objects.get(id=author_id)

        recData.save()
        messages.success(request, "Recipe updated successfully!")
        return redirect('allrecipe')  # Redirect to appropriate view

    return render(request, 'edititem.html', {'recData': recData, 'users': users})


def signup(request):
    if request.method == 'POST':
        name = request.POST.get['name']
        email = request.POST.get['email']
        password = request.POST.get['password']

        user = User.objects.create_user(username=name, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "User created successfully!")
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')