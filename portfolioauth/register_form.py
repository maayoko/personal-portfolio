import django.forms as forms


class RegisterForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=100)
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(label="Password", min_length=8, required=True)
    password_1 = forms.CharField(
        label="Confirm Password", min_length=8, required=True)
    email = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Phone number", required=False)
