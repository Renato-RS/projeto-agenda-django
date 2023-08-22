from django.shortcuts import render, redirect
from contact.forms import ContactForm
# Create your views here.


def create(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )
