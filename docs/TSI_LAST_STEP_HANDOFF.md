# TSI — instrukcja wznowienia

**2026-11-11. Ostatni etap 031. Następny 032.**

## Obowiązek: SYMULACJA
Przed uruchomieniem jakiegokolwiek symulatora wyraźnie uprzedź użytkownika: **SYMULACJA**, podaj co jest symulowane. Nie myl treningu wag, inferencji i symulacji.

## 031: test rzeczywistych checkpointów H512 — bez symulacji i bez treningu
Lokalny artefakt: `TSI_H512_ROBUSTNESS_031.zip`; zawiera `robustness.py`, `result.json`, `run.log`, `README.md`. Uruchom `python TSI_H512_ROBUSTNESS_031/robustness.py`; wymagane katalogi 005, 028, 029 oraz PyTorch.

Na 70 znanych instrukcjach (z etapu 028), 4 wersje formatowania, 560 wywołań modelu. Oryginalny H512: oryginał **24/70**, uppercase **12/70**, pytajnik **26/70**, spacje **24/70**. Kandydat 029: oryginał **28/70**, uppercase **9/70**, pytajnik **25/70**, spacje **28/70**. Niezmienność predykcji po uppercase: bazowy 9/70, kandydat 3/70. Wniosek: poważna wrażliwość na wielkość liter, szczególnie 029; nie promować checkpointu.

**Ograniczenie:** ponownie wykorzystano przykłady z 028. To nie jest zewnętrzny benchmark ani nowy trening. W 031 nie aktualizowano wag.

## 032
Sprawdź kod przetwarzania tekstu (normalizacja wielkości liter) i wykonaj kontrolowane porównanie z i bez normalizacji, bez ingerencji w checkpointy. Poszukaj zewnętrznego zbioru poleceń z pochodzeniem i licencją. Wyniki negatywne zachowuj.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
