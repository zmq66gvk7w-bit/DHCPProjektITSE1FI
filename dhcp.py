from datetime import date, timedelta
heute = date.today()

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
    print("1. Neuen eintrag Erstellen")
    print("2 Programm beenden")
    print("3 Gib das ganze Netzwerk aus")
    auswahl = input("Geben sie eine auswahl ein: ")

    #neue IP Registrieren
    if auswahl == "1":
        #TODO INPUT CHECK FÜR MAC ADRESSE1
        clientinput = input("gib MAC: ")
        for items in IPListe:
            hostAdresse += 1
        clientenEintrag = [netzIp + str(hostAdresse), clientinput]
        IPListe.append(clientenEintrag)
        print(f"Ihre Neue IP ist: {netzIp + str(hostAdresse)}")

    #Programm Beenden
    if auswahl == "2":
        ende = True

    #Ganze Netzwerkliste ausgeben
    if auswahl == "3":
        for item in IPListe:
            print(f"IP: {item[0]} MAC: {item[1]}")
    else:   
        print()
        print("Bitte geben sie eine gültige eingabe ein!")
    print()
print("Programm Ende!")
