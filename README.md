# Gitarren Konfigurator Django + Vue
Eine Webapp zum Erstellen einer benutzerdefinierten Gitarre.


*Überspringen Sie die Sektion "Django Setup" und beginnen Sie bei Sektion "Vue Setup", wenn Sie diesen Teil in der Django Version (Kombination 1) bereits durchgeführt haben.*
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
python manage.py loaddata complete-database.json
```

## Django Applikation starten
Führen Sie den folgenden Befehl in der aktivierten virtuellen Umgebung aus:

```
python manage.py runserver 8000
```

<br>

# Vue Setup 

## Datenbank Setup
*Überspringen Sie diesen Schritt, wenn Sie die Sektion "Django Setup" in diesem Branch bereits durchgeführt haben*
Stellen Sie sicher das, dass die Apache und MySQL Module von XAMPP gestartet sind.

## Installation der Abhängigkeiten
*Überspringen Sie diesen Schritt, wenn Sie die Sektion "Django Setup" in diesem Branch bereits durchgeführt haben*
Führen Sie den folgenden Befehl im Projektverzeichnis aus, um die Abhängigkeiten zu installieren:

*Linux / MacOS*
```
env/bin/python -m pip install -r requirements.txt
```

*Windows*
```
env\Scripts\python -m pip install -r requirements.txt
```

## Migration der Django Models 
*Überspringen Sie diesen Schritt, wenn Sie die Sektion "Django Setup" in diesem Branch bereits durchgeführt haben*

Führen Sie folgende Befehle in der aktivierten virtuellen Umgebung aus:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

## Django Applikation starten
*Überspringen Sie diesen Schritt, wenn Sie die Sektion "Django Setup" in diesem Branch bereits durchgeführt haben*
Führen Sie den folgenden Befehl in der aktivierten virtuellen Umgebung aus:

```
python manage.py runserver 8000
```

## Vue Installation
Installieren Sie Node.js Version 16.0 oder höher. <br>

Öffnen Sie ein neues Terminal und wechseln Sie im Projektverzeichnis in den Vue Unterordner:

```
cd vue-guitar_configurator
```

## Installation der Vue Abhängigkeiten 
Führen Sie den folgenden Befehl im Vue Unterordner aus, um die Abhängigkeiten zu installieren:

```
npm install
```

## Vue Applikation starten 
Führen Sie den folgenden Befehl im Vue Unterordner aus, um die Vue Applikation zu starten:

```
npm run dev
```
Öffnen Sie die Applikation: http://localhost:5173/