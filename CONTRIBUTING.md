# Wie neue Daten hinzugefügt werden können
## Erweiterungen vorschlagen
Wenn du eine bestimmte Erweiterung haben oder selbst machen möchtest, ist es gut, wenn du zunächst ein Issue im Haupt-Repository (https://github.com/marhei/TrainCompany-Data) anlegst:  
```Issues > New issue > Erweiterung/Get started```  
Es muss dabei nicht zwingend alles ausgefüllt werden, es dient in erster Linie dazu um mehrere gleichzeitige Erweiterungen zu verhindern.  
Willst du die Erweiterung selbst machen, bzw. fängst damit an, kannst du das als Kommentar hinzufügen, damit niemand anderes auch damit anfängt.
## Vorbereitungen
Wenn du eine Erweiterung selbst machen möchtest, solltest du einen Github-Fork erstellen, auf dem du dann die Änderungen/Ergänzungen machen kannst..
Das geht ganz einfach über den "Fork"-Button oben rechts und muss (und kann) nur ein Mal gemacht werden.
## Das allgemeine Vorgehen
1. Zunächst einmal solltest du deinen Datenstand mit dem Haupt-Repository abgleichen, was z.B. über die "Sync fork"-Option von GitHub geht oder die Pull-Funktion in einem Code-Editor o.Ä.
2. Falls möglich, solltest du einen Branch erstellen und darauf arbeiten. Das kannst du bspw. auf GitHub machen, wenn du eine Datei bearbeitest. In Visual Studio Code (oder github.dev oder Gitpod) geht das, indem du unten links auf den aktuellen Branch-Namen klickst (der zunächst `main` heißen wird) und dann oben "create new branch" auswählst.
3. Nun kannst du die Dateien bearbeiten, auf Github direkt, mit github.dev, mit Gitpod, lokal, usw.
4. Bist du soweit, musst du ggf. einen Git-Commit mit den geänderten Dateien erstellen (und benennen) und den in deinen Fork `Push`en.
5. Du kannst dann eine Pull Request erstellen mit den Änderungen, die du hinzufügen willst. Das geht von deinem Fork aus mit `Contribute > Open pull request` oder unter https://github.com/marhei/TrainCompany-Data/pulls > `New pull request` - wenn der Commit/Push gerade erst erstellt worden ist, wird es dir ggf. auch direkt angeboten.
  In der Ansicht kannst du dann Titel und Text bearbeiten (geht auch noch nachträglich) und (falls du noch nicht fertig bist) eine noch nicht fertigen/Draft-Pull Request erstellen
6. Ist die Pull-Request (PR) erstellt, laufen ein paar Tests und es kann dann darüber diskutiert werden usw., ist alles in Ordnung, kann die Pull Request gemergt werden und die Daten landen dann im Spiel.


## Tools zur Erstellung neuer Strecken
Es gibt mehrere Tools, mit denen neue Strecken hinzugefügt werden können, die jeweils verschieden Vor- und Nachteile haben.

Mit diesen Tools ist es vor allem leichter, neue Streckenerweiterungen und z.T. auch Ausschreibungen zu erstellen.
### tcroute (von @f2k1de)
- Erlaubt es, innerdeutsche Strecken aus https://trassenfinder.de zu importieren
- Web-basiert und zu finden auf https://tcroute.f2k1.de

### TrainCompany-Tools (von @c1710)
- Mehrere Tools, die es erlauben, neue Stationen, Strecken, Aufgaben zu erstellen - in Deutschland auch mit trassenfinder.de-Exporten, international teilweise manuell
- Kommandozeilen-Tools in Python entwickelt
- Direkt verfügbar in GitPod (einer Online-basierten Entwicklungsumgebung basierend auf Visual Studio Code):
  https://gitpod.io/#https://github.com/<Dein-Benutzername>/TrainCompany-Data (Registrierung/Anmeldung erforderlich; beschränkt auf 30 Stunden Nutzung im Monat)
- https://github.com/c1710/TrainCompany-tools