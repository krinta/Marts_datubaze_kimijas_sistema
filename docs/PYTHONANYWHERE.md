# Projekts Python Anywhere vidē

## Priekšrocības

- par brīvu pieejami viens publisks projekts
- publiski pieejama adrese:
  - lai dalītos ar savu projektu
  - lai reāli lietotu projektu
- pieejama papildus funkcionalitāte, kā piemēram MySQL, memcache
- MySQL datubāzes izmēra limits ir daudz lielāks nekā citos par brīvu pieejamos resursos (līdz 512 MB kopā ar kodu un attēliem)

## Trūkumi

- nepieciešams izveidot kontu
- nepieciešama speciāla konfigurācija, lai projekts vispār strādātu
- savienojums ar GitHub ir manuāls, jāveic `git clone ...` `git pull` izmantojot komandrindu uz Pythonanywhere servera.

## Darba Process

1. Izveido [EU PythonAnywhere](https://eu.pythonanywhere.com//)  kontu
1. Apstiprina konta izveidi no reģistrētā e-pasta
1. Izveido jaunu web aplikāciju
1. Atver jaunu Bash console
1. Atvērtajā Bash konsolē ar git klonē savu projektu
1. Rediģē `*_wsgi.py` datni, lai ta atspoguļotu projekta atrašanās vietu un darbināšanas komandu

## Kā pārbaudīt darbību

1. Tabā "Web" nospiež "Reload ProjektaNosaukums"
1. Kad beidz griezties progresa indikators, atveram linku uz projektu lapas augšpusē
1. Ja viss strādā - urā!
1. Ja rāda kļūdu, tabā "Web", nedaudz uz leju sameklējam sadaļu "Logs" un skatamies, kas varētu būt par kļūdu.
