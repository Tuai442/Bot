# App

[Hoe schrijf ik in markdown tips en tricks.](https://www.markdownguide.org/basic-syntax/)

## Installatie
1. Ga naar de folder in cmd.
2. Activeer virtuele enviroment (.\env\Scripts\activate)
3. Installer alle dependencies (pip install -r requirements.txt)


## Werking
Alles wordt via de README gecommuniceerd er kunnen dingen aangevuld en toegevoegd worden.
Als er dingen zijn die je niet duidelijk vind of denkt die beter op een andere manier gedaan worden.
Doe je dit aan de hand van een reply te plaatsen.

> *Voorbeeld*
> > <span style="color:Green">*Tuur*.
> >
> > Ik Denk dat dit beter .... gedaan wordt.

Je kan [Hier](template_reply.md) een template vinden die ja kan kopiëren en plakken waar je wilt.
Het enige wat je moet aanpassen is de kleur van je naam.

__Beschikbare kleuren:__

- <span style="color:Green">*Groen*. Tuur
- <span style="color:Purple">*Paars*. Vrij
- <span style="color:yellow">*Geel*. Vrij

## Onderdelen


#### User Interface

- [Simulatie Pagina](#Simulatie Pagina)
- [Account Pagina](#Account Pagina)
- [Instellingen Pagina](#Instelling Pagina)
- [Home Pagina](#Home Pagina)


### Simulatie Pagina

De simulatie pagina gaat de gebruiker de mogelijk heid geven om een simulatie op een dataset te doen.

#### Werking

1. De Gebruiker Geef een dataset in waarmee hij wilt werken *(Het is misschien een goed idee zijn
om een paar data setten op de website zelf te voorzien en dat de gebruiker daar uit kan kiezen.)*
2. De Gebruiker Kiest wat hij precies wilt testen een strategie of/en een pattern.
3. Eens dit gebreurt is word alles van de front-end naar de back-end gestuurd, de back-end maakt een
simulatie en stuurt die terug naar de front-end.
4. De gebruiker kan nu een simulatie uitvoeren hier bij kan hij de simulatie versnellen, pauzeren en vertragen.

> <span style="color:Green">*Tuur*.
>
> We kunnen belangerijke datasetten opslaan in een gezamelijke [map](Data).

