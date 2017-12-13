# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Addresses
from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect

from .forms import ContactForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main_app/index.html'
    context_object_name = 'addresses'
    paginate_by = 4

    def get_queryset(self):
        return Addresses.objects.all()

class DetailView(generic.DetailView):
    model = Addresses
    template_name = 'main_app/detail.html'

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('main_app:index'))
    else:
        form = ContactForm()
        return render(request, 'main_app/addcontact.html', {'form': form})
