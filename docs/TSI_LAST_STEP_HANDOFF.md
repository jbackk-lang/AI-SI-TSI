# TSI — instrukcja wznowienia

**2026-11-11. Ostatni etap: 034. Następny: 035.**

## Obowiązkowe oznaczenie symulacji
Zanim uruchomisz symulator, wyraźnie napisz użytkownikowi **SYMULACJA** i zakres. Etap 034: **BEZ SYMULACJI, BEZ TRENINGU WAG**.

## Etap 034 — fakty z NASA + pamięć TSI
Archiwum w rozmowie: `TSI_KNOWLEDGE_034.zip`. Zawiera `experiment.py`, `result.json`, `run.log`, `README.md`. Do reprodukcji potrzebne są sąsiednie katalogi `TSI_H512_RUN_005` (checkpoint H512-005), `TSI_KNOWLEDGE_033` (ledger) i PyTorch. Uruchom: `python TSI_KNOWLEDGE_034/experiment.py`.

Ręcznie wydobyto i sprawdzono 14 faktów z 3 stron NASA: https://science.nasa.gov/planetary-science/focus-areas/ ; https://science.nasa.gov/solar-system/solar-system-facts/ ; https://science.nasa.gov/solar-system/moons/facts/ . Każdy fakt ma URL pochodzenia i status ręcznego sprawdzenia. Test: **15/15** poprawnych wyników przy podanym wprost kluczu subject/relation (14 znanych + 1 brak wiedzy). Restart ledgeru przeszedł. Inferencja rzeczywistego H512-005 została wykonana i zalogowana dla każdego pytania.

**KRYTYCZNE OGRANICZENIE:** H512 nie wybierał kluczy wyszukiwania i nie generował odpowiedzi; subject/relation podawał evaluator. 15/15 nie jest miarą rozumienia pytań ani autonomicznego uczenia. Nie trenowano wag. Status verified = ręcznie sprawdzone źródło NASA, nie niezależny fact-check.

## Etap 035
Połączyć pytanie użytkownika z wyborem subject/relation i wyszukiwaniem, testować na nowych parafrazach i przypadkach negatywnych. Raportować błędy parsera. Dopiero po tym rzeczywisty trening wag na wiedzy z odłożonym zbiorem. Nie wracać do symulatorów bez uprzedzenia.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
