from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Template, Context, loader
from items.forms import Contacts, NewsForms, SearchNewsForms
from items.models import Contact, New

# Create your views here.
def items(request):
    tittle =request.GET.get('tittle')
    if tittle:
        items = New.objects.filter(tittle__icontains=tittle)
    else:
        items = New.objects.all()
    
    form = SearchNewsForms()
    return render(request, 'items/items.html', {'items': items, 'form': form})

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