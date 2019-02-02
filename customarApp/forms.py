from django import forms
from django.utils.translation import gettext_lazy
from django.core.validators import EmailValidator

from .models import CustomarRegistration

class CustomarRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomarRegistration
        fields = ['name', 'email', 'username', 'password_1', 'password_2',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password_1': forms.PasswordInput(attrs={'class': 'form-control', 'minlength': 8}),
            'password_2': forms.PasswordInput(attrs={'class': 'form-control', 'minlength': 8}),
        }
        # labels = {
        #     'first_name': gettext_lazy('FIRST NAME'),
        #     'password_2': gettext_lazy('PASSWORD REPEAT')
        # }
        help_texts = {
            'first_name': gettext_lazy('Max Lenth 20 words'),
            'password_1': gettext_lazy('Min 8 Lenth, combine special @ character, upper and lower case letter'),
            'password_2': gettext_lazy('Preview Password Repeat'),
        }
        error_messages = {
            'first_name': {
                'max_length': gettext_lazy("This writer's name is too long."),
            },
        }
        def clean_data(self):
            user = self.clean_data('username')
            try:
                match = CustomarRegistration.objects.get(username=user)
            except:
                return self.clean_data('username')
            raise forms.ValidationError('User name already Exists')

        def clean_data(self):
            email = self.clean_data('email')
            try:
                EmailValidator(email)
            except:
                raise forms.ValidationError('Email is not in correct format')
            return self.clean_data('email')

        def clean_data(self):
            password = self.clean_data('password_1')
            password2 = self.clean_data('password_2')
            minLen = 8
            if password == password2:
                if len(password) < minLen:
                    raise forms.ValidationError('Password is too Short, Try %d or more Character' %minLen)
                if password.isdigit():
                    raise forms.ValidationError('Password Should not be all numuric ')
            else:
                raise forms.ValidationError('Password Is not match')