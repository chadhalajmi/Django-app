
from django.http.response import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect, render
def index(request):
    return render(request,'magasin\index.html')


def AjProduit(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = ProduitForm()
    return render(request,'magasin/majProduits.html',{'form':form})


def list_Produit(request):
    listp = Produit.objects.filter().all()
    return render(request,'magasin/Produits.html',{'list':listp})

def delprod(request,id):
    p = Produit.objects.filter(id = id).first()
    p.delete()
    return redirect('Produit')
def delFourn(request,id):
    p = Fournisseur.objects.filter(id = id).first()
    p.delete()
    return redirect('Fournisseur')
def delComm(request,id):
    p = Commande.objects.filter(id = id).first()
    p.delete()
    return redirect('Commande')

def update_Produit(request,id):
    p = Produit.objects.filter(id = id).first()
    f = Fournisseur.objects.all()
    e = Emballage.objects.all()
    if request.method == "POST":
        p.libelle = request.POST['libelle']
        p.description = request.POST['description']
        p.prix = request.POST['prix']
        p.emballag = Emballage.objects.filter(id = request.POST['emballage']).first()
        p.fournisser = Fournisseur.objects.filter(id = request.POST['fournisseur']).first()
        p.save(update_fields = ['libelle','description','prix','emballag','fournisser'])
        print(request.POST['fournisseur'])
        return redirect('/magasin')

    else:
        return render(request,'magasin/updateproduit.html',{'f':f,'p':p,'e':e})

def update_Commande(request):
    form = ProduitForm()
    context = {'form':form}

def update_Fournisseur(request,id):
    f = Fournisseur.objects.filter(id = id).first()
    if request.method == 'POST':
        f.nom = request.POST['nom']
        f.adresse = request.POST['adresse']
        f.email = request.POST['email']
        f.telephone = request.POST['telephone']
        f.save(update_fields = ['nom','adresse','email','telephone'])
        return redirect('Fournisseur')
    else:
        return render(request,'magasin/updatefournisseur.html',{'f':f})

def AjFornisseur(request):
    if request.method == "POST" :
        form = FrsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Fournisseur')
    else :
        form = FrsForm() 
    return render(request,'magasin/FormFornisseur.html',{'form':form})
def list_Fournisseur(request):
    list=Fournisseur.objects.all()
    return render(request,'magasin/Fornisseur.html',{'list':list})

def AjCommande(request):
    if request.method == "POST" :
        form = ComForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/magasin/list_Commande')
    else :
        form = ComForm() 
    return render(request,'magasin/AjCommande.html',{'form':form})

def list_Commande(request):
    list=Commande.objects.all()
    return render(request,'magasin/Commande.html',{'list':list})


