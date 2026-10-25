# Słownik znaczeń i lekcje TSI — 25 października 2026

## Stan wdrożenia

Sieć słownika, schowek oraz przyjmowanie wyjaśnień działają w lokalnym ogólnym TSI. Zaplecze lekcji jest dostępne przez API; panel nauki zostawiono na później. MUZ, walidator i portable nie otrzymały tych zmian. Wagi sieci pozostały bez zmian, odczyt F/U jest wyłączony, trening gotowych odpowiedzi zatrzymany.

## Struktura słownika

| Warstwa | Liczba |
|---|---:|
| Hasła po normalizacji | 114 215 |
| Wpisy gramatyczne | 125 720 |
| Znaczenia | 172 772 |
| Relacje | 733 529 |
| Relacje bez indeksu znaczenia, przechowywane oddzielnie | 436 196 |
| Powiązania tematyczne | 60 730 |
| Powiązania form odmiany | 1 437 842 |
| Wpisy nazw własnych, obejmujące też nazwy miejsc | 9 350 |
| Wpisy wyraźnie oznaczające imiona w definicji | 1 900 |

Nowa baza grafu zajmuje 153 186 304 B. Korzysta z istniejącej bazy form odmiany. Relacje bez indeksu znaczenia nie są dowodem dotyczącym konkretnego znaczenia. Ranking wskazówek kontekstowych nie wybiera sam znaczenia za użytkownika.

Źródło: [polski eksport Wikisłownika przez Kaikki/Wiktextract](https://kaikki.org/dictionary/rawdata.html). Zachowano autorstwo, odnośniki do haseł i warunki ponownego wykorzystania tekstów Wikimedia. Nie importowano rejestru imion PESEL ani nowej listy frekwencyjnej. Liczba haseł nie oznacza liczby słów powszechnie używanych.

## Naprawiony przebieg rozmowy

Wcześniej TSI po otrzymaniu wyjaśnienia ponownie pytała o to samo słowo. Po zmianie przebieg w działającej aplikacji był następujący:

1. „Co oznacza glipnovar?” — prośba o znaczenie.
2. „Glipnovar to lokalna nazwa przycisku startowego.” — zapis wyjaśnienia użytkownika.
3. „Co oznacza glipnovar?” — „lokalna nazwa przycisku startowego.”

Wyjaśnienie jest przypisane do profilu i tematu, z oznaczeniem pochodzenia od użytkownika. Nie trafia do treningu wag ani do pamięci jako niezależnie potwierdzony fakt o świecie. „Nie wiem” nie staje się definicją. „Co oznacza zamek?” przedstawia oddzielne znaczenia; numer 2 wybrał mechanizm zamykający drzwi i szuflady. Pytanie o termin spotkania nadal kończy się prośbą o brakujące dane.

## Lekcje tematyczne

Lekcja zachowuje temat, treść materiału, datę, adres źródła oraz skrót kontrolny treści. Zawiera listę słów i odnośniki do schowka, a po potwierdzeniu znaczenia odczytuje je ponownie. Tematy oraz profile mają oddzielne zapisy.

Skrót jest wyciągiem z początkowych akapitów lub zdań materiału. W pierwszej próbie ranking fragmentów listy urwał kontekst definicji; poprawiono zachowanie całych akapitów. Nie jest to jeszcze samodzielna synteza znaczenia tematu przez generator.

Próba internetowa: [Trójkąt — Wikipedia](https://pl.wikipedia.org/wiki/Tr%C3%B3jk%C4%85t). TSI pobrała materiał, zachowała definicję wprowadzającą i pełną listę jej warunków. Samo pobranie źródła nie nadaje mu statusu zweryfikowanego faktu.

## Wyniki

| Sprawdzian | Wynik | Zakres |
|---|---:|---|
| Sieć znaczeń | 21/21 | Oddzielne znaczenia, formy, nazwy, trwałość i cofanie |
| Dialog wyjaśnień | 13/13 | Zapis, odczyt, profile, tematy, odmowa i zmiana kontekstu |
| Lekcje | 10/10 | Źródło, zachowanie tekstu, nieznane słowo, trwałość i izolacja |
| Działająca aplikacja | 14/14 | Rzeczywista rozmowa, wybór znaczenia, rachunek, brak terminu, API lekcji i pobranie Wikipedii |

Są to kontrole wymienionych przebiegów. Swobodna rozmowa nie osiągnęła wymaganego poziomu. Kolejny etap: odczyt właściwości i zależności z definicji, pytania do treści lekcji oraz bardziej elastyczne parafrazy. Panel lekcji później.
