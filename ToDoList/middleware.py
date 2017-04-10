# __author__ = 'lius'

from django.http import HttpResponse
from django.shortcuts import render

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class CheckVersionsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'rv:11.0' in request.META["HTTP_USER_AGENT"]:
            return render(request,"upgrade.html")
        return None

# from django.http import HttpResponse
#
# class CheckVersionsMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if 'Chrome' in request.META["HTTP_USER_AGENT"]:
#             print("AAAAAAAAAAAAAA")
#         response = self.get_response(request)
#
#         return response