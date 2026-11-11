# TSI WikiMemory 038 — rzeczywisty kod importu, bez rzeczywistego zrzutu Wiki

Ten etap tworzy **implementację**, nie udaje zaimportowania Wikipedii. Próba pobrania danych Wikidata z kontenera zakończyła się błędem DNS. Test `test.py` używa **SZTUCZNYCH FIKSTUR TESTOWYCH** (dwa fikcyjne QID); to nie jest symulacja uczenia H512 ani wiedza Wikipedii. Brak treningu wag i inferencji H512.

## Import prawdziwych danych

Pobierz legalny oficjalny dump Wikidata z https://dumps.wikimedia.org/wikidatawiki/entities/ , zachowaj plik, datę i licencję. Następnie:

```
python wikimemory.py --dump latest-all.json.bz2 --db wiki_db --shards 16 --limit 10000
```

Parser strumieniowy czyta format `latest-all.json(.bz2/.gz)`, nie ładuje całego zrzutu do RAM. Rozdziela encje deterministycznie po SHA256 QID do plików SQLite, zapisuje identyfikatory Q/P, treści i adres pochodzenia, filtruje deprecated statements. SQLite WAL i commit co 1000 encji. `--limit` jest tylko limitem testowego importu, a nie reprezentatywną próbą.

## Ograniczenia

* To **partycjonowanie na jednym komputerze**, nie prawdziwa rozproszona baza wielowęzłowa.
* Zachowuje surowe wartości claims; nie rozwiązuje etykiet wartości QID, qualifierów, referencji pojedynczych claims ani konfliktów.
* Status `source` wskazuje plik importu; nie zastępuje licencji, metadanych daty zrzutu ani weryfikacji poszczególnych stwierdzeń.
* Nie ma jeszcze wyszukiwarki języka polskiego, indeksu FTS ani wyuczonego kontrolera H512. To etap infrastruktury, nie zdobycie wiedzy przez wagi.

## Test

`python test.py` — zapis/odczyt, partycjonowanie, filtracja deprecated, restart, abstencja.
