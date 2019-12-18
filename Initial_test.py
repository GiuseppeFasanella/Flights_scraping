## 1. Capire il sito .
## Ho cercato un po' link di voli

## Venezia --> Parigi
#https://www.google.com/flights?hl=it#flt=/m/07_pf./m/05qtj.2019-12-18;c:EUR;e:1;sd:1;t:f;tt:o
## Ginevra --> Parigi
#https://www.google.com/flights?hl=it#flt=/m/03902./m/05qtj.2019-12-18;c:EUR;e:1;sd:1;t:f;tt:o
## Ginevra --> Venezia
#https://www.google.com/flights?hl=it#flt=/m/03902./m/07_pf.2019-12-18;c:EUR;e:1;sd:1;t:f;tt:o

## Da cui mi sembra capire che
## GVA = 03902.
## Venezia = 07_pf.
## Parigi = 05qtj.

## Verifico questa teoria: questo link dovrebbe cercare voli da Parigi a Ginevra
#https://www.google.com/flights?hl=it#flt=/m/05qtj./m/03902.2019-12-18;c:EUR;e:1;sd:1;t:f;tt:o

## Ok. Teoria verificata

## 2. Procediamo con trovare gli aeroporti che io uso molto spesso
## Bari = 0c66m.
## Napoli = 0fhsz.
## Milano = 0947l.
## GVA = 03902.
## Venezia = 07_pf.
## Parigi = 05qtj.

## 3. Ok, direi che abbiamo capito la struttura del sito.
start='0c66m.'
destination='0947l.'
date='2020-01-01'
currency='CHF'
url='https://www.google.com/flights?hl=it#flt=/m/'+str(start)+'/m/'+str(destination)+date+';c:'+currency+';e:1;sd:1;t:f;tt:o'
print(url)
