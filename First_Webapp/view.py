from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import Counter


def home(request):
    return render(request, 'index.html')


def result(request):
    article = request.GET['article']
    var_dict, count_word, = Counter.count(article)
    return render(request, "result.html",
                  {'article': article, "count_word": count_word, "var_dict": var_dict})
