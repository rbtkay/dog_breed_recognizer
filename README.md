# Dog Breed Recognizer

## Sujet

L'objectif du projet est de définir la race du chien sur une image importée par un utilisateur. Pour ce faire une IA est implémentée. Les chiens sont identifiables à partir des pixels de l'image grâce à un modèle entrainé au préalable. Celui-ci va pouvoir à ce moment-là prédire le type de chien dont il est question.

## Banque d'images

-   Créer un dossier Images.
-   Telecharger les images de chiens classifiées depuis [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar).
-   Déposer les dans le dossier.

## venv

### Créer le venv : <br/>

    python3 -m venv venv

### Lancer le venv

#### Windows :

    venv\Scripts\activate

#### Unix :

    venv/bin/activate

### Installer les packages requis : <br/>

    pip install -r requirements.txt

### Mettre à jour la liste des package : <br/>

    pip freeze > requirements.txt

## Lancer le notebook en local

    jupyter notebook

## Visualisation du notebook sur Colab

Exécuter le [CNN Colab](https://colab.research.google.com/drive/1pkAMho_nuQvx7bFl7jUDOF55PbJdGXsX?usp=sharing).
Exécuter le [Transfer learning Colab](https://colab.research.google.com/drive/15SX2p6iwSYDh1dvYXhaqrMNbl3OjeJc0?usp=sharing).

## L'application

Pour tester avec le vgg16, il suffit de télécharger le fichier `vgg16_model.h5` depuis google drive et de l'ajouter à la racine du dossier. lien :<br />
https://drive.google.com/file/d/1pm9BmXU3Zolw2SSL2XHCV0IZqKUnhLBR/view?usp=sharing

On peut tester l'application avec le cnn en récupérent le modèle `ccn_model.h5` à l'adresse :<br/>
https://drive.google.com/file/d/1Du7Q_D40fHRlxI9hQhX8hLIsScbcSrHP/view?usp=sharing

Pour que ça fonctionne, il faut aussi modifier le nom du `MODEL_FILE` dans `app.py` et passer le `target_size` ligne 43 de `(224, 224)` à `(150, 150)`

### Lancer l'API python via flask

    flask run
