import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, ADS


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        """
        Получение всех категорий
        """
        context = get_list_or_404(Category)
        result = [{"id": item.id,
                   "name": item.name} for item in context]

        return JsonResponse(result, safe=False)

    def post(self, request):
        """
        Запись новой категории
        """
        category_data: dict = json.loads(request.body)
        category_obj = Category()
        category_obj.name = category_data.get('name')

        try:
            category_obj.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        category_obj.save()
        return JsonResponse({"id": category_obj.id,
                             "name": category_obj.name})


@method_decorator(csrf_exempt, name='dispatch')
class ADSView(View):
    def get(self, request):
        """
        Получение всех объявлений
        """
        context = get_list_or_404(ADS)
        result = [{"id": item.id,
                   "name": item.name,
                   "author": item.author,
                   "price": item.price} for item in context]

        return JsonResponse(result, safe=False)

    def post(self, request):
        """
        Запись нового объявления
        """
        ads_data: dict = json.loads(request.body)

        ads_obj = ADS()
        ads_obj.name = ads_data.get('name')
        ads_obj.author = ads_data.get('author')
        ads_obj.price = ads_data.get('price')
        ads_obj.description = ads_data.get('description', '')
        ads_obj.address = ads_data.get('address')
        ads_obj.is_published = ads_data.get('is_published')

        try:
            ads_obj.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        ads_obj.save()

        return JsonResponse({"id": ads_obj.id,
                             "name": ads_obj.name})


class CategoryDetailsView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        item = self.get_object()
        return JsonResponse({"id": item.id,
                             "name": item.name})


class ADSDetailsView(DetailView):
    model = ADS

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        item = self.get_object()
        return JsonResponse({"id": item.id,
                             "name": item.name,
                             "author": item.author,
                             "price": item.price,
                             "description": item.description,
                             "address": item.address,
                             "is_published": item.is_published})
