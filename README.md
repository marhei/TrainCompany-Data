[![Open in Remote - Containers](https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/marhei/TrainCompany-Data) [![Contribute with Gitpod](https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/marhei/TrainCompany-Data)

![Lint](https://github.com/marhei/Traincompany-Data/actions/workflows/eclint.yml/badge.svg) ![Validation](https://github.com/marhei/Traincompany-Data/actions/workflows/json_validate.yml/badge.svg) ![Check JSON content](https://github.com/marhei/Traincompany-Data/actions/workflows/check_content.yml/badge.svg)

# TrainCompany Daten
In diesem Repository finden sich die Daten, die von TrainCompany genutzt werden. Die Daten sind in JSON-Dateien gespeichert, die ein data-Objekt beinhalten. Um ähnliche Objekte zusammenzufassen gibt es einfache Vererbung: **"objects": []** führt dazu, dass alle Objekte, die zwischen den [] eingefügt werden automatische die Eigenschaften des Mutter-Objekts erhalten, wenn diese nicht überschrieben wurden.

Eine Anleitung zum Erstellen neuer Erweiterungen usw. findet sich in [`Contributing.md`](CONTRIBUTING.md)

**Jede*r ist herzlich eingeladen ein PR einzureichen und damit die Welt von TrainCompany zu erweitern. Um den Aufwand der Abarbeitung von PR für mich in einem angemessenen Rahmen zu halten bitte ich euch diese klein zu halten. Anstatt große Sammel-PR, die eine Vielzahl an verschiedene Regionen und Elemente betreffen, am besten pro Region/Element ein eigenes PR erstellen.**

## Train.json
Fahrzeuge, die in TC zur Verfügung stehen

* **id** *(int)* Eindeutige ID jedes Fz
* **group** *(int)* Art des Fahrzeuges
	* **0** Lokomotive
	* **1** Wagen
	* **2** Triebzug
	* **3** fixer Wagenverband
* **service** *(int)* Zuordnung zu einer passenden Service-Klasse (siehe TaskModel.json)
* **name** *(string)* Name des Fahrzeuges
* **shortcut** *(string)* Baureihen/-art-Bezeichnung des Fahrzeuges *(optional)*
* **speed** *(int)* Höchstgeschwindigkeit in km/h
* **weight** *(int)* Gewicht in t
* **force** *(int)* Anfahrzugkraft in kN
* **length** *(int)* Länge in Metern
* **drive** *(int)* Traktionsart
	* **0** Keine Traktion
	* **1** E-Traktion
	* **2** Diesel-Traktion
	* **3** Batterie
	* **4** Hybrid
	* **5** Wasserstoff
	* **6** Last Mile
	* **7** Dampf
* **reliability** *(float)* Zuverlässigkeit in Prozent (0.8-1.0)
* **cost** *(int)* Kosten in Plops
* **maxConnectedUnits** *(int)* Maximale Anzahl der kuppelbaren Einheiten (bei Triebzügen, Nicht gesetzt = Unbegrenzt)
* **operationCosts** *(int)* Betriebskosten pro km in Plops (Nur bei Fz mit Antrieb benutzen!)
* **equipments** *(array)* Fahrzeugausstattung (siehe TrainEquipments.json)
* **exchangeTime** *(int)* Aufenthaltsdauer bei Planhalten in Sekunden (Optional, Standard = 40)
* **compatibleWith** *(array)* Für Triebzüge und Wagenverbände: Lässt sich zusätzlich mit den angegeben Fz kuppeln
* **equivalentTo** *(int)* Nur für fixe Wagenverbände: Entspricht wie vielen Wagen?
* **range** *(int)* Reichweite im Batteriebetrieb in km
* **capacity** *(array)* Art der Beladung und Menge (optional, siehe Capacity.json)

## Capacity.json
Art der Beladungen eines Fahrzeuges

* **idString** *(int)* Eindeutige ID einer Capacity
* **name** *(string)* Name der Capacity
* **needsPlatform** *(bool)* Benötigt einen Bahnsteig?
* **unit** *(string)* Einheit der Capacity
* **unitMass** *(float)* Eine Einheit entspricht wie viel t Gewicht?
* **emoji** *(string)* Emoji der Einheit
* **exchangeFactor** *(float)* Faktor für automatischen Zustieg: 1 ist normale Fahrgäste (optional)


## DelayModel.json
Modelle für Verspätungen

* **type** *(int)* Art der Verspätung
	* **0** Fahrzeugstörung
	* **1** Personal
	* **2** Ladung
	* **3** Streckenstörung (noch nicht implementiert)
	* **4** Fahrplan
* **name** *(string)* Verspätungstext
* **delay** *(int)* Erzeugte Verspätung in Sekunden (+/-5 %)
* **capacity** *(string)* In Kombination mit **type**/**2** wird eine ladungssbezifische Störung angegeben

## Path.json
Verbindungen zwischen zwei Bahnhöfen

* **name** *(string)* Streckenname (optional)
* **group** *(int)* Art der Strecke (optional, Standard = 0)
	* **0** Hauptbahn
	* **1** Nebenbahn
	* **2** SFS
	* **3** Fähre
* **start** *(string)* Ril100 des Startbahnhofs
* **end** *(string)* Ril100 des Endbahnhofs
* **twistingFactor** *(float)* Angebe der Kurvigkeit von 0.0 bis 1.0 wobei 1.0 am kurvigsten ist
* **lenght** *(int)* Länge der Strecke in km
* **maxSpeed** *(int)* Höchstgeschwingkeit des Streckenabschnitts
* **electrified** *(bool)* Elektrifiziert (optional, Standard = true)
* **neededEquipments** *(array)* Benötigte Fahrzeugaustattung (siehe TrainEquipments.json, optional)

## Station.json
Bahnhöfe

* **name** *(string)* Bahnhofsname
* **ril100** *(string)* Ril100 des Bf
* **group** *(int)* Art des Bahnhofs
	* **0** Knotenbahnhof
	* **1** Hauptbahnhof
	* **2** kleiner Bahnhof
	* **3** Betriebsbahnhof
	* **4** Abzweigstelle
	* **5** Haltepunkt (Wird nicht auf der Karte gerendert)
	* **6** Wegpunkt (Wird nicht auf der Karte gerendert)
* **x** *(int)* x-Position auf Karte
* **y** *(int)* y-Position auf Karte
* **platformLength** *(int)* maximale Bahnsteiglänge (optional, Standard = 0)
* **platforms** *(int)* Bahnsteiganzahl (optional, Standard = 0)
* **network** *(string)* (optional, Standard = default Network)
* **forRandomTasks** *(bool)* (optional, Standard = true)

## TaskModel.json
Modelle für Aufträge, aus denen automatisch neue Aufträge erstellt werden

* **group** *(int)* Art des Auftrags
	* **0** Direktvergabe
	* **1** Ausschreibung
* **name** *(string)* Name des Auftrags
* **service** *(int)* Servicelevel zur automatischen Berechnung des Gewinns
	* **0** HGV
	* **1** IC
	* **2** Regionalverkehr
	* **3** kurzer Regionalverkehr
	* **4** Sonderzug
	* **5** Nachtzug
	* **10** wichtiger Güterzug
	* **11** Güterzug
* **descriptions** *(array)* Array mit mehreren Strings für die Ausschreibung
* **stations** *(array)* Ril100 aller Bahnhöfe, die angefahren  sollen in der richtigen Reihenfolge, wenn keine angegeben wurden, dann werden zwei zufällige gewählt (optional)
* **pathSuggestions** *(array)* Ril100 aller Bahnhöfe, die standardmäßig mit oder ohne Halt angefahren werden sollen in der richtigen Reihenfolge.
* **stopsEverywhere** *(bool)* Wenn true dann wird auch automatisch ein Halt an allen Bahnhöfen, die zwischen den oben angegeben Bahnhöfen eingeplant (optional)
* **neededCapacity** *array* Art der Beladung und Menge, wenn die Menge weggelassen wird führt es zu automatischer Beladung, wenn von Capacity unterstützt (siehe Capacity.json)
