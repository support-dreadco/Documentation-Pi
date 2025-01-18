####
#16.01.2025 Raspberry Pi LED Ansteuern:
#GPIO definieren, Zeiten definieren, GPIO abfragen
####

####
#In 6 Schritten zu mehr Wissen
#In 3 Einfachen Schritten zur leuchtenden LED
#In 5 Einfachen Schritten zum Lichtschalter
####


#GPIO am Raspberry auslesen mit hilfe von Tutorials / Quellen:
#https://tutorials-raspberrypi.de/raspberry-pi-gpio-erklaerung-beginner-programmierung-lernen/
#https://blog.berrybase.de/raspberry-pi-gpio-dein-leitfaden-zu-pins/
#Copilot von Microsoft
#Wikipedia
#https://www.elektronik-kompendium.de/
#Letzte bearbeitung: 18.01.2025

################

####F(or) Y(our) I(nformation)####

##FYI 1/6##
    #Pin Belegung des Raspberry wie auf dem Board:
    #	Pin	Funktion und Beschreibung					          Pin	Funktion und Beschreibung
    #	1	3V3 Power 3.3V / max 50mA Stromversorgung	    2	5V Power 5V / max 1 A Stromversorgung
    #	3	GPIO 2 (I2C1 SDA) I2C Datenleitung			      4	5V Power 5V / max 1 A Stromversorgung
    #	5	GPIO 3 (I2C1 SCL) I2C Clock-Leitung			      6	Ground Masse
    #	7	GPIO 4 (GPCLK0) General Purpose Clock		      8	GPIO 14 (UART0 TX) Serielle Übertragung
    #	9	Ground Masse								                  10	GPIO 15 (UART0 RX) Serieller Empfang
    #	11	GPIO 17 Allgemeiner Eingang/Ausgang			    12	GPIO 18 (PCM CLK) Pulscode-Modulation
    #	13	GPIO 27 Allgemeiner Eingang/Ausgang			    14	Ground Masse
    #	15	GPIO 22 Allgemeiner Eingang/Ausgang			    16	GPIO 23 Allgemeiner Eingang/Ausgang
    #	17	3V3 Power 3.3V / max 50mA Stromversorgung	  18	GPIO 24 Allgemeiner Eingang/Ausgang
    #	19	GPIO 10 (SPI0 MOSI) SPI Master Out Slave In	20	Ground Masse
    #	21	GPIO 9 (SPI0 MISO) SPI Master In Slave Out	22	GPIO 25 Allgemeiner Eingang/Ausgang
    #	23	GPIO 11 (SPI0 SCLK) SPI Clock-Leitung		    24	GPIO 8 (SPI0 CE0) SPI Chip Enable
    #	25	Ground Masse								                26	GPIO 7 (SPI0 CE1) SPI Chip Enable
    #	27	GPIO 0 (EEPROM SDA) EEPROM Datenleitung		  28	GPIO 1 (EEPROM SCL) EEPROM Clock-Leitung
    #	29	GPIO 5 Allgemeiner Eingang/Ausgang			    30	Ground Masse
    #	31	GPIO 6 Allgemeiner Eingang/Ausgang			    32	GPIO 12 (PWM0) Pulsweitenmodulation
    #	33	GPIO 13 (PWM1) Pulsweitenmodulation			    34	Ground Masse
    #	35	GPIO 19 (PCM FS) Pulscode-Modulation		    36	GPIO 16 Allgemeiner Eingang/Ausgang
    #	37	GPIO 26 Allgemeiner Eingang/Ausgang			    38	GPIO 20 (PCM DIN) Pulscode-Modulation
    #	39	Ground Masse								                40	GPIO 21 (PCM DOUT) Pulscode-Modulation
    #Achtung der Ampere output Variiert von Modell zu Modell und natürlich von deiner Stromversorgung!
    
##FYI 2/6##
#1 A (Ampere) = 1.000mA (Milli) = 1.000.000μA (Mikro)
#1 Milliampere (mA) ist gleich 1.000 Mikroampere (μA)
#1 Ampere (A) ist gleich 1.000 Milliamperes (mA)
#1 Mikroampere (μA) ist ein Millionstel Ampere (1 μA = 0,000001 A)
#500μA = 0,5mA = 0,0005 A
    
##FYI 3/6##  
#Raspberry Pi Modell 3 liefert Gleichspannung
    
#Thonny ist eine Textbearbeitungsprogramm das zusetzlich ein direktes Stoppen und Ausführen des Textes / Scripts zulässt.
#Zusätzlich hat Thonny eine Shell, mit der wir sehen was unser Script eigentlich macht. Eine Shell ist ein Benutzerschnittstelle zu deinem Script. Sie fungiert ähnlich einem eigenen Betriebssystem ohne das eigentliche Kern Betriebsystem, den Kernel zu stören.
    #Üblicherweise starten Betriebssysteme am Ende des Hochfahrens eine primäre Shell-Instanz und -Sitzung, die im Normalbetrieb erst beim Ausschalten/​Herunterfahren/​Abmelden beendet wird und typischerweise eine Anmeldung erfordert. Die Shell-Instanz erzeugt zur Laufzeit (englisch runtime) eine Arbeitsumgebung (englisch environment).
    #Innerhalb dieser Umgebung können Programme gestartet werden und laufen (vgl. Laufzeitumgebung). Freilich können dies auch weitere, sekundäre (Sub-)Shells sein – sowohl zusätzliche Instanzen derselben oder einer anderen Software. 
    #Je nach Zweck und Leistung eines Computers und seines Betriebssystems werden unterschiedliche Typen von Shells eingesetzt. Eine Shell hat typischerweise entweder …
    #Eine Befehlszeilenschnittstelle (englisch command-line interface, CLI) und arbeitet zeilenweise und zeichenorientiert im Textmodus, oder …
    #Eine grafische Benutzerschnittstelle (englisch graphical user interface, GUI) und arbeitet pixelorientiert im Grafikmodus.
    #In Raspberry Pi's Fall hat unser Kernel eine Desktop Umgebung geschaffen (Gnome, KDE, ....) und wir haben Thonny gestartet der eine Sub-Shell GUI bereitstellt. Alternativ könnte man Geany benutzen.
    #Würden wir nur mit dem Terminal arbeiten ist dies auch eine CLI Shell. Dann würden wir über den Texteditor nano unser Text bearbeiten können.
    #Der Vorteil von GUI also Graphical User Interface ist das man mit der Maus Knöpfe zum steuern hat.
    #Während eine CLI ähnlich dem Programmieren wissen zu Befehlen benötigt.
    #Der Befehl cd um einen Order zu wechseln oder dir der uns den Ordnerinhalt anzeigt.
    #Bei einigen nicht sehr Leistungsstarken Computern empfiehlt sich eine einfache CLI-Shell.

##FYI 4/6##
##Wiederstände    
    #Widerstandsbestimmung mit der Widerstandsfarbcode-Tabelle
    #Bevor man mit der Widerstandsbestimmung anfängt, muss man zählen, wie viele Farbringe auf dem Widerstand aufgebracht sind. Kohleschichtwiderstände haben üblicherweise 4 Ringe. Metallschichtwiderstände haben 5 Ringe. Bei Widerständen mit 5 Ringen ist der Widerstandswert etwas genauer angegeben.
    #Dann muss man feststellen welcher Ring der erste ist. Üblicherweise versucht man herauszufinden, welcher Ring der letzte Ring ist. Es ist der Toleranzring, der angibt, wieviel Prozent der bestimmte Widerstandswert vom tatsächlichen Widerstandswert abweichen darf.
    #Meistens hat der Toleranzring die Farbe Gold. Wenn es diese Farbe nicht gibt, dann muss man auf die beiden äußeren Ringe achten. In der Regel hat einer einen größeren Abstand zum Körperende. Das ist der Toleranzring.
    #Dann beginnt man von vorne an den Widerstandswert zusammenzusetzen. Die Farben haben bestimmte Werte. Der erste und der zweite Ring bestimmen den Widerstandszähler (beim Kohleschichtwiderstand, 4 Ringe). Der dritte Ring dient als Multiplikator. Er bestimmt wie hoch der Widerstandswert ist.
    #Der vierte Ring ist der Toleranzring, der die Abweichung des Widerstandswerts bestimmt (beim Kohleschichtwiderstand, 4 Ringe).
    #Hinweis: Die Farben Gold und Silber enthalten Metallpigmente, die man an Hochspannungswiderständen nicht mag. Deshalb gilt hier für die Toleranzringe 5% Gelb statt Gold und 10% Weiß statt Silber.

#Widerstandsbestimmung (4 Ringe) bei Kohleschichtwiderständen
#	Ringfarbe	  1. Ring	  2. Ring	  3. Ring (Multiplikator)	  4. Ring (Toleranz)
# 	schwarz		0		      0		      -						              -
# 	braun		  1		      1		      × 10					            1 %
# 	rot			  2		      2		      × 100					            2 %
# 	orange		3		      3		      × 1.000					          -
# 	gelb		  4		      4		      × 10.000				          -
# 	grün		  5		      5		      × 100.000				          0,5 %
# 	blau		  6		      6		      × 1.000.000				        0,25 %
# 	violett		7		      7		      × 10.000.000			        0,1 %
# 	grau		  8		      8		      -						              -
# 	weiß		  9		      9		      -						              -
# 	gold		  -		      -		      × 0,1					            5 %
# 	silber		-		      -		      × 0,01					          10 %

#Widerstandsbestimmung (5 Ringe) bei Metallschichtwiderständen
#Ringfarbe	  1. Ring	  2. Ring	  3. Ring	  4. Ring (Multiplikator)	  5. Ring (Toleranz)
# 	schwarz	  0		      0		      0		      -						              -
# 	braun	    1		      1		      1		      × 10					            1 %
# 	rot		    2		      2		      2		      × 100					            2 %
# 	orange	  3		      3		      3		      × 1.000					          -
# 	gelb	    4		      4		      4		      × 10.000				          -
# 	grün	    5		      5		      5		      × 100.000				          0,5 %
# 	blau	    6		      6		      6		      × 1.000.000				        0,25 %
# 	violett	  7		      7		      7		      × 10.000.000			        0,1 %
# 	grau	    8		      8		      8		      -						              -
# 	weiß	    9		      9		      9		      -						              -
# 	gold	    -		      -		      -		      × 0,1					            5 %
# 	silber	  -		      -		      -		      × 0,01					          10 %


##LED Spannung und Wiederstände
#Entscheident ist die Farbe der LED für die Versorgung mit Spannung:
#LED Farbe:		  Spannung	  Typisch Spannung (V):	  Typische Stromstärke (A):
#Infrarot-LED: 	1,2–1,8 V, 	1,3 V					          0,02 - 0,05 A
#Rot: 			    1,6–2,2 V	  2 V						          0,02 - 0,05 A
#Gelb, Grün: 	  1,9–2,5 V	  2 V						          0,02 - 0,05 A
#Blau, Weiß: 	  2,7–3,5 V	  3 V						          0,02 - 0,05 A
#UV-LED: 		    3,1–4,5 V 	3,7 V					          0,02 - 0,05 A
#Bei 5 V ist die Sperrspannung erreicht, die LED wird normalerweise zerstört

##FYI 5/6##
#Um den Wiederstand zu berrechnen Wird das Ohm Gesetz benutzt.
#U(nterschied) = Spannung in V(olt), geteilt durch R(esistance) = Wiederstand in Ω(Ohm), mal I(ntensität) = Stromstärke
    #Also U/R*I
        #Beispiel Berrechnung:
        #Wir haben Beispiel eine Grüne LED und wollen sie mit 2 V und 0,2 A zu versorgen.
        #Wir wissen auf dem Board gibt es 3,3 V und 5 V zur versorgung, wir beschließen 3,3 V zu nutzen.
        #Da wir bereits 2 V für die LED brauchen ziehen wir von 3,3 V den Betrag ab, übrig bleibt, 1,3V.
        #Das ist die Spannung die am Wiederstand anliegt.
        #1,3 V / 0,02 A = 65 Ω
        #Uns reicht also ein 65 Ω Wiederstand!

##FYI 5/6##
        #Beispiel 2:
        #Blaue LED 2 V, ich habe einen 22 Ω Wiederstand vorgeschaltet brennt Sie durch oder nicht?
        #Sie brennt nicht durch da sie bis zu 3,5 V aushält und nur max 3,3 V anliegen richtig?
        #Es liegen maximal 0,2 V für den Wiederstand an und es reicht ein 10 Ω Wiederstand um die LED zu schützen, richtig oder falsch?
        #In Wahrheit soll man immer einen Wiederstand vorschalten aber hier brauchen wir keinen da nie mehr als 3,3 V anliegen können, oder?
            #Lösung:
            #¡ʇsı ʇƃǝlǝƃsnɐ ʌ 5,3 sıq ǝıs pun uǝƃǝıluɐ ʌ 3,3 ɹnu ɥɔılɥɔäsʇɐʇ ɐp ɥɔɹnp ʇɥɔıu ʇuuǝɹq pǝl ǝnɐlq ǝıp

            #Die Wahrheit: Die LED wird so viel Strom ziehen wie sie kann ! Ein Vorwiederstand ist also immer nötig!
            #Ohne einen Wiederstand gibt mir das Messgerät 17,7mA - 17,8mA aus. Hierfür muss in den Aufbau in Reihe, das Messgerät zugeschaltet Werden, ohne einen Verbraucher wie eine LED gibt es einen Kurzschluss.
            #Das Messgerät bietet kaum Wiederstand, daher muss ein Verbrauche mit einem höheren Wiederstand zugeschaltet werden.
            #Die blaue LED hat also selbst einen Wiederstand von Gerundet 185Ω, oder anders gesagt sie verbraucht 0,0178 A.
            #Die blaue LED hat also einen Verbrauch von 0,05874 Watt beziehungsweise in einer Stunde sind das ganze 0,05874 Wattstunden!!!
                #Eine Standart Badewann fast 150 Liter. Dafür braucht man 0,25kWh Energie um Sie zu Füllen und zum erwährmen braucht man 250 Wattstunden.
                #t=Wh/W oder Zeit=Energie/Leistung. Das heißt für die LED t=250Wh/0,05874W ≈ 4258 Stunden ≈ (/24) 177 Tage 
                #Die blaue LED braucht also etwa 4258 Stunden (rund 177 Tage) um die selbe Energie einer Badewanne zu Verbrauchen.
            #Zuletzt noch, ein Kurzschluss ist wenn Strom ungehindert fließen kann, ist die Badewanne undicht läuft Sie aus.

################

####LED 1/3####
##Aufbau
    #Verbinde einen Ground Pin mit einem Steckboard. Schalte einen Wiederstandt 110Ω - 400Ω vor eine LED und Verbinde die LED mit dem anzusteuernden PIN (23)

import RPi.GPIO as GPIO #Importieren der Bibliothek GPIO
        #Um die fuctionen anzusehen und was in der Bibliothek alles steckt, öffne eine shell und gebe den Import befehl wie oben ein (In Thonny unteres Fenster).
        #Dann help(GPIO) eingeben. Meistens muss noch ein Doppelklick ausgeführt werden jedoch sieht man jetzt den Bibliotheks Inhalt.


import time #Die Bibliothek Time importieren um Halt befehle aus geben zu können.


GPIO.setmode(GPIO.BCM) # Definieren der Boardnummern (1-40) oder GPIO Nummern die wir ansprechen wollen.

GPIO.setup(23, GPIO.OUT) # Pin Out definieren

####LED 2/3####
##Zum aktivieren jeweils ausklamern:
    GPIO.output(23, GPIO.HIGH) # Function definieren LED an 3,3V
    GPIO.output(23, GPIO.LOW) # Function definieren LED aus 0V

        #Troubleshooting:
        #Die Funktionen müssem jeweils ausgeklammert werden, ob LED an oder aus
        #Gegeb. das Script stoppen und dann auf run klicken.
        #Je nach dem ob LED an oder aus seien soll. Das lange Bein der LED an Plus (GPIO 23)
        #Wiederstand vor oder danach in "reihe" schalten cirka 110Ω - 400Ω ! Ist Minus an einen Ground angeschlossen?

####LED 3/3####
##Zum aktivieren ausklammern
    #Blinkschaltung:
    #for i in range(5):
    #    GPIO.output(23, GPIO.HIGH)
    #    time.sleep(0.5)
    #    GPIO.output(23, GPIO.LOW)
    #    time.sleep(0.5)
    #LED sollte 5mal blinken

################

####Schalter 1/5####
##Aufbau für das auslesen von einen Taster / Schalter
    #Zu dem obigen Aufbau zusätzlich benötigt man einen Schalter / Taster & einen 10KΩ Wiederstand (rot, rot, rot, gold)
    #In Reihe den Wiederstand zu einer neuen Leitung und Minus Schalten.
    #Danach Kreuzung bauen Leitung zu GPIO 25 legen und dahinter in Reihe den Schalter / Taster.
    #Hinter dem Schalter Ausgang eine Leitung in reihe zu Plus legen.
    #Warum das ganze? Solange der Schalter nicht gedrückt ist, ist die Verbindung zwischen der 3.3V Spannung und dem GPIO offen. Damit aber ein eindeutiger Zustand erkannt wird (entweder 0V oder 3.3V), ist die Verbindung über einen sehr großen Widerstand zum Masseanschluss verbunden.
    #Sobald der Taster gedrückt wird, schließt sich die Verbindung und am GPIO liegen 3.3V an.
        
# Input GPIO definieren
GPIO.setup(24, GPIO.IN)

#Status abfragen
GPIO.input(24)
#Dies wird entweder 0 (wenn der Taster nicht gedrückt wurde) oder 1 (Taster gedrückt) ausgeben.
#GPIO.input ist zum lesen des Pins da!
#GPIO.output zum schreiben / setzen des Pins!

####Schalter 2/5####
##Zum aktivieren ausklammern
    #Im letzten Schritt erweitern wir das Programm nun noch folgendermaßen, sodass die LED immer dann an ist, wenn der Taster auch gedrückt wird.
    # Endlosschleife
    #while True: 								#Beginn der Endlosschleife
    #    if GPIO.input(24) == 0:  				#lesen des Zustands an 24 ob 0
            # Ausschalten
    #        GPIO.output(23, GPIO.LOW)  		#setzen des pin 23 auf 0
    #    else:
            # Einschalten
    #        GPIO.output(23, GPIO.HIGH) 		#setzen des pin 23 auf 1 (strom 3,3V)

####Schalter 3/5####
##Zum aktivieren ausklammern
    #Diese Schleife können wir auch erweitern um uns anzeigen zu lassen ob der Schalter / Taster gedrückt wurde.
    #while True:
    #    if GPIO.input(24) == 0:  
    #        GPIO.output(23, GPIO.LOW)
    #        print("LED aus")					#Schreibe "LED aus"
    #    else:
    #        GPIO.output(23, GPIO.HIGH)
    #        print("LED an")					#Schreibe "LED an"

####Schalter 4/5####
##Zum aktivieren ausklammern
#Damit der Print befehl nur einmal angezeigt wird

#prev_input = 1  # Initialer Zustand (HIGH)

#Dieser Schritt setzt die Variable prev_input auf 1 (HIGH). Das bedeutet, dass wir davon ausgehen, dass der Taster initial nicht gedrückt ist. Dies dient als Referenzpunkt, um zu erkennen, ob sich der Zustand des Tasters ändert.

#while True:
#    input = GPIO.input(24)					#Lesen des Zustands an Pin 24
#    if input == 0 and prev_input == 1:		#Überprüfung des Zustand und ob der Vorherige High war
#        GPIO.output(23, GPIO.LOW)			#Wenn dies der Fall ist wurde der Taster gerade gedrückt
#        print("LED aus")					#Damit sollte er "LED aus" ausgeben
#    elif input == 1 and prev_input == 0:	#Überprüft gedrückt ist
#        GPIO.output(23, GPIO.HIGH)			#Überprüft ob er gerade losgelassen wurde
#        print("LED an")						#Sollte "LED an" ausgeben
    
#    prev_input = input  					#Speichert den Wert input in prev_input
                                            #Dies stellt sicher, dass der aktuelle Zustand des Tasters beim nächsten Durchlauf der Schleife als vorheriger Zustand erkannt wird.

####Schalter 5/5####
##Zum Aktivieren ausklammern
    #Noch komplizierter / Nützlicher
    #Was wenn wir die Aktuelle Zeit wann der Schalter gedrückt wurde ausgeben wollen?
    #Wir haben bereits die time Bibliothek implementiert
    #Wir müssen zusätzlich das Ausgabe Format definieren also Stunden Minuten Sekunden oder Jahr, etc
    #Wir müssen dann den Print Befehl syntax gerecht umschreiben für python3



#prev_input = 1  															# Initialer Zustand (HIGH)

#while True:
    #input = GPIO.input(24)
    #current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())		#Die aktuelle zeit im Stringformat, Jeder Buchstabe steht für einen Teil der Zeit, %Y-%m-%d %H:%M:%S = 2025-01-16 11:47:03
    #if input == 0 and prev_input == 1:
        #GPIO.output(23, GPIO.LOW)
        #print(current_time + " - LED aus")									#Siehe weiter unten Syntax print
    #elif input == 1 and prev_input == 0:
        #GPIO.output(23, GPIO.HIGH)
        #print(current_time + " - LED an")
    
    #prev_input = input  													# Update den vorherigen Zustand


#Der Syntax zu Print befehlen in Python kann auf drei verschiedenen Arten gemacht werden:

#Als F-string:
    #print(f"{current_time} - LED aus")
        #Vorteile:
        #Lesbarkeit: Sehr klar und leicht verständlich, direkt in den String eingebettet.
        #Leistung: Schneller als die anderen Methoden, da es direkt von der Sprache unterstützt wird.
        #Flexibilität: Unterstützt komplexe Ausdrücke direkt innerhalb der geschweiften Klammern.
        #Nachteile:
        #Kompatibilität: Funktioniert nur mit Python 3.6 und höher.
        #Sicherheit: Mögliche Sicherheitsrisiken bei der Verwendung mit unkontrollierten Eingaben, da der Ausdruck direkt ausgewertet wird.

#Als String Format:
    #print("{} - LED aus".format(current_time))
        #Vorteile:
        #Lesbarkeit: Klar und leicht verständlich, besonders bei komplexeren Formatierungen.
        #Kompatibilität: Funktioniert mit allen Python-Versionen ab 2.7.
        #Nachteile:
        #Leistung: Etwas langsamer als f-Strings, da es eine zusätzliche Methode aufruft.
        #Länge: Kann länger und weniger lesbar sein, besonders bei mehreren Platzhaltern.

#Und als Verkettung:
    #print(current_time + " - LED aus")
        #Vorteile:
        #Einfachheit: Einfach und direkt, keine zusätzlichen Funktionen erforderlich.
        #Kompatibilität: Funktioniert mit allen Python-Versionen.
        #Nachteile:
        #Lesbarkeit: Kann weniger lesbar sein, besonders bei vielen Teilen.
        #Leistung: Weniger effizient bei vielen Verkettungen, da jedes + einen neuen String erzeugt.
        #Fehleranfälligkeit: Erfordert explizites Konvertieren von Nicht-String-Typen, z.B. str(variable), was Fehler verursachen kann.

################

##
#Wir haben gelernt wie man einen einfachen Aufbau mit script für eine LED am Raspberry Pi ausführt.    
#Wir haben gelernt wie wir einfache Scripte verkomplizieren können in dem wir Zustände zum abfragen speichern.
#Darüber hinaus könnte man das Script für die Zukunft erweitern um eine Abfrage wie lange war die LED an und wie oft wurde sie angeschaltet.
#Dies könnte sehr nützlich sein, nicht nur als Hausmeister, sondern um Wartungspläne zu schreiben und Geld zusparen beim Einkauf von Leuchtmitteln.
#(Leuchtmittel sind Tagespreis abhängig) Wichtig sind Brenndauer und Schaltzyklen, die norm. vom Hersteller angegeben werden.
#Viel Hintergrundwissen ist nötig um eigentliche Projekte zu verwirklichen und Probleme zu vermeiden.
#Keep it simple and stupid, KISS  ♥‬ 

################
####  Ende  ####
################   
