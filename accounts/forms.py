from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    User registration form without verbose password help texts.
    Keeps all default validation; only hides help_texts.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2")
        # Clear default help texts defined on the model/meta
        help_texts = {field: "" for field in fields}

    def __init__(self, *args, **kwargs):
        """
        Also clear the dynamic help_text that Django attaches
        to password fields from password validators.
        """
        super().__init__(*args, **kwargs)
        for name in ("username", "password1", "password2"):
            if name in self.fields:
                self.fields[name].help_text = ""


