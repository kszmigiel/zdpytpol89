import json

from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from django.conf import settings

from .models import Image



def index(request):
    # template = loader.get_template("index.html")
    context = {"header": "STRONA TESTOWA"}

    return render(request,"index.html", context)
    # return HttpResponse(template.render(context, request))

def image_view(request, id=None, *args, **kwargs):
    if id:
        image = get_object_or_404(Image, pk=id)
        context = {"title": f'Obraz {id}', "images": [image]}
        return render(request, "images.html", context)

    likes = request.GET.get('likes', None)
    if 'likes':
        images  = Image.objects.annotate(num_likes=Count('imagelike')).filter(num_likes__gte=likes)
        context = {"title": "Obrazy", "images": images}
        return render(request, "images.html", context)


    images = Image.objects.all()
    context = {"title":"Obrazy", "images": images}
    return render(request, "images.html", context)




def login(request, *args, **kwargs):
    print(args, kwargs)

    request.GET.get('next', None)

    # write all request attributes and methods
    print(request)
    print(request.META)
    print(request.scheme)
    print(request.body)
    print(json.loads(request.body.decode('utf-8')))
    print(request.path)
    print(request.path_info)
    print(request.content_type)
    print(request.content_params)

    return HttpResponse("Hello, world. You're at the polls login.")