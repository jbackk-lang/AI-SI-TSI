# TSI — instrukcja wznowienia (nadpisywana)

**Data:** 2026-11-11. **Ostatni etap:** TSI_CURIOSITY_022. **Następny:** 023.

## Etap 022 — test checkpointu 021
Pakiet lokalny rozmowy: `TSI_CURIOSITY_022.zip` (`evaluate.py`, `value_predictor.pt`, `result.json`, `README.md`). Kod odtwarzania: `python evaluate.py` z PyTorch. Test 300 epizodów dla znanych nazw tematów oraz 300 dla nowych, wszystkie trzy strategie w każdym epizodzie. Wyniki kontrfaktyczne są deterministycznie przypisane do (seed, obiekt, relacja) przez SHA256 i nie zależą od kolejności losowań strategii. To symulacja w pamięci, nie test trwałości grafu.

| Strategia | Znane nazwy | Nowe nazwy |
|---|---:|---:|
| Losowa | 3,0130 | 2,8325 |
| Heurystyka | 5,7165 | 5,6102 |
| Wyuczona | 5,7068 | 5,6633 |

Różnica wyuczona minus heurystyka: znane −0,00967 (bootstrap 95% CI −0,14983..0,12083); nowe +0,05317 (CI −0,09183..0,18850). Brak wiarygodnej przewagi; oba modele wybierają docelowy temat przez 100% kroków. Brak dowodu długoterminowych zainteresowań. Środowisko syntetyczne, nowe tylko etykiety tematów, generator ten sam. H512 bez zmian.

## Następny krok 023
Trenować na wielu odmiennych strukturach grafu, z opóźnionym zyskiem informacyjnym, bez łatwego sygnału identyfikującego temat docelowy. Testować nowe generatory, retencję zainteresowań między epizodami, kalibrację i baseline'y. Zachować oryginalne checkpointy.

## Zasady kontynuacji
Przy wznowieniu odczytaj ten plik, sprawdź faktyczną dostępność lokalnego ZIP/checkpointu; nie zakładaj ich obecności w kolejnej sesji. Po każdym zakończonym etapie **nadpisz ten plik** i zachowaj historię w Git.
