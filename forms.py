from django import forms
from rekrutamentu.models import UserApplication, UserAttachment
from django.forms import inlineformset_factory
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Button, Div, Field
from travel.models import *






class RequestTravelForm(forms.ModelForm):
    class Meta:
        model = TravelAutorization
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['contract','is_draft']

    def __init__(self, *args, **kwargs):
        super(RequestTravelForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('project_name', css_class='col-md-12'),

            ),

            Row(
                Column('purpose_of_travel', css_class='col-md-12'),

         
            ),
            Row(

                Column('departure_date', css_class='col-md-6'),
                Column('place_of_departure', css_class='col-md-6'),
            ),


            Row(
                Column('return_date', css_class='col-md-6'),
            ),
            
            Row(
                Column('description', css_class='col-md-6'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['project_name'].widget.attrs['class'] = 'form-control'
        self.fields['purpose_of_travel'].widget.attrs['class'] = 'form-control'
        self.fields['departure_date'].widget.input_type = 'date'
        self.fields['place_of_departure'].widget.attrs['class'] = 'form-control'
        self.fields['return_date'].widget.input_type = 'date'
        self.fields['description'].widget.attrs['class'] = 'form-control'


class CarRequestForm(forms.ModelForm):
    class Meta:
        model = CarRequest
        fields = ['car', 'driver']

    def __init__(self, *args, **kwargs):
        super(CarRequestForm, self).__init__(*args, **kwargs)

        # Ambil semua mobil dan pengemudi yang belum terdaftar di CarRequest
        existing_cars = CarRequest.objects.values_list('car', flat=True)
        existing_drivers = CarRequest.objects.values_list('driver', flat=True)

        # Filter querysets untuk menampilkan mobil dan pengemudi yang belum terdaftar
        self.fields['car'].queryset = Car.objects.exclude(id__in=existing_cars)
        self.fields['driver'].queryset = Employee.objects.exclude(id__in=existing_drivers)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                
                Column('car', css_class='col-md-6'),
            ),


            Row(
                Column('driver', css_class='col-md-12'),
            ),
      

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['car'].widget.attrs['class'] = 'form-control'
        self.fields['driver'].widget.attrs['class'] = 'form-control'
  


class PersonTravelingForm(forms.ModelForm):
    class Meta:
        model = PersonTraveling
        fields = ['employee']

    def __init__(self, *args, **kwargs):
        super(PersonTravelingForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                
                Column('employee', css_class='col-md-6'),
            ),
      

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['employee'].widget.attrs['class'] = 'form-control'
        


class RouteTravelForm(forms.ModelForm):
    class Meta:
        model = RouteTravel
        fields = ['munisipiu','deskrisaun']

    def __init__(self, *args, **kwargs):
        super(RouteTravelForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                
                Column('munisipiu', css_class='col-md-6'),
            ),
            Row(
                
                Column('deskrisaun', css_class='col-md-12'),
            ),
      

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['munisipiu'].widget.attrs['class'] = 'form-control'
        self.fields['deskrisaun'].widget.attrs['class'] = 'form-control'
        


class MissionTravelingForm(forms.ModelForm):
    class Meta:
        model = DetailMission
        fields = ['mission']

    def __init__(self, *args, **kwargs):
        super(MissionTravelingForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                
                Column('mission', css_class='col-md-6'),
            ),
      

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['mission'].widget.attrs['class'] = 'form-control'


class TravelRequestAproveForm(forms.ModelForm):
    class Meta:
        model = AproveTravelAutorization
        fields = ['description']

    def __init__(self, *args, **kwargs):
        super(TravelRequestAproveForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

  


            Row(
                Column('description', css_class='col-md-12'),
            ),
      

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
                css_class='text-right',
            ),
        )


        self.fields['description'].widget.attrs['class'] = 'form-control'