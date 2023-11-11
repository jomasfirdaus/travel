from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
# from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Temporary,ChangeFamily
# from population.utils import getnewidp,getnewidf
# from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Changefamily_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

# from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import date
from django.http import JsonResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from rekrutamentu.forms import FileUploadForm
from travel.models import *
from custom.models import RequestSet

from settingapps.utils import  decrypt_id, encrypt_id
from django.core.paginator import Paginator

from django.utils import translation
from django.utils import timezone
from datetime import datetime

from django.contrib.auth.models import User, Group

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from travel.forms import *
from employee.models import EmployeeUser
import logging
from django.core.exceptions import ObjectDoesNotExist





def addmissiontraveling(request,id_riquest):
    encript_id_riquest = id_riquest
    id_riquest = decrypt_id(id_riquest)
    travelautorization = TravelAutorization.objects.get(id=id_riquest)

    form = MissionTravelingForm()

    if request.method == 'POST':
        form = MissionTravelingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.travel_autorization = travelautorization
            instance.status = "Pendente"
            instance.save()
            messages.success(request, 'Request created successfully.')  # Success message
            return redirect('travel:detallutravelrequest', id = encript_id_riquest )
        else:
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
            return redirect('travel:addmissiontraveling', id_riquest = encript_id_riquest)

    context = {
        "form" : form,
        "pajina_travel" : "active",
            }
    return render(request, 'travel/addmissiontraveling.html',context)



def editmissiontraveling(request,id_item):


    dec_id_item = decrypt_id(id_item)
    itemedit = DetailMission.objects.get(id=dec_id_item)

    id_request = encrypt_id(str(itemedit.travel_autorization.id))

    form = MissionTravelingForm(instance = itemedit)

    if request.method == 'POST':
        form = MissionTravelingForm(request.POST, instance = itemedit)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Request created successfully.')  # Success message
            return redirect('travel:detallutravelrequest', id = id_request )
        else:
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
            return redirect('travel:addmissiontraveling', id_item = id_item)

    context = {
        "form" : form,
        "pajina_travel" : "active",
            }
    return render(request, 'travel/addmissiontraveling.html',context)


def apagamissiontraveling(request, id_item):
    id_item = decrypt_id(id_item)
    itemapaga = DetailMission.objects.get(id=id_item)
    id_request = encrypt_id(str(itemapaga.travel_autorization.id))
    item = itemapaga
    item.delete(user=request.user)
    return redirect('travel:detallutravelrequest', id = id_request )


def aproveditempurchase(request, id_item):
    id_item = decrypt_id(id_item)
    itemprosses = ItemRequest.objects.get(id=id_item)
    id_request = encrypt_id(str(itemprosses.request_order.id))
    item = itemprosses
    item.status = "Aproved"
    item.save()
    return redirect('purchase_request:detallupurchaserequest', id = id_request )

def rijectitempurchase(request, id_item):
    id_item = decrypt_id(id_item)
    itemprosses = ItemRequest.objects.get(id=id_item)
    id_request = encrypt_id(str(itemprosses.request_order.id))
    item = itemprosses
    item.status = "Rejected"
    item.save()
    return redirect('purchase_request:detallupurchaserequest', id = id_request )


def deliveritempurchase(request, id_item):
    id_item = decrypt_id(id_item)
    itemprosses = ItemRequest.objects.get(id=id_item)
    id_request = encrypt_id(str(itemprosses.request_order.id))
    item = itemprosses
    item.is_delivery = True
    item.save()
    return redirect('purchase_request:detallupurchaserequest', id = id_request )
