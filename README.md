# visa_jobb.py
### Hur använda?
  - Ett enkelt skript skrivet i Python som visar lediga jobb i hela länet.
  - Använder Arbetsförmedlingens öppna API http://api.arbetsformedlingen.se.

### Hur använda?
```sh
$ mkvirtualenv --python=/usr/bin/python3 visajobb
$ git clone git@github.com:dunderrrrrr/visa_jobb.py.git
$ pip install -r requirements.txt
```
```sh
$ python visa_jobb.py --help
Usage: visa_jobb.py [options]
Options:
  -h, --help            show this help message and exit
  -l LAN, --lan=LAN     Visa antal lediga jobb per län. Använd "-l all" för
                        att visa alla län.
  -k KOM, --kommun=KOM  Visa antal lediga jobb per kommun. Använd "-k all" för
                        att visa alla län.
  -t, --total           Visa totalt antal platsannonser samt lediga jobb.
```
### Exempel:
#### Visa kommun
```sh
$ python visa_jobb.py --kommun Stockholm
Stockholm (id: 180)
Antal platsannonser: 8658
Antal ledia jobb: 17443
====================
2018-02-12T00:00:00+01:00, Vanlig anställning
Läkarsekreterare/Vårdadmin/Medicinsk sekreterare
Karolinska Universitetssjukhuset
URL: https://www.arbetsformedlingen.se/Tjanster/Arbetssokande/Platsbanken/annonser/7515021
====================
2018-02-12T00:00:00+01:00, Vanlig anställning
Forskare, samhällsvetenskap
Stockholms universitet
URL: https://www.arbetsformedlingen.se/Tjanster/Arbetssokande/Platsbanken/annonser/7515346
====================
2018-02-12T00:00:00+01:00, Vanlig anställning
Undersköterska, hemtjänst och äldreboende
1:a Hemtjänstkompaniet
URL: https://www.arbetsformedlingen.se/Tjanster/Arbetssokande/Platsbanken/annonser/7538410
====================
[...]
```
#### Visa län
```sh
$ python visa_jobb.py --lan "Södermanlands län"
Stockholm (id: 180)
Antal platsannonser: 8623
Antal ledia jobb: 17388
```
#### Visa total
```sh
$ python visa_jobb.py -t
Totalt antal ledia jobb: 145957
Totalt antal platsannonser: 48155
```
#### Visa alla kommuner
```sh
$ python visa_jobb.py -k all
Karlshamn
Karlskrona
Olofström
Ronneby
[...]
```
#### Visa alla län
```sh
$ python visa_jobb.py -l all
Blekinge län
Dalarnas län
Gotlands län
Gävleborgs län
[...]
```
