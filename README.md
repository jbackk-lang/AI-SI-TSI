# AI-SI-TSI — własny model TSI

**Stan: 28 października 2026.** Lokalnie wdrożony moduł **plan-decoder-8m-3** łączy enkoder, dekoder i TIMDR z dynamiczną macierzą odpowiedzi. Repozytorium publikuje dokumentację; bieżący kod, wagi, słowniki i prywatna pamięć TSI pozostają lokalnie.

## Co obecnie działa

- Sieć układa odpowiedź z planu. Dla prostych zdań oznajmujących moduł słownikowo-gramatyczny sam ustala role; pozostałe plany nadal wymagają podania ról i zaleceń.
- Obsługuje zdania składowe z podanym łącznikiem, etykiety, liczby, znaki matematyczne oraz nowe wiersze.
- Wykonuje dłuższy plan w ograniczonych oknach dekodera i zachowuje pełny ciąg znaków UTF-8.
- Wskazuje brakujący element lub sprzeczne zalecenia.
- Odczytuje pola słownika i korzysta z chronionej logiki dwu- oraz trójstanowej.
- Korzysta z własnej bazy odmiany SQLite: lemat i cechy → forma oraz forma → możliwe interpretacje. Jej odczyt nie wymaga Morfeusza.

Odpowiedź emituje dekoder sieciowy. Kontrola weryfikuje wynik względem planu i nie zastępuje błędnego tekstu odpowiedzią wykonawcy reguł.

**Działa wykonywanie planów oraz odczyt ról w ograniczonym zakresie prostych zdań. Swobodna rozmowa nie osiągnęła wymaganego poziomu.** Nowego modułu nie podstawiono jeszcze do wcześniejszego panelu, MUZ, walidatora ani istniejących portable.

## Potwierdzone działanie po wdrożeniu

| Kontrola | Wynik |
|---|---:|
| Nowe polecenia przez domyślne wejście: kolejność, zdania złożone, symbole i długie odpowiedzi | **24/24** |
| Braki danych i sprzeczne zalecenia | **4/4** |
| Odłożone plany: pełne, osłabione i wyłączone dodatkowe wzmocnienie adresu; macierz nadal podana | **12/12 w każdym wariancie** |
| Wpisy słownika | **32/32** |
| Próby brzegowe, w tym odwrócone pola liczbowe | **20/20** |
| Krótkie kopiowanie / wybór pola | **24/24 / 24/24** |
| Zachowany starszy format kopiowania | **8/8** |
| Chroniona logika: dawne polecenia / pełne tablice | **15/15 / 57/57** |

Sprawdzono model ponownie wczytany po zmianie domyślnej wersji oraz brak przenikania danych między odpowiedziami. Zaliczone **82 testy techniczne** obejmują połączenia, gradienty, macierze, pamięć dekodera i ochronę zapisu. Wyniki dotyczą podanego zakresu wykonania zaleceń.

## Własny słownik odmiany

Początkowa baza zawiera **44 459 rozpoznanych lematów i 1 873 987 rekordów form z cechami**. Zachowuje identyfikatory leksemów, homonimię i źródła. Przy niejednoznaczności zwraca kandydatów, zamiast zgadywać.

Sprawdzono pełną drogę: **Ola + czytać + książka**, wraz z wymaganymi cechami → **Ola czyta książkę.** Podczas tego sprawdzianu import natywnego analizatora był zablokowany.

Dane fleksyjne SGJP pochodzą z jednorazowego lokalnego eksportu; zachowano autorstwo i licencję BSD-2-Clause. [Oficjalne warunki danych](https://morfeusz.sgjp.pl/doc/license/en). Baza obejmuje częściowy eksport 49 663 haseł wejściowych, a nie cały SGJP. Dalsza praca obejmuje rozszerzanie pokrycia i samodzielny odczyt ról z polecenia.

## Automatyczne uzgadnianie form

TSI dobiera już osobę i liczbę czasownika na podstawie podmiotu oraz przypadek dopełnienia z chronionej macierzy gramatycznej. Obsługiwany zakres: czas teraźniejszy, przeszły i przyszły, tryb przypuszczający, podmioty pojedyncze i złożone, 58 wybranych schematów rekcji oraz zmiana biernika dopełnienia na dopełniacz przy zaprzeczeniu.

Rzeczywiste odpowiedzi dekodera, utworzone z lematów i ról bez ręcznego podawania wszystkich cech:

- **Ola czyta książkę.**
- **Ja czytam książkę.**
- **My czytamy książkę.**
- **Ola i Jan czytają książkę.**
- **Ola nie czyta książki.**
- **Ola szuka książki.**
- **Ola pomaga dziecku.**

Kontrola domyślnego wejścia: **20/20 wykonań** i **4/4 poprawnych zgłoszeń braków lub niejednoznaczności**. Import Morfeusza był zablokowany. Przy rzeczywistej homonimii, nieznanej rekcji, nieobsługiwanym trybie albo sprzecznych cechach system prosi o potrzebne dane. Reguły, ich kolejność i macierze są chronione przed zmianą.

To rozszerzenie działa regułowo przez własną bazę i istniejący dekoder. Wagi sieci nie zostały przy tym zmienione. Role nadal są przekazywane jawnie.

## Grupy wyrazów, czasy i tryby

Przymiotniki uzgadniają przypadek, liczbę i rodzaj z rzeczownikiem. Liczebniki **0–10**, w tym formy zbiorowe, zmieniają postać rzeczownika i zgodę z czasownikiem. Sprawdzian odpowiedzi dekodera: **20/20**.

- **Dwie nowe książki leżą.**
- **Pięć nowych książek leży.**
- **Dwoje małych dzieci czyta.**

Kolejny sprawdzian: **18/18 odpowiedzi** dla czasów i trybu przypuszczającego oraz **5/5 zgłoszeń niejednoznaczności lub sprzeczności**.

- **Ola czytała. / Ola będzie czytać. / Ola przeczyta.**
- **Ja mogłem. / Ja mógłbym.** — po wskazaniu rodzaju.
- **My czytałyśmy. / My czytalibyśmy.** — dla odpowiednich rodzajów.
- **Dwie książki leżały. / Pięć książek leżało.**

Tryb przypuszczający jest rozróżniany od czasu. Przy „ja” i czasie przeszłym system prosi o rodzaj, jeśli możliwe formy są różne. Czasownik dokonany nie otrzymuje fikcyjnej formy czasu teraźniejszego. [Zasady aspektu i trybu — ZPE](https://zpe.gov.pl/a/aspekt-i-tryb-czasownika/DPyWEtI3p), [składnia liczebników — RJP](https://rjp.pan.pl/skladnia-liczebnikow-2/).

Odmiany pochodzą z własnej bazy form; reguły są chronione. Rozszerzenie nie zmienia wag sieci i nadal wymaga podania lematów oraz ról.

## Odniesienia między zdaniami

Moduł łączy przygotowane zdania i rozstrzyga podmiotowe „on/ona” na podstawie wcześniej wymienionych obiektów oraz ich cech słownikowych. Zachowuje wskazanie osoby między zdaniami, a przy kilku pasujących osobach zwraca pytanie o doprecyzowanie. Kontekst jest oddzielny dla każdego zapytania.

- **Ola śpi. Ona czyta.**
- **Ola widzi kota. On śpi.**
- **Ola śpi, ponieważ ona czytała.**
- **Ola widzi Ewę. Ona…** → wymagany wybór, o którą osobę chodzi.

Rzeczywisty dekoder: **7/7 odpowiedzi**, **4/4 kontroli brakującego lub niejednoznacznego odniesienia**. Pełne testy techniczne: **82/82**. Na tym etapie role zdań i rejestr osób są przekazywane jawnie; swobodny odczyt tekstu jest kolejnym krokiem.

## Odczyt prostego zdania bez podawania ról

W lokalnym API dodano `read_statement` i `compose_text`. Czytnik korzysta z form słownika, rekcji czasownika oraz zgodności osoby, liczby i rodzaju. Sprawdza pełne przypisanie słów, a przy kilku możliwych interpretacjach prosi o doprecyzowanie.

| Tekst wejściowy | Odpowiedź dekodera |
|---|---|
| Książkę czyta Ola. | **Ola czyta książkę.** |
| Dziecku pomaga Ewa. | **Ewa pomaga dziecku.** |
| Nową książkę czyta Ola. | **Ola czyta nową książkę.** |
| Książki nie czyta Ola. | **Ola nie czyta książki.** |
| Olę widzi Ewa. | **Ewa widzi Olę.** |

Domyślna lokalna ścieżka: **20/20 zdań** i **8/8 kontroli braków, niezgodności lub niejednoznaczności**; bez importu Morfeusza. „Dziecko widzi zwierzę” zwraca dwie możliwe interpretacje, zamiast przypisywać role wyłącznie według kolejności słów.

Zakres: jednozdaniowe oznajmienia z jednym osobowym czasownikiem, podmiotem, opcjonalnym dopełnieniem i prostymi grupami przymiotnikowymi; zaprzeczenie bezpośrednio przy czasowniku. Dodatkowe nieobsługiwane słowa, symbole, pytania i zdania złożone są zgłaszane. Ten etap porządkuje odczyt i odtworzenie treści, nie stanowi jeszcze swobodnej odpowiedzi na pytanie. Wagi pozostały bez zmian.

## Wielkość

| Składnik | Wielkość |
|---|---:|
| Sieć tekstowa: enkoder, dekoder, TIMDR i kanały planu | **8 081 032 parametry** |
| Chroniony moduł operatorów logicznych | **483 parametry** |
| Tensory wag sieci tekstowej FP32 | **30,83 MiB** |
| Checkpoint z optymalizatorem i stanem losowania | **92,71 MiB** |
| Własna baza odmiany | **353,18 MiB** |

1 MiB = 1 048 576 bajtów. Kod, Python, PyTorch, pozostałe słowniki i dane są dodatkowymi składnikami pełnej instalacji. Podane wielkości nie oznaczają rozmiaru kompletnego portable.

## Dalsza praca i zachowanie stanu

Kolejne bloki kontynuują jedną linię najnowszych wag, optymalizatora i losowania. Zatwierdzone punkty są chronione przed zwykłym czyszczeniem kopii. Plan powstaje dla konkretnego zapytania i pozostaje niezmienny do końca odpowiedzi.

Następny krok: połączenie odczytu tekstu z odniesieniami między zdaniami, następnie pytania i polecenia oraz rozmowa. [Szczegóły stanu](docs/STAN_TSI_2026-10-28.md).

## Istniejąca aplikacja

Dotychczasowy panel ma pracę z tekstem, dokumentami, pamięcią, słownikiem i narzędziami. Uruchomienie istniejącej instalacji: **URUCHOM_TSI.bat**, panel `http://127.0.0.1:8791/`; zatrzymanie: **ZATRZYMAJ_TSI.bat**.

Zrzuty z 20 października przedstawiają istniejący panel, nie nowy moduł wykonywania planów.

![Rozmowa TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

## Archiwum

[Historyczne paczki starego AI-SI — 8 zestawów ZIP, około 8,3 GB](https://github.com/jbackk-lang/AI-SI-TSI/releases/tag/archive-ai-si-2026-10-18). [Spis i instrukcja odtworzenia](docs/PACZKI_STAREGO_AI_SI.md).

[Historia prac](HISTORIA_TSI.md) · [Poprzedni README](docs/archiwum/README_przed_aktualizacja_2026-10-28.md) · [Uczestnicy](CONTRIBUTORS.md) · [Walidator](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)
