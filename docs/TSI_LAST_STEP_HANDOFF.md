# TSI — instrukcja wznowienia (nadpisywana)

**Aktualizacja:** 2026-11-11. **Ostatni ukończony etap:** TSI_H512_EVAL_028. **Następny:** 029.

## Obowiązkowa jawność metod
**PRZED** każdą symulacją wyraźnie napisz użytkownikowi: **SYMULACJA**, podaj co jest symulowane i co NIE jest testem rzeczywistego H512. Nie przedstawiaj nagród symulatora jako uczenia sieci. Rozróżniaj: (a) rzeczywisty trening wag, (b) test checkpointu bez treningu, (c) test integracji, (d) symulacja.

## Etap 028 — rzeczywista inferencja checkpointów, bez symulacji
Lokalny ZIP rozmowy: `TSI_H512_EVAL_028.zip`, zawiera `evaluate.py`, `result.json`, `README.md`. Wymaga sąsiednich katalogów `TSI_H512_RUN_005` i `TSI_H512_REAL_TRAIN_027` oraz PyTorch. Uruchom: `python TSI_H512_EVAL_028/evaluate.py`.

70 dodatkowych, ręcznie napisanych przez asystenta instrukcji (10 dla każdego operatora), wspólne wejścia dla obu checkpointów. **Oryginalny H512: 24/70 (34,29%). H512 po treningu 027: 22/70 (31,43%).** Naprawiono 12 błędów, wprowadzono 14 nowych; READ spadł z 8/10 do 2/10, IMPLIES wzrósł z 2/10 do 7/10. **Nie promować checkpointu 027** do głównego rdzenia. Oryginalny H512 zachować.

To rzeczywisty test inferencji modelu, ale nie zewnętrzny niezależny benchmark: 70 przykładów pochodzi od asystenta, testuje tylko klasyfikację operatorów; nie bada pełnej aplikacji ani trwałości pamięci. Nie wykonano treningu w 028.

SHA256 oryginału: `23e7c2f208129776705ea075f855c1afd5d26caf2bd7f1620fdae96b16c48851`. SHA256 checkpointu 027: `6f764725d5ead91060e3a3da74eee690437819634d2ee95a37cd4397caedeb36`.

## Następny etap 029
Zdobyć większy, **niezależnie przygotowany** zestaw poleceń, osobny zestaw regresji i trening. Rozważyć kontrolowany fine-tuning z ochroną dotychczasowych umiejętności; porównywać checkpointy na tych samych wejściach. Nie używać symulacji bez uprzedniej zgody i jawnego oznaczenia.

## Powrót
Odczytaj ten plik oraz [metodologię uczenia](TSI_LEARNING_METHODOLOGY.md). Sprawdź dostępność plików i checkpointów. Po następnym etapie nadpisz ten sam plik.
