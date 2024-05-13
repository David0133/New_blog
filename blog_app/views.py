from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.
from .models import Blog

def blog_list(request):
    blog = Blog.objects.all()
    check = blog[::-1]
    context = {'blogs':check}
    return render(request, 'blog/blog_list.html',context)

def add_blog(request):
    if request.method == 'POST':
        data = request.POST.dict()
        Blog.objects.create(title=data['title'],image=data['image'],story=data['story'])
        return redirect('blog_list')
    else:
        return render(request, 'blog/add_blog.html')
    
def full_blog(request,id):
    blog = get_object_or_404(Blog, id=id)
    context = {'blog':blog}
    return render(request, 'blog/full_blog.html',context)

def edit_post(request,id):
    if request.method == "POST":
        blog = get_object_or_404(Blog,id=id)
        story = request.POST['story']
        if(story == ''):
            return redirect('blog_list')
        blog.story = story
        blog.save()
        return redirect('blog_list')
    return render(request,'blog/edit_post.html',{'id':id})

def delete_post(request,id):
    blog = get_object_or_404(Blog,id=id)
    blog.delete()
    return redirect('blog_list')