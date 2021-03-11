# Dog Breed Recognizer

## Sujet
L'objectif du projet est de définir la race du chien sur une image importée par un utilisateur. Pour ce faire une IA est implémentée. Les chiens sont identifiables à partir des pixels de l'image grâce à un modèle entrainé au préalable. Celui-ci va pouvoir à ce moment-là prédire le type de chien dont il est question.


## Banque d'images

- Créer un dossier Images.
- Telecharger les images de chiens classifiées depuis [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar).
- Déposer les dans le dossier.


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

## Visualisation du notebook sur colab
Exécuter le [Colab](https://colab.research.google.com/drive/1pkAMho_nuQvx7bFl7jUDOF55PbJdGXsX?usp=sharing).

## Entrainer l'IA depuis un script Python

    python ./training.py

