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

    def clean_nome(self):  # Auto aplicado, deve ser a estrutura clean_atributo
        nome = self.cleaned_data.get("nome")

        if nome:
            nome = nome.strip() # trim
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo!")
            else:
                return nome
        
    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("Senha não são iguais!")
            else:
                return senha2