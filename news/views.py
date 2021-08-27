from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from news.models import news, tag


def list_(request):
    page = (int)(request.GET.get("page", 0))
    num = (int)(request.GET.get("num", 10))
    news_ = news.objects.all().values("date", "title", "id", "description")
    news_sum = news_.count()
    news_ = list(news_.order_by('date').reverse()[page * num: page * num + num])

    temp = {}
    temp["contents"] = news_
    temp["total_num"] = news_sum
    return JsonResponse(temp, safe = False)

def detail(request):
    news_ = news.objects.get(id = request.GET.get("id"))
    date = news_.date
    news_ = model_to_dict(news_)
    news_['tag'] = [each.label for each in news_['tag']]
    news_["date"] = date
    news_.pop("cover_img")
    return JsonResponse(news_, safe = False)

def list_page(request):
    return render(request, 'news_list.html')

def detail_page(request):
    return render(request, 'news_detail.html')
