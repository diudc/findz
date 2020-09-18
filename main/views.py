from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
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
    if request.method == 'GET':
        sub_category = SubCategory.objects.filter(slug=sub_category_slug)

        if sub_category.exists():
            sub_category = sub_category.first()
            sub_category_id = sub_category.id
            all_tutorial = Tutorial.objects.filter(sub_category_id=sub_category_id)
        else:
            return render(request, 'main/404.html')

        context = {
            'sub_category': sub_category,
            'tutorials': all_tutorial,
            'category_slug': category_slug
        }
        return render(request, 'main/tutorials.html', context)
    elif request.method == 'POST':
        pricing = request.POST['pricing']
        medium = request.POST.getlist('medium[]')
        level = request.POST.getlist('level[]')

        pricing = ['free', 'paid'] if not pricing else [pricing]
        medium = ['blog', 'video', 'book'] if not medium else medium
        level = ['beginner', 'intermediate', 'advanced'] if not level else level

        tutorials = Tutorial.objects.filter(sub_category__slug=sub_category_slug).filter(Q(pricing__in=pricing) & Q(medium__in=medium) & Q(level__in=level))

        serialized_tutorials = serializers.serialize('json', tutorials, ensure_ascii=False)
        return JsonResponse(serialized_tutorials, safe=False)

def submit_tutorial(request):
    return render(request,'main/submit_tutorial.html')
    

def not_found(request):
    return render(request, 'main/404.html')
