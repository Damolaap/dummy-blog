from django.shortcuts import render
from BlogApp.models import BlogPost

# Create your views here.

# lookup filters 
# Django template filters

#lt
#gt
#startswith
#endswith 
#contains
#icontains : not case sensitive

def show_index(request):
    
    search = request.GET.get('query')

    if search is not None and len(search.strip()) > 0: 
        blog_data = BlogPost.objects.filter(blog_title__icontains = search)
    
    else:
        blog_data = BlogPost.objects.all()

    context = {
        'blog_data' : blog_data
    }
    return render(request, 'index.html', context)

def show_post(request, id):
    post = BlogPost.objects.filter(id = id).first()
    context = {
    'post' : post
        }
    return render(request, 'post.html', context)

def show_contact(request):
    return render(request, 'contact.html')

def show_about(request):
    return render(request, 'about.html')