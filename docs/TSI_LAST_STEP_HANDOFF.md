# TSI — instrukcja wznowienia

**2026-11-11. Ostatni etap: 038. Następny: 039.**

## Obowiązkowa jawność
Przed każdą symulacją napisz użytkownikowi **SYMULACJA** i co jest symulowane. Nie przedstawiaj fikstur testowych jako rzeczywistej wiedzy lub uczenia. W etapie 038 **nie trenowano wag H512 i nie wykonywano inferencji H512**.

## Etap 038 — TSI WikiMemory, rzeczywisty importer i baza
Archiwum rozmowy `TSI_WIKIMEMORY_038.zip` (SHA256 `7d561f69cfe1fd3783fdf709071a476c3e32e3d2c32af9d699ae71c2a6b72c23`). Zawiera `wikimemory.py`, `test.py`, `result.json`, `run.log`, `README.md`. Importer obsługuje strumieniowo `latest-all.json[.bz2/.gz]`, SQLite partycjonowane deterministycznie po SHA256 QID, zapisywanie QID/PID i raw JSON datavalue, filtrację deprecated, restart i unknown. Test z **dwoma SZTUCZNYMI fiksturami QID** zaliczony; nie są to fakty Wikidata. **Rzeczywistych encji Wikidata zaimportowano 0**. Próba HTTPS pobrania z Wikidata w kontenerze nie powiodła się z powodu DNS. To partycjonowanie lokalne, nie rozproszony klaster; brak pełnych referencji claimów, FTS i kontrolera H512.

## Etap 039
Uzyskać prawdziwy dump Wikidata (oficjalne źródło: https://dumps.wikimedia.org/wikidatawiki/entities/), zachować datę i warunki licencji, zaimportować próbkę i zweryfikować wartości i pochodzenie. Nie deklarować importu bez dowodu. Potem dodać wyszukiwanie encji i porównanie odpowiedzi z i bez pamięci. W dalszym etapie podłączyć H512 jako kontroler i wykonać prawdziwy trening wag z niezależną ewaluacją.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).

## Pliki źródłowe etapu 038 na GitHub
Kod, test, instrukcja, wynik i log zostały zapisane w `tools/tsi_wikimemory/` na gałęzi `main`: https://github.com/jbackk-lang/AI-SI-TSI/tree/main/tools/tsi_wikimemory . To nadal wyłącznie importer i testy na fiksturach, bez rzeczywistego importu Wikidata.

## Etap 039 — indeks nazw i aliasów
Kod, testy i wynik: https://github.com/jbackk-lang/AI-SI-TSI/tree/main/tools/tsi_wikimemory/stage039 . 8/8 testów na **czterech sztucznych fiksturach**, trwałość po restarcie. Implementacja: dokładne dopasowanie nazw/aliasów PL/EN, `unknown_entity`, `unknown_property`, `ambiguous`, źródło importu i numer rewizji. **0 prawdziwych encji Wikidata, 0 treningu/inferencji H512.** Sieć kontenera nie umożliwia pobrania Wikidata. Następny etap: prawdziwy import i niezależny test, bez twierdzenia o uczeniu modelu.
