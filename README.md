Für die zweite Kombination: Django + Vue, wechseln Sie bitte auf Branch "Kombination2-DjangoVue".

Es existiert ebenfalls ein Branch "Kombination1-Django", dieser ist identisch mit dem "main" Branch und muss daher nicht genutzt werden.
# Gitarren Konfigurator Django
Eine Webapp zum Erstellen einer benutzerdefinierten Gitarre.

<br>

# Django Setup

## Datenbank Setup
Installieren Sie XAMPP (8.2.0) und wählen Sie die Apache und MySQL Module. <br>
Starten Sie die Apache und MySQL Module. <br>
Erstellen Sie eine Datenbank mit dem Namen "guitardb".

## Installation
Installieren Sie Python (3.x). <br>

Erstellen Sie eine virtuelle Umgebung im Projektverzeichnis:

*Linux / MacOS*
```
python3 -m venv env
```

*Windows*
```
py -m venv env
```

## Installation der Abhängigkeiten 
Führen Sie den folgenden Befehl im Projektverzeichnis aus, um die Abhängigkeiten zu installieren:

*Linux / MacOS*
```
env/bin/python -m pip install -r requirements.txt
```

*Windows*
```
env\Scripts\python -m pip install -r requirements.txt
```

## Virtuelle Umgebung starten
Führen Sie den folgenden Befehl im Projektverzeichnis aus, um die virtuelle Umgebung zu starten:

*Linux / MacOS*
```
source env/bin/activate
```

*Windows*
```
.\env\Scripts\activate
```

## Migration der Django Models und Laden einer fixture
Führen Sie folgende Befehle in der aktivierten virtuellen Umgebung aus:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Laden Sie eine fixture, um die Datenbank mit initialen Daten zu füllen:
```
python manage.py loaddata sample_database.json
```

## Django Applikation starten
Führen Sie den folgenden Befehl in der aktivierten virtuellen Umgebung aus:

```
python manage.py runserver 8000
```
Öffnen Sie die Applikation: http://127.0.0.1:8000/
