# 🐍 Learn2Slither

**Learn2Slither** est un projet d'intelligence artificielle basé sur l’apprentissage par renforcement. Le but est de créer un agent intelligent capable de jouer au jeu **Snake**, en apprenant à maximiser ses récompenses grâce à l’expérience accumulée.

---

## 🎯 Objectif

Développer une IA qui apprend à jouer à Snake en :

* Interagissant avec un environnement défini
* Recevant des récompenses ou pénalités
* Adaptant ses actions pour maximiser ses performances

---

## 🧩 Composants du projet

### 📦 Environnement

Définition du plateau : taille, obstacles, position de la nourriture, règles de déplacement.

### 📍 État

Représentation des données utiles à l'IA : position du serpent, de la nourriture, direction, collisions potentielles.

### 🔁 Actions

Liste des actions possibles : aller à gauche, droite, en haut, en bas.

### 💰 Récompenses

* Manger une pomme ou se rapprocher d'une pomme : récompense positive
* Heurter un mur ou soi-même : récompense négative
* S'éloigner d'une pomme : récompense négative 

### 🧠 Q-Learning

Implémentation de l’algorithme de **Q-learning** :

* Utilisation d’une table de valeurs Q
* Mise à jour selon l’expérience vécue par l’agent
* Apprentissage d’une stratégie optimale

---

## 🧪 Bonus possibles

* Ajout de nouveaux mécanismes de jeu
* Optimisation de l’apprentissage (e.g. epsilon decay, experience replay)
* Visualisation des performances

---
