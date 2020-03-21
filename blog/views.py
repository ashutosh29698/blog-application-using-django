from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

@login_required
def home(request):
    # loading public and private posts in order of recently posted
    public_posts = Post.objects.filter(
                        user = request.user,
                        is_public = True,
                    ).order_by('-date_posted')
    private_posts = Post.objects.filter(
                        user = request.user,
                        is_public = False,
                    ).order_by('-date_posted')
    return render(request,"home.html", {
                                            'public_posts': public_posts,
                                            'private_posts': private_posts
                                        })
@login_required
def show_details(request,id):
    # shows detail of specified post id
    post = Post.objects.get(pk=id)
    return render(request,"detail.html",{'post': post})

@login_required
def make_public(request, id):
    # This function will update ONLY private posts
    # and which are posted by currently loggedin user

    if(request.method == 'POST'):
        
        form = PostForm(request.POST, request.FILES)
            
        if(form.is_valid()):
            cd = form.cleaned_data
            post = Post.objects.get(id = id, user=request.user, is_public = False)
            post.title = cd['title']
            post.description = cd['description']
            post.is_public = cd['is_public']

            if(cd['image']):
                image = request.FILES['image']
            else:
                image = ''
            post.save()
            
            # Flash message
            messages.success(request,"Post updated successfully!")

            return redirect('home')
    else:
        # instantiate new form with details fetched from database
        post = Post.objects.filter(id = id, user=request.user, is_public = False)
        form = PostForm(instance=post[0])

        return render(request,'update_post.html', {'form': form, 'id': id})



    


def search_users(request):
    # function to see PUBLIC posts of requested users
    if(request.method == 'POST'):
        user = request.POST.get('search_for')
        print(user)
        user = User.objects.filter(username = user)
        if(user.exists()):
            user = user[0]
            public_posts = Post.objects.filter(
                        user = user,
                        is_public = True,
                    ).order_by('-date_posted')

            return render(request,"home.html", {
                                            'public_posts': public_posts,
                                            'search_for': user
                                        })
        else:
            messages.warning(request, 'USER DOES NOT EXISTS')
    return render(request,"home.html")


@login_required
def add_post(request):
    # adding a new post
    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        if(form.is_valid()):
            cd = form.cleaned_data
            if(cd.get('image')):
                image = request.FILES['image']
            else:
                image = ''
            post.image = image
            post = Post(user=request.user, 
                        title=cd.get('title'),
                        description = cd.get('description'),
                        image = image,
                        is_public = cd['is_public']
                        )
            post.save()
            return redirect('home')
        
    else:
        # initialized a form to add post
        form = PostForm()
    return render(request,"add_post.html",{'form': form})



@login_required
def delete_post(request,id):
    # function to delete posts
    
    post = Post.objects.get(id=id)
    post.delete()
    messages.success(request,"POST DELETED SUCCESSFULLY")
    return redirect('home')