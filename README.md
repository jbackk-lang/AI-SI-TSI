# AI-SI-TSI — własny model TSI

**Stan: 28 października 2026.** Lokalnie wdrożony moduł **plan-decoder-8m-3** łączy enkoder, dekoder i TIMDR z dynamiczną macierzą odpowiedzi. Repozytorium publikuje dokumentację; bieżący kod, wagi, słowniki i prywatna pamięć TSI pozostają lokalnie.

## Co obecnie działa

- Sieć układa odpowiedź z przekazanych danych, ról i zaleceń, również po zmianie kolejności danych wejściowych.
- Obsługuje zdania składowe z podanym łącznikiem, etykiety, liczby, znaki matematyczne oraz nowe wiersze.
- Wykonuje dłuższy plan w ograniczonych oknach dekodera i zachowuje pełny ciąg znaków UTF-8.
- Wskazuje brakujący element lub sprzeczne zalecenia.
- Odczytuje pola słownika i korzysta z chronionej logiki dwu- oraz trójstanowej.
- Korzysta z własnej bazy odmiany SQLite: lemat i cechy → forma oraz forma → możliwe interpretacje. Jej odczyt nie wymaga Morfeusza.

Odpowiedź emituje dekoder sieciowy. Kontrola weryfikuje wynik względem planu i nie zastępuje błędnego tekstu odpowiedzią wykonawcy reguł.

**Zakres obejmuje wykonywanie planów na danych z oznaczonymi rolami. Swobodna rozmowa nie osiągnęła wymaganego poziomu.** Nowego modułu nie podstawiono jeszcze do wcześniejszego panelu, MUZ, walidatora ani istniejących portable.

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

Sprawdzono model ponownie wczytany po zmianie domyślnej wersji oraz brak przenikania danych między odpowiedziami. Zaliczone **44 testy techniczne** obejmują połączenia, gradienty, macierze, pamięć dekodera i ochronę zapisu. Wyniki dotyczą podanego zakresu wykonania zaleceń.

## Własny słownik odmiany

Początkowa baza zawiera **44 459 rozpoznanych lematów i 1 873 987 rekordów form z cechami**. Zachowuje identyfikatory leksemów, homonimię i źródła. Przy niejednoznaczności zwraca kandydatów, zamiast zgadywać.

Sprawdzono pełną drogę: **Ola + czytać + książka**, wraz z wymaganymi cechami → **Ola czyta książkę.** Podczas tego sprawdzianu import natywnego analizatora był zablokowany.

Dane fleksyjne SGJP pochodzą z jednorazowego lokalnego eksportu; zachowano autorstwo i licencję BSD-2-Clause. [Oficjalne warunki danych](https://morfeusz.sgjp.pl/doc/license/en). Baza obejmuje częściowy eksport 49 663 haseł wejściowych, a nie cały SGJP. Rozszerzanie pokrycia oraz automatyczne ustalanie cech są kolejnymi etapami.

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

Następny krok: odmiana i uzgadnianie wyrazów według ról, następnie samodzielne przygotowywanie planu z polecenia. [Szczegóły stanu](docs/STAN_TSI_2026-10-28.md).

## Istniejąca aplikacja

Dotychczasowy panel ma pracę z tekstem, dokumentami, pamięcią, słownikiem i narzędziami. Uruchomienie istniejącej instalacji: **URUCHOM_TSI.bat**, panel `http://127.0.0.1:8791/`; zatrzymanie: **ZATRZYMAJ_TSI.bat**.

Zrzuty z 20 października przedstawiają istniejący panel, nie nowy moduł wykonywania planów.

![Rozmowa TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

## Archiwum

[Historyczne paczki starego AI-SI — 8 zestawów ZIP, około 8,3 GB](https://github.com/jbackk-lang/AI-SI-TSI/releases/tag/archive-ai-si-2026-10-18). [Spis i instrukcja odtworzenia](docs/PACZKI_STAREGO_AI_SI.md).

[Historia prac](HISTORIA_TSI.md) · [Poprzedni README](docs/archiwum/README_przed_aktualizacja_2026-10-28.md) · [Uczestnicy](CONTRIBUTORS.md) · [Walidator](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)
