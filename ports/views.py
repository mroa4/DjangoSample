from distutils.log import error
import imp
from logging import exception
from django.shortcuts import render, redirect
from ports.models import Port
from ports.forms import PortForm
from django.contrib import messages
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect


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

def upload_csv_page(request):
    data = {}
    if "GET" == request.method:
        return render(request, "upload_csv.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("upload_csv_page"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("upload_csv_page"))

        file_data = csv_file.read().decode("utf-8")        

        lines = file_data.split("\n")
        #loop over the lines and save them in db. If error , store as string and then display
        fine = True
        for line in lines:                        
            fields = line.split(",")
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["temp"] = fields[1]
            data_dict["latitude"] = fields[2]
            data_dict["longitude"] = fields[3]
            try:
                form = PortForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    messages.error(request, form.errors.as_json())
                    fine = False
            except Exception as e:
                messages.error(request,"Unable to add port. "+repr(e))
                pass
    except Exception as e:
        messages.error(request,"Unable to upload file. "+repr(e))
    if fine:
        return redirect(ports_view)
    return HttpResponseRedirect(reverse("upload_csv_page"))