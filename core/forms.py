from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    """
    A form for registering a new user.

    Inherits from UserCreationForm and adds additional fields for email, first name, and last name.

    Attributes:
        email (forms.EmailField): Field for entering the user's email address.
        first_name (forms.CharField): Field for entering the user's first name.
        last_name (forms.CharField): Field for entering the user's last name.

    Meta:
        model (User): The user model to use for the form.
        fields (tuple): The fields to include in the form.

    Methods:
        clean_email: Custom validation method to check if the email already exists in the database.
    """

    email = forms.EmailField(max_length=250)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        """
        Custom validation method to check if the email already exists in the database.

        Returns:
            str: The cleaned email address.

        Raises:
            ValidationError: If the email already exists in the database.
        """
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email
