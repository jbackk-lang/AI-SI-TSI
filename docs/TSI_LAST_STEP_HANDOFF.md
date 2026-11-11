# TSI — instrukcja wznowienia (nadpisywana)

**Data:** 2026-11-11. **Ostatni ukończony etap:** TSI_CURIOSITY_023. **Następny:** 024.

## Etap 023 — trening opóźnionej wartości informacji
Lokalny artefakt rozmowy: `TSI_CURIOSITY_023.zip` (kod `experiment.py`, `value_predictor_023.pt`, `result.json`, `run.log`, `README.md`). Archiwum ma 5 plików, test integralności ZIP przeszedł. Uruchomienie: `python experiment.py` z PyTorch. Nowy model 9→32→16→1, 1200 epizodów treningowych, ocena na 250 seedach z każdego zestawu. Wyniki pytania deterministyczne dla (seed, temat, relacja), więc strategie można porównywać parami.

| Polityka | Znane warunki | Odłożone seedy |
|---|---:|---:|
| Losowa | 3,0754 | 3,1090 |
| Nowość | 2,7660 | 2,9716 |
| Heurystyka | 4,2885 | 4,6961 |
| Wyuczona | 4,6126 | 4,7774 |

Wyuczona minus heurystyka: +0,3241 (bootstrap 95% CI +0,1039..+0,5359) na znanych warunkach; +0,0814 (CI −0,1665..+0,3115) na odłożonych seedach. **Brak wiarygodnej przewagi w teście odłożonym.** Około 3 różne tematy na 8 pytań — nie jest to dowód długoterminowych zainteresowań.

## Ograniczenia
Wszystkie dane i odpowiedzi są symulowane. Odłożone seedy nie oznaczają niezależnego generatora dziedzin. Uczenie na zdyskontowanych nagrodach z własnych trajektorii nie zapewnia bezstronnej wyceny alternatywnych pytań. Brak trwałej pamięci preferencji między sesjami, brak samodzielnego tworzenia pytań przez H512; checkpoint H512 bez zmian.

## Następny krok 024
Dodać zapisywaną między sesjami pamięć preferencji, niezależne generatory środowiska i wielokrotne nasiona treningu. Zmierzyć trwałość zainteresowań, rzeczywisty przyrost sprawdzonej wiedzy oraz odporność na zmianę środowiska. Zachować baseline'y i wyniki negatywne.

## Procedura wznowienia
Odczytać ten plik; zweryfikować dostępność ZIP i checkpointu w aktualnej sesji (lokalny artefakt rozmowy może nie być dostępny później). Po kolejnym etapie **nadpisać ten sam plik** i zachować historię przez commit Git.
