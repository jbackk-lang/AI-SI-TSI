# Metodologia uczenia TSI — plan badawczy (11 listopada 2026)

## Cel
Zwiększać zasób **sprawdzonej wiedzy** i jakość przewidywań, a nie tylko liczbę pytań lub nagrodę symulatora. „Ciekawość” oznacza mierzalną politykę eksploracji, nie subiektywne przeżycie.

## Trzy niezależne mechanizmy
1. **Pamięć:** fakty wraz ze źródłem, czasem, statusem weryfikacji, niepewnością i korektami. Zapis faktu nie zmienia wag.
2. **Polityka eksploracji:** uczy się szacować wartość pytania z uwzględnieniem luki, sprzeczności, poprawy predykcji i kosztu. Porównanie z baseline'ami i testem odłożonym.
3. **H512:** odrębny rdzeń. Dostrajanie dopiero po walidacji, z checkpointem, kontrolą regresji i możliwością cofnięcia.

## Pętla uczenia
Obserwacja → wykrycie luki → hipoteza i niepewność → pytanie → odpowiedź i źródło → niezależna weryfikacja → zapis pochodzenia → aktualizacja polityki → kontrola retencji.

## Etapy
- **026:** selekcja pytań z historią faktów, test bez odczytu faktów i konfliktów (syntetyczne).
- **027:** trwała pamięć faktów między procesami, pochodzenie, korekty, odporność na błędy.
- **028:** trening na różnych generatorach, wielokrotne nasiona i odłożone środowiska.
- **029:** pytania generowane przez model bez gotowego katalogu; walidacja sensowności.
- **030:** ewentualna kontrolowana integracja z H512, po testach jakości.

## Metryki
Nowe poprawnie zweryfikowane fakty na jednostkę kosztu, odsetek fałszywych zapisów, kalibracja przewidywań, retencja po restarcie, wyniki na nowych grafach, trwałość i elastyczność zainteresowań, odporność na sprzeczne źródła. Raportować wyniki negatywne, ablation, przedziały ufności i porównania z losową i heurystyką.

## Stan dowodów
Etapy 020–025: środowiska syntetyczne. Etap 026: odczyt historii odpowiedzi zwiększył różnorodność relacji i poprawnych konsensusów, ale nie zwiększył średniej nagrody. To **reguła korzystania z faktów, a nie nowy trening wag**. Nie potwierdzono autonomicznej ciekawości ani uczenia H512.
