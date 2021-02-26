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
        "duplicate_user_id": _("This user ID gas already been taken.")
    })

    class Meta(forms.UserCreationForm.Meta):
        model = User
    
    def clean_user_id(self):
        user_id = self.cleaned_data["user_id"]

        try:
            User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return user_id

        raise ValidationError(self.error_messages["duplicate_user_id"])

class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'password']