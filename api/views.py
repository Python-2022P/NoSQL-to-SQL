from django.http import HttpRequest, JsonResponse
from .models import Smartphones
import json

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
        data_json = json.loads(data)

        smartphone = Smartphones(
            price=data_json['price'],
            memory=data_json['memory'],
            ram=data_json['ram'],
            color=data_json['color'],
            img_url=data_json['img_url'],
            name=data_json['name'],
            model=data_json['model'],
        )
        smartphone.save()

        return JsonResponse({"result": "OK"})
    return JsonResponse({"result": "OK"})


def get_smartphone(request: HttpRequest,id) -> JsonResponse:
    smartphones = Smartphones.objects.all()
    
    for i in smartphones:
        if i.id==id:
            result={
            "id": i.id,
            "name": i.name,
            "price": i.price,
            }

    return JsonResponse({"result": result})



def del_smartphone(request: HttpRequest,id) -> JsonResponse:
    pass


def upd_smartphone(request: HttpRequest,id) -> JsonResponse:
    pass
