# Nume produse

1. Extragem textul din html

2. Deduplicam liniile exacte

3.a Vizualizam cate cuvinte au liniile in general:
   - Vedem ca avem lungimea medie la 4.5 cuvinte
   - Si o deviatie standard lungimea de 19 cuvinte.
3.b Datorita faptului ca in general liniile vor contine in medie sub 5 cuvinte in peste 93% din cazuri vom aborda problema ca 
un task de clasificare

4. Vom lua toate liniile la o deviatie standard ca fiind posibile nume de produse si vom face inferenta cu T5 pentru adnotare
   - Liniile mai lungi vor fi considerate noise.

5. observam ca modelul care face 0 shot classification pe inferenta are recall destul de mare.
   - propunem sa antrenam un model de clasificare care are precission mare

6. Astfel vom avea 2 faze: 
  - prima care extrage posibile nume de produse folosind inferenta cu T5 (aceasta va da destule false positives)
  - a doua in care selectam manual cateva exemple pozitive si negative si antrenam un model cu contrastive learning pt a avea precizie mare

7. Pentru phase 1, din exemplele adnotate de T5, vedem ca multe sunt nume de produse generice, deci are recall mare. Aceasta faza e utila pentru ca ne scapa 
   de foarte multe exemple noise(din 17k exemple ramanem cu 2.5k posibile produse)

8. Pentru a creste precizia selectam cateva nume de obiecte care sunt produse si altele care nu sunt si antrenam un model ce foloseste contrastive learning.
   Acest model va face o filtrare mult mai granulara in exemplele de la phase 1

9. La evaluare verificam pe un dataset creat in acelasi mod.

Am obtinut urmatoarele scoruri:

F1 score:  0.6190476190476191
Precission:  0.7
Recall:  0.75
