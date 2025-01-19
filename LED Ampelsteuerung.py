####
#18.01.2025 Titel:
#Mehrere LED's, Transistor, Iterationen
####

####
#In 3 Schritten zu mehr Wissen
#In 4 Einfachen Schritten zur Ampelanlage
####


#Quellen:
#https://tutorials-raspberrypi.de/ampelschaltung-mit-gpio-teil-1/
#Microsoft Copilot
#Netzmafia (Nicht mehr erreichbar)
#Prof. xxx , Funklehrganghilfe 
#Letzte bearbeitung: 19.01.2025

################

####F(or) Y(our) I(nformation)####

##FYI 1/3##
    #Pin Belegung des Raspberry wie auf dem Board:
    #	Pin	Funktion und Beschreibung					Pin	Funktion und Beschreibung
    #	1	3V3 Power 3.3V / max 50mA Stromversorgung	2	5V Power 5V / max 1 A Stromversorgung
    #	3	GPIO 2 (I2C1 SDA) I2C Datenleitung			4	5V Power 5V / max 1 A Stromversorgung
    #	5	GPIO 3 (I2C1 SCL) I2C Clock-Leitung			6	Ground Masse
    #	7	GPIO 4 (GPCLK0) General Purpose Clock		8	GPIO 14 (UART0 TX) Serielle Übertragung
    #	9	Ground Masse								10	GPIO 15 (UART0 RX) Serieller Empfang
    #	11	GPIO 17 Allgemeiner Eingang/Ausgang			12	GPIO 18 (PCM CLK) Pulscode-Modulation
    #	13	GPIO 27 Allgemeiner Eingang/Ausgang			14	Ground Masse
    #	15	GPIO 22 Allgemeiner Eingang/Ausgang			16	GPIO 23 Allgemeiner Eingang/Ausgang
    #	17	3V3 Power 3.3V / max 50mA Stromversorgung	18	GPIO 24 Allgemeiner Eingang/Ausgang
    #	19	GPIO 10 (SPI0 MOSI) SPI Master Out Slave In	20	Ground Masse
    #	21	GPIO 9 (SPI0 MISO) SPI Master In Slave Out	22	GPIO 25 Allgemeiner Eingang/Ausgang
    #	23	GPIO 11 (SPI0 SCLK) SPI Clock-Leitung		24	GPIO 8 (SPI0 CE0) SPI Chip Enable
    #	25	Ground Masse								26	GPIO 7 (SPI0 CE1) SPI Chip Enable
    #	27	GPIO 0 (EEPROM SDA) EEPROM Datenleitung		28	GPIO 1 (EEPROM SCL) EEPROM Clock-Leitung
    #	29	GPIO 5 Allgemeiner Eingang/Ausgang			30	Ground Masse
    #	31	GPIO 6 Allgemeiner Eingang/Ausgang			32	GPIO 12 (PWM0) Pulsweitenmodulation
    #	33	GPIO 13 (PWM1) Pulsweitenmodulation			34	Ground Masse
    #	35	GPIO 19 (PCM FS) Pulscode-Modulation		36	GPIO 16 Allgemeiner Eingang/Ausgang
    #	37	GPIO 26 Allgemeiner Eingang/Ausgang			38	GPIO 20 (PCM DIN) Pulscode-Modulation
    #	39	Ground Masse								40	GPIO 21 (PCM DOUT) Pulscode-Modulation
    #Alles Gleichstrom
    #Achtung der Ampere output Variiert von Modell zu Modell und natürlich von deiner Stromversorgung!

##FYI 2/3
#Widerstandsbestimmung (4 Ringe) bei Kohleschichtwiderständen
    #	Ringfarbe	1. Ring	2. Ring	3. Ring (Multiplikator)	4. Ring (Toleranz)
    # 	schwarz		0		0		-						-
    # 	braun		1		1		× 10					1 %
    # 	rot			2		2		× 100					2 %
    # 	orange		3		3		× 1.000					-
    # 	gelb		4		4		× 10.000				-
    # 	grün		5		5		× 100.000				0,5 %
    # 	blau		6		6		× 1.000.000				0,25 %
    # 	violett		7		7		× 10.000.000			0,1 %
    # 	grau		8		8		-						-
    # 	weiß		9		9		-						-
    # 	gold		-		-		× 0,1					5 %
    # 	silber		-		-		× 0,01					10 %

##FYI 3/3
#Transistor-Grundtypen:
    #Typ			Kennzeichnung	Anwendung
    #NPN-Transistor	C, B, E			Verstärkung von Signalen, Schalten
    #PNP-Transistor	C, B, E			Verstärkung von Signalen, Schalten
    #MOSFET			D, G, S			Leistungsschalter, Verstärker

#(Negativ zu Plus) NPN-Transistoren: Fließt ein kleiner Strom von der Basis (B) zum Emitter (E), kann ein größerer Strom von Kollektor (C) zu Emitter (E) fließen.
#(Plus zu Negativ) PNP-Transistoren: Fließt ein kleiner Strom von der Basis (B) zum Kollektor (C), kann ein größerer Strom von Emitter (E) zu Kollektor (C) fließen.
#MOSFETs: Metall-Oxid-Halbleiter-Feldeffekttransistoren, die durch Spannung an der Gate (G) gesteuert werden und den Stromfluss zwischen Source (S) und Drain (D) ermöglichen.

#Warum brauchen wir einen Transistor?
    #Stromverstärkung: Ein Transistor ermöglicht es dir, mit einem kleinen Steuerstrom (wie von einem Mikrocontroller) eine größere Last zu schalten.
    #Ohne Transistor müsste der Mikrocontroller selbst die gesamte Last tragen, was oft nicht möglich oder effizient ist.
    #Effizienz: Während es scheint, dass zusätzliche Komponenten den Stromverbrauch erhöhen, ermöglichen Transistoren oft eine effizientere Steuerung, insbesondere in komplexeren Schaltungen, wo präzise Kontrolle notwendig ist.
    #Sicherheit: Der zusätzliche Widerstand begrenzt den Strom durch den Transistor und schützt so sowohl die LED als auch den Transistor vor Überstrom, was zu einer längeren Lebensdauer deiner Bauteile führt.
    #Also wird die Spannung so wie die Stromstärke erhöht.
    #Hierfür muss man wissen wieviel Strom verbraucht wird.
    #Der 3,3V Versorgung Liefert genug für eine LED aber 3 bräuchten schon mindestens 6V in Reihe.
    #Damit wir die 3,3V Spannung nutzen schalten wir Sie also die LED's Paralell dazu.
    #Kurzum wir brauchen pro LED cirka 20mA und wir bekommen nur 50mA als Steuerstrom geliefert.
    #Der Transistor versorgt also die 3 LED's und kann zusätzlich als Schalter funktionieren.
    
#Wir benutzen einen BC 547, dieser kann bis 45V und 100mA geben ( max 500mW).
#Der BC 547 kann zwischen 100 und 800 Signale effektiv verstärken.    
    #Wir nehmen diesen weill er Kostengünstig und allgemein für Schalt- und Verstärkungsanwendungen benutzt wird.
    #(Der BC 547 ist ein NPN-Bipolarertransistor)
    #Bevor der Transistor überhaupt schalten kann benötigt er min. 0,6V (Schwellspannung), wegen dem Material / Aufbau im Transistor.
    
#Beispiel:
    #Der BC547 kann eine maximale Kollektor-Emitter-Spannung (Vce) von 45V und einen maximalen Kollektorstrom (Ic) von 100mA liefern.
    #Der Basisstrom wird durch einen GPIO-Pin des Raspberry Pi gesteuert, und der Emitter ist mit GND verbunden.
    #Der Kollektor wird mit den LEDs verbunden:   

#GPIO ----[R_base]----|> (Basis)
#                        BC547 
#3,3V ----[R1]----|>---- (Kollektor)
#     \---[R2]----|>---- (Kollektor)
#      \--[R3]----|>---- (Kollektor)
#(GND) (Emitter)

#R_base ist der Vorwiderstand für den Basisstrom des Transistors und hier wird geschaltet (GPIO).
#R1, R2 und R3 sind die Vorwiderstände für die LEDs.
    
################

####Ampelschaltung LED   
##Aufbau 1/4)##
##Steckboard
#Verbine den 3,3V mit einen in Reihe geschalteten 470Ω Wiederstand.
#Vom Wiederstand zum Minus Pol einer LED in reihe weiter zum C Pole eines Transistors.
#Vom B Pol eine Transistors (BC 547) einen 10kΩ WIederstand in reihe und von diesem zum GPIO 21.
#Fehlt noch der E Pol des Transistors den Verbinden wir mit einem Ground z.b.: Pin6
#Als LED habe ich eine Rote gewählt.

#_________________________3,3 V Plus
# |
#470Ω
# |
#LED
# |
# C-(Transistor)-E
# B				|
# |				|
#10kΩ			|
# |				|
#GPIO			|
#				|
#_______________|_________Ground

#Falls noch keine Pakete installiert wurden:
#Ins Terminal wechseln und Thonny installieren oder Geany, gegebenenfalls in nano weiter arbeiten.
#Pakete installieren für python 2 und oder python3 und python-dev
#GPIO Bibliothek installieren!
#sudo apt-get install python3-rpi.gpio
#Gegebenenfalls mit pip installieren, lasst euch vom Copilot helfen oder nutzt euer Gehirn!
#guix ist noch eine alternative paketverwaltung die viele alte pakete hat.

#Die wichtigen Pakete sind:
#RPI.GPIO 
#python-dev

####
##LED blinken lassen 2/4 ##
##Jeweils ausklammern siehe programmierung unten (4/4)
    

#import RPi.GPIO as GPIO #Bibliotheken einbinden
#import time
 

#GPIO.setmode(GPIO.BCM) #GPIO Modus (BOARD / BCM)
#GPIO.setmode(GPIO.BOARD)
 
#GPIO.setup(7, GPIO.OUT) #Richtung der GPIO-Pins festlegen (IN / OUT)
 

#while True:				#unendliche Schleife
    
    #GPIO.output(7, True) 	#Pin 26 HIGH Pegel
    #time.sleep(0.05) 		#eine halbe Sekunde warten
    #GPIO.output(7, False)	#Pin 26 LOW Pegel
    #time.sleep(0.05)		#eine halbe Sekunde warten

####

##LED sollte blinken.
    
    #Troubleshooting:
    #Bauteile durchmessen, sind alle in Ordnung?
    #Schaltung überprüfen, LED pluspol an plus?
    #Gegebenenfalls GPIO adressierung überprüfen, bei GPIO.BCM einstellig, also nicht 07 für PIN 7.
    #Ist der GPIO belegt? Sind Shields oder Hat's installiert die die Pins belegen?
        #Beispiel um in einer Shell mit python nachzuprüfen ob der GPIO belegt ist:
            #import RPi.GPIO as GPIO
            #GPIO.setmode(GPIO.BCM)
            #GPIO.setup(22, GPIO.IN)  # Beispiel für GPIO 17 als Eingang
            #input_state = GPIO.input(22)
            #print("GPIO 22:", "HIGH" if input_state else "LOW")
        #Wenn high ausgegeben wird ist der GPIO belegt. Achtung die Einrückung muss gleich sein! sonst:
        # File "<stdin>", line 2
        #GPIO.setmode(GPIO.BCM)
        #IndentationError: unexpected indent # Einrückungs Fehler
        
##FYI:
    #GPIO.setmode(GPIO.BCM):
    #BCM steht für "Broadcom SOC channel".
    #In diesem Modus werden die GPIO-Pins nach ihrer Broadcom-Nummerierung (den BCM-Nummern) adressiert. Diese Nummern entsprechen den internen Bezeichnungen auf dem Raspberry Pi SoC (System on a Chip).
    #Beispiel: Der GPIO-Pin, der als GPIO 18 auf der Platine bezeichnet wird, ist in der BCM-Nummerierung auch GPIO 18.

    #GPIO.setmode(GPIO.BOARD):
    #In diesem Modus werden die GPIO-Pins nach ihrer physischen Pin-Nummerierung auf dem Board adressiert.
    #Die Pins werden entsprechend ihrer physischen Position auf dem GPIO-Header des Raspberry Pi nummeriert.
    #Beispiel: Der physische Pin 12 auf dem GPIO-Header entspricht GPIO 18 in der BCM-Nummerierung.

################

####
##Ampelschaltung 3/4 ##
##Aufbau

#Wir brauchen 3 LED's, 13 Kabel, 3 Transistoren, Schalter / Taster, 7 Wiederstände.
    #Im Prinziep widerholen wir die Schaltung von oben.
    #Geben aber jedem B Pol eines Transistors einen eigenen GPIO.
    #Zusätzlich schalten wir einen Taster mit Wiederstand an einen GPIO

#Je LED und Schaltung Paralell wiederholen:
    #_________________________3,3 V Plus
    # |
    #470Ω
    # |
    #LED
    # |
    # C-(Transistor)-E
    # B				|
    # |				|
    #10kΩ			|
    # |				|
    #GPIO			|
    #				|
    #_______________|_________Ground

#Plus einmal Schalter dazu aufbauen:
#Schalter:
    #_________________________3,3 V Plus
    # |
    #Taster / Schalter
    #(Eingang)
    # |
    #(Ausgang)
    # |_____________GPIO
    # |
    #20kΩ
    #_|______________________Ground

##Ampelschaltung 4/4 ##
##Jeweils ausklammern siehe programmierung oben (2/4)

#Ich habe die GPIO's überprüft und 17, 27 und gewählt für die LED's. Und GPIO 16 für den Schalter.

#Wir wollen folgenden Phasen:
    #1.kein Tastendruck – dauerhaft rot (gelb und grün aus)
    #2.Taster wird gedrückt – rot und gelb leuchten (grün aus), Dauer: 2 Sekunden
    #3.Wechsel auf grün (rot und gelb aus), Dauer: 10 Sekunden
    #4.Wechsel auf gelb (rot und grün aus), Dauer: 3 Sekunden
    #5.Zurück zu Schritt 1.
    

import RPi.GPIO as GPIO		#Bibliotheken einbinden
import time

GPIO.setmode(GPIO.BCM)		#GPIO Modus (BOARD / BCM)

GPIO.setwarnings(False)		#Warnungen ausschalten für doppelte Pin Belegung. Nur wenn Ihr Die GPIO's überprüft hast!

ROT = 17					#GPIO Pin Belegung mit Namen versehen
GELB = 27
GRUEN = 22
TASTER = 16

GPIO.setup(ROT, GPIO.OUT) 	#rot  #Ausgabe / Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GELB, GPIO.OUT) 	#gelb
GPIO.setup(GRUEN, GPIO.OUT) #gruen
GPIO.setup(TASTER, GPIO.IN) #Taster 

def umschalten():			#def = function mit Namen "umschalten". Definiert den Ablauf ähnlich boot programm. Liste wird nur einmal abgearbeitet.
    
    GPIO.output(ROT, True)	#Phase 2
    GPIO.output(GELB, True)
    GPIO.output(GRUEN, False)
    time.sleep(2)
    
    GPIO.output(GRUEN, True)#Phase 3
    GPIO.output(ROT, False)
    GPIO.output(GELB, False)
    time.sleep(10)
    
    GPIO.output(GELB, True)	#Phase 4
    GPIO.output(GRUEN, False)
    time.sleep(3)
    
    GPIO.output(ROT, True)	#zurueck zu Phase 1
    GPIO.output(GELB, False)
 

while True:					#Endlosschleife
    
    GPIO.output(ROT, True)	#Phase 1
    GPIO.output(GELB, False)
    GPIO.output(GRUEN, False)
 
    
    tasterStatus = GPIO.input(TASTER) #Diese Zeile liest den aktuellen Zustand des Tasters ein (ob er gedrückt ist oder nicht) und speichert diesen Zustand in der Variable tasterStatus. Der aktuelle Status wird in jeder Iteration der Endlosschleife überprüft.
    if (tasterStatus): 					#Wenn der Taster gedrückt ist (tasterStatus ist True), wird die Funktion umschalten() aufgerufen, die die Zustände der LEDs ändert.
        umschalten()

##FYI
#Eine Iteration ist im Wesentlichen ein Durchlauf in einer Schleife. In der Programmierung bedeutet das, dass ein bestimmter Codeblock wiederholt ausgeführt wird, bis eine bestimmte Bedingung erfüllt ist oder die Schleife bewusst beendet wird.

################

##
#Wir haben gelernt was ein Transistor ist und wofür man den braucht.    
#Wir haben gelernt wie man GPIO's ausließt und welche Modus man benutzt.
#Wir haben gelernt wie wir vorhandenes Wissen mit LED programmierung erweitern kann, in dem wir für die GPIO's und functionen Namen vergeben.
#Und wir haben gelernt was eine Iteration ist.
#Keep it simple and stupid, KISS  (◕‿↼) 

################
####  Ende  ####
################     
 