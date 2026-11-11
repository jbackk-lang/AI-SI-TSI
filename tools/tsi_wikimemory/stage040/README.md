# TSI WikiMemory 040 — pomiar rozmiaru

Rzeczywisty pomiar plików SQLite na **czterech sztucznych fiksturach**, nie import prawdziwej Wikidata i nie trening H512. W kontenerze dostęp HTTPS do Wikidata zakończył się błędem DNS. Liczba zaimportowanych prawdziwych encji: **0**.

`python measure.py /sciezka/do/wiki_db` — rozmiar stron baz SQLite, plików wraz z WAL/SHM oraz liczby encji, stwierdzeń i nazw.

Pomiar testowy: 4 encje, 4 stwierdzenia, 6 nazw, 4 partycje, **163840 bajtów stron SQLite** i **294912 bajtów plików na dysku**. To narzut małych baz, nie miara skali pełnego Wikidata. Pełne pliki testowe i kod: archiwum `TSI_WIKIMEMORY_040.zip` w rozmowie.

Następny krok: prawdziwy dump z https://dumps.wikimedia.org/wikidatawiki/entities/ , data i licencja, import oraz pomiar bez ekstrapolacji z fikstur.
