from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Terms
# Create your views here.


@login_required
def home(request):
    if request.method == 'POST':
        pass
    
    else:

        if not Terms.objects.filter(user_id=request.user.id).exists():
            return redirect('terms')
        return render(request,'home/home.html')
