��    W      �     �      �     �  �  �  b   a  M   �  p     �   �  q   %  �   �  �   g  �   9  #   �     �          1  )   G  	   q  3   {     �  �   �      Z  ,   {  $   �     �      �          #  #   B  !   f     �     �  %   �     �     �          +     B     Q     e     |     �  �   �  &   v     �     �     �  �   �  d   �     0  $   G  u   l  C   �  =   &     d  &   }  +   �     �  (   �  )   
     4     M    g  (   o  �   �  }   T  .   �  F     "   H  -   k     �  
   �     �  2   �  $   
  ,   /  '   \  '   �     �     �  +   �     �                 $      -      4      <   x  C       �!  ,  �!  ^   
&  V   i&  t   �&  �   5'  �   �'  �   s(  �   N)  �   A*  $   �*     +     9+     T+  =   q+     �+  @   �+  $   �+  �   #,  3   �,  @   �,  9   4-      n-  *   �-  &   �-  &   �-  2   .  -   ;.      i.  &   �.  %   �.  )   �.      /  #   "/     F/     b/     u/     �/      �/  "   �/  �   �/  ,   �0  #   �0     1  "   1  �   >1     2     �2  #   �2  {   �2  D   N3  =   �3     �3      �3  +   4     74  +   N4  6   z4  &   �4     �4  �  �4  '   �9  �   �9  �   j:  1   �:  I   ;     h;  4   �;  %   �;     �;     �;  7   
<  -   B<  =   p<  )   �<  1   �<     
=     =  /   %=     U=     j=     ~=  	   �=  	   �=     �=     �=     ,          $             V       +   3   8                    1   B   &   M       H       6   =      (      U   P               E   0       )          L   G                     >              #       4      '       R   "         D            T              C   A      7          I      W   Q   5   K       /                 J       @   .   ?   S   -   	       !   ;      :           2   F               %   N               
   <              O   *   9                          
Display a tree of processes.

        killall -l, --list
       killall -V, --version

  -e,--exact          require exact match for very long names
  -I,--ignore-case    case insensitive process name match
  -g,--process-group  kill process group instead of process
  -y,--younger-than   kill processes younger than TIME
  -o,--older-than     kill processes older than TIME
  -i,--interactive    ask for confirmation before killing
  -l,--list           list all known signal names
  -q,--quiet          don't print complaints
  -r,--regexp         interpret NAME as an extended regular expression
  -s,--signal SIGNAL  send this signal instead of SIGTERM
  -u,--user USER      kill only process(es) running as USER
  -v,--verbose        report if the signal was successfully sent
  -V,--version        display version information
  -w,--wait           wait for processes to die
  -n,--ns PID         match processes that belong to the same namespaces
                      as PID
   -4,--ipv4             search IPv4 sockets only
  -6,--ipv6             search IPv6 sockets only
   -C, --color=TYPE    color process by attribute
                      (age)
   -Z,--context REGEXP kill only process(es) having context
                      (must precede other arguments)
   -a, --arguments     show command line arguments
  -A, --ascii         use ASCII line drawing characters
  -c, --compact-not   don't compact identical subtrees
   -g, --show-pgids    show process group ids; implies -c
  -G, --vt100         use VT100 line drawing characters
   -h, --highlight-all highlight current process and its ancestors
  -H PID, --highlight-pid=PID
                      highlight this process and its ancestors
  -l, --long          don't truncate long lines
   -s, --show-parents  show parents of the selected process
  -S, --ns-changes    show namespace transitions
  -t, --thread-names  show full thread names
  -T, --hide-threads  hide threads, show only processes
   -u, --uid-changes   show uid transitions
  -U, --unicode       use UTF-8 (Unicode) line drawing characters
  -V, --version       display version information
 %*s USER        PID ACCESS COMMAND
 %s is empty (not mounted ?)
 %s: Invalid option %s
 %s: no process found
 %s: unknown signal; %s -l lists signals.
 (unknown) /proc is not mounted, cannot stat /proc/self/stat.
 Bad regular expression: %s
 CPU Times
  This Process    (user system guest blkio): %6.2f %6.2f %6.2f %6.2f
  Child processes (user system guest):       %6.2f %6.2f %6.2f
 Can't get terminal capabilities
 Cannot allocate memory for matched proc: %s
 Cannot find socket's device number.
 Cannot find user %s
 Cannot open /proc directory: %s
 Cannot open /proc/net/unix: %s
 Cannot open a network socket.
 Cannot open protocol file "%s": %s
 Cannot resolve local port %s: %s
 Cannot stat %s: %s
 Cannot stat file %s: %s
 Copyright (C) 2007 Trent Waddington

 Could not kill process %d: %s
 Error attaching to pid %i
 Invalid namespace PID Invalid namespace name Invalid option Invalid time format Kill %s(%s%d) ? (y/N)  Kill process %d ? (y/N)  Killed %s(%s%d) with signal %d
 Memory
  Vsize:       %-10s
  RSS:         %-10s 		 RSS Limit: %s
  Code Start:  %#-10lx		 Code Stop:  %#-10lx
  Stack Start: %#-10lx
  Stack Pointer (ESP): %#10lx	 Inst Pointer (EIP): %#10lx
 Namespace option requires an argument. No process specification given No processes found.
 No such user name: %s
 PSmisc comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under
the terms of the GNU General Public License.
For more information about these matters, see the files named COPYING.
 Page Faults
  This Process    (minor major): %8lu  %8lu
  Child Processes (minor major): %8lu  %8lu
 Press return to close
 Process with pid %d does not exist.
 Process, Group and Session IDs
  Process ID: %d		  Parent ID: %d
    Group ID: %d		 Session ID: %d
  T Group ID: %d

 Process: %-14s		State: %c (%s)
  CPU#:  %-3d		TTY: %s	Threads: %ld
 Scheduling
  Policy: %s
  Nice:   %ld 		 RT Priority: %ld %s
 Signal %s(%s%d) ? (y/N)  Specified filename %s does not exist.
 Specified filename %s is not a mountpoint.
 TERM is not set
 Unable to allocate memory for proc_info
 Unable to open stat file for pid %d (%s)
 Unable to scan stat file Unknown local port AF %d
 Usage: fuser [-fIMuvw] [-a|-s] [-4|-6] [-c|-m|-n SPACE]
             [-k [-i] [-SIGNAL]] NAME...
       fuser -l
       fuser -V
Show which processes use the named files, sockets, or filesystems.

  -a,--all              display unused files too
  -i,--interactive      ask before killing (ignored without -k)
  -I,--inode            use always inodes to compare files
  -k,--kill             kill processes accessing the named file
  -l,--list-signals     list available signal names
  -m,--mount            show all processes using the named filesystems or
                        block device
  -M,--ismountpoint     fulfill request only if NAME is a mount point
  -n,--namespace SPACE  search in this name space (file, udp, or tcp)
  -s,--silent           silent operation
  -SIGNAL               send this signal instead of SIGKILL
  -u,--user             display user IDs
  -v,--verbose          verbose output
  -w,--writeonly        kill only processes with write access
  -V,--version          display version information
 Usage: killall [OPTION]... [--] NAME...
 Usage: prtstat [options] PID ...
       prtstat -V
Print information about a process
    -r,--raw       Raw display of information
    -V,--version   Display version information and exit
 Usage: pstree [-acglpsStTuZ] [ -h | -H PID ] [ -n | -N type ]
              [ -A | -G | -U ] [ PID | USER ]
   or: pstree -V
 You can only use files with mountpoint options You cannot search for only IPv4 and only IPv6 sockets at the same time You must provide at least one PID. all option cannot be used with silent option. asprintf in print_stat failed.
 disk sleep fuser (PSmisc) %s
 killall: %s lacks process entries (not mounted ?)
 killall: Bad regular expression: %s
 killall: Cannot get UID from process status
 killall: Maximum number of names is %d
 killall: skipping partial match %s(%d)
 paging peekfd (PSmisc) %s
 procfs file for %s namespace not available
 prtstat (PSmisc) %s
 pstree (PSmisc) %s
 running sleeping traced unknown zombie Project-Id-Version: psmisc 23.3
Report-Msgid-Bugs-To: csmall@dropbear.xyz
PO-Revision-Date: 2020-03-09 15:55+0100
Last-Translator: Francesco Groccia <fg@snopyta.org>
Language-Team: Italian <tp@lists.linux.it>
Language: it
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Bugs: Report translation errors to the Language-Team address.
 
Mostra l'albero dei processi.

      killall -l, --list
     killall -V, --version

  -e,--exact          richiede una corrispondenza esatta per i nomi molto lunghi
  -I,--ignore-case    ignora maiuscole/minuscole nei nomi
  -g,--process-group  termina il gruppo di processi invece del processo
  -y,--younger-than   termina i processi più recenti di ORARIO
  -o,--older-than     termina i processi più vecchi di ORARIO
  -i,--interactive    chiede conferma prima di terminare
  -l,--list           elenca i nomi di segnale conosciuti
  -q,--quiet          non visualizzare commenti
  -r,--regexp         interpreta NOME come un'espressione regolare estesa
  -s,--signal SEGNALE invia il segnale indicato invece di SIGTERM
  -u,--user UTENTE    termina solo i processi eseguiti dall'UTENTE
  -v,--verbose        riporta se il segnale è stato inviato con successo
  -V,--version        mostra le informazioni sulla versione
  -w,--wait           aspetta la terminazione del processo
  -n,--ns PID         agisce su processi che appartengono allo stesso spazio dei nomi
                      di PID
   -4,--ipv4             cerca solo socket IPv4
  -6,--ipv6             cerca solo socket IPv6
   -C, --color=TIPO    processo del colore dall'attributo
                      (età)
   -Z,--context REGEXP termina solo i processi aventi context
                      (deve precedere altri argomenti)
   -a, --arguments     mostra gli argomenti della riga di comando
  -A, --ascii         usa i caratteri grafici ASCII
  -c, --compact-not   non comprimere i sotto alberi identici
   -g, --show-pgids    mostra gli identificativi del gruppo di processo; implica -c
  -G, --vt100         usa i caratteri grafici di VT100
   -h, --highlight-all evidenzia il processo corrente e i suoi antenati
  -H PID, --highlight-pid=PID
                      evidenzia questo processo e i suoi antenati
  -l, --long          non troncare le linee lunghe
   -s, --show-parents  mostra i genitori del processo selezionato
  -S, --ns-changes    mostra le transizioni del contesto
  -t, --thread-names  mostra i nomi completi del thread
  -T, --hide-threads  nascondi i thread, mostra solo i processi
   -u, --uid-changes   mostra l'uid delle transitions
  -U, --unicode       usa i caratteri grafici di UTF-8 (Unicode)
  -V, --version       visualizza le informazioni sulla versione
 %*s UTENTE      PID ACCESSO COMANDO
 %s è vuoto (non montato?)
 %s: Opzione %s non valida
 %s: nessun processo trovato
 %s: segnale sconosciuto; usare %s -l per elencare i segnali.
 (sconosciuto) /proc non è montato, impossibile fare stat di /proc/self/stat.
 Espressione regolare non valida: %s
 Utilizzo temporale CPU
  Questo processo (user system guest blkio): %6.2f %6.2f %6.2f %6.2f
  Processi figli  (user system guest):       %6.2f %6.2f %6.2f
 Impossibile determinare le capacità del terminale
 Impossibile allocare memoria per il processo corrispondente: %s
 Impossibile trovare il numero di dispositivo del socket.
 Impossibile trovare l'utente %s
 Impossibile aprire la directory /proc: %s
 Impossibile aprire /proc/net/unix: %s
 Impossibile aprire un socket di rete.
 Impossibile aprire il file di protocollo "%s": %s
 Impossibile risolvere la porta locale %s: %s
 Impossibile fare stat di %s: %s
 Impossibile fare stat del file %s: %s
 Copyright (C) 2007 Trent Waddington

 Impossibile terminare il processo %d: %s
 Errore nel collegarsi al pid %i
 PID del nome di contesto non valido Nome di contesto non valido Opzione non valida Formato orario non valido Terminare %s(%s%d)? (s/N)  Terminare il processo %d? (s/N)  Terminato %s(%s%d) con segnale %d
 Memoria
  Vsize:       %-10s
  RSS:         %-10s 		 RSS Limit: %s
  Code Start:  %#-10lx		 Code Stop:  %#-10lx
  Stack Start: %#-10lx
  Stack Pointer (ESP): %#10lx	 Inst Pointer (EIP): %#10lx
 L'opzione di contesto richiede un argomento. Nessun tipo di processo specificato Nessun processo trovato.
 Questo nome utente non esiste: %s
 PSmisc è distribuito senza ALCUNA GARANZIA.
Questo è software libero, ed è possibile redistribuirlo secondo i termini
della GNU General Public License.
Si consulti il file COPYING per ulteriori informazioni.
 Errori di pagina (page faults)
  Questo processo (minore maggiore): %8lu  %8lu
  Processi figli  (minore maggiore): %8lu  %8lu
 Premere Invio per chiudere
 Il processo con pid %d non esiste.
 ID di processo, gruppo e sessione
  ID Processo: %d		  ID Parent: %d
    ID Gruppo: %d		ID Sessione: %d
  ID Gruppo T: %d

 Processo: %-14s		Stato: %c (%s)
  CPU#:  %-3d		TTY: %s	Threads: %ld
 Scheduling
  Policy: %s
  Nice:   %ld 		 RT Priority: %ld %s
 Segnale %s(%s%d)? (s/N)  Il file indicato %s non esiste.
 Il file indicato %s non è un mount point.
 TERM non è impostato
 Impossibile allocare memoria per proc_info
 Impossibile aprire il file di stat per il pid %d (%s)
 Impossibile analizzare il file di stat Porta locale AF %d sconosciuta
 Uso: fuser [-fIMuvw] [-a|-s] [-4|-6] [-c|-m|-n CONTESTO]
             [-k [-i] [-SIGNALE]] NOME...
       fuser -l
       fuser -V
Mostra quali processi stanno usando un certo file, socket o filesystem.

  -a,--all              mostra anche i file inutilizzati
  -i,--interactive      conferma prima di terminare (ignorato senza -k)
  -I,--inode            usa sempre gli inode per confrontare i file
  -k,--kill             termina i processi che accedono al file specificato
  -l,--list-signals     elenca i nomi dei segnali disponibili
  -m,--mount            mostra tutti i processi che usano i filesystem o i
                        dispositivi a blocchi specificati
  -M,--ismountpoint     soddisfa la richiesta solo se NOME è un mount point
  -n,--namespace SPACE  cerca nel CONTESTO specificato (file, udp, o tcp)
  -s,--silent           opera silenziosamente
  -SIGNAL               invia il segnale indicato invece di SIGKILL
  -u,--user             mostra gli ID utente
  -v,--verbose          output prolisso
  -w,--writeonly        termina solo i processi con accesso alla scrittura
  -V,--version          mostra le informazioni sulla versione
 Uso: killall [OPZIONE]... [--] NOME...
 Uso: prtstat [opzioni] PID ...
     prtstat -V
Stampa informazioni su un processo
    -r,--raw       Mostra informazioni grezze
    -V,--version   Mostra le informazioni sulla versione ed esce
 Uso: pstree [-acglpsStTuZ] [ -h | -H PID ] [ -n | -N tipo ]
              [ -A | -G | -U ] [ PID | UTENTE ]
   oppure: pstree -V
 Con l'opzione -m si possono specificare solo file Impossibile cercare solo socket IPv4 e solo socket IPv6 allo stesso tempo Occorre indicare almeno un PID. L'opzione -a non può essere usata con l'opzione -s. asprintf in print_stat non riuscito.
 in attesa del disco fuser (PSmisc) %s
 killall: %s non ha una voce di processo (non montato?)
 killall: Espressione regolare non valida: %s
 killall: Impossibile ottenere l'UID dallo stato del processo
 killall: Il massimo numero di nomi è %d
 killall: ignorata corrispondenza parziale %s(%d)
 paging peekfd (PSmisc) %s
 file procfs per il contesto %s non disponibile
 prtstat (PSmisc) %s
 pstree (PSmisc) %s
 in esecuzione in attesa tracciato sconosciuto zombie 