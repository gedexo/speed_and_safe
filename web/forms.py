from django import forms

from .models import Contact, ProductEnquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your name:"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Enter Your Email:",
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Enter Your Number:",
                }
            ),
            "subject":forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Subject:"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Enter Your Message:",
                }
            ),
        }

    
class ProductEnquiryForm(forms.ModelForm):
    class Meta:
        model = ProductEnquiry
        exclude = ("product",)
        fields = ["name", "email", "phone", "quantity", "message"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your name:"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Enter Your Email:",
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Enter Your Number:",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Quantity:",
                    "min": "1", 
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Enter Your Message:",
                }
            ),
        }