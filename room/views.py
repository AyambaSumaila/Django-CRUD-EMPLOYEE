from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create our views here.
from .models import Rooms


@login_required 

def rooms(request):
    rooms =Rooms.objects.all()
    return render(request, 'room/rooms.html', {'rooms':rooms})



