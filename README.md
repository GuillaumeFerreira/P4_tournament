#Tournoi d'échec - Projet 4 - Openclassrooms
##Description
Mini programme avec interface console de gestion de tournoi d'échec
##Fonctionnalités
* Gestion tournois
* Gestion joueurs
* Sauvegarde sous format JSON du tournoi
* Génération de rapport
##Installation
####Environnement virtuel
#####Créer l'environnement virtuel
```python 
python -m venv env 
```
#####Activer l'environnement virtuel
```python 
env\Scripts\activate.bat
```
####Installer les librairies necessaires
```python 
pip install -r requirements.txt
```
####Lancer le script
```python
python tournament
```
##Contribuer
Pour toutes contibutions, veuillez utiliser **flake8** et **black**
####Executer black
```python
black -l79 tournament
```
####Executer flake8
```python
flake8 tournament
```