from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        str = """<h1>Hello, World</h1>"""

        return HttpResponse(str)


class IndexView(View):
   def get(self, request: HttpRequest) -> HttpResponse:

       return render(request, 'common/index.html')
# Create your views here.
