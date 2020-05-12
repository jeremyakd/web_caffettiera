from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse # necesario para volver al template de contacto
from django.core.mail import EmailMessage

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Si esta todo bien:
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                'De {} <{}> \n Escribió: \n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['jeremyakd@gmail.com'],
                reply_to=[email],
            )
        try:
            email.send()
            return redirect('respuesta/'+'?ok')
            # return redirect(reverse('contact')+"?ok") < ==== vuelve a la misma pagina
        except:
            return redirect('respuesta/'+'?fail')
    return render(request, "contact/contact.html",{'formulario':contact_form})

def respuesta(request):#Opcional para redirigir a esta pagina
    return render(request, 'contact/respuesta.html')