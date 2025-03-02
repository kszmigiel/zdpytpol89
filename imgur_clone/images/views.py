import json

from django.shortcuts import render
from django.template import loader



def index(request):
    # template = loader.get_template("index.html")
    context = {"header": "STRONA TESTOWA"}

    return render(request,"index.html", context)
    # return HttpResponse(template.render(context, request))





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