# WikiMemory 041 — pierwszy import oficjalnego zrzutu

Dane pochodzą z [oficjalnego zrzutu z 2026-11-09](https://dumps.wikimedia.org/wikidatawiki/entities/20261109/wikidata-20261109-all.json.bz2). Dane strukturalne są udostępniane na [CC0](https://www.wikidata.org/wiki/Wikidata:Licensing). Pobrano bajty 0–8388607 i wybrano pierwsze 50 różnych QID z kompletnych wierszy JSON. Sumy SHA256 są w `result.json`.

## Odtworzenie

Z katalogu `tools/tsi_wikimemory` w PowerShell:

```powershell
curl.exe --fail --location --range 0-8388607 --max-filesize 8388608 --output dump-prefix.bz2 https://dumps.wikimedia.org/wikidatawiki/entities/20261109/wikidata-20261109-all.json.bz2
$env:PYTHONPATH = "stage039;stage040"
python stage041/import_sample.py dump-prefix.bz2 run041
```

W ZIP kod zależności i pobrany fragment są obok skryptu. Uruchom `python import_sample.py dump-prefix.bz2 run041` z rozpakowanego katalogu. Katalog wynikowy musi być nowy.

## Wynik

50 autentycznych encji, 14 126 unikatowych stwierdzeń, 258 wpisów nazw i aliasów oraz 4 partycje. Po ponownym otwarciu bazy sprawdzono 3 zestawy wartości QID/PID przez identyfikator i nazwę oraz abstencję dla nieznanej nazwy. Regresja etapu 039 dała 8/8 na oddzielnych sztucznych fiksturach.

Próbka jest uporządkowana według kolejności w zrzucie i nie jest reprezentatywna. Sprawdzono zgodność ze zrzutem i identyfikację źródła oraz rewizji. Referencje poszczególnych twierdzeń nie są indeksowane. Słownik PL/EN nie obsługuje etykiet języka domyślnego `mul`. W etapie 041 nie wykonywano inferencji ani treningu H512.
