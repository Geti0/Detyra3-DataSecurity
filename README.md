# Programimi i punes se SBox-eve dhe fitimi i 16-SubKey per secilin round te DES Algoritmit

Për të programuar punën e S-Box-eve dhe fitimin e 16-SubKey për secilin round të DES algoritmit, duhet të:

- Për të filluar, duhet të kemi një funksion që realizon funksionin e S-Box-it të DES. S-Box-at janë 8 tabela prej 4 x 16, dhe secili prej tyre pranon 6 bit si input dhe prodhon 4 bit si output. Këto tabela janë të shkruara në specifikatën e DES. Në këtë funksion, ne duhet të marrim 6 bitët e hyrjes dhe të shikojmë rreshtin dhe kolonën përkatëse në tabelën e S-Box-it për të kthyer 4 bitët e daljes.

- Pastaj, duhet të krijojmë funksionin e fjalëkalimit të DES. Kjo është pjesa e algoritmit që realizohet në secilin round. Funksioni i fjalëkalimit përdor funksionin e S-Box-it dhe një subkey të caktuar për të prodhuar output-in përfundimtar. Ky subkey ndryshon në secilin round, dhe në total ka 16 subkey të ndryshëm.

Pasi kemi funksionin e fjalëkalimit të DES, ne mund të përdorim atë për të realizuar algoritmin e DES. Kjo përfshin përdorimin e subkeys për çdo round dhe realizimin e funksionit të fjalëkalimit në secilin round.


Grupi 21

- [Gentrit Ademi](https://github.com/GentritAdemi)
- [Getuar Kelmendi](https://github.com/geti0)
- [Ylljete Kicaj](https://github.com/ylljetakicaj)
