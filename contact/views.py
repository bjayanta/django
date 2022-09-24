from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm

# Create your views here.
class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/form.html', {
            'form': form
        })

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            # print("The form is valid.")
            html = render_to_string('contact/emails/template.html', {
                'name': name,
                'email': email,
                'content': content
            })

            # send email
            send_mail('The contact form subject', 'This is the message', 'noreply@jayanta.com', ['bjayanta.neo@gmail.com'], html_message = html)

            return redirect('contact')
        else:
            form = ContactForm()

            return render(request, 'contact/form.html', {
                'form': form
            })