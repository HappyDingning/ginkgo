import io
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import achievement
from accounts.models import user_profile


def achievement_(request):
    target_level = request.GET.get('target_level', 3)
    achievements = achievement.objects.filter(level__lte = target_level).values("title", "outline", "news_id", "date").order_by('date').reverse()
    achievements = list(achievements)
    return JsonResponse(achievements, safe = False)

def members_list(request):
    identity = (int)(request.GET.get("identity"))
    members = user_profile.objects.filter(is_shown = True, identity = identity).values("name", "duty", "id", "photo")
    members = list(members)
    
    temp = {}
    for each in members:
        if each["duty"] in temp:
            temp[each["duty"]].append(each)
        else:
            temp[each["duty"]] = [each]

    return JsonResponse(temp, safe = False)

def member_detail(request):
    member = user_profile.objects.get(id = request.GET.get('id'))
    photo = member.photo.url if member.photo else None
    member = model_to_dict(member, ["name", "introduction", "duty"])
    member["photo"] = photo
    return JsonResponse(member, safe = False)

def member_avatar(request):
    path = '%s/%d.jpg' % (os.path, request.GET.get('id'))

    return

def achievement_page(request):
    return render(request, 'achievement.html')

def list_page(request):
    return render(request, 'members_list.html')

def member_detail_page(request):
    return render(request, 'member_detail.html')
