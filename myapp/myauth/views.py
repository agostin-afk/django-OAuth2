from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userAuth

def login_view(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = userAuth.objects.get(username=username)
            if user.check_password(password):
               
                return redirect('home') 
                error_message = "Senha incorreta"
        except userAuth.DoesNotExist:
            error_message = "Usuário não encontrado"
    
    return render(request, 'userAuth.html', {'error_message': error_message})