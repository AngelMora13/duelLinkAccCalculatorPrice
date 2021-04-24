from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import RequestContext,Template
import math

# Create your views here.
totalAccount = 0
def FormCalc(request):
    form = {}
    global totalAccount
    totalAccount = 0
    if request.method=="POST":
        form = request.POST
        form = form.dict()     
        form["PriceGems"] = priceGems(form["gems"]) if form["gems"] else "0.0$"
        form["PriceCards"] = priceCards(form["URcards"],form["SRcards"]) \
            if form["URcards"] or form["SRcards"] else "0.0$"

        phases = [form["PhaseDM"],form["PhaseDSOD"],form["PhaseGX"],\
            form["PhaseDS"],form["PhaseZexal"]]

        form["PricePhases"] = pricePhases(phases)

        i=35
        characterLvl=[]
        while i>=10 :
            characterLvl.append(form["Cha"+str(i)])
            i-=5
        form["PriceChar"] = priceCharacters(characterLvl)

        tickets = [form["ticketsUR"],form["ticketsURDream"],form["ticketsSR"],\
            form["ticketsSRDream"],form["ticketsSU"],form["ticketsR"],\
                form["ticketsN"],form["ticketsSkill"]]

        form["PriceTickets"] = priceTickets(tickets)
        form["total"] = f"{round(totalAccount,2)}$"
    return render(request,"form/index.html",form)

def page_404_not_found(request,exception,template_name='404.html'):
    return render(request,"error/404.html",status=404)

def page_500_error_server(request,template_name='500.html'):
    return render(request,"error/500.html",status=500)

def priceGems(gems):
    gems=int(gems)
    gems = gems*math.exp((gems/(gems+1)))/3000 
    gems= round(gems,2)

    global totalAccount
    totalAccount += gems
    return f"{gems}$"

def priceCards(ur,sr):
    ur = int(ur) if ur else 0
    sr = int(sr) if sr else 0
    ur = (0.1*math.exp(ur/(ur+1)))*ur/3
    sr = sr/15
    cards = ur + sr
    cards = round(cards,2)

    global totalAccount
    totalAccount += cards
    return f"{cards}$"

def pricePhases (phases):
    total = 0
    for world in phases:
        world = int(world) if world else 0
        total += world/15
    total = round(total,2)

    global totalAccount
    totalAccount += total
    return f"{total}$"

def priceCharacters (char):
    i = 0
    total = 0
    for c in char:
        char[i] = int(c) if c else 0
        i += 1
    char[0]*=1.5  
    char[2]/=1.5
    char[3]/=4
    char[4]/=7
    char[5]/=10
    for c in char:  
        total += c
    total =round(total,2)

    global totalAccount
    totalAccount += total
    return f"{total}$"

def priceTickets (tickets):
    i = 0
    total = 0
    for ticket in tickets:
        tickets[i] = int(ticket) if ticket else 0
        i += 1
    tickets[0] /= 4
    tickets[2] /=10
    tickets[4] /=2
    tickets[5] /= 20
    tickets[6] /= 25
    for ticket in tickets:
        total += ticket
    total = round(total,2)

    global totalAccount
    totalAccount += total
    return f"{total}$"