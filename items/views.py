from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required

from items.forms import Contacts, SearchNewsForms
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


class CreateItem(LoginRequiredMixin, CreateView):
    model = New
    success_url = '/items'
    template_name = 'items/create-item.html'
    fields = '__all__'
    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())
    
class ReadItem(ListView):
    model = New
    template_name = 'items/read-item.html'
    fields = '__all__'
    def get_queryset(self):
        queryset = New.objects.filter(owner_name= self.request.user.id)
        return queryset


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