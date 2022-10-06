from distutils.log import error
from logging import exception
from django.shortcuts import render, redirect
from ports.models import Port, Trip
from ports.forms import PortForm, TripForm
from django.contrib import messages
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect

def get_home_view(request):
    return render(request, template_name='home.html')

######## PORTS

def get_ports_view(request):
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
            return redirect(get_ports_view)
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
        return redirect(get_ports_view)
    return HttpResponseRedirect(reverse("upload_csv_page"))



def edit_port(request,id):
    port = Port.objects.get(pk=id)

    if request.method == 'GET':
            form = PortForm(instance=Port(port))
            return render(request, template_name='edit_port.html', context={'port':port, 'port_form': form})
    else:
        # try:
        form = PortForm(request.POST, instance=port)
        if form.is_valid():
            tform = form.save(commit=False)
            port = form.save()
            port.save()
            return redirect(get_ports_view)
        else:
            messages.error(request, form.errors)
            return render(request, template_name='edit_port.html', context={'port':port, 'port_form': form.data})
        # except:
        #     return redirect(get_ports_view)

    return redirect(get_ports_view)



def del_port(request,id):
    try:
        port = Port.objects.get(id=id)
        port.delete()
        return redirect(get_ports_view)
    except:
        return redirect(get_ports_view)

######## TRIPS

def get_trips_view(request):
    trips = Trip.objects.all()
    ports = Port.objects.all()
    return render(request, template_name='trips.html', context={
        'trips': trips, 'ports': ports
    })


def add_trip_page(request):
    if request.method == 'GET':
        form = TripForm()
    else:
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save()
            trip.save()
            return redirect(get_trips_view)
        else:
            messages.error(request, form.errors)
            #  TODO add error to event

            return render(request, template_name='add_trip_page.html', context={'trip_form': form.cleaned_data})

    return render(request, template_name='add_trip_page.html')


def add_trip_view(request):
    trips = Trip.objects.all()
    if request.method == 'GET':
        form = TripForm()
    else:
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save()
            trip.save()
        else:
            messages.error(request, form.errors)

            return render(request, template_name='trips.html', context={'trips': trips, 'trip_form': form.cleaned_data})

    return render(request, template_name='trips.html', context={'trips': trips, 'trip_form': form.cleaned_data})


def edit_trip(request,id):
    trip = Trip.objects.get(pk=id)

    if request.method == 'GET':
            form = TripForm(instance=Trip(trip))
            return render(request, template_name='edit_trip.html', context={'trip':trip, 'trip_form': form})
    else:
        # try:
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            tform = form.save(commit=False)
            trip = form.save()
            trip.save()
            return redirect(get_trips_view)
        else:
            messages.error(request, form.errors)
            return render(request, template_name='edit_trip.html', context={'trip':trip, 'trip_form': form.data})
        # except:
        #     return redirect(get_trips_view)

    return redirect(get_trips_view)



def del_trip(request,id):
    try:
        trip = Trip.objects.get(id=id)
        trip.delete()
        return redirect(get_trips_view)
    except:
        return redirect(get_trips_view)
