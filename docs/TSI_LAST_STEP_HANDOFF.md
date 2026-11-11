# TSI — instrukcja wznowienia

**2026-11-11. Ostatni ukończony etap: 033. Następny: 034 — rzeczywiste pozyskiwanie wiedzy.**

## Jawność
Zawsze uprzedzaj **przed** symulacją słowem **SYMULACJA** i określ zakres. W 033 nie używano symulatora ani nie trenowano wag. Rozróżniaj pamięć zewnętrzną od wiedzy wyuczonej w parametrach H512.

## Etap 033 — wiedza, nie sam klasyfikator instrukcji
Archiwum rozmowy: `TSI_KNOWLEDGE_033.zip` (`knowledge.py`, `test.py`, `result.json`, `run.log`, `README.md`). Zależności: katalogi 005 i 028, PyTorch. Uruchom `python TSI_KNOWLEDGE_033/test.py`.

Rzeczywisty graf `TSI_H512_RUN_005/graph` zawierał **1 fakt**: `woda / stan / ciekly`. Dodano osobny trwały rejestr pochodzenia i statusów faktów, detekcję konfliktu, wycofanie i odpowiedź `unknown`; testy zapisu, odczytu po ponownym otwarciu, konfliktu, wycofania i braku wiedzy zaliczone. Rzeczywisty checkpoint H512-005 wykonał inferencję na `jaki jest stan wody` i przewidział operator `READ`, ale **nie odczytywał z rejestru odpowiedzi**. Testowe ustawienie statusu `verified` ręcznie nie jest niezależną weryfikacją prawdy. **Nie dodano sprawdzonej wiedzy zewnętrznej i nie trenowano wag.**

## Etap 034
Pozyskać prawdziwe źródła z pochodzeniem/licencją, zbudować odczyt faktów do odpowiedzi na pytania, porównać odpowiedzi z i bez pamięci. Następnie zbadać uczenie wag H512 na weryfikowalnym materiale i test niezależny. Nie wracać do samych symulatorów.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
