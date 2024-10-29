from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'numero_de_telefono', 'fecha_de_nacimiento', 'ubicacion', 'biografia']
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary mt-2'))
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-2'),
                Column('numero_de_telefono', css_class='form-group col-md-6 mb-2'),
            ),
            Row(
                Column('fecha_de_nacimiento', css_class='form-group col-md-6 mb-2'),
                Column('ubicacion', css_class='form-group col-md-6 mb-2'),
            ),
            'biografia',
        )



class ActivateForm(forms.Form):
    codigo_de_activacion = forms.CharField(max_length=12, min_length=12, required=True)

    def __init__(self, *args, **kwargs):
        super(ActivateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Activar', css_class='btn-primary mt-2'))
        self.helper.layout = Layout(
            Row(
                Column('codigo_de_activacion', css_class='form-group col-md-12 mb-0'),
            ),
        )
