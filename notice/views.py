from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from notice.models import notice

def list_(request):
    page = (int)(request.GET.get("page", 0))
    num = (int)(request.GET.get("num", 10))
    notices_ = notice.objects.all().values("date", "title", "id")
    notices_sum = notices_.count()
    notices_ = list(notices_.order_by('date').reverse()[page * num: page * num + num])
    
    temp = {}
    temp["contents"] = notices_
    temp["total_num"] = notices_sum
    return JsonResponse(temp, safe = False)

def detail(request):
    notice_ = notice.objects.get(id = request.GET.get("id"))
    date = notice_.date
    notice_ = model_to_dict(notice_)
    notice_["date"] = date

    return JsonResponse(notice_, safe = False)

def detail_page(request):
    return render(request, "notice_detail.html")

def list_page(request):
    return render(request, "notice_list.html")
