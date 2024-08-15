from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email", required=False)
    review = forms.CharField(label="리뷰를 작성해주세요.", max_length=100, 
                             required=False,
                             widget=forms.Textarea(attrs={
                                 'class':'myform',
                                 'rows':'7',
                                 'cols':'50'})
                             )