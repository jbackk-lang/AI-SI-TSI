# TSI — instrukcja wznowienia

**2026-11-11. Ostatni ukończony etap 032. Następny 033.**

## Obowiązkowa jawność
**Przed każdą symulacją** poinformuj użytkownika: **SYMULACJA** i dokładny zakres. Odróżniaj trening wag, inferencję, integrację i symulację. Nie deklaruj treningu, jeśli nie aktualizowano wag.

## Etap 032 — normalizacja wejścia, rzeczywista inferencja, bez symulacji i treningu
Archiwum rozmowy: `TSI_H512_NORMALIZE_032.zip` z `evaluate.py`, `result.json`, `run.log`, `README.md`. Zależności: katalogi 005, 028, 029, 031 i PyTorch. Uruchom: `python TSI_H512_NORMALIZE_032/evaluate.py`.

Normalizacja przed wejściem: Unicode NFC, lower(), strip(), usunięcie końcowych znaków ?!. i scalenie białych znaków. Porównano 70 wcześniej użytych instrukcji × 4 warianty × 2 checkpointy × 2 sposoby wejścia.

H512-005: bez normalizacji poprawne odpowiedzi (oryginał/uppercase/pytajnik/spacje) **24/12/26/24 na 70**; po normalizacji **24/24/24/24**. H512-029: bez **28/9/25/28**, po **28/28/28/28**. Zgodność predykcji z oryginałem po normalizacji 70/70 dla wszystkich trzech wariantów, co wynika z identycznego kanonicznego wejścia. **Nie wzrosła podstawowa trafność; nie jest to dowód nowej zdolności modelu.** Checkpointy bez zmian. Wszystkie przykłady pochodzą z wcześniej używanego zestawu, nie z niezależnego benchmarku.

## Etap 033
Zweryfikować normalizację na trudnych przykładach, gdzie wielkość liter/interpunkcja jest semantycznie istotna, oraz pozyskać zewnętrzny, licencjonowany, niezależny zbiór danych. Dopiero potem rozważać dalszy trening H512. Nie wdrażać kandydata 029 jako głównego rdzenia.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
