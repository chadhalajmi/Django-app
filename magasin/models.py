from django.db import models
from datetime import date

# Create your models here.

TYPE_CHOICES =[('em','emballé'),('Ne','Nom emballé')]

COUL_CHOICES=[('bl','blanc'),('rg','rouge'),('bl','bleu'), ('vr','vert'),('muli','multicolore'),('tr','Transparent')]


class Produit(models.Model) :
    libelle = models.CharField(max_length=100)
    description = models.TextField(default = 'Non definie')
    prix = models.DecimalField(max_digits = 100, decimal_places=3)
    Type = models.CharField(max_length=2,default='cs',choices=TYPE_CHOICES)
    image = models.ImageField(blank=True)
    emballag =models.ForeignKey('Emballage',on_delete=models.CASCADE,null=True)
    fournisser=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self) :

        return "le libbélle : {} la description : {} le prix : {} le type : {}".format(self.libelle,self.description,self.prix,self.Type)

class Emballage(models.Model) :
    matiere=models.CharField(max_length=100)        
    couleur=models.CharField(max_length=100, choices=COUL_CHOICES,default='Transparent')
    def __str__(self) :

        return "matiere : {} couleur : {} ".format(self.matiere,self.couleur)

class Fournisseur(models.Model) :
    nom = models.CharField(max_length=100)
    adresse = models.TextField(null=True)
    email = models.EmailField(null=True)
    telephone = models.CharField(max_length=8)
    

    def __str__(self) :
        return "nom : {}, adresse : {}, email : {},telephone : {}".format(self.nom,self.adresse,self.email,self.telephone)

class ProduitNC(Produit,models.Model):
    Duree_garantie=models.CharField(max_length=100)

    def __str__(self):
        super.__str__()
        return "duree de garanti {}".format(self.Duree_garantie)

class Commande(models.Model):
    Duree_garantie=models.CharField(max_length=100)
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')

    def __str__(self):
        return "Le Produits : {}, duree de garanti : {},dateCde : {}, totalCde : {}".format(self.produits,self.Duree_garantie,self.dateCde,self.totalCde)
