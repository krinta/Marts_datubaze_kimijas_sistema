#Importē SQlitle
import sqlite3
import requests
import json

#izveido datu bāzi Dati.db
conn = sqlite3.connect('Dati.db')
#pieslēdz kursoru
c = conn.cursor()
#Sākumā izveidosim tabulu “Inventars”.
c.execute('CREATE TABLE IF NOT EXISTS Inventars (ID INTEGER PRIMARY KEY, NOSAUKUMS TEXT, TIPS TEXT, APAKSTIPS TEXT, SKAITS INTEGER, KOMENTARI TEXT)')
#Ievietojam pirmos datus tabulā.
c.execute("INSERT INTO Inventars (NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) VALUES ('Mērkolba','Trauks','Mērtrauks',2,'Trauks ar tiplumu 300ml, kas paredzēts šķidrumu mērīšanai')")
# Lai izdzēstu liekos id
c.execute("DELETE FROM Inventars WHERE ID > 1")
#Lai piekļūtu datiem, mums ir jāveic pieprasījums uz vietu, kur inventars.json fails glabājas
inventars_api_res = requests.get('https://pytonc.eu.pythonanywhere.com/api/v1/inventars')
#Saņemtos datus pārveidojam sev saprotamā json formātā.
inventars = inventars_api_res.json()
#Izprintējam
#print(inventars)
#Lai ierakstītu saņemtos datus tabulā, ir jāizveido cikls, kurš izietu cauri visiem datiem un tos pa rindiņai ierakstītu tabulā.
for inv in inventars:
    c.execute("INSERT INTO Inventars (ID, NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) values (?, ?, ?, ?, ?, ?)", [inv['id'], inv['nosaukums'], inv['tips'], inv['apakstips'], inv['skaits'], inv['komentari']])

print(inventars)
# labo nepareizu ierakstītu
c.execute("UPDATE Inventars SET APAKSTIPS = 'Trauki' WHERE ID = 1")




#saglabā izmaiņas Datubāzē
conn.commit()
# datu izsaukšana no tabulas
c.execute("SELECT * FROM Inventars")
# datu parādīšana konsolē
print(c.fetchall())

#jāaizver savienojums.
c.close()
conn.close()



