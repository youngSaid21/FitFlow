from django import forms
from .models import Membre
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div

class MembreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.add_input(Submit('submit', 'Enrgistrer les modifications', css_class='btn btn-primary profile-button'))

    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'email', 'tel']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'email': 'Email',
            'tel': 'Téléphone'
        }
