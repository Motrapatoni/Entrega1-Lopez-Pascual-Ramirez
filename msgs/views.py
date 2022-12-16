from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from msgs.forms import MsgsForms
from msgs.models import Msg


@login_required(login_url='/login')
def show_msgs(request):    
    if request.method == 'POST':
        form = MsgsForms(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            msg = Msg()
            msg.msg_send = data['msg_send']
            msg.sender = data['sender']
            msg.save()
            return redirect('msgs')
    
    form = MsgsForms()
    
    h = datetime.now()
    hour = h - timedelta(hours=3)
    hour = hour.strftime('%H:%M')
    
    context = {
        'hour':hour,
        'form':form
    }
    
    return render(request, 'msgs/msgs.html', context)

@login_required(login_url='/login')
def show_div(request):     
    msg = Msg.objects.order_by('-create_date')

    return render(request, 'msgs/div.html', {'msg': msg})
