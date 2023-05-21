from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login


def home(request):
    type=Type.objects.all()
    return render(request,'Home.html',{'type':type})
def upload_document(request, id):
    grade = Type.objects.get(id=id)
    critérs_list = Critéres.objects.filter(nom_de_Grille=grade)
    form_submitted = False
    if request.method == 'POST':
        form = StageForm(request.POST)
        critere = request.POST.get('critere')
        critere_object = Critéres.objects.get(id = int(critere))
        document_form = DocumentForm(request.POST, request.FILES)
       # critérs_form = CritérsForm(request.POST)
        print("omar" ,critere_object)
        if form.is_valid() and document_form.is_valid() :
            stage = form.save(commit=False)
            stage.critérs = critere_object
            stage.save()
           # critérs = critérs_form.cleaned_data['critérs']
            for i in range(stage.nombre_document):
                file = request.FILES.getlist('file')[i]
               # critérs = critérs_list[i].critérs if i < len(critérs_list) else None
                Stage.objects.create(
                    faculté=stage.faculté,
                    nom=stage.nom,
                    prenom=stage.prenom,
                    date_de_naissance=stage.date_de_naissance,
                    Grade=stage.Grade,
                    critérs=stage.critérs,
                    nombre_document=stage.nombre_document,
                    file=file
                )
            form_submitted = True
    else:
        form = StageForm()
        document_form = DocumentForm()

    context = {
        'form': form,
        'document_form': document_form,
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
            return redirect('success')
        else:
            # Authentication failed, show an error message
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        # Render the login form
        return render(request, 'login.html')


def Adminhome(request):
    AllStatge= Stage.objects.all()
    context={
        'AllStage':AllStatge,
    }
    return render(request,'AdminHome.html',context)
def allFaculté(request):
    fac= Faculté.objects.all()
    context={
        'allFaculté':fac,
    }
    return render(request,'AllFaculté.html',context)
def allCri(request):
    creters= Critéres.objects.all()
    context={
        'allCreter':creters,
    }
    return render(request,'AllCretiers.html',context)

