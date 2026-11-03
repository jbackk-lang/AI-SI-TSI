# AI-SI-TSI — lokalny system TSI

**Stan: 3 listopada 2026.** TSI łączy własną sieć enkoder–dekoder, słowniki, pamięć, jawne reguły logiczne i narzędzia obliczeniowe. Aplikacja działa lokalnie. Konsultant AI i źródła internetowe są opcjonalne.

Repozytorium zawiera dokumentację. Aktualny kod TSI, wagi i prywatna pamięć pozostają lokalne. Dawny kod AI-SI i modele zewnętrzne są w [archiwach Releases](docs/PACZKI_STAREGO_AI_SI.md).

## Co potrafi obecna aplikacja

- Odczytuje nazwane dane i odpowiada na pytania o podany materiał; wskazuje braki i sprzeczności.
- Układa zdania z rozpoznanych ról, zachowuje wybrane zaprzeczenia, przyczynę, skutek i kolejność zdarzeń. Obsługuje kolejne pytania dotyczące materiału.
- Korzysta ze słowników, odmiany, lokalnych notatek i pamięci rozmowy.
- Przyjmuje tekst i dokumenty TXT, MD, CSV, DOCX i PDF. Stary DOC wymaga Microsoft Worda.
- Wykonuje obliczenia, równania, pochodne, całki i macierze przez lokalne narzędzia matematyczne.
- Udostępnia panel PL/EN, ustawienia źródeł i konsultanta AI oraz pasek aktywności.
- Wspólny moduł odpowiedzi jest podłączony do [MUZ](https://github.com/jbackk-lang/TSI-MUZ) i [walidatora matematycznego](https://github.com/jbackk-lang/TSI-math-validator-5).

**Swobodna rozmowa nie osiągnęła wymaganego poziomu.** Poniższe wyniki dotyczą wskazanych zestawów zadań.

## Aktualne wyniki i wagi

| Zakres | Stan |
|---|---|
| Moduł odpowiedzi wdrożony lokalnie | **krok 5217; 9 074 672 parametrów** |
| Próby rozmowy o źródle | **30/30** |
| Próby całej aplikacji: dane, dokument, brak, sprzeczność, PL/EN i obliczenie | **10/10** |
| Odczyt kontekstu / transfer danych | **48/48 · 17/17** |
| Rozwijana większa sieć — ostatni oceniony zapis | **krok 5632; 21 731 408 parametrów**, zachowane stany optymalizatora i losowania |
| Ostatnia ocena tej sieci | dawne prośby **41/48**, chronione odpowiedzi **5/7**, odczyt kontekstu **46/48**, odłożone nowe sformułowania **0/4** |
| Dodatkowa kontrola nowych pytań | **3/18**; pytania nie są dodawane do treningu |
| Bieżąca praca | Automatyczna korekta z kontrolą zachowania dawnych umiejętności. Po pogorszeniu najpierw odzyskiwane są wcześniejsze odpowiedzi, następnie wraca nowy materiał. Wagi aplikacji pozostają na kroku 5217. |
| Przebieg i przyczyny zmian | [Historia automatycznych ćwiczeń](HISTORIA_TSI.md#3-listopada--automatyczne-ćwiczenia-języka-i-sygnałów) |

Stałe reguły logiki dwu- i trójstanowej pozostają osobnym, kontrolowanym elementem. Zwykłe odpowiedzi „tak”, „nie” i „nie wiem” nie są automatycznie zadaniami T/F/U.

## Wielkość

| Składnik | Rozmiar |
|---|---:|
| Parametry wdrożonego modułu odpowiedzi, FP32 | **34,62 MiB** |
| Parametry większej sieci treningowej, FP32 | **82,90 MiB** |

To wielkość samych parametrów. Pełna instalacja obejmuje dodatkowo kod, Python, biblioteki, słowniki, pamięć i narzędzia; checkpoint treningowy zawiera też stany optymalizatora. Historyczne kopie nie są częścią rozmiaru samego modelu. [Poprzednie pomiary](docs/archiwum/README_przed_porzadkami_20261103.md).

## Jak korzystać

W lokalnej instalacji uruchom **URUCHOM_TSI.bat** i otwórz `http://127.0.0.1:8791/`.

Przykład materiału: `Objętość: 3 l. Gotowanie: 75 min.` Pytania: „Jaka jest objętość?”, „Podaj obie wartości”, „Jaka jest temperatura?”. W ostatnim przypadku materiał nie zawiera odpowiedzi.

Przykład rozmowy: `Iga czyta list, bo Leon otwiera okno. Co robi Iga?` Następnie: „Dlaczego?”, „A Leon?”. Wynik powinien zachowywać zależność podaną w źródle.

W **Ustawienia AI i źródeł** wybierz dostawcę albo **Bez AI**. Klucz zapisuj lokalnie. Bez klucza TSI pomija konsultację, a bez internetu korzysta z dostępnych narzędzi i materiału lokalnego. Repozytorium dokumentacyjne nie instaluje aplikacji.

## Podgląd panelu

Zrzut z 29 października przedstawia układ panelu.

![Panel TSI — przykład całki](docs/tsi-chat-current.png)

## Archiwum i historia

[Archiwa dawnego AI-SI i odtwarzanie](docs/PACZKI_STAREGO_AI_SI.md) · [Porządki z 3 listopada](docs/PORZADKI_20261103.md) · [Historia prac](HISTORIA_TSI.md) · [Wcześniejszy stan i szczegółowe próby](docs/archiwum/README_przed_porzadkami_20261103.md) · [Uczestnicy](CONTRIBUTORS.md)
