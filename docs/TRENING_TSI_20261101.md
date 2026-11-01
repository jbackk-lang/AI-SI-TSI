# Trening swobodnych odpowiedzi — 1 listopada 2026

**Swobodna rozmowa nie osiągnęła wymaganego poziomu. Trening trwa.** Działająca aplikacja zachowuje sprawdzony moduł odpowiedzi na nazwane dane. Poniższe próby dotyczą osobnej, kontynuowanej linii treningowej.

Po wykryciu słabego wykorzystania źródła dodano treningowe wskazywanie powiązań między tekstem wejściowym a odpowiedzią oraz uczony kanał kopiowania znaków ze źródła. Podczas swobodnego generowania sieć sama wybiera znaki i kanał wyjścia. Nie otrzymuje oczekiwanej odpowiedzi ani planu emisji.

Najlepszy dotąd zakończony blok, zapis **4220**, dał **5/8 wiernych odpowiedzi w małej kontroli podstaw**. Próby obejmują powtarzanie, pytania o treść i krótką rozmowę. Są wielokrotnie używanymi kontrolami walidacyjnymi; nie stanowią niezależnego sprawdzianu ogólnej rozmowy.

| Wejście | Surowa odpowiedź sieci | Ocena |
|---|---|---|
| Ola czyta list. Co robi Ola? | Ola czyta list. | poprawna |
| Adam otwiera okno. Co robi Adam? | Adam otwiera okno. | poprawna |
| Jan niesie plecak. Jaką czynność wykonuje Jan? | Jan niesie plecak. | poprawna, inne sformułowanie pytania |
| Cześć, jak się nazywasz? | Cześć! Nazywam się TSI. | poprawna, pytanie obecne w nauce |
| Jak się nazywasz? | Jan niesie plecak. | błędna |
| Powtórz: Iga ogląda mapę. | Ina I. | błędna |
| Iga ogląda mapę. Co robi Iga? | Ina Isie plecak. | błędna |

Piątym poprawnym wynikiem było powtórzenie zdania „Ola czyta list.”. Odpowiedzi w tabeli są wynikiem surowej generacji, nie aplikacyjnych reguł grzecznościowych. W tym bloku zachowano odczyt **48/48**, transfer krótkich danych **17/17** oraz niezmienione stałe reguły logiczne. Kontrola reguł nie oznacza formalnego potwierdzenia każdej wypowiedzi sieci.

Dalszy trening uczy wyboru między kopiowaniem potwierdzonego tekstu a samodzielnym generowaniem. Enkoder i dekoder są uczone wspólnie; zachowywane są wagi, optymalizator, losowanie i pozycja w kolejce lekcji. Spadek straty nie wystarcza do uznania rozmowy za gotową.

Lokalna linia treningowa z uczonym kanałem źródłowym ma **9 040 880 parametrów**. Sprawdzony moduł aplikacyjny na zapisie 3944 ma **9 040 623 parametry**. Są wykazywane oddzielnie. Kod, bieżące wagi i pamięć pozostają lokalnie.


## Kolejna próba i powtórki

Dodatkowy nadzór wyboru kopiowania w kolejnym bloku pogorszył wynik do **3/8** (zapis **4317**). Nie wdrożono go w aplikacji. Lepszy zapis 4220 zachowano; dalsza nauka kontynuuje najnowszą linię wag, bez automatycznego cofania.

Wyłączono dodatkowe wymuszanie wyboru kanału. Nowy blok ma bardziej zróżnicowane przykłady kopiowania poprawnych zdań, 12 imion, 8 czynności i warianty pytań dialogowych. Kategorie są równoważone; każdy krok zawiera też powtórkę dawnej lekcji. Publiczne teksty służą tu do ćwiczenia wiernego powtarzania, a nie automatycznego zatwierdzania zawartych w nich faktów. Nie ma jeszcze wyniku potwierdzającego ukończenie tego etapu.
