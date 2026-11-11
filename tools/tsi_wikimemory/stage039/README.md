# TSI WikiMemory 039 — wyszukiwanie encji i kontrola niejednoznaczności

Etap 039 rozbudowuje importer 038 o deterministyczny indeks nazw i aliasów w SQLite. **Nie jest to symulacja H512; nie uruchomiono ani nie trenowano modelu.** Testy wykorzystują cztery jawnie sztuczne rekordy (fikstury), nie rzeczywiste encje Wikidata.

Uruchomienie: `python test.py`.

**Uwaga:** CLI w `wikimemory.py` korzysta z klasy bazowej i nie indeksuje aliasów. Do importu użyj:

```python
from search import WikiSearch
m = WikiSearch('wiki_db',4)
print(m.import_stream('/sciezka/latest-all.json.bz2',limit=10000))
print(m.answer('nazwa encji','P31'))
m.close()
```

Indeksuje polskie i angielskie etykiety i aliasy; stosuje Unicode NFC/casefold, exact-match; zwraca `unknown_entity`, `unknown_property`, `ambiguous`; zachowuje źródło importu i rewizję. Nie generuje odpowiedzi naturalnojęzykowej. SQLite działa lokalnie, nie jako rozproszony klaster.

Test: **8/8 na sztucznych fiksturach** i retencja po restarcie. **Prawdziwych encji Wikidata: 0.** Następnie: pozyskać rzeczywisty dump, udokumentować datę i licencję, sprawdzić autentyczne fakty i dopiero wtedy podłączyć H512.
