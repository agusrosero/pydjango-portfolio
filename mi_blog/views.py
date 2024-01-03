from django.shortcuts import redirect, render, get_object_or_404
from .models import Post


def render_posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})

def delete_post(request, post_id):
    del_post = get_object_or_404(Post, pk=post_id)
    del_post.delete()
    return redirect("/")
