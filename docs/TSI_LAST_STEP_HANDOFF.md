# TSI — instrukcja wznowienia

**2026-11-11. Ostatni ukończony etap 036. Następny 037.**

## Jawność
Zawsze przed symulacją powiedz **SYMULACJA** i co symulujesz. 036: rzeczywista inferencja checkpointu H512-005, **bez symulacji i bez treningu wag**.

## 036 — bramka wiedzy sterowana rzeczywistym H512
Archiwum rozmowy: `TSI_KNOWLEDGE_036.zip` z `experiment.py`, `result.json`, `run.log`, `README.md`. Zależności: katalogi 005, 033, 035 i PyTorch. Uruchom `python TSI_KNOWLEDGE_036/experiment.py`.

Na 16 pytaniach z 035 parser regułowy bez bramki uzyskał **16/16**, z bramką sterowaną wyjściem H512 (odczyt dozwolony wyłącznie dla operatora `READ`) **9/16**. H512 wskazał `READ` 8 razy. To istotny negatywny wynik: połączenie realnej decyzji H512 pogorszyło skuteczność. **H512 nie wybiera klucza faktu; robi to nadal parser regułowy.** Dane nie są niezależne, model nie zdobył nowej wiedzy w wagach. Import skryptu 035 uruchamia również jego test, więc run.log zawiera dwa raporty.

## 037 — następny krok
Przygotować dane z prawdziwymi pytaniami o odczyt vs inne intencje, podzielić train/validation/test **przed** treningiem, wytrenować rzeczywisty klasyfikator H512, zmierzyć poprawę bramki i retencję wcześniejszych operatorów. Nie traktować małych ręcznie pisanych testów jako niezależnej generalizacji. Dążyć do realnego wykorzystania wiedzy, nie symulacji.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
