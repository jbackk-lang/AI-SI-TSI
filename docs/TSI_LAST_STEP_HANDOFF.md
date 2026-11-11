# TSI — instrukcja wznowienia (nadpisywana)

**Aktualizacja:** 2026-11-11. **Ostatni ukończony etap:** TSI_CURIOSITY_021. **Następny:** 022.

## Kontekst
TSI: oryginalny H512, graf pamięci i osobne eksperymentalne moduły ciekawości. H512 pozostaje zamrożony. Etap 020: 32 syntetyczne epizody treningu; polityka wyuczona 2,8775, heurystyka 4,5800. Etap 021 rozszerza trening przewidywania wartości informacji i sprawdza inne nazwy dziedzin.

## Etap 021 — rzeczywiście wykonany
Plik lokalny: `TSI_CURIOSITY_021.zip`, zawiera `train.py`, `distributed_memory.py`, `checkpoints/value_predictor.pt`, `result.json`, `README.md`. PyTorch, model 7→24→1. 64 epizody treningowe; 20 epizodów oceny dla każdego zestawu. Zestaw treningowy: fizyka, biologia, astronomia, informatyka. Zestaw testowy: geologia, chemia, ekologia, lingwistyka.

| Strategia | Dziedziny treningowe | Nowe nazwy dziedzin |
|---|---:|---:|
| Losowa | 2,2750 | 3,1575 |
| Heurystyka grafowa | 5,2525 | 5,6875 |
| Wyuczona | 5,7600 | 5,8325 |

Checkpoint zapisany i ponownie wczytany; porównanie wyjścia po odczycie przeszło. **Ograniczenia:** symulowane odpowiedzi i weryfikacja, szablony relacji, mała próba; nowe nazwy tematów, ale ten sam generator środowiska; losowanie odpowiedzi zależy od sekwencji działań polityki, więc nie jest to ścisły test sparowany ze wspólnymi wynikami. Nie wnioskować o autonomii ani świadomości. H512 nietknięty.

## Następny krok 022
Zaprojektować rygorystyczną ocenę z predefiniowanymi wynikami dla każdego (epizod, podmiot, relacja, próba), oddzielonymi od kolejności losowań strategii; zwiększyć liczbę seedów i raportować niepewność. Zmierzyć także trwałość zainteresowań i rzeczywisty przyrost wiedzy. Dopiero później rozważać integrację z H512.

## Procedura powrotu
1. Pobierz ten plik z GitHub i odczytaj jako instrukcję ostatniego kroku.
2. Sprawdź dostępność ZIP i checkpointu w nowej sesji; nie zakładaj, że lokalny plik przetrwał.
3. Odtwórz testy i zapisuj tylko zweryfikowane wyniki.
4. Po ukończeniu następnego etapu nadpisz **ten sam plik**, zachowując historię przez Git commity.

Repozytoria: https://github.com/jbackk-lang/AI-SI-TSI oraz https://github.com/jbackk-lang/Belzi/tree/tsi-v003-curiosity.
