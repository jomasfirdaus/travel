from django.shortcuts import render,redirect
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from travel.models import TravelAutorization, AproveTravelAutorization
from travel.forms import TravelRequestAproveForm



def aceptedtravelautorization(request, id, last):
    form = TravelRequestAproveForm()

    last = decrypt_id(last)

    iddecript = decrypt_id(id)
    dados = AproveTravelAutorization.objects.get(id=iddecript)
    idrequest = TravelAutorization.objects.get(id = dados.travelautorization.id)
    idrequest2 =  encrypt_id(str(idrequest.id))

    if request.method == 'POST':
        form = TravelRequestAproveForm(request.POST, instance = dados )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = "Acepted"
            instance.save()
            if last == 'last':
                idrequest.is_aproved=True
                idrequest.save()
            messages.success(request, 'Rejeita ho susesu')  # Success message
            return redirect('travel:detallutravelrequest', id = idrequest2)
        else:
            messages.success(request, 'Rejeita Faila')  # Success message
            return redirect('travel:detallupurchaserequest', id = idrequest2)


    context = {
        "form" : form,
        "asaun" : "aceita",
        "dados" : dados ,
        "pajina_travel" : "active",
            }
    return render(request, 'travel/travel__actiondescription.html',context)


def rijectedtravelautorization(request, id):

    form = TravelRequestAproveForm()
    iddecript = decrypt_id(id)
    dados = AproveTravelAutorization.objects.get(id=iddecript)
    idrequest = TravelAutorization.objects.get(id = dados.travelautorization.id)
    idrequest2 =  encrypt_id(str(idrequest.id))

    if request.method == 'POST':
        form = TravelRequestAproveForm(request.POST, instance = dados )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = "Rejected"
            instance.save()
            messages.success(request, 'Rejeita ho susesu')  # Success message
            return redirect('travel:detallupurchaserequest', id = idrequest2)
        else:
            messages.success(request, 'Rejeita Faila')  # Success message
            return redirect('travel:detallupurchaserequest', id = idrequest2)


    context = {
        "form" : form,
        "asaun" : "rejeita",
        "dados" : dados ,
        "pajina_travel" : "active",
            }
    
    
    return render(request, 'travel/travel__actiondescription.html',context)




