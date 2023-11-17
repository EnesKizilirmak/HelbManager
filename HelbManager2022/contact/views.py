from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import FormContact

def icontact(request):
    if request.method == 'POST':
        form = FormContact(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('contact/emails/contactform.html', {
                'name' : name,
                'email': email,
                'message': message
            })

            send_mail('The contact subject', 'This is message', 'noreply@KizilirmakEnes.com', ['helbmanager2022@gmail.com'], html_message=html )
            
            return redirect('contact')
    else:
        form = FormContact()

    return render(request, 'contact/contact.html', {
        'form': form
    })
    

#Source Code With Stein (Rapport Bibliographie)