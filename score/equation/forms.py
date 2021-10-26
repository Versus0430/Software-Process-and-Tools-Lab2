from django import forms


class EquationForm(forms.Form):
    EQ_input = forms.CharField(max_length=128, required=True)


class UserForm(forms.Form):
    US_account = forms.CharField(max_length=128, required=True)
    US_password = forms.CharField(max_length=128, required=True)
