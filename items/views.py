from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
    fields = ['tittle', 'body', 'owner_name', 'image']
    

class ReadItem(DetailView):
    model = New
    template_name = 'items/read-item.html'
    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(DetailView, self).get_context_data(**kwargs)
        context['item'] = New.objects.get(pk=pk)
        return context
     
     
class EditItem(LoginRequiredMixin, UpdateView):
    model = New
    success_url = '/items'
    template_name = 'items/edit-item.html'
    fields = ['tittle', 'body', 'owner_name', 'image']
    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['item'] = New.objects.get(pk=pk)
        return context


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = New
    success_url = '/items'
    template_name = 'items/delete-item.html'
    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['item'] = New.objects.get(pk=pk)
        return context
    

def contact(request):
    if request.method == 'POST':
        form = Contacts(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            name=data['name']
            mail=data['mail']
            message=data['message']
            contact = Contact(name=name, mail=mail, message=message)
            contact.save()
            return redirect('index')
    
    form = Contacts()
    return render(request, 'items/contact.html', {'form': form})