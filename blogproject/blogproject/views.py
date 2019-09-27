from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    return render(request,'home.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # form.cleaned_data # preventing from XSS, sql_injection, ...
        print(form.cleaned_data["email"])
        form = ContactForm()
    return render(request,'contact.html',{'form':form})
