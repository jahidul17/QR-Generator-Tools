from django import forms


class QRCodeForm(forms.Form):
    restaurant_name=forms.CharField(
        max_length=50,
        label="Title",
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Title'
        }))
    
    url=forms.URLField(
        max_length=200,
        label="URL",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Enter the URL'
        })
        )
    

