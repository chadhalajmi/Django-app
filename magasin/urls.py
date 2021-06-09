from django.urls import path
from magasin import views
urlpatterns = [
    path("",views.list_Produit),
    path('ajouter_Produit/', views.AjProduit, name='ajouter_Produit'),
    path('list_Produit/', views.list_Produit, name='Produit'),
    path('ajouter_Fournisseur/', views.AjFornisseur, name='ajouter_Fournisseur'),
    path('list_Fournisseur/', views.list_Fournisseur, name='Fournisseur'),
    path('ajouter_Commande/', views.AjCommande, name='ajouter_Commande'),
    path('list_Commande/', views.list_Commande, name='Commande'),  
    path('index/',views.index) ,   
    path('deletep/<id>',views.delprod,name='deletep'),
    path('deletef/<id>',views.delFourn,name='deletef'),
    path('deletec/<id>',views.delComm,name='deletec'),
    path('updatep/<id>',views.update_Produit,name="updatep"),
        path('updatef/<id>',views.update_Fournisseur,name="updatef")

]
