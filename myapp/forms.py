from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import authenticate,get_user_model


class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # import pdb;pdb.set_trace()
        self.fields['username'].required = True

    class Meta:
        model =UserProfile
        fields = ['user','username','profile_image','bio','first_name','last_name','hobby']



class SignUpForm(UserCreationForm):
    # import pdb;pdb.set_trace()
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'inputbody in1'}))
    # first_name = forms.CharField(max_length=32,widget=forms.TextInput(attrs={'class': 'inputbody in1', 'placeholder': 'First Name'}),  help_text='First name')
    # last_name=forms.CharField( max_length=32,widget=forms.TextInput(attrs={'class': 'inputbody in1', 'placeholder': 'Last Name'}), help_text='Last name')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'inputbody in2', 'placeholder': 'Email'}), help_text='Enter a valid email address')
    password1=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'inputbody in2', 'placeholder': 'Password'}))
    password2=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'inputbody in2', 'placeholder': 'Password Again'}))


    class Meta:
        model = User
        fields = ("username","email",'password1','password2')




class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user_name','description','pic','date_posted']
        # read_only_fields = ("user_name",)

    



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'inputtext'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class': 'inputtext', 'placeholder': 'Password'}))



class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        # import pdb;pdb.set_trace()
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified email address!")
        return email



class UserloginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())


    def clean(self,*args,**kwargs):
        # import pdb;pdb.set_trace()
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)

            if not user:
                raise forms.ValidationError('user does not exist')

            
            if not user.check_password(password):
                raise forms.ValidationError('incorrect password')

        return super(UserloginForm,self).clean(*args,**kwargs)
        
user = get_user_model()
