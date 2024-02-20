from django.shortcuts import render, redirect
from django.contrib.auth import login 

from .forms import SignUpForm 

def frontpage_view(request):
    # Your view logic here
    return render(request, 'core/base.html')

#Sign up view 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            
            return redirect(request, 'base.html')
        
    else:
        form=SignUpForm()
    return render(request, 'core/signup.html', {'form':form})

