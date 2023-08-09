from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWorld(View):
    def get(self, request):
        data = {
            "name": "Dinz kramer",
            "years": 26,
            "Languages": ["Python", "Javascript", "PHP", "Typescript"]
            
        }
        return render(request, "hello_world.html", context=data)