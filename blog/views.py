from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            Post.objects.create(title=title, content=content)
        return redirect("home")
    posts = Post.objects.order_by("-created_at")
    return render(request, "home.html", {"posts": posts})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("home")

def about(request):
    return render(request, "about.html")
