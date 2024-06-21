# SmartHomeWeb

Untersuchen der bisherigen WebApplikation:
1. Untersuchen Sie, wie Django HTML-Seiten generiert ("zusammengebaut")
- In welchem Unterordner steht das HTML?
+ A: web/templates/web
- Welche Elemente in der HTML-Datei sehen nicht so aus wie HTML? Welche Aufga be haben diese?
+ A: Alle Daten zwieschen {{}} z.B {{ form }}. Die haben die Aufgabe Daten dynamisch zu generiert 
2. Untersuchen Sie die Anzeige und Verlinkung der Web-Seiten.
- Was passiert beim Aufruf der Startseite, also dem Aufruf
von "http://127.0.0.1:8000/"?
+ A: Das Index wird wiedergegeben
-- Betrachten Sie hierzu die Datei "urls.py" im Projektkonfigurations Verzeichnis.
--- Wohin verweist diese Datei, wenn keine Unterverzeichnisse angegeben wer den?
+ A: zu dem haupt Route
--- Wohin verweist diese Datei, wenn das Unterverzeichnis "web/" angegeben 
wird? Probieren Sie das im Browser aus.
+ A: zu dem Index
--- Wohin verweist diese Datei, wenn das Unterverzeichnis "rest/" angegeben 
wird? Probieren Sie das im Browser aus.
+ A: zu der vom django-Framework bereitgestellten Api
--- Wohin verweist diese Datei, wenn das Unterverzeichnis "admin" angegeben 
wird? Probieren Sie das im Browser aus.
+ A: zu der von django bereitgestellten Verwaltungsseite
3. Untersuchen Sie die Aufgabe der "urls.py"-Datei in den "App"-
Verzeichnissen.
- Wohin verweist die Datei?
+ A: Die in urls.py angegebenen Pfade verweisen auf Funktionen, in denen wir unsere Logik erstellen und dann die gewünschte Vorlage rendern können
