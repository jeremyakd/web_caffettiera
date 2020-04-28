from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    return render(request, "contact/contact.html",{'formulario':contact_form})

