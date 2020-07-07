# UTTT
Dette er Jonathan Melcher's forsøg på at laven kode hvor i man kan battle i Ultimate tic-tac-toe.

Reglerne i dette er; 

Each small 3 × 3 tic-tac-toe board is referred to as a local board, and the larger 3 × 3 board is referred to as the global board.

The game starts with X playing wherever they want in any of the 81 empty spots. This move "sends" their opponent to its relative location. 
For example, if X played in the top right square of their local board, then O needs to play next in the local board at the top right of the global board. 
O can then play in any one of the nine available spots in that local board, each move sending X to a different local board.
If a move is played so that it is to win a local board by the rules of normal tic-tac-toe, then the entire local board is marked as a victory for the player in the global board.
Once a local board is won by a player or it is filled completely, no more moves may be played in that board. If a player is sent to such a board, then that player may play in any other board.
Game play ends when either a player wins the global board or there are no legal moves remaining, in which case the game is a draw. - Fra Wikipedia


Det som denne konkurrence så går ud på er at lave bots som kan spille mod hinanden. Der er følgende krav til en bot

Den skal kunne spille som både spiller1 og spiller2 altså enten starte spillet eller være nummer to. 

Den skal skrives som en funktion der tager 3 argumenter hvordan boardet ser ud lige nu, arrayet 'board' i koden, hvilket local board spilleren er tvunget til at tage et træk på, variablen 'T' og hvilke local boards der er vundet, arrayet 'won'.

Som output skal den returnerer to int som skal indeksere hvor på boardet der skal sættes et 1 eller 2 tal alt efter om man er spiller 1 eller 2, dette svare til at kryds eller bolle.
Det første index skal være hvilket local board og det andet hvilken position i det local board som der skal sættes et 1 eller 2 tal på.

Den måde 'board' fungere er en 2d array med 9 arrays der er 9 lange i. Altså kan alle positioner findes ved et index i fra 0 til 8 som giver hvilket local board og så et index j fra 0 til 8
som giver hvilket sted på dette local board. Både global og local board er indekseret på følgende måde

                                                       0 | 1 | 2
                                                       ---------
                                                       3 | 4 | 5
                                                       ---------
                                                       6 | 7 | 8

Altså er board[4][4] svare til det midterste local boards midter felt. Et vundet local board kan se således ud [0,1,2,1,2,0,2,1,1], her har 2 vundet på diagonalen.

Won er et array som er 9 langt, den holder styr på om de enkelte local boards er afgjorte eller ej. 0 betyder at der stadig kan tages træk på boardet, 1 er at spiller1 har vundet det
2 er at spiller to har vundet det og 3 er uafgjort. Won tjekkes efter hvert træk for at se om der nogen der har vundet global boardet og der med vundet spillet.

T er et int og fortæller spillerne hvor de skal trække næste gang fra 0 til 8 svare til de 9 local boards mens 9 betyder at der er frit træk på alle boards. Det førte træk er altid helt
frit og T er derfor 9 som start værdi men opdateres efter hvert træk.

Det er tilladt at bruge alle mulige former for fikse og feje trick til at lave sin funktion. Der er to eksempler i filen player_generation.py disse er simple men kan hjælpe med at forstå hvad der er af input output for funktionerne.

Selve tuneringsformattet er ikke afgjort endnu men vil blive lagt op her også når vi har besluttet os, det samme med datoen.
Hvis man har spørgsmål til koden så skriv til mig på facebook.
