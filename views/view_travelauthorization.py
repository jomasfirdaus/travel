from django.shortcuts import render,redirect
from travel.models import *
from custom.models import RequestSet
from django.contrib import messages
from settingapps.utils import  decrypt_id
from django.contrib.auth.models import User
from employee.models import EmployeeUser
from travel.forms import RequestTravelForm
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here

def listatravelautorization(request):
    dadosta = TravelAutorization.objects.filter(contract=request.contract).order_by('-id')
    context = {
        "dadosta" : dadosta,
        "pajina_travel" : "active",
    }
    return render(request, 'travel/lista_travel.html',context)

def requesttravel(request):
    data = EmployeeUser.objects.get(user=request.user.id, user__is_active = True)
    form = RequestTravelForm()

    if request.method == 'POST':
        form = RequestTravelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contract = Contract.objects.get(employeeuser=data)
            instance.created_by = User.objects.get(id=request.user.id) 
            instance.save()
            messages.success(request, 'Request created successfully.')  # Success message
            return redirect('travel:listatravelautorization')
        else:
            error_messages = []  # Initialize an empty list to store custom error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            print(str(error_messages))
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
            return redirect('travel:requesttravel')

    context = {
        "form" : form,
        "pajina_travel" : "active",
        "data": data,
            }
    return render(request, 'travel/request_travelrequest.html',context)


def editrequesttravel(request, id):
    id = decrypt_id(id)
    travelautorization = TravelAutorization.objects.get(id=id)
    form = RequestTravelForm(instance=travelautorization)  # Menggunakan instance=travelautorization

    if request.method == 'POST':
        form = RequestTravelForm(request.POST, instance=travelautorization)  # Menggunakan instance=travelautorization
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Request updated successfully.')  # Pesan sukses
            return redirect('travel:listatravelautorization')
        else:
            messages.error(request, 'There was an error. Please correct the form.')  # Pesan kesalahan
            return redirect('travel:requesttravel')

    context = {
        "form": form,
        "pajina_travel": "active",
    }
    return render(request, 'travel/request_travelrequest.html', context)


def detallutravelrequest(request, id):
    id = decrypt_id(id)
    travelautorization = TravelAutorization.objects.get(id=id)
    # timeline = RequestOrderAprove.objects.filter(request_order=id)
    context = {

        "travelautorization" : travelautorization,
        "pajina_travel" : "active",
        # "timeline" : timeline,
    }
    return render(request, 'travel/detallu_travelrequest.html',context)


def detallutravelrequesttab(request, id, tab):
    id = decrypt_id(id)
    travelautorization = TravelAutorization.objects.get(id=id)
    dados = None
    if tab == 'Car':
        dados = CarRequest.objects.filter(travel_autorization=travelautorization)
    elif tab == 'Person':
        dados = PersonTraveling.objects.filter(travel_autorization=travelautorization)
    elif tab == "Tour":
        dados = RouteTravel.objects.filter(travel_autorization=travelautorization)
    elif tab == "Mission":
        dados = DetailMission.objects.filter(travel_autorization=travelautorization)

    # timeline = RequestOrderAprove.objects.filter(request_order=id)

    context = {
        "pajina_travel" : "active",
        "travelautorization" : travelautorization,
        "dados": dados,
        "tab_"+str(tab): "active border-left-0",
        "tab" : tab,
        # "timeline" : timeline,
    }
    return render(request, 'travel/detallu_travelrequest.html',context)