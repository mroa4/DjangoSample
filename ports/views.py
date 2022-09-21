import imp
from django.shortcuts import render, redirect
from ports.models import Port
from ports.forms import PortForm
from django.contrib import messages

from django.http import HttpResponse


# Create your views here.


def ports_view(request):
    ports = Port.objects.all()
    return render(request, 'ports.html', {
        'ports': ports
    })


def add_port_page(request):
    if request.method == 'GET':
        form = PortForm()
    else:
        form = PortForm(request.POST)
        if form.is_valid():
            port = form.save()
            port.save()
            return redirect(ports_view)
        else:
            messages.error(request, form.errors)
            #  TODO add error to event

            return render(request, template_name='add_port_page.html', context={'port_form': form.cleaned_data})

    return render(request, template_name='add_port_page.html')


def add_port_view(request):
    ports = Port.objects.all()
    if request.method == 'GET':
        form = PortForm()
    else:
        form = PortForm(request.POST)
        if form.is_valid():
            port = form.save()
            port.save()
        else:
            messages.error(request, form.errors)

            return render(request, template_name='ports.html', context={'ports': ports, 'port_form': form.cleaned_data})

    return render(request, template_name='ports.html', context={'ports': ports, 'port_form': form.cleaned_data})
