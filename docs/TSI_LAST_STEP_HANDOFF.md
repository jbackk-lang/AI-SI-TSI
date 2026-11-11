# TSI — instrukcja wznowienia

**Aktualizacja: 2026-11-11. Ostatni ukończony etap: 030. Następny: 031.**

## Jawność symulacji
Zanim użyjesz symulatora, wyraźnie napisz użytkownikowi **SYMULACJA** i co jest symulowane. Oddziel: trening wag, inferencję, integrację i symulację. Użytkownik oczekuje pracy na realnych checkpointach H512.

## Etap 030 — audyt rzeczywistych checkpointów, bez symulacji i bez treningu
Lokalny ZIP rozmowy: `TSI_H512_AUDIT_030.zip` (audit.py, result.json, run.log, README.md). Do odtworzenia wymagane katalogi 005, 027, 028 i 029, w tym checkpointy. Komenda: `python TSI_H512_AUDIT_030/audit.py`.

Porównanie oryginalnego H512 z kandydatem 029: 21 przykładów z 027: **6/21 vs 7/21**; pełne 70 z 028: **24/70 vs 28/70** (13 naprawionych, 9 regresji); podział 029: treningowe 21 **8/21 vs 8/21**, walidacyjne 14 **5/14 vs 8/14**, testowe 35 **11/35 vs 12/35**.

**OSTRZEŻENIE: dane nie są niezależne!** Wszystkie polecenia pisał ten sam asystent, 70 z 028 było już analizowanych, 21/70 użyto do treningu 029, 14/70 do wyboru checkpointu. Wynik 28/70 jest częściowo skażony treningiem; NIE jest miarą generalizacji. Etap 030 nie aktualizował wag. Nie promować 029 do głównego rdzenia.

## Następny etap 031
Pozyskać naprawdę niezależny zbiór zewnętrzny (źródło i licencja), zablokować go przed treningiem, ocenić na nim H512-005 i H512-029. Następnie planować trening z kontrolą retencji. Nie wprowadzać symulacji bez jawnego uprzedzenia.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
