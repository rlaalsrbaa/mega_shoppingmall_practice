from django.shortcuts import render
from .models import Product, ProductReal
from questions.forms import QuestionForm

def list(request):
    products_list = Product.objects.order_by('-reg_date')
    context = {'products_list': products_list}
    return render(request, 'products/products_list.html', context)

def detail(request, products_id):
    products = ProductReal.objects.get(id=products_id)
    context = {'products': products}
    return render(request, 'products/products_detail.html', context)

def question_create(request, products_id):

    form = QuestionForm()
    return render(request, 'products/question_form.html', {'form': form})