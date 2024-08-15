from django import forms
from .models import CarReview
from django.forms import ModelForm

## MODEL FORM ##
class ReviewForm(ModelForm):
    class Meta:
        model = CarReview
        fields = '__all__'	# 모든 필드를 불러온다.
        #fields = ['first_name', 'last_name'] # 불러올 필드를 선택한다.

        labels = {
            'first_name': "YOUR FIRST NAME",
            'last_name': "YOUR LAST NAME",
            'stars': "Rating"
        }

        error_messages = {
            'stars': {
                'min_value':"Min Value is 1",
                'max_value':"Max Value is 5",
            }
        }

        # widgets = {
        #     'stars': forms.NumberInput(attrs={
        #         'max': '5',    # For maximum number
        #         'min': '0',    # For minimum number
        #     }),
        # }

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