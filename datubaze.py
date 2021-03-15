#Importē SQlitle
import sqlite3
import requests
import json

#izveido datu bāzi Dati.db
conn = sqlite3.connect('Dati.db')
#pieslēdz kursoru
c = conn.cursor()
#Sākumā izveidosim tabulu “Inventars”.
#c.execute('CREATE TABLE IF NOT EXISTS Inventars (ID INTEGER PRIMARY KEY, NOSAUKUMS TEXT, TIPS TEXT, APAKSTIPS TEXT, SKAITS INTEGER, KOMENTARI TEXT)')
#Ievietojam pirmos datus tabulā.
#c.execute("INSERT INTO Inventars (NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) VALUES ('Mērkolba','Trauks','Mērtrauks',2,'Trauks ar tiplumu 300ml, kas paredzēts šķidrumu mērīšanai')")
# Lai izdzēstu liekos id
#c.execute("DELETE FROM Inventars WHERE ID > 1")
#Lai piekļūtu datiem, mums ir jāveic pieprasījums uz vietu, kur inventars.json fails glabājas
#inventars_api_res = requests.get('https://pytonc.eu.pythonanywhere.com/api/v1/inventars')
#Saņemtos datus pārveidojam sev saprotamā json formātā.
#inventars = inventars_api_res.json()
#Izprintējam
#print(inventars)
#users_json = json.load(open('dati/users.json'))
#Lai ierakstītu saņemtos datus tabulā, ir jāizveido cikls, kurš izietu cauri visiem datiem un tos pa rindiņai ierakstītu tabulā.
#for inv in inventars:
  #  c.execute("INSERT INTO Inventars (ID, NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) values (?, ?, ?, ?, ?, ?)", [inv['id'], inv['nosaukums'], inv['tips'], inv['apakstips'], inv['skaits'], inv['komentari']])

#print(inventars)
# labo nepareizu ierakstītu
#c.execute("UPDATE Inventars SET APAKSTIPS = 'Trauki' WHERE ID = 1")
# datu izsaukšana no tabulas
#c.execute("SELECT * FROM Inventars")

#conn.commit()
#t = ('trauks')
#c.execute('SELECT * FROM Inventars WHERE TIPS=?', t)
#print(c.fetchall())
#users_json = json.load(open('dati/users.json'))
#kolonas = ['id', 'vards', 'uzvards', 'loma', 'parole', 'Komentāri']
#for data in users_json['users']:
  #dati = tuple( data[c] for c in kolonas)
  #c.execute("INSERT INTO  Users values (?,?,?,?,?,?)", dati)
#1.uzdevums
#c.execute("UPDATE Inventars SET APAKSTIPS =LOWER(APAKSTIPS),TIPS =LOWER(TIPS)")

#2.uzdevums
c.execute('CREATE TABLE IF NOT EXISTS Vielas (ID INTEGER PRIMARY KEY, NOSAUKUMS TEXT, APAKSTIPS TEXT, TIPS TEXT, SKAITS INTEGER, KOMENTARI TEXT, DAUDZUMS INTEGER, MERVIENIBAS TEXT)')
conn.commit()
vielas_api_res = requests.get('https://pytonc.eu.pythonanywhere.com/api/v1/vielas')

vielas = vielas_api_res.json()
for inv in vielas:
    c.execute("INSERT INTO Vielas (NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, DAUDZUMS, KOMENTARI, MERVIENIBAS) values (?, ?, ?, ?, ?,?,?)", [inv['nosaukums'], inv['tips'], inv['apakstips'],inv['skaits'],inv['daudzums'], inv['komentari'], inv['mervienibas']])

#saglabā izmaiņas Datubāzē
conn.commit()

c.execute("SELECT * FROM Vielas")
# datu parādīšana konsolē
print(c.fetchall())

#Atlasa visus traukus izmantojot parametru ‘t’

#jāaizver savienojums.
c.close()
conn.close()



