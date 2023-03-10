import re

from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from home.models import Terms
from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def sign_in(request):
    form = UserLoginForm()
    if request.method == 'POST':
    
        username = request.POST['username']
        password = request.POST['password']

        if username =="" or password == "":
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return render(request,'users/sign_in.html',{'form': form})
        
        user = User.objects.filter(username=username)
        if user.exists():
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                userid = user.id
                if Terms.objects.filter(user_id=userid).exists():
                    return redirect('home')
                else:
                    return redirect('terms')
        else:
            messages.error(request,'Usuário não cadastrado')
            return render(request,'users/sign_in.html',{'form': form})
    return render(request,'users/sign_in.html',{'form': form})


def sign_up(request):
    signUpForms = UserRegistrationForm()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        repeatPassWord = request.POST['password2']
        
        pw = verifica_senha(password)
        
        if  pw['status'] == 0:
            messages.error(request,pw['message'])
            return render(request,'users/sign_up.html',{'form':signUpForms})
        
        if not first_name.split():
            messages.error(request,"seu nome esta em branco ou invalido")
            return render(request,'users/sign_up.html',{'form':signUpForms})
        
        if password != repeatPassWord:
            messages.error(request,"as senhas não conferem!")
            return render(request,'users/sign_up.html',{'form':signUpForms})
        
        #autenticar se usuario ja tem cadastro no banco de dados 
        if User.objects.filter(email=email).exists():
            messages.error(request,"esse E-Mail já está cadastrado")
            return render(request,'users/sign_up.html',{'form':signUpForms})
                #autenticar se o userName ja tem cadastro no banco de dado
        
        if len(username.split()) > 1:
            messages.error(request,"userName não pode ter espaços")
            return render(request,'users/sign_up.html',{'form':signUpForms})
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"esse userName já está cadastrado")
            return render(request,'users/sign_up.html',{'form':signUpForms})
        
        try:
            if len(first_name.split()) > 1:
                messages.error(request,"O campo primeiro nome não pode ter espaços e nem seu nome completo")
                return render(request,'users/sign_up.html',{'form':signUpForms})
            else:
                User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password)
                messages.success(request,f"Bem vindo, {first_name} {last_name}, fico feliz que você escolheu o CoinControl para tomar conta do seu dinheiro!")
                return render(request,'users/sign_in.html',{'form':UserLoginForm()})
        except:
            messages.error(request,"Problemas na criação do seu cadastro, por gentileza atualize a pagina e tente novamente")
            return render(request,'users/sign_up.html',{'form':signUpForms})
    else:
        return render(request,'users/sign_up.html',{'form':signUpForms})
def sign_out(request):
    auth.logout(request)
    messages.error(request,'Espero ter ajudado!')
    return render(request,'users/sign_in.html',{'form':UserLoginForm()})


def verifica_senha(senha):
    """
    Verifica se a senha atende a alguns requisitos mínimos, como ter pelo menos 8 caracteres,
    uma letra maiúscula, um número e um caractere especial.
    Retorna True se a senha é válida e False caso contrário.
    """
    if len(senha) < 8:
        return {'status':0,'message':'Senha menor que 8 caracteres.'}

    if not re.search(r"[A-Z]", senha):
        return {'status':0,'message':'A senha deve possuir uma ou mais letras maiúsculas'}

    if not re.search(r"\d", senha):
        return {'status':0,'message':'Senha invalida'}

    if not re.search(r"[!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", senha):
        return {'status':0,'message':'A senha deve possuir um ou mais caractere especial.'}

    return {'status':1}