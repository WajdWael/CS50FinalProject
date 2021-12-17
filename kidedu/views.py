from django.http.response import HttpResponseRedirectBase, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


# the main page
def index(request):
    # get all the articles
    article = Article.objects.first()
    return render(request, "kidedu/index.html", {
        "article": article,
    })


# view articles & search functionality
def articles(request):
    if 'q' in request.GET:
        q = request.GET['q']
        article = Article.objects.filter(title__icontains=q)
    else:
        article = Article.objects.all()
    return render(request, "kidedu/articles.html", {"article": article})


# view single article  & comment form
def view_page(request, id):
    article = Article.objects.get(id=id)
    context = {
        "article": article,
        "comment_form": AddComment(),
        "comments": article.comments.all()
    }
    return render(request, "kidedu/view-page.html", context)


# logic of adding comment
@login_required
def comments(request, id):
    article = Article.objects.get(id=id)
    # Attempt To get the data of the form
    form = AddComment(request.POST)
    newComment = form.save(commit=False)
    newComment.author = request.user
    newComment.article = article
    newComment.save()
    return HttpResponseRedirect(reverse("view_page", args=[id]))


# render colors page
def colors(request):
    colors = Colors.objects.all()
    return render(request, "kidedu/colors.html", {"colors": colors})


# render games page
def games(request):
    return render(request, 'kidedu/games.html')


# render game one page
def game_1(request):
    return render(request, 'kidedu/game_1.html')


# Log user in logic
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username and/or password is incorrect')
            return render(request, "kidedu/login.html")

    return render(request, "kidedu/login.html")


# sign user up logic
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("log_in"))
        else:
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if len(password1) != 8:
                return render(request, "kidedu/register.html", {
                    "message": "Password should be 8 charchters at least.",
                    "form": form
                })
            elif password1 != password2:
                return render(request, "kidedu/register.html", {
                    "message": "Passwords must match.",
                    "form": form
                })
            elif IntegrityError:
                return render(request, "kidedu/register.html", {
                    "message": "Username already taken.",
                    "form": form
                })
    else:
        return render(request, "kidedu/register.html", {"form": form})


# Log user out logic
def log_out(request):
    logout(request)
    return redirect('index')
