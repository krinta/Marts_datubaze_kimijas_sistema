# Projekts Heroku vidē

## Priekšrocības

- par brīvu pieejami vairāki publiski projekti, limitēti ar darbības ilgumu (automātiski iemieg, kad netiek lietoti)
- publiski pieejama adrese:
  - lai dalītos ar savu projektu
  - lai reāli lietotu projektu
- viegli savienojams ar GitHub, ar automātisku servera atjaunošanu, kad GitHub ir iesūtītas jaunas izmaiņas
- pieejama papildus funkcionalitāte, kā piemēram datubāzes

## Trūkumi

- nepieciešams izveidot kontu
- nepieciešama speciāla konfigurācija, lai projekts vispār strādātu
- par brīvu pieejamās datubāzes ir ļoti limitētas izmērā

## Darba Process

1. Izveido [Heroku](https://heroku.com/)  kontu
1. Apstiprina konta izveidi no reģistrētā e-pasta
1. [Heroku dashboardā](https://dashboard.heroku.com/apps) izvēlas "Create new app"
1. Izveido nosaukumu - šis nosaukums būs webadreses sastāvdaļa, izvēlieties kaut ko atbilstošu projektam, piemēram "mans-klus"
1. Izvēlas reģionu - Europe
1. Nospiež "Create App"

## App savienošana ar GitHub

1. Jaunizveidotās aplikācijas tabā "Deploy" atrod sadaļu "Deployment method" un izvēlas GitHub (Connect to GitHub).
1. Pievieno savu GitHub repozitoriju, pārbauda, ka pareizais repozitorijs rādās sadaļā "App connected to GitHub"
1. Sadaļā "Automatic deploys" pārbauda, ka ir izvēlēts zars "master" un nospiez "Enable Automatic deploys" - tagad pēc katrs commit vai merge uz *master* zaru tiks automātiski palaists uz Heroku servera (paiet apmēram 30-60 sekundes)

## Kā pārbaudīt darbību

1. Tabā "Deploy" sadaļā "Manual deploy" nospiezam "Deploy" un pagaidām
1. Ja parādās ziņa "Your app was successfully deployed.", nospiežam pogu "Open App" labajā augšējā stūrī.
1. Ja viss strādā - urā!
1. Ja rāda kļūdu, Heroku lapā nospiežam labajā augšējā stūrī uz pogas "More" un izvēlamies "View Logs".
