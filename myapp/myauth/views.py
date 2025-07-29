from django.shortcuts import render

from .models import userAuth


def list_view(request):
    context ={}
    context["dataset"] = userAuth.objects.all()
        
    return render(request,)