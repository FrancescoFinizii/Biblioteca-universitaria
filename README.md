<div align="center">
  <img src="View/Amministratore/Resources/logo biblioteca.png">
</div>

# Biblioteca-universitaria
Il progetto proposto consiste nella realizzazione di un software per la gestione del Sistema Bibliotecario dell'Università Politecnica delle Marche. Il software in questione si occupa di due principali servizi:
+ Prestito librario.
+ Prenotazione posto aula studio.

Per ulteriori informazioni sul progetto è disponibile una documentazione dettagliata al seguente [link](Documentazione/Biblioteca_universitaria.pdf)

## Installazione
Per poter eseguire il software occore aver installato l'**interprete** python (3.10) ed impostare come predefinita la lingua italiana nel proprio sistema operativo. 

Su linux è possibile settare il locale utilizzando il seguente commando: 

- `sudo dpkg-reconfigure locales`
- selezionare it_IT.UTF-8 e confermare.


Inoltre è neccessario installare le seguenti librerie:
+ schedule (`pip install schedule`)
+ PyQt5 (`pip install PyQt5`)


> **Note**
> Nel file <a href="config.json">config.json</a> è possibile modificare la capienza delle aule adibite allo studio e il codice di sicurezza per gli amministratori (identificato con "secureCode").

> **Warning**
> Se si desidera registrarsi sulla piattaforma come amministratore occore inserire il codice di sicurezza **1234**.


## Accesso alla piattaforma
Per poter testare il sistema sono stati forniti di default un amministratore e uno studente. 

Puoi accedere come **amministratore** usando le seguenti credenziali:
- **Matricola:** `987654321`
- **Password:** `qwertyuiop`

Puoi accedere come **studente** usando le seguenti credenziali:
- **Matricola:** `123456789`
- **Password:** `qwertyuiop`
