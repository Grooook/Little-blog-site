from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from .models import Article, Comment
from django.urls import reverse
from .forms import AddArticleForm
from django.contrib import messages

def index(request):
    articles = Article.objects.all().order_by('-date')
    content = {
        'articles':articles,
    }
    return render(request, 'articles/list.html', content)


def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('No page')

    comments = article.comment_set.all().order_by('-date')
    content = {
        'article':article ,
        'comments':comments,
    }

    return render(request, 'articles/article.html', content)


def leave_coment(request, article_id):
    try:
        if request.POST:
            article = Article.objects.get(id=article_id)
            content = {
                'article':article ,
        }
    except:
        raise Http404('No page')
    article.comment_set.create(author=request.user, text=request.POST['text'])

    return redirect(f'/articles/{article_id}')

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(f'/articles/{comment.article.id}')

def add_article(request):
    if request.POST:
        form = AddArticleForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            response = redirect('/articles/')
            return response
    else:
        form = AddArticleForm()

    context = {
        'form' : form,
    }
    return render(request, 'articles/new_article.html',context)

def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/articles/')

def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    form = AddArticleForm(instance=article)

    if request.POST:
        form = AddArticleForm(request.POST, instance=article)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            response = redirect('/articles/')
            return response


    context = {
        'form' : form,
        'article' :article,
    }
    return render(request, 'articles/update_article.html',context)
