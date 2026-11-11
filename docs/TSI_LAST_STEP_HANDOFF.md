# TSI — instrukcja wznowienia

**2026-11-11. Ostatni etap: 042. Następny: 043.**

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

## Etap 040 — realny pomiar rozmiaru SQLite
https://github.com/jbackk-lang/AI-SI-TSI/tree/main/tools/tsi_wikimemory/stage040 — skrypt pomiaru, wynik i README. Na 4 sztucznych encjach: 4 stwierdzenia, 6 nazw, 4 partycje, 163840 bajtów stron SQLite i 294912 bajtów plików. **0 autentycznych encji Wikidata**, brak treningu/inferencji H512. Próba pobrania danych przez HTTPS nie powiodła się (DNS). Pełny pakiet kodu/testów w archiwum rozmowy `TSI_WIKIMEMORY_040.zip`. Następny krok: import rzeczywistego dumpu.


## Etap 041 — pierwszy import autentycznych danych Wikidata

[Skrypt, wynik i log](../tools/tsi_wikimemory/stage041). Oficjalny zrzut z 2026-11-09, CC0. Zaimportowano pierwsze 50 różnych QID z pobranego fragmentu 8 MiB. SQLite zawiera 14 126 unikatowych stwierdzeń i 258 nazw lub aliasów. Trzy kontrole wartości, źródła i rewizji oraz jedna kontrola abstencji przeszły po ponownym otwarciu bazy. Regresja 039 przeszła 8/8 na sztucznych fiksturach. Pakiet sesji `TSI_WIKIMEMORY_041.zip` zawiera kod, dane wejściowe, wynik, log i instrukcje. Bez inferencji i treningu H512.

Oryginalny H512 jest w lokalnym archiwum `C:/Users/jback/Downloads/_checkpoint/TSI_H512_RUN_005.zip` jako `src/h512.pt`; jego SHA256 zgadza się z instrukcją. Archiwum zawiera też `src/null_gate_75.pt` i moduły. Eksperymentalny 037 jest w `TSI_KNOWLEDGE_TRAIN_037.zip` w tym samym katalogu. Pliku `h512_candidate_029.pt` nie odnaleziono w sprawdzonych lokalizacjach.

## Plan etapu 042

Zbudować niezależny zestaw zapytań na rzeczywistych encjach, z kontrolami abstencji. Porównać tę samą pamięć i zestaw zapytań w trybie leksykalnym oraz z faktyczną inferencją oryginalnego H512. Oddzielnie zmierzyć trafność, abstencję i retencję. Zachować checkpoint bazowy.


## Etap 042 — inferencja H512 jako bramka READ

[Skrypt, wynik i log](../tools/tsi_wikimemory/stage042). Na 250 encjach rozłącznych z etapem 041 porównano 12 ręcznie ułożonych pytań z ustalonym kluczem encji i właściwości. Leksykalnie 12/12, bramka oryginalnego H512 6/12, w tym 2/8 poprawnych odpowiedzi na pytania z danymi i 4/4 poprawne abstencje. Sześć dodatkowych abstencji zablokowało poprawne odpowiedzi. Checkpointy przeszły kontrolę SHA256. Bez treningu i pomiaru retencji. Pakiet sesji `TSI_WIKIMEMORY_042.zip` zawiera fragment zrzutu, kod, wynik, log i instrukcje.

## Następny etap 043

Przygotować rozdzielone zbiory treningowy, walidacyjny i testowy oraz stały zestaw retencji. Zachować wynik leksykalny jako punkt odniesienia. Jeśli trenowana będzie bramka, zapisać osobny checkpoint i ocenić go przed rozważeniem użycia w normalnym odczycie.
