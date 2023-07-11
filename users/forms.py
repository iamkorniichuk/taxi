from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model


class LogInForm(AuthenticationForm):
    ...


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("phone", "password1", "password2")

    def save(self):
        model = self.Meta.model
        user = model.objects.create_user(
            self.cleaned_data["phone"], self.cleaned_data["password1"]
        )
        return user


class UpdateForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "image")
