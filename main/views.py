from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from main.models import *


def index(request):
    all_category = Category.objects.all()

    context = {
        'categories': all_category
    }
    return render(request, 'main/index.html', context)


def category(request, category_slug):
    categories = Category.objects.filter(slug=category_slug)

    if categories.exists():
        category = categories.first()
        category_id = category.id
        all_sub_category = SubCategory.objects.filter(category_id=category_id)

        context = {
            'category': category,
            'sub_categories': all_sub_category
        }
        return render(request, 'main/categories.html', context)
    else:
        return render(request, 'main/404.html')


def sub_category(request, category_slug, sub_category_slug):
    sub_category = SubCategory.objects.filter(slug=sub_category_slug)

    if sub_category.exists():
        sub_category = sub_category.first()
        sub_category_id = sub_category.id
        all_tutorial = Tutorial.objects.filter(sub_category_id=sub_category_id)
    else:
        return render(request, 'main/404.html')

    context = {
        'sub_category': sub_category,
        'tutorials': all_tutorial
    }
    return render(request, 'main/tutorials.html', context)


def not_found(request):
    return render(request, 'main/404.html')
