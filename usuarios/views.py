from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth, messages

from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome"].value()
            senha = form["senha"].value() 

            usuario = auth.authenticate(
                request = request, 
                username = nome,
                password = senha
            )
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                return redirect("index")
            else:
                messages.error(request, "Erro ao efetuar login!")
                return redirect("login")

    return render(request, "usuarios/login.html", {"form" : form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha1"].value() != form["senha2"].value():
                messages.error(request, "Senha não são iguais!")
                return redirect("cadastro")
            
            nome = form["nome"].value()
            email = form["email"].value()
            senha1 = form["senha1"].value()

            if User.objects.filter(username = nome).exists():
                messages.error(request, "Usuário já existe!")
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username = nome, email = email, password = senha1
            )

            usuario.save()
            messages.success(request, f"{nome} cadastrado com sucesso!")
            return redirect("login")
        
    return render(request, "usuarios/cadastro.html", {"form" : form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    
    return redirect("login")