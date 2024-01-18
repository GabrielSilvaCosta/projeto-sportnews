# news/views.py
from django.shortcuts import render, get_object_or_404, redirect

from news.forms import CategoryForm
from .models import News


def home_page(request):
    news_list = News.objects.all()
    return render(request, "home.html", {"news_list": news_list})


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news': news})


def categories_form(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")

    return render(request, "categories_form.html", {"form": form})
