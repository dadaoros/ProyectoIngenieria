from django import forms
from miscelanea.models import Persona, Producto, Proveedor,Categoria

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
    class Meta:
        model = Producto
        fields = ('numeroReferencia','nombreProducto','marca','existencias','existenciaMinima','descripcion','precio','proveedor','categorias')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombreCategoria',)

class BuscarProductoForm(forms.Form):
    numeroReferencia = forms.CharField(max_length=15,widget=forms.NumberInput,label='numeroRef',required=False)
    nombreProducto = forms.CharField(max_length=10,widget=forms.TextInput,label='nombre',required=False)
    marca = forms.CharField(max_length=15,widget=forms.TextInput,label='marca',required=False)     
    
