import json
from datetime import datetime

import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from bank.models import Bank, CentralBank
from home.models import Terms

from .forms import BanckForms, TermsForm


# Create your views here.
@login_required
def terms(request):
    if request.method == 'POST':
        if Terms.objects.filter(user_id=request.user.id).exists():
            return redirect('bank')    
        else:
            terms = Terms()
            if request.method == 'POST':
                if request.POST['accepted'] == 'on':
                    terms.accepted = 1
                else:
                    terms.accepted = 0
            terms.user = request.user
            terms.save()
            return redirect('bank')
    else:
        return render(request,'firststaps/terms.html',context={"form":TermsForm()})

@login_required
def bank(request):
    bancoForms = BanckForms()
    context = getBancos(request,bancoForms)     

    if request.method == 'POST':
        if request.POST.get('save_banco_and_add_another'):
            bankName = request.POST['bankname']
            try:
                if CentralBank.objects.filter(name=bankName).exists():
                    user_banco = Bank()
                    bancosCadastrados = list(CentralBank.objects.filter(name=bankName).all().values())[0]
                    user_banco.user_id = request.user.id
                    user_banco.bank_id = bancosCadastrados['id']
                    user_banco.bankname = bankName
                    user_banco.description = request.POST['description']
                    user_banco.createdAt = datetime.now()
                    user_banco.save()


                    context = getBancos(request,bancoForms)

                    messages.success(request,'Banco cadastrado com sucesso!')
                    return render(request,'firststaps/bank.html',context)

                else:
                    messages.error(request,f'{bankName} : não foi encontrado na lista de bancos cadastrados do Banco Central')
                    return render(request,'firststaps/bank.html',context)
            
            except:
                messages.error(request,f'Falha ao cadastrar o banco: {bankName} tente novamente mais tarde')
                return render(request,'firststaps/bank.html',context)

        elif request.POST.get('next'):
            return redirect('cad_cartoes')
    else:

        return render(request,'firststaps/bank.html',context)
    

def card(request):
    return render(request, 'firststaps/card.html')


def getBancos(request,bancoForms):
    context = {}
    context['bancoforms'] = bancoForms

    df = pd.DataFrame(list(Bank.objects.filter(user_id=request.user.id).all().values())) 
    if len(df) >0:
        df = df.drop(columns=["createdAt"])
        table = height_table(df)
        context['bancosSalvos'] = table['df']
        context['height'] = table['height']  

    return context


def height_table(df):
    try:
        df = df.to_dict('recording')
        tamanhoTh = len(df)*40+75
        if tamanhoTh > 200:
            tamanhoTh = 200
        return {'df':df,'height':tamanhoTh}
    except:
        return False
    
def ajax(request,model):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        q = request.GET.get('term', '')

        if model == "CentralBank":
            lista = CentralBank.objects.filter(fullName__icontains=q)
        elif model == "Bancos_usuario":
            lista = Bank.objects.filter(name__icontains=q)

        data = ajax_results(lista)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def ajax_results(lista):
        results = []
        for item in lista:
            return_json = {}
            return_json['label'] = item.name
            return_json['value'] = item.name
            results.append(return_json)
        return json.dumps(results)