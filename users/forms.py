import django
from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms as django_forms

User = get_user_model()

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update({
        "duplicate_username": _("This user ID gas already been taken.")
    })

    class Meta(forms.UserCreationForm.Meta):
        model = User
    
    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_user_id"])

class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'password']

        labels = {
            'username': "ID",
            'name': '성명',
            'password': '비밀번호'
        }

        widgets = {
            'password': django_forms.PasswordInput(),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user