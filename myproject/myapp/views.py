from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .filters import StageFilter
from datetime import datetime
from django.utils import timezone

def home_principle(request):
     current_datetime = timezone.now()
     specific_datetime = Myfinal.objects.first().datetime_field
     print('specific_datetime',specific_datetime)
     print('current_datetime',current_datetime)
     
     if current_datetime >= specific_datetime:
        print('yessssssss')
        # Do something when datetime matches
        return render(request, 'NOcontent.html', {'content': 'No content'})
     else :
             
       return render(request, 'HOME/first_home.html')

    

def upload_docs(request):
    critérs_list = Critéres.objects.all()
    form_submitted = False

    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES)

        if form.is_valid():
            stage = form.save(commit=False)
            #stage.save()

            for critere in critérs_list:
                nombre_document = request.POST.get('nombre_' + str(critere.id))
                x = Stage.objects.create(
                    faculté=stage.faculté,
                    nom=stage.nom,
                    prenom=stage.prenom,
                    date_de_naissance=stage.date_de_naissance,
                    Grade=stage.Grade,
                    payes_Destiné=stage.payes_Destiné,
                    ville=stage.ville,
                    labo_de_rechercher=stage.labo_de_rechercher,
                    critérs=critere,
                    nombre_document=nombre_document,
                    file=stage.file,
                    dossier_construction=stage.dossier_construction
                )
                x.save()

            form_submitted = True
    else:
        form = StageForm()

    context = {
        'form': form,
        'form_submitted': form_submitted,
        'criteres': critérs_list
    }
    return render(request, 'ADD/up.html', context)


def upload_doc(request, id):
    grade = Type.objects.get(id=id)
    critérs_list = Critéres.objects.filter(nom_de_Grille=grade)
    form_submitted = False

    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES)
        critere_ids = request.POST.getlist('critere')
        nombre_documents = request.POST.getlist('nombre')

        if form.is_valid():
            stage = form.save(commit=False)

            for critere_id, nombre_document in zip(critere_ids, nombre_documents):
                critere_object = Critéres.objects.get(id=int(critere_id))
                x = Stage.objects.create(
                    faculté=stage.faculté,
                    nom=stage.nom,
                    prenom=stage.prenom,
                    date_de_naissance=stage.date_de_naissance,
                    Grade=stage.Grade,
                    payes_Destiné=stage.payes_Destiné,
                    ville=stage.ville,
                    labo_de_rechercher=stage.labo_de_rechercher,
                    critérs=critere_object,
                    nombre_document=nombre_document,
                    file=stage.file,
                    dossier_construction=stage.dossier_construction
                )
                x.save()

            form_submitted = True
    else:
        form = StageForm()

    context = {
        'form': form,
        'form_submitted': form_submitted,
        'criteres': critérs_list
    }
    return render(request, 'ADD/add.html', context)
######################""""
def home(request):
    type=Type.objects.all()
    return render(request,'Home.html',{'type':type})

def upload_document(request, id):
    grade = Type.objects.get(id=id)
    critérs_list = Critéres.objects.filter(nom_de_Grille=grade)
    form_submitted = False
    if request.method == 'POST':
        form = StageForm(request.POST,request.FILES)
        critere = request.POST.get('critere')
        critere_object = Critéres.objects.get(id = int(critere))
#        document_form = DocumentForm(request.POST, )
       # critérs_form = CritérsForm(request.POST)
        print("omar" ,critere_object)
        if form.is_valid()  :
            stage = form.save(commit=False)
            stage.critérs = critere_object
            stage.save()
            form_submitted = True
    else:
        form = StageForm()
    context = {
        'form': form,
        #'critérs_form': critérs_form,
        'form_submitted': form_submitted,
        'criteres':critérs_list
    }
    return render(request, 'upload_document.html', context)

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            # Superuser login successful, perform login and redirect to a success page
            login(request, user)
            return redirect('homeadd')
        else:
            # Authentication failed, show an error message
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        # Render the login form
        return render(request, 'login.html')



from django.db.models import Count
@login_required(login_url='login')  # Replace 'login' with your actual login URL
def Homeadmin(request):
    unique_names = Stage.objects.values('nom','prenom').annotate(num_entries=Count('nom'))
    context = {
        'unique_names': unique_names,
    }
    return render(request, 'homeADD.html', context)

@login_required(login_url='login')  # Replace 'login' with your actual login URL
def Adminhome(request):
    AllStatge = StageFilter(request.GET, queryset=Stage.objects.all())
    

    context={
        'AllStage':AllStatge,
    }
    return render(request,'AdminHome.html',context)
@login_required(login_url='login')  # Replace 'login' with your actual login URL

def allFaculté(request):
    fac= Faculté.objects.all()
    context={
        'allFaculté':fac,
    }
    return render(request,'AllFaculté.html',context)
@login_required(login_url='login')  # Replace 'login' with your actual login URL

def allCri(request):
    creters= Critéres.objects.all()
    context={
        'allCreter':creters,
    }
    return render(request,'AllCretiers.html',context)

@login_required(login_url='login')  # Replace 'login' with your actual login URL

def uploadcritérs(request):
    form_submitted = False
    if request.method == 'POST':
        form = CritéresForm(request.POST)
       # critérs_form = CritérsForm(request.POST)
       # print("omar" ,critere_object)
        if form.is_valid():
            form.save()
            form_submitted = True
            
    else:
        form = CritéresForm()

    context = {
        'form': form,
        'form_submitted':form_submitted,
       

    }
    return render(request, 'ADD/AddCréter.html', context)
@login_required(login_url='login')  # Replace 'login' with your actual login URL

def uploadFaculté(request):
    form_submitted = False
    if request.method == 'POST':
        form = FacultéForm(request.POST)
       # critérs_form = CritérsForm(request.POST)
       # print("omar" ,critere_object)
        if form.is_valid():
            form.save()
            form_submitted = True
            
    else:
        form = FacultéForm()

    context = {
        'form': form,
        'form_submitted':form_submitted,
       

    }
    return render(request, 'ADD/AddFaculté.html', context)

#@login_required(login_url='login')  # Replace 'login' with your actual login URL
@method_decorator(login_required(login_url='login'), name='dispatch')

class FacultéUpdateView(View):
    def get(self, request, pk):
        item = get_object_or_404(Faculté, pk=pk)
        form = FacultéForm(instance=item)
        return render(request, 'update/faculté_update.html', {'form': form})

    def post(self, request, pk):
        item = get_object_or_404(Faculté, pk=pk)
        form = FacultéForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('faculté')  # Replace 'item-list' with the appropriate URL name
        return render(request, 'update/faculté_update.html', {'form': form})
@login_required(login_url='login')  # Replace 'login' with your actual login URL

def delete(request, pk):
        item = get_object_or_404(Faculté, pk=pk)
        item.delete()
        return redirect('faculté')

#@login_required(login_url='login')  # Replace 'login' with your actual login URL
@method_decorator(login_required(login_url='login'), name='dispatch')

class CritéresUpdateView(View):
    def get(self, request, pk):
        item = get_object_or_404(Critéres, pk=pk)
        form = CritéresForm(instance=item)
        return render(request, 'update/Critéres_update.html', {'form': form})

    def post(self, request, pk):
        item = get_object_or_404(Critéres, pk=pk)
        form = CritéresForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('critiers')  # Replace 'item-list' with the appropriate URL name
        return render(request, 'update/Critéres_update.html', {'form': form})
@login_required(login_url='login')  # Replace 'login' with your actual login URL

def deleteCre(request, pk):
        item = get_object_or_404(Critéres, pk=pk)
        item.delete()
        return redirect('critiers')
@login_required(login_url='login')  # Replace 'login' with your actual login URL
def addCommission(request,pk):
    stage_obj=Stage.objects.get(pk=pk)
    form_submitted = False
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        stage=request.POST.get('stage')
       # critérs_form = CritérsForm(request.POST)
       # print("omar" ,critere_object)
        if form.is_valid():
            x=  form.save(commit=False)
            x.stage=stage_obj
            x.save()
            form_submitted = True
    else:
        form = CommissionForm()
    context = {
        'form': form,
        'form_submitted':form_submitted,
        'stage':stage_obj
    }
    return render(request, 'ADD/AddCommission.html', context)
@login_required(login_url='login')  # Replace 'login' with your actual login URL
def voirCommission(request,pk):
    commision = Commission.objects.filter(stage_id=pk)
    print(commision)
    
        
        
    return render(request, 'VoirCommission.html', {'comm':commision})

    
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login') 
@login_required(login_url='login')  # Replace 'login' with your actual login URL
def show_details(request, name):
    stages = Stage.objects.filter(nom=name)
    context = {
        'stages': stages,
    }
    return render(request, 'show_details.html', context)