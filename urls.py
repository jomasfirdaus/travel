from django.urls import path 

from travel import views

app_name = "travel"

urlpatterns = [
	path('lista/travel/authorization', views.listatravelautorization, name='listatravelautorization'),
	path('request/travel', views.requesttravel, name='requesttravel'),
	path('edit/request/travel/<str:id>/', views.editrequesttravel, name='editrequesttravel'),
	path('detallu/request/travel/<str:id>/', views.detallutravelrequest, name='detallutravelrequest'),
    
	path('detallu/request/travel/tab/<str:id>/<str:tab>/', views.detallutravelrequesttab, name='detallutravelrequesttab'),
	path('send/request/travel/<str:id>/', views.sendtravelrequest, name='sendtravelrequest'),
    
	path('add/car/travel/<str:id_riquest>/', views.addcarrequest, name='addcarrequest'),
	path('edit/car/travel/<str:id_item>/', views.editcarrequest, name='editcarrequest'),
	path('apaga/car/travel/<str:id_item>/', views.apagacarrequest, name='apagacarrequest'),
    
	path('add/person/travel/<str:id_riquest>/', views.addpersontraveling, name='addpersontraveling'),
	path('edit/person/travel/<str:id_item>/', views.editpersontraveling, name='editpersontraveling'),
	path('apaga/person/travel/<str:id_item>/', views.apagapersontraveling, name='apagapersontraveling'),
    
	path('add/route/travel/<str:id_riquest>/', views.addroutetraveling, name='addroutetraveling'),
	path('edit/route/travel/<str:id_item>/', views.editroutetraveling, name='editroutetraveling'),
	path('apaga/route/travel/<str:id_item>/', views.apagaroutetraveling, name='apagaroutetraveling'),
    
	path('add/mission/travel/<str:id_riquest>/', views.addmissiontraveling, name='addmissiontraveling'),
	path('edit/mission/travel/<str:id_item>/', views.editmissiontraveling, name='editmissiontraveling'),
	path('apaga/mission/travel/<str:id_item>/', views.apagamissiontraveling, name='apagamissiontraveling'),

	path('acepted/trip/request/<str:id>/<str:last>/', views.aceptedtravelautorization, name='aceptedtravelautorization'),
	path('rijected/trip/request<str:id>/', views.rijectedtravelautorization, name='rijectedtravelautorization'),
]

