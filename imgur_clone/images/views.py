from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request, *args, **kwargs):
    print(args, kwargs)

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