from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import TermsForm
from home.models import Terms

# Create your views here.
@login_required
def terms(request):
    if request.method == 'POST':
        if Terms.objects.filter(user_id=request.user.id).exists():
            return redirect('cad_banco')    
        else:
            terms = Terms()
            if request.method == 'POST':
                if request.POST['aceite'] == 'on':
                    terms.accepted = 1
                else:
                    terms.accepted = 0
            terms.user = request.user
            terms.save()
            return redirect('cad_banco')
    else:
        return render(request,'firststaps/terms.html',context={"form":TermsForm()})
