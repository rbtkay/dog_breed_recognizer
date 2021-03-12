# Dog Breed Recognizer

## Sujet

L'objectif du projet est de définir la race du chien sur une image importée par un utilisateur. Pour ce faire une IA est implémentée. Les chiens sont identifiables à partir des pixels de l'image grâce à un modèle entrainé au préalable. Celui-ci va pouvoir à ce moment-là prédire le type de chien dont il est question.

## Banque d'images

Une commande `wget` est disponible directement dansles notebooks pour récupérer les images.<br/>
Pour le système windows vous pouvez modifier la commande dans les notebooks ou télécharger une archive depuis l'adresse :<br/>
http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar

Vous devrez renommer le dossier contenant les images : `Images`

## venv

### Créer le venv :

    python3 -m venv venv

### Lancer le venv

Windows :

    venv\Scripts\activate

Unix :

    venv/bin/activate

### Installer les packages requis :

    pip install -r requirements.txt

## Lancer les notebooks en local

    jupyter notebook

## L'application

Vous pouvez tester une image sur le modele entrainé avec une application flask.

Pour tester avec le vgg16, il suffit de télécharger le fichier `vgg16_model.h5` depuis google drive et de l'ajouter à la racine du dossier, lien :<br />
https://drive.google.com/file/d/1pm9BmXU3Zolw2SSL2XHCV0IZqKUnhLBR/view?usp=sharing

Pour tester avec le cnn, il faut télécharger le fichier `ccn_model.h5` depuis google drive et de l'ajouter à la racine du dossier, lien :<br />
https://drive.google.com/file/d/1Du7Q_D40fHRlxI9hQhX8hLIsScbcSrHP/view?usp=sharing

Pour que ça fonctionne, il faut aussi modifier le nom du `MODEL_FILE` dans `app.py` et passer le `target_size` ligne 43 de `(224, 224)` à `(150, 150)`

### Lancer l'API python via flask

    flask run
