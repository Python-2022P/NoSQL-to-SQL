from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, JsonResponse

from .models import Smartphones

def smartphones(request: HttpRequest) -> JsonResponse:
    smartphones = Smartphones.objects.all()

    result = []
    for i in smartphones:
        result.append({
            "id": i.pk,
            "name": i.name,
            "price": i.price,
        })

    return JsonResponse({'result': result})


def add_smartphone(request: HttpRequest) -> JsonResponse:
    if request.method=='POST':
        data = request.body.decode()
        print(JsonResponse(data))
        # p = Smartphones(name=)
        # p.save()
        #print('davron\n')
        return JsonResponse({"result": "OK"})
    return JsonResponse({"result": "OK"})


def get_smartphone(request: HttpRequest,id) -> JsonResponse:
    smartphones = Smartphones.objects.all()
    print(smartphones)
    for i in smartphones:
        if i.id==int(id):
            result={
            "id": i.id,
            "name": i.name,
            "price": i.price,
            }

    return JsonResponse({"result": result})