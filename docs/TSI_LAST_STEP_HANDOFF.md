# TSI — instrukcja wznowienia

**2026-11-11. Ostatni etap 037. Następny 038.**

## Jawność
Zawsze **przed** symulacją oznacz **SYMULACJA** i określ jej zakres. 037: **rzeczywisty trening wag PyTorch, bez symulacji**.

## Etap 037 — trening operatora READ H512
Archiwum rozmowy `TSI_KNOWLEDGE_TRAIN_037.zip`, zawiera `train.py`, `result.json`, `run.log`, `README.md`, `h512_trained_037.pt`. Do reprodukcji potrzebne są katalogi 005, 028, 035, PyTorch.

Z oryginalnego checkpointu H512-005 trenowano przez 8 epok AdamW lr 0.00015 parametry `expansion_operator` i `expansion_context` na 28 przykładach: 16 pytań z 035 oznaczonych READ (w tym pytania o brakujące fakty) i 12 nie-READ z 028. Wynik na **treningowych** przykładach: **9/28 przed → 15/28 po**. Kontrola retencji na 56 wcześniej znanych przykładach z 028: **18/56 → 17/56**. To regresja o jeden przypadek, nie promować checkpointu. Nie było niezależnego testu ani treningu wiedzy faktograficznej; operator READ nie oznacza, że model zna odpowiedź. Zbiór kontrolny był wykorzystywany w poprzednich etapach.

## Etap 038
Rozdzielić zadanie: (1) klasyfikacja intencji odczytu, (2) wydobycie klucza wiedzy, (3) weryfikowalna odpowiedź i abstencja. Zbudować zewnętrzny odłożony test z dokumentacją źródeł; trenować tylko na zbiorze treningowym, nie selekcjonować modelu według testu. Zmierzyć retencję operatorów i działanie pełnego potoku. Bez udawania autonomicznego uczenia.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
