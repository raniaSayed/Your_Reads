from django.http import HttpResponse
from django.http import JsonResponse
import json

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object
class ViewMiddleware(MiddlewareMixin):
    def process_request(self,request):
        request.dept = "OS"
        # return JsonResponse(request.body)
        return None
