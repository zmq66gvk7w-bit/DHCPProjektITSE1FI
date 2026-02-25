from datetime import date, timedelta
heute = date.today()

#Checkt MAC nach Gültigkeit
def MAC_Überprüfer(clientinput):
    
    if clientinput == "":
        print("Bitte geben Sie etwas ein")
        return False

    split_Ergebnis = str(clientinput).split(":")

    if len(split_Ergebnis) != 6:
        print(f"Ihre Eingabe {clientinput} ist nicht gültig, da diese\n"
              "aus weniger oder mehr als 6 Hexadezimalgruppen besteht.")
        return False

    # Broadcastcheck
    if all(group.upper() == "FF" for group in split_Ergebnis):
        print("Broadcasts sind nicht erlaubt.")
        return False

    # Hexadezimalcheck
    for group in split_Ergebnis:
        if len(group) != 2:
            print("Jede Gruppe muss genau 2 Zeichen haben.")
            return False

        for char in group:
            if char.upper() not in "0123456789ABCDEF":
                print("Ungültige Hexadezimalzeichen gefunden.")
                return False

    print("MAC-Adresse ist gültig.\n1")
    return True
#Checkt MAC nach Gültigkeit

leasetime = heute + timedelta(days=7)
hostAdresse = 1
netzIp= "192.168.1."
IPListe = []
ende = False
while ende == False:
    #IPliste leeren wenn lease time vorbei
    heute = date.today()
    if heute > leasetime:
        leasetime = heute + timedelta(days=7)
        IPListe = []

    #chat start
    print("1 Neuen Eintrag erstellen")
    print("2 Programm beenden")
    print("3 Gib das ganze Netzwerk aus")
    auswahl = input("Geben Sie eine Auswahl ein: \n")

    #neue IP Registrieren
    if auswahl == "1":

        clientinput = input("Geben Sie Ihre Mac an: \n")

        if (MAC_Überprüfer(clientinput == True)):
            for items in IPListe:
                hostAdresse += 1
            clientenEintrag = [netzIp + str(hostAdresse), clientinput]
            IPListe.append(clientenEintrag)
            print(f"Ihre Neue IP ist: {netzIp + str(hostAdresse)}")
        else:
            print("Ungültige MAC-Adresse. Bitte versuchen Sie es erneut.")
        
    
    #Programm Beenden
    elif auswahl == "2":
        ende = True

    #Ganze Netzwerkliste ausgeben
    elif auswahl == "3":
        for item in IPListe:
            print(f"IP: {item[0]} MAC: {item[1]}")
    else:   
        print()
        print("Bitte geben Sie eine gültige Eingabe ein!")
    print()
print("Programmende!")
