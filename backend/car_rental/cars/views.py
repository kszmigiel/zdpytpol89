from django.http import HttpResponse

def home(request):
    return HttpResponse("Witaj na stronie głównej!")

def with_argument(request, arg):
    params = request.GET.keys()
    print(params)

    params = [ request.GET[x]  for x in request.GET.keys()]

    return HttpResponse(f"Otrzymany argument: {arg} i parametry {params}")

def with_query_param(request):
    arg = request.GET.get('a', 'brak')
    return HttpResponse(f"Otrzymany parametr zapytania: {arg}")