# TSI — instrukcja wznowienia (nadpisywana)

**Aktualizacja:** 2026-11-11. **Ostatni ukończony etap:** TSI_CURIOSITY_024. **Następny:** 025.

## Etap 024 — pamięć preferencji między sesjami
Pakiet lokalny: `TSI_CURIOSITY_024.zip` zawierający `experiment.py`, `result.json`, `run.log`, `README.md`. Zależność od `TSI_CURIOSITY_023/value_predictor_023.pt` (checkpoint nie jest duplikowany w paczce 024). Uruchomienie: `python TSI_CURIOSITY_024/experiment.py`, z oboma katalogami obok siebie. Wymaga PyTorch. 200 środowisk na wariant × 5 sesji; pamięć preferencji zapisywana i ponownie wczytywana z JSON pomiędzy sesjami.

| Strategia | Zgodne warunki | Odwrócona zależność |
|---|---:|---:|
| Losowa | 17,8507 | 18,4297 |
| Heurystyka | 38,4795 | 16,1086 |
| Wyuczona | 37,5378 | 21,3863 |
| Wyuczona + pamięć | 37,6088 | 22,6177 |

Wyuczona z pamięcią minus bez pamięci: zgodne +0,0710 (bootstrap 95% CI −0,2762..+0,3826); odwrócone +1,2314 (CI +0,8252..+1,6582). Wyniki to średnia sumy nagród w pięciu sesjach. Test odtwarzania JSON i integralność ZIP zaliczone.

**Ograniczenia:** środowisko syntetyczne, przesunięcie rozkładu ręcznie skonstruowane, te same tematy w kolejnych sesjach, brak rzeczywistych faktów, brak generowania pytań przez H512. Pamięć JSON w katalogu tymczasowym podczas testu, nie trwała pamięć produkcyjna. H512 bez zmian.

## Następny etap 025
Sprawdzić reset pamięci jako ablation, nowe obiekty w kolejnych sesjach, retencję sprawdzonej wiedzy i trwałe preferencje w nowym środowisku. Zapisać negatywne wyniki i ocenić różnice na wspólnych scenariuszach.

## Powrót
Odczytaj ten plik; sprawdź dostępność lokalnych ZIP 023 i 024 oraz checkpointu w nowej sesji. Nie zakładaj, że pliki z poprzedniej sesji są dostępne. Po etapie 025 nadpisz **ten sam plik**, zachowując historię Git.
