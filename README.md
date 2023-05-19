# Nume produse

1. Extragem textul din html
2. Deduplicam liniile exacte

3. Vizualizam cate cuvinte au liniile in general:
   - Vedem ca avem lungimea medie la 5 cuvinte
   - Si o deviatie standard lungimea de 19 cuvinte.

4. Vom lua toate liniile la o deviatie standard ca fiind posibile nume de produse si le vom face inferenta cu T5 pentru adnotare
   - Liniile mai lungi vor fi considerate noise.

5. Avem cateva cuvinte pe linie si vrem sa vedem daca reprezinta un produs -> model de clasificare 

6. Trimitem liniile la adnotare cu T5

7. Din exemplele selectate de T5, vedem ca multe sunt nume de produse generice, deci are recall mare.

8. Pentru a creste precizia selectam cateva nume de obiecte care sunt produse si altele care nu sunt si antrenam un model ce foloseste contrastive learning

9. La evaluare verificam pe un dataset creat in acelasi mod.

