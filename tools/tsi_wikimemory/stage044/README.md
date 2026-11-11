# TSI WikiMemory — etap 044: intencja odczytu a dostępność faktu

**Status: prototyp polityki odczytu.** Nie trenowano H512, nie wykonano nowej inferencji checkpointu etapu 043. Testy bazodanowe wykonały prawdziwe transakcje SQLite, ale na **SZTUCZNYCH FIKSTURACH**. Nie zmieniono jeszcze lokalnego panelu Windows.

## Wyniki i kontekst

Raport etapu 043: walidacja 55/100 → 53/100, test 86/100 → 65/100, retencja 6/12 → 7/12. W zapisanym raporcie jest **21 wcześniej poprawnych odczytów zablokowanych po treningu**. Reguły etapu 044 rozpoznają formę wszystkich 21 pytań, wszystkich 12 pytań retencji i 8/8 kontrolnych zdań logicznych. **To retrospektywna analiza danych już znanych z raportu, a NIE niezależny test lub pomiar nowej inferencji H512.**

## Interfejs

`read_policy.py`: `detect_intent(question)` rozpoznaje jawnie pytania o fakt albo logiczne; `decide(question, h512_operator)` wybiera działania; `answer(db, question, entity_label, property_id, h512_operator)` odpytuje istniejącą `WikiSearch`. W przypadku nieznanej encji, właściwości lub niejednoznaczności zachowuje abstencję.

Model **nie wydobywa encji ani właściwości** — oba parametry dostarcza zewnętrzny parser. Dla jednoznacznych pytań faktograficznych reguły nie dopuszczają do blokowania faktów przez błędny operator H512. Operator modelu jest rejestrowany; przy nierozpoznanym pytaniu może jeszcze uruchomić próbę odczytu. To baza regułowa, nie uczenie H512.

## Uruchomienie lokalne

Docelowy katalog: `C:\Users\jback\Downloads\a\AI-SI-TSI\tools\tsi_wikimemory\stage044`. Po pobraniu ZIP z rozmowy uruchom w PowerShell `install-local.ps1` z katalogu rozpakowanego pakietu; tworzy kopie poprzednich plików docelowych, nie modyfikuje wag `.pt` ani panelu. Następnie w folderze docelowym:

```powershell
python test_policy.py
python audit_043.py C:\sciezka\do\TSI-043\result.json
```

Audyt wymaga lokalnego `result.json` z etapu 043, a pełna ewaluacja wymaga też `TSI-043.zip`, prawdziwej WikiMemory i checkpointu. ZIP z etapu 043 jest według przekazania użytkownika w `C:\Users\jback\Documents\Codex\2026-11-11\w-plikach-download-jest-katalog-timdr\outputs\TSI-043.zip`, ale ścieżka ta nie jest osiągalna przez ten runtime.

## Dalsza praca

Zamrozić **nowy** test pytań niezależnych od reguł dobranych do 21 regresji. Dopiero po lokalnej instalacji i weryfikacji rzeczywistej bazy porównać trzy tryby: leksykalny, H512-043 i nowy router; osobno mierzyć trafność, prawidłową abstencję i retencję operatorów. Nie promować checkpointu 043 na podstawie dotychczasowych wyników.
