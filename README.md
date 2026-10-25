# AI-SI-TSI — lokalny asystent TSI

**Stan: 25 października 2026.** TSI łączy własne modele, macierze językowe, pamięć źródeł i narzędzia obliczeniowe. Pracuje lokalnie. Repozytorium zawiera dokumentację; kod, wagi i dokumenty użytkownika pozostają lokalnie.

## Co obecnie potrafi

| Obszar | Możliwości |
|---|---|
| Tekst i rozmowa | Pytania do podanej treści, skróty, listy, wiadomości i obsługiwane korekty |
| Dokumenty | Wklejanie treści oraz TXT, MD, CSV, PDF, DOCX i DOC; do 10 plików, 8 MB na plik i 32 MB łącznie; DOC wymaga Worda, skany OCR |
| Słownik offline | 114 215 haseł, 125 720 wpisów, 1 437 842 powiązania form odmiany; znaczenia, przykłady i źródła |
| Pamięć | Notatki, źródła oraz nowy inkubator: trwałość między rozmowami, tematy, powiązania, konflikty, cofanie, pauza i eksport |
| Matematyka | Działania, równania, pochodne, całki, macierze i wykresy przez narzędzia obliczeniowe |
| Logika | Dziewięć bramek T/F/U, nawiasy, symbole i kroki; formalne wyrażenia w poleceniach PL/EN |
| Sygnały | Serie liczbowe JSON, wykresy i uczona ocena wybranych trendów, anomalii i okresowości |
| Obsługa | PL/EN, Enter wysyła, Shift+Enter dodaje wiersz, nowa rozmowa, pomoc i przykłady |

## Podłączone lokalnie — odczyt F/U

**Nowy odczyt działa w panelu AI-SI-TSI** przy pytaniach o odrzuconą albo niepotwierdzoną informację w wybranym temacie inkubatora. Kontrole zgodności: **11/11**, uruchomiony panel przez HTTP: **6/6**. PL/EN; w szczegółach odpowiedzi pojawia się `truth_readout`. Wyłączenie: **COFNIJ_ODCZYT_FU.bat**; ponowne włączenie: **WLACZ_ODCZYT_FU.bat**. [Zakres, pomiary i cofnięcie](docs/WDROZENIE_ODCZYTU_FU_2026-10-25.md).

Główny rdzeń, pełna rozmowa, MUZ, walidator i portable zachowują dotychczasową konfigurację. Podłączono tylko sprawdzoną obsługę F/U.

## Trwała pamięć

**Podłączony do lokalnej aplikacji TSI.** Panel „Inkubator pamięci” znajduje się na istniejącej stronie. Nowa rozmowa zachowuje zapisane informacje. Przy sprzeczności lub niejasnym temacie TSI prosi o wybór kontekstu. Można zamknąć temat, cofnąć jedną lub dwie decyzje oraz zatrzymać korzystanie z pamięci.

Bufor rośnie zależnie od wejścia i liczby zapisów: **10 000 → 200 000 wpisów**, **64 MiB → 1 GiB treści**. To limity treści, nie rozmiar całej bazy. Zapis nie uruchamia treningu wag.

Sprawdziany: **18/18** pamięci, **20/20** integracji HTTP, **15/15** przywołań trzech informacji po nowej rozmowie. Mediana pełnej odpowiedzi: **208 ms wcześniej, 215 ms po zmianie** — 15 próbek na wariant. Sam odczyt bazy 50 000 wpisów: **1066 → 14 ms**, 60 zapytań. [Zakres i wyniki](docs/INKUBATOR_PAMIECI_TSI_2026-10-24.md).

## Pamięć i rozwijana rozmowa

W wariancie badawczym połączono trwały zapis T/F/U z rekurencyjną pamięcią roboczą. Kontrole pamięci: **24/24**; ostatni sprawdzian pełnych odpowiedzi tego połączenia: **4/8**. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**. Pełnego połączenia rekurencyjnego nie ustawiono jako domyślnego w panelu. [Zakres i odpowiedzi](docs/PAMIEC_HYBRYDOWA_TSI_2026-10-24.md).

W rozwijanym generatorze dobór kontekstu uwzględnia dostępne miejsce zamiast sztywnego limitu dwóch faktów i czterech tur. Przebieg wcześniejszych treningów znajduje się w [historii](HISTORIA_TSI.md).

## Ostatni trening — 25 października

Odczyt F/U przy podanym źródle: **1/4 → 4/4**; nowe źródła: **8/8**. Wcześniejsze kontrole bez treści źródła: **15/15 → 15/15**. Trenowano warstwę odczytu na 148 przykładach z powtórkami. Wytrenowane wagi wykorzystuje teraz ograniczony odczyt F/U w lokalnym panelu; pełnej rozmowy i portable nie podmieniono. [Pełne wyniki i odpowiedzi](docs/TRENING_ODCZYTU_TSI_2026-10-25.md).

## Model i rozmiar

| Zakres | Aktualny stan |
|---|---|
| Wagi działającej aplikacji | Zachowane przy podłączeniu pamięci; inkubator nie zastępuje modelu |
| Rozwijany wspólny model językowy | Dwa enkodery z H512 oraz dekoder transformera; **23 542 811 parametrów**, około **94,67 MB** zapisu wag |
| Model odczytu F/U i badań nad rozmową | **23 843 739 parametrów**, **95,874 MB** zapisu wag; w panelu używany tylko do obsługiwanych F/U |
| Kontrola nowego połączenia | Pamięć **24/24**; pełne odpowiedzi po treningu odczytu **4/8** |
| Katalog aplikacji z kodem i danymi | Ostatni pomiar z 23 października: **1 989,89 MB**, bez środowiska Pythona, treningów i kopii |

Rozmiar modelu nie jest rozmiarem kompletnego portable. Dużego modelu badawczego nie ustawiono jako głównego generatora panelu ani portable. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**. Internetowa pętla uczenia wag pozostaje wyłączona. [Dokładny wcześniejszy pomiar katalogu](docs/POMIAR_TSI_2026-10-23.json).

**Rozmowę i nową pamięć podłączono również do lokalnych MUZ i walidatora.** Każda aplikacja ma własne zapisy. Kontrole połączeń: **10/10**; działające aplikacje przez HTTP: **12/12**. Osobne portable nie zostały w tym etapie przebudowane. W walidatorze rozwijana będzie rola nauczyciela: wskazówki, kontrola kroków i ćwiczenia dobierane do błędów.

## Jak korzystać

Uruchom **URUCHOM_TSI.bat** i otwórz `http://127.0.0.1:8791/`. Aplikację zatrzymuje **ZATRZYMAJ_TSI.bat**.

| Przykład | Zastosowanie |
|---|---|
| `Przeczytaj: Anna daje książkę Markowi.` | Dodanie źródła |
| `Komu Anna daje książkę?` | Pytanie do źródła |
| `słownik: państwo` | Znaczenia offline |
| `Wyznacz pochodną i całkę: x^2` | Matematyka |
| `logika: NOT (T AND U) OR F` | Logika z krokami |
| `Ola ma niebieski plecak.` → nowa rozmowa → `Jaki kolor ma plecak Oli?` | Przywołanie zachowanego źródła |

## Podgląd

Poniższe zrzuty z 20 października pokazują wcześniejszy układ panelu, sprzed dodania inkubatora.

![Rozmowa TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

[Historia prac](HISTORIA_TSI.md) · [Pamięć i testy](docs/INKUBATOR_PAMIECI_TSI_2026-10-24.md) · [Walidator](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)
