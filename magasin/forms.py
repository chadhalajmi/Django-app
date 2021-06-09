from django.forms import ModelForm
from django import forms
from .models import Commande, Fournisseur, Produit
class ProduitForm(ModelForm):
    class Meta :
        model = Produit
        fields = "__all__" #pour tous les champs de la table
        #fields=['libelle','description'] #pour quelques champs
class FrsForm(ModelForm):
    class Meta :
        model = Fournisseur
        fields = "__all__"

class ComForm(ModelForm):
    class Meta :
        model = Commande
        fields = "__all__"
   

    