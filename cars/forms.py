from django import forms
from .models import CarReview
from django.forms import ModelForm

## MODEL FORM ##
class ReviewForm(ModelForm):
    class Meta:
        model = CarReview
        fields = '__all__'	# 모든 필드를 불러온다.
        #fields = ['first_name', 'last_name'] # 불러올 필드를 선택한다.

## FORM ##
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=100)
#     last_name = forms.CharField(label="Last Name", max_length=100)
#     email = forms.EmailField(label="Email", required=False)
#     review = forms.CharField(label="리뷰를 작성해주세요.", max_length=100, 
#                              required=False,
#                              widget=forms.Textarea(attrs={
#                                  'class':'myform',
#                                  'rows':'7',
#                                  'cols':'50'})
#                              )