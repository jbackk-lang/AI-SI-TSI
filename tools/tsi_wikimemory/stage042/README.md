# WikiMemory 042 — porównanie bramki READ H512

Zaimportowano 250 różnych QID, pozycje 51–300 w kolejności zrzutu Wikidata z 2026-11-09 (CC0). Próbka jest rozłączna z etapem 041. Wykorzystano zachowane 8 MiB z etapu 041. Kod weryfikuje SHA256 fragmentu oraz obu oryginalnych checkpointów.

Oceniono 12 ręcznie ułożonych pytań ustalonych przed poprawnym przebiegiem inferencji. Oba warianty używają tego samego indeksu i ręcznie przypisanych nazw oraz PID. Wariant H512 wykonuje zapytanie do bazy tylko wtedy, gdy najwyższy logit wskazuje READ. Model dostaje pełne pytanie z normalizacją jak w etapie 036, ponieważ jego alfabet nie obsługuje wszystkich znaków z nazw Wikidata.

| Metryka | Wyszukiwanie leksykalne | Bramka H512 |
|---|---:|---:|
| Poprawne rozstrzygnięcia | 12/12 | 6/12 |
| Poprawne odpowiedzi przy dostępnych danych | 8/8 | 2/8 |
| Poprawne abstencje | 4/4 | 4/4 |
| Wszystkie abstencje | 4 | 10 |

Przypadki abstencji obejmują prawdziwy wspólny alias IL, encję poza próbką i dwa brakujące PID. Wynik dotyczy małego zestawu z ręcznie przypisanymi kluczami. Nie ocenia rozpoznawania encji z tekstu, retencji ani generalizacji poza zestawem. Nie trenowano wag. Bramka READ w tym ustawieniu obniżyła trafność.

## Odtworzenie

Rozpakuj własne `TSI_H512_RUN_005.zip` i wskaż jego katalog `src`. Z ZIP etapu 042 uruchom w środowisku z PyTorch:

```powershell
python -X utf8 evaluate_read_gate.py dump-prefix.bz2 PATH/TO/src run042
```

W repozytorium dodaj `stage039` do `PYTHONPATH` i użyj `stage042/evaluate_read_gate.py`. Plik wejściowy można uzyskać według instrukcji etapu 041. Testowano na PyTorch 2.14.0+cpu. ZIP nie zawiera checkpointów.
