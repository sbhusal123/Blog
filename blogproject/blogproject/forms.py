from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


    # custome validator: https://docs.djangoproject.com/en/2.2/ref/forms/validation/#form-and-field-validation
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        non_allowed_email = ('.edu','.abc','.asd')
        # print(type(email)) checking the data type of the email variable
        if email.endswith(non_allowed_email): # endswith is a class method defined within the class str(string)
            raise forms.ValidationError("Invalid are not accepted.")
        return email

