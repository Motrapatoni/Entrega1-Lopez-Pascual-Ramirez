import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template, loader
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from items.forms import Contacts, NewsForms, SearchNewsForms
from items.models import Contact, New


# Create your views here.
class Items(ListView):
    item = New
    template_name = 'items/items.html'
        
    def get_queryset(self):
        tittle = self.request.GET.get('tittle', '')
        if tittle:
            object_list = self.item.objects.filter(tittle__icontains=tittle)
        else:
            object_list = self.item.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchNewsForms()
        return context


@login_required
def create_item(request):
    if request.method == 'POST':
        form_create = NewsForms(request.POST)
    
        if form_create.is_valid():
            data = form_create.cleaned_data
            
            tittle = data['tittle']
            body = data['body']
            creation_date = data['creation_date']
            if not creation_date:
                creation_date = datetime.now()
            owner_first_name = data['owner_first_name']
            owner_last_name = data['owner_last_name']
            collaborators = data['collaborators']
            new = New(tittle=tittle, body=body, creation_date=creation_date, owner_first_name=owner_first_name, 
                      owner_last_name=owner_last_name, collaborators=collaborators)
            new.save()
            return redirect('items')
    
    form_create = NewsForms()
    return render(request, 'items/create-item.html', {'form_create': form_create})

def contact(request):
    if request.method == 'POST':
        form_create = Contacts(request.POST)
        
        if form_create.is_valid():
            data = form_create.cleaned_data
            
            name=data['name']
            mail=data['mail']
            message=data['message']
            contact = Contact(name=name, mail=mail, message=message)
            contact.save()
            return redirect('index')
    
    form_create = Contacts()
    return render(request, 'items/contact.html', {'form_create': form_create})