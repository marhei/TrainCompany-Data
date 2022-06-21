# TrainCompany Daten
In diesem Repository finden sich die Daten, die von TrainCompany genutzt werden. Die Daten sind in JSON-Dateien gespeichert, die ein data-Objekt beinhalten. Um ähnliche Objekte zusammenzufassen gibt es einfache Vererbung: **"objects": []** führt dazu, dass alle Objekte, die zwischen den [] eingefügt werden automatische die Eigenschaften des Mutter-Objekts erhalten, wenn diese nicht überschrieben wurden

## Train.json
Fahrzeuge, die in TC zur Verfügung stehen

* **id** *(int)* Eindeutige ID jedes Fz
* **group** *(int)* Art des Fahrzeuges
	* **0** Lokomotive
	* **1** Wagen
	* **2** Triebzug
	* **3** fixer Wagenverband
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
* **reliability** *(float)* Zuverlässigkeit in Prozent (0.0-1.0)
* **cost** *(int)* Kosten in Plops
* **maxConnectedUnits** *(int)* Maximale Anzahl der kuppelbaren Einheiten (bei Triebzügen, 0 = Unbegrenzt)
* **operationCosts** *(int)* Betriebskosten pro km in Plops
* **equipments** *(array)* Fahrzeugausstattung (siehe TrainEquipments.json)
* **exchangeTime** *(int)* Aufenthaltsdauer bei Planhalten in Sekunden (Optional, Standard = 40)
* **compatibleWith** *(array)* Für Triebzüge und Wagenverbände: Lässt sich zusätzlich mit den angegeben Fz kuppeln
* **equivalentTo** *(int)* Nur für fixe Wagenverbände: Entspricht wie vielen Wagen?
* **capacity** *(array)* Art der Beladung und Menge (siehe Capacity.json)

## Capacity.json
Art der Beladungen eines Fahrzeuges

* **idString** *(int)* Eindeutige ID einer Capacity
* **name** *(string)* Name der Capacity
* **needsPlatform** *(bool)* Benötigt einen Bahnsteig?
* **unit** *(string)* Einheit der Capacity
* **unitMass** *(float)* Eine Einheit entspricht wie viel t Gewicht?
* **emoji** *(string)* Emoji der Einheit


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
* **x** *(int)* x-Position auf Karte
* **y** *(int)* y-Position auf Karte
* **platformLength** *(int)* maximale Bahnsteiglänge (optional, Standard = 0)
* **platforms** *(int)* Bahnsteiganzahl (optional, Standard = 0)
* **forRandomTasks** *(bool)* (optional, Standard = true)

## TaskModel.json
Modelle für Aufträge, aus denen automatisch neue Aufträge erstellt werden

* **group** *(int)* Art des Auftrags
	* **0** Direktvergabe
	* **1** Ausschreibung
* **name** *(string)* Name des Auftrags
* **descriptions** *(array)* Array mit mehreren Strings für die Ausschreibung
* **plops** *(int)* Verdienst für die Ausschreibung
* **plopDifference** *(int)* Abweichung des Verdiensts in Prozent +/- (optional, Standard = 5)
* **stations** *array* Ril100 aller Bahnhöfe, die angefahren werden sollen in der richtigen Reihenfolge, wenn keine angegeben wurden, dann werden zwei zufällige gewählt (optional)
* **neededCapacity** *array* Art der Beladung und Menge, 0 bei passengers führt zu automatischer Berechnung der Fahrgäste (siehe Capacity.json)