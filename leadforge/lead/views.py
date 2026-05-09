from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
# Create your views here.
@login_required
def add_lead(request):
    form=AddLeadForm()
    return render(request,"leads/leads.html",
                {'form':form}) 