from datetime import *
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
    today = datetime.today()
    dadosta = TravelAutorization.objects.filter(contract=request.contract, created_at__year=today.year).order_by('is_aproved')
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
    timeline = AproveTravelAutorization.objects.filter(travelautorization=id)
    context = {

        "travelautorization" : travelautorization,
        "pajina_travel" : "active",
        "timeline" : timeline,
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
    elif tab == "Route":
        dados = RouteTravel.objects.filter(travel_autorization=travelautorization)
    elif tab == "Mission":
        dados = DetailMission.objects.filter(travel_autorization=travelautorization)

    timeline = AproveTravelAutorization.objects.filter(travelautorization=id)

    context = {
        "pajina_travel" : "active",
        "travelautorization" : travelautorization,
        "dados": dados,
        "tab_"+str(tab): "active border-left-0",
        "tab" : tab,
        "timeline" : timeline,
    }
    return render(request, 'travel/detallu_travelrequest.html',context)


def sendtravelrequest(request, id):

    id = decrypt_id(id)
    today = datetime.today()

    travelautorization = TravelAutorization.objects.get(id=id)

    # car = CarRequest.objects.get(travel_autorization=travelautorization)
    # travelautorizationyear = TravelAutorization.objects.filter(created_at__year=today.year)

    if DetailMission.objects.filter(
        travel_autorization=travelautorization
        ).exists() and PersonTraveling.objects.filter(
            travel_autorization=travelautorization
            ).exists() and RouteTravel.objects.filter(
                travel_autorization=travelautorization
                ).count() > 1:
        try:
            request_trip_aprove = AproveTravelAutorization.objects.filter(travelautorization__id=id)
            request_trip_aprove.delete()
        except ObjectDoesNotExist:
            print("RequestTripAprove instance not found")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


        unique_group_names = RequestSet.objects.filter(category__name='travel',level__name='jeral')

        for group_name in unique_group_names.iterator():
            contract = Contract.objects.get(employeeuser__user__groups__name=group_name.group.name, employeeuser__user__is_active=True)
        
            addtimeline = AproveTravelAutorization()
            addtimeline.travelautorization = TravelAutorization.objects.get(id=id)
            addtimeline.contract = contract
            addtimeline.status = "Review"
            addtimeline.created_by = request.user

            try:
                addtimeline.save()

            except Exception as e:
                print(e)
                messages.success(request, 'Falhansu teknika favor manda fali')  
                return redirect('travel:listatravelautorization')

        travel_autorization = TravelAutorization.objects.get(id=id)
        travel_autorization.is_draft = False
        travel_autorization.save()
        messages.success(request, 'Pedidu Prossesa ona')  


        return redirect('travel:listatravelautorization')
    else:
        print('faila')
        messages.success(request, 'Ladauk input item balun') 
    
    return redirect('travel:listatravelautorization')