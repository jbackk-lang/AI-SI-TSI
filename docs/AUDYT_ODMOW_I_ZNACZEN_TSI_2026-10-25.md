# Powrót do odmowy i audyt znaczeń — 25 października 2026

**Trening gotowych odpowiedzi zatrzymany. Nowy odczyt F/U w lokalnym panelu wyłączony.** Pliki i wagi zachowano; głównego rdzenia nie podmieniono.

## Co wykryto

- W zdaniu „Kuba ma czerwony plecak” odczytywane są osoba, przedmiot i przymiotnik. Pytanie „Jaki kolor ma plecak Kuby?” nie otrzymuje poprawnego rozbioru ról. Powód: niepotwierdzona zgodność przypadków, liczby, rodzaju lub rekcji.
- Klasyfikator rozpoznaje ogólny zamiar „relacja” z prawdopodobieństwem około 99%, lecz nie dostarcza powiązania osoby, przedmiotu i szukanej właściwości. Tego wyniku nie można traktować jako dowodu zrozumienia pytania.
- W badawczej ścieżce nierozstrzygnięte znaczenie mogło przejść do swobodnego generatora. Brakowało obowiązkowej oceny wystarczalności rozumienia przed generowaniem.
- W trzech porównanych zapisach wag nie uzyskano poprawnej odmowy na pytaniach o zagubiony klucz i termin spotkania bez źródła. Wcześniejsze komunikaty odmowy były obsługiwane przez aplikację. Nie ustalono jeszcze wag, do których można bezpiecznie cofnąć cały generator.

## Logika T/F/U a znaczenie słów

Formalna tablica bramek: **69/69**. Kodowanie czterech stanów ról: **81/81** kombinacji bez zmiany etykiet. Ta kontrola nie potwierdza poprawnego rozumienia języka.

Próba „NOT U”: surowy generator odpowiedział „Deść opisany.”, a jawnie podłączony moduł logiczny „U”. W badanym modelu wejściowym nie znaleziono podmodułów `logic_*`; swobodna generacja nie wywoływała interfejsu odpowiedzi logicznej. Problem połączenia pozostaje do rozwiązania.

Trzeba rozdzielać fałsz twierdzenia, sprzeczność danych i odrzucenie zapisu pamięci. W referencji konflikt danych jest oznaczany jako niespójność F, a prawda twierdzenia pozostaje U. Nie wolno przenosić litery F pomiędzy tymi znaczeniami bez określonego typu.

## Słowa i temat

Lokalny słownik zawiera definicje „koloru” jako cechy przedmiotu, znaczenia karcianego i kwantowego. „Zamek” ma znaczenia budynku, mechanizmu drzwi i zapięcia. Nieznane słowo „glip” nie ma wpisu. Sam większy słownik nie zastępuje wyboru znaczenia i powiązania go z kontekstem.

Diagnostyczne porównanie lematu osoby i przedmiotu pozwoliło odróżnić temat Kuby od Ewy bez zależności od kolejności źródeł. Brak osoby, obca osoba, zaimek bez kontekstu i dwie osoby pozostawały nierozstrzygnięte. Był to sprawdzian diagnostyczny, bez wdrażania nowego wybierania tematów i bez generowania odpowiedzi.

Ustalona kolejność dalszej pracy: słowo i jego znaczenie → osoba i temat → szukana zależność lub właściwość → wystarczalność danych → odpowiedź albo konkretne pytanie wyjaśniające. Najpierw lokalny słownik; przy braku lub wieloznaczności wyjaśnienie użytkownika z zapisanym pochodzeniem. Odmowa jest poprawnym wynikiem przy nierozstrzygniętych danych.

## Zatrzymany eksperyment

Ostatnia tura wspólnego treningu po 10 aktualizacjach dała 80/83 chronionych odpowiedzi. Aktualizacje cofnięto. Nie zapisano nowego kandydata i nie wdrożono tych wag. Sam spadek błędu ćwiczeń nie jest podstawą do włączania generowania faktów.

## Potwierdzony stan panelu

Na pytanie „Kiedy odbędzie się spotkanie?” bez źródła panel zwrócił: „Brakuje informacji o terminie. Dodaj dokument lub wklej odpowiedni tekst w „Dokumenty i tekst źródłowy”, a następnie ponów pytanie.”. Nowy odczyt F/U jest wyłączony, a jego proces zakończony. Starsze dane i wagi pozostają zachowane. Portable, MUZ i walidatora nie zmieniano w tym cofnięciu.
