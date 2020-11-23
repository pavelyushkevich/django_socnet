from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm

@login_required
def index(request):
    latest_posts = Post.objects.order_by('-date')[:10]
    context = {'latest_posts': latest_posts}
    return render(request, 'posts/feed.html', context)

@login_required
def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        raise Http404('Post Not Found')

    latest_comments = post.comment_set.order_by('-id')[:10]
    
    context = {'post': post, 'comments': latest_comments}
    return render(request, 'posts/post.html', context)

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('posts:index'))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/add_post.html', context)

# @login_required
# def add_comment(request, post_id):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid:
#             new_comment = form.save(commit=False)
#             new_comment.user = request.user
#             # new_comment.post = post_id
#             new_comment.save()
#             return HttpResponseRedirect(reverse('posts:index'))
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return HttpResponseRedirect(reverse('posts:post', args=(post_id,)))

@login_required
def add_comment(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        raise Http404('Post Not Found')

    post.comment_set.create(comment_text=request.POST['text'], user=request.user)
    # post.save() 
    return HttpResponseRedirect(reverse('posts:post', args=(post.id,)))
