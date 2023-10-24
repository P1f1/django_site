from .models import Review, Profile
from django import forms
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['text', 'image']
        labels = {'text': '', 'image': ''}
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Ваш отзыв', 'style': 'width: 100%; height: 100px'}),
            'image': forms.FileInput(),
        }


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтори пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'Ник', 'email': 'Эл.почта'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с такой почтой уже существует')
        return email


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'Ник', 'email': 'Эл.почта'}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
        labels = {'date_of_birth': 'День рождения', 'photo': 'Фото'}
        widgets = {
            'date_of_birth': forms.DateInput(format='%d-%m-%Y',
                                             attrs={'placeholder': 'дд.мм.гггг'}),
        }
