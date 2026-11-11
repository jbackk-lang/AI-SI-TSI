# TSI — instrukcja wznowienia

**2026-11-11. Ostatni etap: 035. Następny: 036.**

## Jawność metod
Przed jakąkolwiek symulacją napisz wyraźnie **SYMULACJA** i co jest symulowane. Nie utożsamiaj regułowego parsera z wiedzą wyuczoną przez H512. Etap 035: **bez symulacji, bez treningu wag**.

## Etap 035 — tekst pytania → parser regułowy → trwała pamięć
Archiwum rozmowy: `TSI_KNOWLEDGE_035.zip` (`experiment.py`, `result.json`, `run.log`, `README.md`). Wymaga katalogów 005, 033 oraz PyTorch. Uruchom `python TSI_KNOWLEDGE_035/experiment.py`.

Na 16 pytaniach po polsku: **16/16** poprawnych rezultatów, z czego **11/11** znanych faktów i **5/5** właściwych odmów. Fakty (11) ręcznie przepisane z wcześniejszego zestawu NASA; nie weryfikowano źródeł na nowo. Parser regułowy sam odczytuje subject/relation z pytania, ale **H512 nie wybiera klucza ani nie generuje odpowiedzi** — jego inferencja jest wykonywana i zapisywana oddzielnie. Wynik 16/16 to test integracyjny na małej liczbie przykładów, nie niezależny benchmark rozumienia, nie uczenie wag. Normalizacja usuwa diakrytyki, obsługuje ł.

## Następny etap 036
Zbudować mechanizm, w którym rzeczywiste wyjście H512 wpływa na wybór klucza lub odpowiedzi, z bezpiecznym odrzuceniem niepewnych predykcji. Porównać z regułowym baseline'em na odłożonych pytaniach, pozyskać niezależny materiał i trenować na nim wagi dopiero po rozdzieleniu danych. Zachować wyniki negatywne.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
