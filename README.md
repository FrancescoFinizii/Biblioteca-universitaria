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

Su linux è possibile settare il locale utilizzando i seguenti commandi: 

- `sudo update-locale LANG=LANG=it_IT.UTF-8 LANGUAGE`

- `sudo update-locale LC_TIME=it_IT.UTF-8`

Inoltre è neccessario installare le seguenti librerie:
+ schedule
+ PyQt5


> **Note**
> Nel file [config.json](config.json) è possibile modificare la capienza delle aule adibite allo studio e il codice di sicurezza per gli amministratori (identificato con "secureCode").

> **Warning**
> Se si desidera registrarsi sulla piattaforma come amministratore occore inserire il codice di sicurezza **1234**.


## Accesso alla piattaforma
Per poter testare il sistema sono stati forniti di default un amministratore e uno studente. 

Puoi accedere come **amministratore** usando le seguenti credenziali:
- **Matricola:** `0987654321`
- **Password:** `qwertyuiop`

Puoi accedere come **studente** usando le seguenti credenziali:
- **Matricola:** `1234567890`
- **Password:** `qwertyuiop`
