# Threading in Python - Simple Encryption

## Aufgabenstellung

Sieh dir auf GitHub [1] das Beispiel *CounterThread* an und analysiere, wie einem Thread Parameter übergeben werden
und Klassenvariablen verwendet werden können!

Erstelle anschließend eine eigene Klasse, die von Thread erbt und die parallele Verschlüsselung und Entschlüsselung
von einfachen Textnachrichten erlaubt!

Beispiel:

    Which message do you want to encrypt? -> Eingabe: HALLO WELT
    How many threads should encrypt the message? -> Eingabe: 3
    Your encrypted message: EVTTD AGTC

### Grundanforderungen

* Eigene Klasse erbt von Thread
* Über Parameter im Konstruktor wird geregelt, für welche Teile der Nachricht dieser Thread zuständig ist (z.B. jedes
 dritte Zeichen, erste Hälfte der Nachricht, ...)
* Die Nachricht wird von allen Threads geteilt und bearbeitet (verschlüsselt)
* Die Verschlüsselungstabelle für den Substitutionsalgorithmus wird von allen Threads geteilt (z.B. durch ein Dictionary,
 welches für jedes Ursprungszeichen das Zielzeichen speichert)
* In der run-Methode werden jene Zeichen ersetzt, für die der Thread zuständig ist. Hierbei kommen sich die Threads
 nicht in die Quere
* In einem Skript wird der Benutzer gefragt, welche Nachricht verschlüsselt werden soll und wie viele Threads dafür
 verwendet werden sollen
* Anschließend wird die Nachricht entsprechend verschlüsselt und die verschlüsselte Nachricht wird ausgegeben
* In einem zweiten Schritt wird die Nachricht wieder entschlüsselt und die Ursprungsnachricht wird wieder ausgegeben
* Es werden nur Großbuchstaben verschlüsselt 
* Leerzeichen bleiben Leerzeichen
* Eingaben in lower case und Sonderzeichen bleiben unverschlüsselt


### Erweiterungen

* Unter Beibehaltung der ursprünglichen Verschlüsselungsmethode für Großbuchstaben sollen nun zusätzlich alle anderen, lesbaren ascii Zeichen verschlüsselt und auch wieder entschlüsselt werden, wobei dies durch den Parameter Distanz (=0,1,2...) spezifiziert wird.
Überlege dir, wie beliebige Zeichen (auch Sonderzeichen) unterstützt werden können und implementiere es dementsprechend ohne dabei die bestehende Großbuchstabenverschlüsselung zu ändern!
Zum Beispiel hat '{' den Dezimalwert 123 in der ASCII-Tabelle und wird mit der Distanz 2 auf das Zeichen '}' verschlüsselt. 
* Das Leerzeichen soll weiterhin unverschlüsselt bleiben.
* Als Distanz soll jede beliebige Integer Zahl, negativ oder positiv, angegeben werden können.   
* Achte auf saubere Fehlerbehandlung (don't trust user input)!

### Umgebung und Tests

Es wird PyBuilder als Build-Umgebung verwendet. Nähere Informationen sind unter [3] zu finden. Um eine Liste an Tasks
zu erhalten können folgende Befehle ausgeführt werden:

    python setup.py # installs necessary packages
    pyb -t 

Um die Umgebung auch für PyCharm einzurichten, kann der folgende Task ausgeführt werden:

    pyb pycharm_generate

Die Abhängigkeiten können optional auch in einer virtuellen Umgebung geladen werden. Dabei werden alle notwendigen
Pakete in ein eigenes Verzeichnis geladen und die PATH Variable auf dieses Verzeichnis hin angepasst. Die 
Benutzeranleitung für Virtualenv ist hier [5] zu finden.

Das Beispiel soll entsprechend der mitgelieferten Tests implementiert werden. Folgende Befehle werden bei der Abnahme
ausgeführt und bewertet:

    pyb publish run_unit_tests
    pyb sphinx_generate_documentation

## Umsetzung
<!---
Was musste recherchiert werden um die Aufgabe lösen zu können?
Welche Erfahrungen wurden gemacht?
Wie ist man zum Ergebnis gekommen?
-->

## Quellen
[1] Repository mit Python Beispiel-Sourcecode; online: <https://github.com/TGM-HIT/sew4_examples.git>  
[2] Complete walkthrough for a new PyBuilder project; online: <http://pythonhosted.org/pybuilder/walkthrough-new.html>  
[3] PyBuilder Manual <http://pybuilder.github.io/documentation/manual.html>  
[4] PyBuilder Plugins documentation <https://pybuilder.github.io/documentation/plugins.html>  
[5] Virtualenv User Guide <https://virtualenv.pypa.io/en/stable/userguide/#using-virtualenv-without-bin-python>
