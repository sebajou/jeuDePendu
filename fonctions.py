#!/usr/bin/python3
# -*-coding:Utf-8 -*

def pseudo():
    """ Fonction pour le jeu du pendu, permet d'enregistrer un pseudo avec un score correspondant. Ou si le pseudo existe déjà de l'afficher. """

    import pickle

# ouvre le fichier score, extrait l'objet dico et le stock dans score_recupere
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        score_recupere = mon_depickler.load()

# demande le pseudo puis compare dans score_ recupere si il existe dejà
    pseudo_temp = input ("Quelle est votre pseudo ? ") 
    if 
