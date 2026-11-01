# AI-SI-TSI — lokalny system TSI

**Stan: 1 listopada 2026. Generator 3 jest wdrożony w lokalnej aplikacji.** TSI łączy własną sieć enkoder–dekoder, słowniki, pamięć, jawne reguły oraz narzędzia obliczeniowe. Aktualny zakres obejmuje układanie wypowiedzi z odczytanych ról i rozmowę o podanym materiale. Konsultacje AI i źródła internetowe są opcjonalne.

Repozytorium publikuje dokumentację. Aktualny kod TSI, wagi i prywatna pamięć pozostają lokalne.

## Co działa

- **Pytania o krótkie nazwane dane**: sieć wybiera wartość, kontrola sprawdza źródło i rolę, następnie dekoder wykonuje plan pełnego zdania. Obsługiwane są dwa fakty, zmiana materiału i sygnalizowanie sprzecznych wartości.
- **Układanie wypowiedzi z ról — generator 3**: odczyt osoby, czynności i dopełnień → plan gramatyczny → neuronowy dekoder → kontrola odpowiedzi. `Mapę ogląda Iga` przekształca w **Iga ogląda mapę.** Wierne powtarzanie pozostaje osobną operacją.
- **Zdania złożone i zaprzeczenia**: zachowanie „nie”, „i”, „a”, „oraz” i „ale”; rozróżnienie przyczyny („bo”, „ponieważ”, „gdyż”), skutku („więc”, „dlatego”) oraz podanej kolejności („potem”, „następnie”). Kolejność nie jest uznawana za dowód przyczyny.
- **Odwołania i rozmowa o materiale**: zaimki „on/ona/ono”, wspólny podmiot kolejnych czynności, pytania „Dlaczego?”, „A Leon?”, „Co z tego wynika?” i „Co potem?”. Przy konkurujących osobach podaje możliwe imiona; wybór użytkownika uzupełnia kontekst i ponawia pierwotne pytanie. Nowy materiał i reset unieważniają wcześniejszy punkt odniesienia.
- **Kilka akapitów**: odczyt do 64 KiB tekstu UTF-8 i 128 zdań w bieżącej ścieżce, przekazanie do dekodera wybranych danych. Przekroczenia limitu, niejasne istotne fragmenty i sprzeczne zaprzeczenia wymagają doprecyzowania.
- **Kontrola gotowej odpowiedzi**: ponowny odczyt ról, obiektów, zaprzeczeń i relacji względem źródła. Odpowiedź wraca również do gałęzi K. Jej stan jest osobno zapisanym kierunkowskazem; o przyjęciu nie decyduje sam sygnał K.
- **Praca z tekstem i dokumentami**: wklejanie materiału, obsługa TXT, MD, CSV, DOCX i PDF; DOC wymaga Microsoft Worda. Odczyt wzorów wymaga kontroli z oryginałem.
- **Narzędzia matematyczne**: obliczenia, równania, całki, pochodne i macierze przez lokalny solver. Dekoder składa odpowiedź według planu zadania.
- **Słowniki, odmiana i proste relacje zdań**: części mowy, przypadki, role i wybrane zaprzeczenia; trwałe notatki i kontekst rozmowy.
- **Jawne reguły logiki dwu- i trójstanowej**, niezależne od swobodnego generowania tekstu.
- **Panel PL/EN**: rozmowa, lokalne podpowiedzi, reguły grzecznościowe, daty i święta, pasek aktywności, ustawienia źródeł i konsultanta AI.

W pytaniach z zaznaczoną pracą na materiale naprawiono pierwszeństwo dokumentu przed domyślnym wyszukiwaniem w Wikipedii. Jawne polecenie wyszukiwania pozostaje dostępne.

## Przykłady aktualnej ścieżki odpowiedzi

W „Dokumenty i tekst źródłowy” wklej `Objętość: 3 l. Gotowanie: 75 min.`, wybierz pracę z materiałem i zadaj pytanie.

Możesz też wpisać `Iga czyta list, bo Leon otwiera okno. Co robi Iga?`, a następnie zadawać pytania:

| Kolejna wiadomość | Odpowiedź generatora 3 |
|---|---|
| Co robi Iga? | **Iga czyta list.** |
| Dlaczego? | **Iga czyta list, ponieważ Leon otwiera okno.** |
| A Leon? | **Leon otwiera okno.** |
| Co z tego wynika? | **Leon otwiera okno, więc Iga czyta list.** |
| Co potem? | **Źródło nie podaje dalszej kolejności zdarzeń.** |

W tym przykładzie źródło podaje zależność, ale nie kolejność zdarzeń. Dla `Iga czyta list, potem Leon zamyka drzwi` pytanie „Co potem?” otrzymuje odpowiedź zachowującą tę podaną kolejność.

Przykłady nazwanych pól z pierwszego materiału:

| Pytanie lub zmiana | Rzeczywista odpowiedź |
|---|---|
| Jaka jest objętość? | **Wartość pola „Objętość” wynosi 3 l.** |
| Podaj obie wartości | **Wartość pola „Objętość” wynosi 3 l. Wartość pola „Gotowanie” wynosi 75 min.** |
| Zamień materiał: objętość 8 l | **Wartość pola „Objętość” wynosi 8 l.** |
| Podaj jednocześnie objętość 3 l i 6 l | **Podane wartości wymagają uzgodnienia: Objętość: 3 l / 6 l.** |
| Jaka jest temperatura? | **Odczyt nie potwierdził odpowiedzi na podstawie tych danych.** |

Odpowiedzi powstają według planu gramatycznego i przechodzą kontrolę zgodności z materiałem. Odczyt nazwanych pól ma okno **512 tokenów bajtowych**; dłuższa proza jest dzielona na zdania przed wyborem danych dla dekodera. Sprawdzono polskie odczyty oraz angielskie odpowiedzi dla nazwanych pól i komunikaty doprecyzowania. Rozszerzenia gramatyczne generatora 3 dotyczą polskiego tekstu źródłowego.

## Potwierdzone wyniki

| Kontrola z 1 listopada | Wynik |
|---|---:|
| Generator 3: role, negacje, relacje i dłuższy materiał — plan | **35/35** |
| Generator 3: pełna aplikacja, kolejne pytania, wybór osoby, dokumenty, reset i izolacja rozmów | **57/57** |
| Kontrola gotowej odpowiedzi: poprawne, błędne i nierozstrzygnięte propozycje | **9/9** |
| Cała aplikacja: materiał, sprzeczność, zmiana wartości, język, przywitanie i dodawanie | **10/10** |
| Celowo uszkodzone wyjście dekodera | **odrzucone** |
| Wagi podczas powyższych prób | **niezmienione** |

Wyniki dotyczą osobnych prób i opisanego zakresu; nie są jedną oceną całej sprawności językowej. [Przebieg prac i wcześniejsze wyniki](HISTORIA_TSI.md).

## Aktualny stan uczenia i kontroli

**Trening pozostaje zatrzymany. Wdrożono generator 3 z planowaniem wypowiedzi i kontrolą gotowej odpowiedzi.** Ostatni stan treningu 5051, optymalizator i stan losowania są zachowane. Moduł neuronowy nowej ścieżki korzysta z zapisu 3944. Dalszy trening domyślnie jest normalny, a 3:1 pozostaje trybem korekcji potwierdzonego pogorszenia.

Gałąź K otrzymuje ponownie źródło, pytanie i gotową propozycję. Zmiana jej składowych jest obserwacją, a nie skalibrowaną oceną prawdziwości. Weryfikacja znaczenia działa w granicach odczytanych ról i jawnych relacji. Złożone warunki, nieobsługiwane konstrukcje i brakujące dane wymagają doprecyzowania. [Historia wcześniejszych generatorów](docs/archiwum/README_przed_generator_v3_20261101.md).

## Wielkość

| Składnik | Aktualny pomiar |
|---|---:|
| Sieć modułu źródłowego, zapis 3944 | **9 040 623 parametrów** |
| Jej parametry FP32 | **34.49 MiB** |
| Zapis kroku 3944 z optymalizatorem i stanem treningu | **103.71 MiB** |

To rozmiar nowej sieci, nie kompletnej instalacji ani portable. Główna dotychczasowa aplikacja zachowuje swój rdzeń i narzędzia; nowy moduł `TSI-grounded-step-3944` jest wykazywany oddzielnie. Słowniki, PyTorch, Python, dokumenty i kopie zajmują dodatkowe miejsce. [Wcześniejsze pomiary i wyniki](docs/archiwum/README_przed_2026-11-01.md).

## Uruchomienie lokalne

Uruchom **URUCHOM_TSI.bat** w katalogu instalacji i otwórz `http://127.0.0.1:8791/`. Repozytorium dokumentacyjne nie zawiera obecnego kodu ani gotowej nowej instalacji. Portable nie przebudowano w tym etapie.

W **Ustawienia AI i źródeł** można wybrać Gemini, OpenAI, Claude lub **Bez AI**. Klucze zapisuje się wyłącznie lokalnie. Bez klucza aplikacja pomija konsultację. Wyłączenie internetu pozostawia narzędzia i źródła lokalne. [Opis ustawień i źródeł](docs/archiwum/README_przed_2026-11-01.md#nauczyciel-ai--konfiguracja).

## Panel

Zrzut z **29 października 2026**, zachowany jako podgląd układu; nie przedstawia nowego sprawdzianu z 1 listopada.

![Panel TSI — przykład całki](docs/tsi-chat-current.png)

## Historia i pozostałe zastosowania

[Historia prac](HISTORIA_TSI.md) · [Poprzedni README](docs/archiwum/README_przed_2026-11-01.md) · [Uczestnicy](CONTRIBUTORS.md)

[Sprawdzian sygnałów z 29 października](docs/RAPORT_SYGNALY_2026-10-29.md) — diagnostyka awarii nie osiągnęła wymaganego poziomu.

[Walidator matematyczny](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)

[Historyczne paczki starego AI-SI](https://github.com/jbackk-lang/AI-SI-TSI/releases/tag/archive-ai-si-2026-10-18) · [Spis i odtworzenie](docs/PACZKI_STAREGO_AI_SI.md)
