import os
import time
import random

# Farben für die Konsolenausgabe
class Colors:
    HEADER = '\033[91m'  # Dunkelrot
    LIGHT_RED = '\033[91m'  # Heller Rot
    LIGHT_BLUE = '\033[94m'  # Hellblau
    PINK = '\033[95m'  # Pink
    TURQUOISE = '\033[96m'  # Türkis
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Farbe zum Zurücksetzen der Konsolenausgabe
reset_color = Colors.ENDC

# Lösche den Bildschirm
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Cool gestalteter Header mit "T9 Hacking Toolkit"
header_color = Colors.HEADER  # Dunkelrot

header = header_color + """
@@@@@@@   @@@@@@      @@@@@@@   @@@@@@    @@@@@@   @@@       
@@@@@@@  @@@@@@@@     @@@@@@@  @@@@@@@@  @@@@@@@@  @@@       
  @@!    @@!  @@@       @@!    @@!  @@@  @@!  @@@  @@!          
  !@!    !@!  @!@       !@!    !@!  @!@  !@!  @!@  !@!      MADE BY @TucoT9            
  @!!    !!@!!@!!       @!!    @!@  !@!  @!@  !@!  !!:       FROM @TeamT9
  !!!      !!@!!!       !!!    !@!  !!!  !@!  !!!  !!!                
  !!:         !!!       !!:    !!:  !!!  !!:  !!!  !!:       
  :!:         !:!       :!:    :!:  !:!  :!:  !:!   :!:      
   ::    ::::: ::        ::    ::::: ::  ::::: ::   :: ::::  
   :      : :  :         :      : :  :    : :  :   : :: : :   

                                                             
""" + reset_color

# Header für das geheime Tool (@T9)
secret_header_color = Colors.PINK  # Pink und Türkis
secret_header = secret_header_color + """
    
 ___                                    .--.                                                             
(   )                                   |  |                                                             
 | |_      ___  ___    .--.      .--.   '..'     .--.       ___ .-. .-.     .--.    ___ .-.    ___  ___  
(   __)   (   )(   )  /    \    /    \         /  _  \     (   )   '   \   /    \  (   )   \  (   )(   ) 
 | |       | |  | |  |  .-. ;  |  .-. ;       . .' `. ;     |  .-.  .-. ; |  .-. ;  |  .-. .   | |  | |       
 | | ___   | |  | |  |  |(___) | |  | |       | '   | |     | |  | |  | | |  | | |  | |  | |   | |  | |        CODET BY                
 | |(   )  | |  | |  |  |      | |  | |       _\_`.(___)    | |  | |  | | |  |/  |  | |  | |   | |  | |        <TucoT9>
 | | | |   | |  | |  |  | ___  | |  | |      (   ). '.      | |  | |  | | |  ' _.'  | |  | |   | |  | |          and 
 | ' | |   | |  ; '  |  '(   ) | '  | |       | |  `\ |     | |  | |  | | |  .'.-.  | |  | |   | |  | |     <WunderElchT9>
 ' `-' ;   ' `-'  /  '  `-' |  '  `-' /       ; '._,' '     | |  | |  | | '  `-' /  | |  | |   ' `-'  /              
  `.__.     '.__.'    `.__,'    `.__.'         '.___.'     (___)(___)(___) `.__.'  (___)(___)   '.__.'   
                                                                                                         
                                                                                                         
""" + reset_color

# Funktion zur Auswahl des Tools
def choose_tool():
    while True:
        clear_screen()
        print(header)

        print(Colors.LIGHT_RED + "Wähle ein Tool aus:")
        print("1. Port-Scanner")
        print("2. Passwort-Knacker")
        print("3. Netzwerk-Angriff")
        print("4. Daten-Exfiltration")
        print("5. Exploit ausführen")
        print("6. Phishing-Angriff")
        print("7. Verschlüsselung")
        print("8. Trojaner erstellen")
        print("9. DDoS-Angriff")
        print("10. Dox (Daten analysieren)")
        print(Colors.LIGHT_RED + "11. Exit" + Colors.ENDC)

        # Benutzereingabe für die Auswahl
        choice = input("Gib die Nummer des Tools ein (1/2/3/4/5/6/7/8/9/10/11): ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            password_cracker()
        elif choice == "3":
            network_attack()
        elif choice == "4":
            data_exfiltration()
        elif choice == "5":
            execute_exploit()
        elif choice == "6":
            phishing_attack()
        elif choice == "7":
            encryption()
        elif choice == "8":
            create_trojan()
        elif choice == "9":
            ddos_attack()
        elif choice == "10":
            dox()
        elif choice == "11":
            exit()
        elif choice == "@T9":
            secret_menu()
        else:
            print(Colors.FAIL + "Ungültige Eingabe. Bitte wähle eine der Optionen (1/2/3/4/5/6/7/8/9/10/11)." + Colors.ENDC)
            input("Drücke Enter, um fortzufahren...")

# Funktion für zufällige Textzeilen mit 1 Sekunde Pause
def generate_random_text_lines(num_lines, theme):
    text = ""
    for i in range(num_lines):
        if theme == "Port-Scanner":
            text += Colors.FAIL + random.choice([
                "Scanne Port 80...",
                "Suche nach offenen Ports...",
                "Port 22 ist geschlossen...",
                "Scanne Port 443...",
                "Port 8080 ist offen...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Passwort-Knacker":
            text += Colors.FAIL + random.choice([
                "Brute-Force-Angriff gestartet...",
                "Knacke Passwort für Benutzer 'admin'...",
                "Passwort erfolgreich geknackt: 'geheim123'...",
                "Dictionary-Angriff läuft...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Netzwerk-Angriff":
            text += Colors.FAIL + random.choice([
                "Starte Man-in-the-Middle-Angriff...",
                "Netzwerk-Paketanalyse läuft...",
                "Führe ARP-Spoofing durch...",
                "Ziel-IP-Adresse: 192.168.1.100...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Daten-Exfiltration":
            text += Colors.FAIL + random.choice([
                "Exfiltriere Datenbankinhalte...",
                "Daten werden verschlüsselt übertragen...",
                "Exfiltriere 100 MB sensibler Daten...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Exploit ausführen":
            text += Colors.FAIL + random.choice([
                "Lade Exploit-Code herunter...",
                "Exploit wird ausgeführt...",
                "Systemzugriff gewonnen...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Phishing-Angriff":
            text += Colors.FAIL + random.choice([
                "Erstelle Phishing-Seite...",
                "Phishing-E-Mail versendet...",
                "Warte auf Benutzerinteraktion...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Verschlüsselung":
            text += Colors.FAIL + random.choice([
                "Verschlüssle Daten mit AES...",
                "Public-Key-Verschlüsselung läuft...",
                "Entschlüsselungstoken generiert...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Trojaner erstellen":
            text += Colors.FAIL + random.choice([
                "Erstelle Trojaner für Windows...",
                "Verbinde zum Command-and-Control-Server...",
                "Trojaner wird übertragen...",
                "Fake-Download: Herunterladen von 1 GB Datei...",
                "Download abgeschlossen (1 GB)",
            ]) + Colors.ENDC + "\n"
        elif theme == "DDoS-Angriff":
            text += Colors.FAIL + random.choice([
                "Starte DDoS-Angriff gegen Ziel-IP...",
                "Verbinde zum Botnetz...",
                "DDoS-Angriff läuft...",
                "Ziel-IP-Adresse: 192.168.1.100...",
            ]) + Colors.ENDC + "\n"
        elif theme == "Dox":
            text += Colors.FAIL + random.choice([
                "Analysiere Daten...",
                "Suche nach Informationen...",
                "Doxing läuft...",
                "Ziel: Benutzer 'Max Mustermann'...",
            ]) + Colors.ENDC + "\n"
        else:
            text += Colors.FAIL + "Unbekanntes Thema..." + Colors.ENDC + "\n"
        # Änderung: Füge den Fortschritt in Prozent hinzu
        progress = (i + 1) / num_lines * 100
        text += f"Fortschritt: {progress:.2f}%\n"
        print(text, end="", flush=True)
        time.sleep(0.6)  # Änderung: Ändere den Pausenintervall auf 0,6 Sekunden
    return text

# Funktionen für die verschiedenen Tools
def port_scanner():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Port-Scanner: Scanne nach offenen Ports..." + Colors.ENDC)
    ip = input("Gib die Ziel-IP-Adresse ein: ")
    print(generate_random_text_lines(100, "Port-Scanner"))
    input("Drücke Enter, um fortzufahren...")

def password_cracker():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Passwort-Knacker: Knacke Passwörter..." + Colors.ENDC)
    username = input("Gib den Benutzernamen ein, und die Plattform. Es klappen Twitch, Youtube, Tiktok, Twitter. Beachte, dass der Account kein 2FA aktiviert haben darf: ")
    print(generate_random_text_lines(100, "Passwort-Knacker"))
    input("Drücke Enter, um fortzufahren...")

def network_attack():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Netzwerk-Angriff: Führe Netzwerkangriff durch..." + Colors.ENDC)
    target_ip = input("Gib die Ziel-IP-Adresse ein: ")
    print(generate_random_text_lines(100, "Netzwerk-Angriff"))
    input("Drücke Enter, um fortzufahren...")

def data_exfiltration():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Daten-Exfiltration: Exfiltriere Daten..." + Colors.ENDC)
    print(generate_random_text_lines(100, "Daten-Exfiltration"))
    input("Drücke Enter, um fortzufahren...")

def execute_exploit():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Exploit ausführen: Führe Exploit aus..." + Colors.ENDC)
    print(generate_random_text_lines(100, "Exploit ausführen"))
    input("Drücke Enter, um fortzufahren...")

def phishing_attack():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Phishing-Angriff: Führe Phishing-Angriff durch..." + Colors.ENDC)
    print(generate_random_text_lines(100, "Phishing-Angriff"))
    input("Drücke Enter, um fortzufahren...")

def encryption():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Verschlüsselung: Verschlüssele Daten..." + Colors.ENDC)
    print(generate_random_text_lines(100, "Verschlüsselung"))
    input("Drücke Enter, um fortzufahren...")

def create_trojan():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Trojaner erstellen: Erstelle Trojaner..." + Colors.ENDC)
    
    # Änderung: Benutzereingabe für die Anzahl der generierten Trojaner
    num_trojans = int(input("Gib die Anzahl der Trojaner ein (1-500): "))
    if num_trojans < 1:
        num_trojans = 1
    elif num_trojans > 500:
        num_trojans = 500

    for i in range(num_trojans):
        # Änderung: Wechsel zwischen Orange und Grün
        if i % 2 == 0:
            print(Colors.FAIL + f"Erstelle Trojaner {i + 1}/{num_trojans} (Orange)..." + Colors.ENDC)
        else:
            print(Colors.OKGREEN + f"Erstelle Trojaner {i + 1}/{num_trojans} (Grün)..." + Colors.ENDC)
        # Änderung: Füge den Fortschritt in Prozent hinzu
        progress = (i + 1) / num_trojans * 100
        print(f"Fortschritt: {progress:.2f}%")
        time.sleep(0.6)  # Änderung: Ändere den Pausenintervall auf 0,6 Sekunden
    
    print("Download abgeschlossen (1 GB)")
    input("Drücke Enter, um fortzufahren...")

def ddos_attack():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "DDoS-Angriff: Führe DDoS-Angriff durch..." + Colors.ENDC)
    target_ip = input("Gib die Ziel-IP-Adresse ein: ")
    print(generate_random_text_lines(100, "DDoS-Angriff"))
    input("Drücke Enter, um fortzufahren...")

def dox():
    clear_screen()
    print(header)
    print(Colors.LIGHT_RED + "Dox (Daten analysieren): Analysiere Daten..." + Colors.ENDC)
    target_user = input("Gib den Benutzernamen oder die E-Mail-Adresse ein: ")
    print(generate_random_text_lines(100, "Dox"))
    input("Drücke Enter, um fortzufahren...")

# Funktionen für das geheime Tool (@T9)
def secret_menu():
    while True:
        clear_screen()
        print(secret_header)

        print(Colors.LIGHT_BLUE + "SECRET T9 TOOl" + Colors.ENDC)
        print(Colors.LIGHT_BLUE + "Wähle eine geheime Option:")
        print("1. Android Knacker")
        print("2. Windows Key Generator")
        print("3. PayPal Tool")
        print("4. Exit" + Colors.ENDC)

        # Benutzereingabe für die Auswahl
        choice = input("Gib die Nummer der geheimen Option ein (1/2/3/4): ")

        if choice == "1":
            android_hacker()
        elif choice == "2":
            windows_key_generator()
        elif choice == "3":
            paypal_tool()
        elif choice == "4":
            return
        else:
            print(Colors.FAIL + "Ungültige Eingabe. Bitte wähle eine der Optionen (1/2/3/4)." + Colors.ENDC)
            input("Drücke Enter, um fortzufahren...")

# Funktionen für die geheimen Tools
def android_hacker():
    clear_screen()
    print(secret_header)
    print(Colors.LIGHT_BLUE + "Android Knacker: Verbinde Android-Gerät mit dem Device..." + Colors.ENDC)
    print("Fehler: Verbindung zum Android-Gerät konnte nicht hergestellt werden.")
    input("Drücke Enter, um fortzufahren...")

def windows_key_generator():
    clear_screen()
    print(secret_header)
    print(Colors.LIGHT_BLUE + "Windows Key Generator: Generiere Windows-Keys..." + Colors.ENDC)

    # Änderung: Benutzereingabe für die Anzahl der generierten Keys
    num_keys = int(input("Gib die Anzahl der zu generierenden Windows-Keys ein (1-500): "))
    if num_keys < 1:
        num_keys = 1
    elif num_keys > 500:
        num_keys = 500

    for i in range(num_keys):
        # Änderung: Windows-Key generieren und untereinander ausgeben
        windows_key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(25))
        print(windows_key)
        # Änderung: Wechsel zwischen Orange und Grün
        if i % 2 == 0:
            print(Colors.FAIL + f"Generiere Windows-Key {i + 1}/{num_keys} (Orange)..." + Colors.ENDC)
        else:
            print(Colors.OKGREEN + f"Generiere Windows-Key {i + 1}/{num_keys} (Grün)..." + Colors.ENDC)
        # Änderung: Füge den Fortschritt in Prozent hinzu
        progress = (i + 1) / num_keys * 100
        print(f"Fortschritt: {progress:.2f}%")
        time.sleep(0.6)  # Änderung: Ändere den Pausenintervall auf 0,6 Sekunden
    
    print("Generierung abgeschlossen.")
    input("Drücke Enter, um fortzufahren...")

def paypal_tool():
    clear_screen()
    print(secret_header)
    print(Colors.LIGHT_BLUE + "PayPal Tool: Zugriff auf PayPal-Konten..." + Colors.ENDC)
    print("Fehler: Keine PayPal-Konten gefunden.")
    input("Drücke Enter, um fortzufahren...")

# Hauptfunktion, um das Tool zu starten
def main():
    choose_tool()

# Das Hauptprogramm starten
if __name__ == "__main__":
    main()
