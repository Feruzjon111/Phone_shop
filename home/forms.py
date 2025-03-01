from django import forms
from .models import Phone, Comment

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['brand', 'model', 'color', 'price', 'description', 'image']

    def clean_brand(self):
        brand = self.cleaned_data.get('brand')
        if len(brand) < 2:
            raise forms.ValidationError(f"Brandni to'g'ri kiriting!!!")
        return brand

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError(f"Narxni to'g'ri kiriting!!!")
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 50:
            raise forms.ValidationError(f"Descriptionni 50 tadan ko'p bolmasligi kerak!!!")
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image is None:
            return None
        if image.size > 2*1024*1024:
            raise forms.ValidationError(f"Image 2 MB dan oshmasligi kerak!!!")
        return image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['phone', 'name', 'email', 'text']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) > 50:
            raise forms.ValidationError(f"Kommentni 50 tadan ko'p bolmasligi kerak!!!")
        return text

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError(f"Ismni to'g'ri kiriting!!!")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@gmail.com' not in email:
            raise forms.ValidationError(f"Emailni to'g'ri kiriting!!!")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 9:
            raise forms.ValidationError(f"Telefon raqami to'g'ri kiriting!!!")
        return phone
