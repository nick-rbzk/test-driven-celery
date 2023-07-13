from django import forms


class YourForm(forms.Form):
    email = forms.EmailField(max_length=100)
    username = forms.CharField(max_length=100)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
           visible.field.widget.attrs['class'] = 'form-control'
           