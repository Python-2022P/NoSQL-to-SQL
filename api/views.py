from django.http import HttpRequest, JsonResponse

from .models import Smartphones

def smartphones(request: HttpRequest) -> JsonResponse:
    smartphones = Smartphones.objects.all()

    result = []
    for i in smartphones:
        result.append({
            "id": i.pk,
            "name": i.name,
            "price": i.price
        })

    return JsonResponse({'result': result})