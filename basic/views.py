from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import carousel as carousel_model


def home(request):
    return render(request, "temp.html")

def info(request):
    return render(request, "info.html")

def contactus(request):
    return render(request, "contactus.html")

def carousel(request):
    carousels = carousel_model.objects.filter(place = request.GET.get("place")).order_by("-date").values("title", "description", "link", "content_class", "img_filename")[:3]
    carousels = list(carousels)
    return JsonResponse(carousels, safe=False)
