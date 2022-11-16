from django import forms
from .models import BookVehicle, Testimonial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyCustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(MyCustomSignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BookVehicleForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "id":"datepicker", "placeholder":"mm/dd/yyyy"}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "id":"datepicker2", "placeholder":"mm/dd/yyyy"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placholder":"Message", "class":"form-control", "rows": "5"}))
    class Meta:
        model = BookVehicle
        fields = '__all__'
        exclude = ('customer', 'vehicle',)

class TestimonialForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"placholder":"Message", "class":"form-control", "rows": "5"}))

    class Meta:
        model = Testimonial
        fields = '__all__'
        exclude = ('customer','date_sent',)
