from cProfile import label
from django import forms

def makehours():
    hours = []
    for i in range(24):
        hours.append(("{}:00".format(i),"{}:00".format(i)))
    return hours

HOURS = makehours()

OPERATION_TYPE = [
    ('PPA','PPA'),
    ('On-site generation', 'On-Site Generation')
]

PROFILE_CHOICES = [
    ('24/7','24/7'),
    ('customized','Customized'),
]

ELECTROLYZER_CHOICES = [
    ('pem','PEM'),
    ('alk','ALK'),
    ('soec','SOEC'),
]

WATER_TYPE_CHOICES = [
    ('tap','Tap Water'),
    ('demi','Deionized-demi Water'),
]

class TechnicalDesignForm(forms.Form):
    # Project assessment
    project_name = forms.CharField(max_length=30, label="Project Name", required=True, initial="Project")
    location = forms.CharField(max_length=30, label="Location", required=True)
    cod = forms.IntegerField(min_value=2000, label="Start of production (Year)", initial=2025, required=True)
    horizon = forms.IntegerField(min_value=1, label="Years of operation", initial=20, required=True)
    op_type = forms.ChoiceField(choices=OPERATION_TYPE, label="Operation type", initial="PPA", required=True, widget=forms.Select(attrs={'class':'form-control','id':'op_type'}))
    # If PPA:
    ppa_type = forms.ChoiceField(choices=PROFILE_CHOICES, label="PPA type", initial="24-jul", widget=forms.Select(attrs={'class':'form-control'}))
    nom_power = forms.IntegerField(max_value=100,min_value=1, label="Nominal power (MW)", initial=10)
    # If customized:
    customized_from = forms.ChoiceField(choices=HOURS, label="From:", initial="8:00", widget=forms.Select(attrs={'class':'form-control'}))
    customized_to = forms.ChoiceField(choices=HOURS, label="To:", initial="18:00", widget=forms.Select(attrs={'class':'form-control'}))
    # Electrolyzer:
    elec_type = forms.ChoiceField(choices=ELECTROLYZER_CHOICES, label="Electrolyzer type", initial="PEM", widget=forms.Select(attrs={'class':'form-control'}))
    elec_size = forms.IntegerField(min_value=1, max_value=100, label="Nominal power (MW)", initial=10)

class TechnicalDesignForm2(forms.Form):
    # Project assessment
    project_name = forms.CharField(max_length=30, label="Project Name", required=True, initial="Project")
    location = forms.CharField(max_length=30, label="Location", required=True)
    cod = forms.IntegerField(min_value=2000, label="Start of production (Year)", initial=2025, required=True)
    horizon = forms.IntegerField(min_value=1, label="Years of operation", initial=20, required=True)
    op_type = forms.ChoiceField(choices=OPERATION_TYPE, label="Operation type", initial="PPA", required=True, widget=forms.RadioSelect(attrs={'id':'op_type'}))
    # If PPA:
    ppa_type = forms.ChoiceField(choices=PROFILE_CHOICES, label="PPA type", initial="24-jul", widget=forms.Select(attrs={'class':'form-control'}))
    nom_power = forms.IntegerField(max_value=100,min_value=1, label="Nominal power (MW)", initial=10)
    # If customized:
    customized_from = forms.ChoiceField(choices=HOURS, label="From:", initial="8:00", widget=forms.Select(attrs={'class':'form-control'}))
    customized_to = forms.ChoiceField(choices=HOURS, label="To:", initial="18:00", widget=forms.Select(attrs={'class':'form-control'}))
    # Electrolyzer:
    elec_type = forms.ChoiceField(choices=ELECTROLYZER_CHOICES, label="Electrolyzer type", initial="PEM", widget=forms.Select(attrs={'class':'form-control'}))
    elec_size = forms.IntegerField(min_value=1, max_value=100, label="Nominal power (MW)", initial=10)


class EconomicDesignForm(forms.Form):
    # Costs
    energy_cost = forms.FloatField(min_value=1, max_value=100, label="Energy cost [USD/MWh]", initial=50, required=True)
    water_cost = forms.FloatField(min_value=1, max_value=100, label="Water cost [USD/m3]", initial=3, required=True)
    water_type = forms.ChoiceField(choices=WATER_TYPE_CHOICES, label="Water type", initial="TAP", widget=forms.Select(attrs={'class':'form-control'}))
    elec_cost = forms.FloatField(min_value=1, max_value=100, initial=1.2, label="Electrolyzer cost [USD/MW]")
    develop_cost = forms.FloatField(min_value=1, max_value=100, initial=1, label="Development cost [USD/MW]")