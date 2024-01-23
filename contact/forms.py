from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": 'escreva aqui',
            }
        ),
        label="primeiro nome",
        help_text="texto de ajuda"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #         'class': "classe-a classe-b",
        #         "placeholder": 'escreva aqui',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': "classe-a classe-b",
        #             "placeholder": 'escreva aqui'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'AB':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite AB neste campo',
                    code='invalid'
                )
            )
        return first_name
