from django import forms
from miscelanea.models import Persona, Producto

class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput,label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
    
        
class PersonaForm(forms.ModelForm):
    username = forms.CharField(max_length=15,widget=forms.TextInput,label='Usuario')
    password1 = forms.CharField(max_length=10,widget=forms.PasswordInput,label='Contrasena')
    password2 = forms.CharField(max_length=10,widget=forms.PasswordInput,label='Repita la contrasena')
    class Meta:
        model = Persona
        fields = ('nombre','apellido','correo','direccion','idPersona','telefono')
    def clean_password(self):
        password1 = self.cleaned_data.get('password1', '')
        password2 = self.cleaned_data.get('password2', '')
        if password1==password2:
            return password2
        else:
            return None

class ProductoForm(forms.ModelForm):
    username = forms.CharField(max_length=15,widget=forms.TextInput,label='Usuario')
    password1 = forms.CharField(max_length=10,widget=forms.PasswordInput,label='Contrasena')
    password2 = forms.CharField(max_length=10,widget=forms.PasswordInput,label='Repita la contrasena')
    class Meta:
        model = Producto
        fields = ('numeroReferencia','nombreProducto','marca','existencias','existenciaMinima','descripcion','precio')

        
    
