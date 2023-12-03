from django import forms

class LoginForms(forms.Form):
    nome = forms.CharField(
        label = "Nome de login",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    senha = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome = forms.CharField(
        label = "Nome de cadastro",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    email = forms.EmailField(
        label = "Email",
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@gmail.com"
            }
        )
    )
    senha1 = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha"
            }
        )
    )
    senha2 = forms.CharField(
        label = "Confirmação de senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha novamente"
            }
        )
    )