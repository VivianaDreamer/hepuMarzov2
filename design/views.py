from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import TechnicalDesignForm, TechnicalDesignForm2, EconomicDesignForm
from django import forms

DATA = {}

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class TechnicalDesignView(FormView):
    template_name = "design/design.html"
    form_class = TechnicalDesignForm
    success_url = reverse_lazy("economic_design")

    def form_valid(self, form):
        info = form.cleaned_data
        if info['op_type'] == 'PPA':
            info.pop('customized_from')
            info.pop('customized_to')
        if info['op_type'] == 'On-site generation':
            info.pop('ppa_type')
            info.pop('nom_power')
        DATA.update(info)
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super(TechnicalDesignView, self).get_form()
        form.fields['project_name'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Enter project name"})
        form.fields['location'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Enter location'})
        form.fields['cod'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['horizon'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['nom_power'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['elec_size'].widget = forms.NumberInput(attrs={'class':'form-control'})
        return form

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class TechnicalDesignView2(FormView):
    template_name = "design/design2.html"
    form_class = TechnicalDesignForm2
    success_url = reverse_lazy("economic_design")

    def form_valid(self, form):
        info = form.cleaned_data
        if info['op_type'] == 'PPA':
            info.pop('customized_from')
            info.pop('customized_to')
        if info['op_type'] == 'On-site generation':
            info.pop('ppa_type')
            info.pop('nom_power')
        DATA.update(info)
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super(TechnicalDesignView2, self).get_form()
        form.fields['project_name'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Enter project name"})
        form.fields['location'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Enter location'})
        form.fields['cod'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['horizon'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['nom_power'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['elec_size'].widget = forms.NumberInput(attrs={'class':'form-control'})
        return form

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class EconomicDesignView(FormView):
    template_name = "design/economic_design.html"
    form_class = EconomicDesignForm
    success_url = reverse_lazy("results")

    def form_valid(self, form):
        DATA.update(form.cleaned_data)
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(EconomicDesignView, self).get_form()
        form.fields['energy_cost'].widget = forms.NumberInput(attrs={"class":"form-control"})
        form.fields['water_cost'].widget = forms.NumberInput(attrs={"class":"form-control"})
        form.fields['elec_cost'].widget = forms.NumberInput(attrs={"class":"form-control"})
        form.fields['develop_cost'].widget = forms.NumberInput(attrs={"class":"form-control"})
        return form

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class ResultsView(TemplateView):
    template_name = "design/results.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['data']=DATA
        return context