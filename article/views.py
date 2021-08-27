from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from article.models import article, tag


def list_(request):
    page = (int)(request.GET.get("page", 0))
    num = (int)(request.GET.get("num", 10))
    article_ = article.objects.all().values("date", "title", "id")
    article_sum = article_.count()
    article_ = list(article_.order_by('date').reverse()[page * num: page * num + num])

    temp = {}
    temp["contents"] = article_
    temp["total_num"] = article_sum
    return JsonResponse(temp, safe = False)

def detail(request):
    article_ = article.objects.get(id = request.GET.get("id"))
    date = article_.date
    article_ = model_to_dict(article_)
    article_['tag'] = [each.label for each in article_['tag']]
    article_["date"] = date
    return JsonResponse(article_, safe = False)

def list_page(request):
    return render(request, 'article_list.html')

def detail_page(request):
    return render(request, 'article_detail.html')
