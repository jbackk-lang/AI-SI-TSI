# AI-SI-TSI — lokalny system TSI

**Stan: 1 listopada 2026.** TSI łączy własną sieć enkoder–dekoder, słowniki, pamięć, jawne reguły oraz narzędzia obliczeniowe. Działa lokalnie; konsultacje AI i źródła internetowe są opcjonalne. **Swobodna rozmowa nie osiągnęła wymaganego poziomu — trwa jej trening.**

Repozytorium publikuje dokumentację. Aktualny kod TSI, wagi i prywatna pamięć pozostają lokalne.

## Co działa

- **Pytania o krótkie nazwane dane**: sieć wybiera wartość, kontrola sprawdza źródło i rolę, następnie dekoder wykonuje plan pełnego zdania. Obsługiwane są dwa fakty, zmiana materiału i sygnalizowanie sprzecznych wartości.
- **Praca z tekstem i dokumentami**: wklejanie materiału, obsługa TXT, MD, CSV, DOCX i PDF; DOC wymaga Microsoft Worda. Odczyt wzorów wymaga kontroli z oryginałem.
- **Narzędzia matematyczne**: obliczenia, równania, całki, pochodne i macierze przez lokalny solver. Dekoder składa odpowiedź według planu zadania.
- **Słowniki, odmiana i proste relacje zdań**: części mowy, przypadki, role i wybrane zaprzeczenia; trwałe notatki i kontekst rozmowy.
- **Jawne reguły logiki dwu- i trójstanowej**, niezależne od swobodnego generowania tekstu.
- **Panel PL/EN**: rozmowa, lokalne podpowiedzi, reguły grzecznościowe, daty i święta, pasek aktywności, ustawienia źródeł i konsultanta AI.

W pytaniach z zaznaczoną pracą na materiale naprawiono pierwszeństwo dokumentu przed domyślnym wyszukiwaniem w Wikipedii. Jawne polecenie wyszukiwania pozostaje dostępne.

## Przykłady aktualnej ścieżki odpowiedzi

W „Dokumenty i tekst źródłowy” wklej `Objętość: 3 l. Gotowanie: 75 min.`, wybierz pracę z materiałem i zadaj pytanie.

| Pytanie lub zmiana | Rzeczywista odpowiedź |
|---|---|
| Jaka jest objętość? | **Wartość pola „Objętość” wynosi 3 l.** |
| Podaj obie wartości | **Wartość pola „Objętość” wynosi 3 l. Wartość pola „Gotowanie” wynosi 75 min.** |
| Zamień materiał: objętość 8 l | **Wartość pola „Objętość” wynosi 8 l.** |
| Podaj jednocześnie objętość 3 l i 6 l | **Podane wartości wymagają uzgodnienia: Objętość: 3 l / 6 l.** |
| Jaka jest temperatura? | **Odczyt nie potwierdził odpowiedzi na podstawie tych danych.** |

To generowanie według jawnego planu gramatycznego. Błędny tekst dekodera jest odrzucany. Powyższy zakres dotyczy danych `Nazwa: wartość`, a nie dowolnego dokumentu ani swobodnej rozmowy. Okno nowego odczytu: **512 tokenów bajtowych** łącznie z pytaniem. Dłuższy materiał obsługuje dotychczasowy czytnik, bez cichego obcinania. Sprawdzono pytania po polsku oraz polskie i angielskie brzmienie odpowiedzi.

## Potwierdzone wyniki

| Kontrola z 1 listopada | Wynik |
|---|---:|
| Pełne zdania: etykiety, jednostki, godziny i brakujące dane | **23/23** |
| Cała aplikacja: materiał, sprzeczność, zmiana wartości, język, przywitanie i dodawanie | **10/10** |
| Celowo uszkodzone wyjście dekodera | **odrzucone** |
| Wagi podczas powyższych prób | **niezmienione** |

Po rozgrzaniu podstawowe odpowiedzi na dane trwały około **2–3 s** na użytym komputerze; start procesu jest dłuższy. Wyniki dotyczą tych prób i opisanego zakresu. [Szczegóły wdrożenia](docs/ODCZYT_ODPOWIEDZI_20261101.md).

## Aktualny trening

Kontynuowana jest jedna linia wag, od zapisu **3944**, z momentami optymalizatora i stanem losowania. Wspólnie uczą się enkoder, warstwy TIMDR, połączenie słownikowe i dekoder. Obecny etap obejmuje proste pełne zdania, pytania o ich treść i krótkie odpowiedzi dialogowe. Powtarzanie tekstu jest mierzone oddzielnie od odpowiadania na pytania.

Podczas treningu zapisywane są surowe wypowiedzi oraz kontrole zachowania odczytu, planowania i reguł. Sam spadek straty nie oznacza zaliczenia rozmowy. Włączony moduł odpowiedzi na nazwane dane korzysta z przypiętego, sprawdzonego zapisu; kolejne zmiany treningowe nie zmieniają go automatycznie.

## Wielkość

| Składnik | Aktualny pomiar |
|---|---:|
| Nowa sieć współdzielonego odczytu i generowania | **9 040 623 parametrów** |
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
