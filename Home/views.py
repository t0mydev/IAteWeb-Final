from django.shortcuts import render, redirect
from .forms import NewRegister

from django.shortcuts import get_object_or_404

from Home.models import Survey, estadocasino, Submission, datoimp
from Home.forms import SurveyForm

from django.urls import reverse
from django.contrib import messages
import sqlite3
from . import aplantillas


# Create your views here.

def IAteHome(request):
    return render(request, 'IAteHome.html')

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = NewRegister()
    return render(request,'registration/register.html',{'form':NewRegister})


def Horariopref(request):
    datoimp = []
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    for turno in cur.execute('SELECT * FROM Home_submission_answer'):
        datoimp.append(turno[2])
    
    def bloquemayor(lista):
        texto = ""
        index = lista.index(max(lista))
        if (lista[index] == lista[0]) and (index != 0):
            texto = "no hay bloque saturado"
        elif (lista[index] == lista[1]) and (index != 1):
            texto = "no hay bloque saturado"
        elif (lista[index] == lista[2]) and (index != 2):
            texto = "no hay bloque saturado"
        elif (lista[index] == lista[3]) and (index != 3):
            texto = "no hay bloque saturado"
        else:
            if index == 0:
                texto = "7-8"
            elif index == 1:
                texto = "9-10"
            elif index == 2:
                texto = "11-12"
            elif index == 3:
                texto = "13-14"
        return texto
    
    datalun = [0,0,0,0]
    datamar = [0,0,0,0]
    datamie = [0,0,0,0]
    datajue = [0,0,0,0]
    datavie = [0,0,0,0]
    
    for turno in datoimp:
        if turno <= 4:
            if turno == 1:
                datalun[0] += 1
            elif turno == 2:
                datalun[1] += 1
            elif turno == 3:
                datalun[2] += 1
            elif turno == 4:
                datalun[3] += 1
        elif turno > 4 and turno <= 8:
            if turno == 5:
                datamar[0] += 1
            elif turno == 6:
                datamar[1] += 1
            elif turno == 7:
                datamar[2] += 1
            elif turno == 8:
                datamar[3] += 1
        elif turno > 8 and turno <= 12:
            if turno == 9:
                datamie[0] += 1
            elif turno == 10:
                datamie[1] += 1
            elif turno == 11:
                datamie[2] += 1
            elif turno == 12:
                datamie[3] += 1
        elif turno > 12 and turno <= 16:
            if turno == 13:
                datajue[0] += 1
            elif turno == 14:
                datajue[1] += 1
            elif turno == 15:
                datajue[2] += 1
            elif turno == 16:
                datajue[3] += 1
        elif turno > 16 and turno <= 20:
            if turno == 17:
                datavie[0] += 1
            elif turno == 18:
                datavie[1] += 1
            elif turno == 19:
                datavie[2] += 1
            elif turno == 20:
                datavie[3] += 1
    
    textolun = bloquemayor(datalun)
    textomar = bloquemayor(datamar)
    textomie = bloquemayor(datamie)
    textojue = bloquemayor(datajue)
    textovie = bloquemayor(datavie)
    
    context = {
        "textolun":textolun,
        "textomar":textomar,
        "textomie":textomie,
        "textojue":textojue,
        "textovie":textovie,
    }
    
    return render(request, 'HorarioTemp.html', context)


def estadocasinoview(request):
    texto = estadocasino.objects.latest('id')
    return render(request, 'estadocasino.html', {'texto':texto})

def estadofila(request):
    texto = aplantillas.evaluar("abase.txt")
    messages.info(request, texto)
    return render(request, 'estadofila.html', {'texto':texto})

########################################################################################################

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data)
    
    url = reverse("show_survey", args=(id,))
    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "survey.html", context)


########################################################################################################
