# AI-SI-TSI — lokalny asystent TSI

**Stan: 25 października 2026.** TSI łączy własne modele, macierze językowe, pamięć źródeł i narzędzia obliczeniowe. Pracuje lokalnie. Repozytorium zawiera dokumentację; kod, wagi i dokumenty użytkownika pozostają lokalnie.

## Co obecnie potrafi

| Obszar | Możliwości |
|---|---|
| Tekst i rozmowa | Pytania do podanej treści, skróty, listy, wiadomości i obsługiwane korekty |
| Dokumenty | Wklejanie treści oraz TXT, MD, CSV, PDF, DOCX i DOC; do 10 plików, 8 MB na plik i 32 MB łącznie; DOC wymaga Worda, skany OCR |
| Słownik offline | 114 215 haseł, 172 772 znaczenia, 1 437 842 powiązania form; ścieżki znaczeń, przykłady i źródła |
| Pamięć | Notatki, źródła oraz nowy inkubator: trwałość między rozmowami, tematy, powiązania, konflikty, cofanie, pauza i eksport |
| Matematyka | Działania, równania, pochodne, całki, macierze i wykresy przez narzędzia obliczeniowe |
| Logika | Dziewięć bramek T/F/U, nawiasy, symbole i kroki; formalne wyrażenia w poleceniach PL/EN |
| Sygnały | Serie liczbowe JSON, wykresy i uczona ocena wybranych trendów, anomalii i okresowości |
| Obsługa | PL/EN, Enter wysyła, Shift+Enter dodaje wiersz, nowa rozmowa, pomoc i przykłady |

## Aktualna decyzja — odmowa przed zgadywaniem

**Zatrzymano trening gotowych odpowiedzi i wyłączono nowy odczyt F/U w panelu.** Przywrócono wcześniejsze komunikaty o brakujących danych. Wagi i kopie zachowano. Problem dotyczy powiązania znaczeń słów, tematu i szukanej właściwości; samo rozpoznanie rodzaju pytania oraz poprawne tablice T/F/U tego nie rozwiązują.

Dalsza praca: odczyt słownika i znaczeń, przypisanie osoby i tematu, sprawdzenie danych oraz konkretne doprecyzowanie, gdy czegoś brakuje. Nowego treningu samych docelowych odpowiedzi nie wznowiono. [Wyniki audytu i cofnięcia](docs/AUDYT_ODMOW_I_ZNACZEN_TSI_2026-10-25.md).

## Słowa, znaczenia i lekcje tematyczne

**Wdrożono w lokalnym TSI:** sieć słownika z **114 215 hasłami**, **172 772 oddzielnymi znaczeniami**, **733 529 relacjami** i **60 730 powiązaniami tematycznymi**. Formy odmiany prowadzą do hasła, znaczenia i źródła. Relacje bez przypisanego znaczenia pozostają oddzielne. Baza zawiera również nazwy własne i imiona.

TSI przyjmuje wyjaśnienie nieznanego słowa w rozmowie i zachowuje je dla danego profilu oraz tematu. Przy wieloznaczności przedstawia znaczenia do wyboru. Odpowiedź „nie wiem” pozostawia znaczenie nierozstrzygnięte. Schowek słów pozwala sprawdzić źródło, wybrać znaczenie i cofnąć zmianę.

Gotowe zaplecze lekcji zapisuje temat, materiał, źródło, słowa i skrót z zachowanych fragmentów. Sprawdzono pobranie materiału o trójkącie. **Panel lekcji pozostaje do przygotowania**; stara internetowa pętla treningu wag nie została wznowiona.

Testy: **13/13** przebiegów wyjaśniania słów, **10/10** lekcji oraz **14/14** kontroli działającej aplikacji. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**. [Przebiegi i zakres sprawdzeń](docs/SLOWNIK_I_LEKCJE_TSI_2026-10-25.md).

### Pytania do słownika bez wklejania lekcji

Nowe TSI wyszukuje fragmenty przypisane do znaczeń słownikowych także dla krótkich pytań. „Suma kątów w trójkącie?”, „Jaka jest suma kątów w trójkącie?” i „Ile wynosi suma kątów wewnętrznych trójkąta?” zwracają cytat o **180° dla trójkąta płaskiego**. Odpowiedź zachowuje pochodzenie i warunki z materiału. Działają też formy „Czym jest…”, „Wyjaśnij…” i „Podaj definicję…”.

Sprawdzono **12/12** przypadków odczytu i **10/10** kontroli aplikacji. W badanym zestawie iloczyn, inna figura i trójkąt sferyczny nie otrzymały cytatu o sumie w trójkącie płaskim. Wagi oraz panel walidatora pozostały bez zmian; tę aktualizację wdrożono tylko w ogólnym TSI.

### Pytania do materiału lekcji

Podłączono odczyt relacji **obiekt → właściwość → liczba**. Z materiału „Trójkąt ma trzy boki. Kwadrat ma cztery boki.” TSI odpowiada odpowiednio „trzy boki” i „cztery boki”, z odnośnikiem do zapisanego źródła. Przy innych pytaniach korzysta z istniejącego odczytu ról albo wskazuje powiązany fragment. Brak właściwości oraz sprzeczne wartości wymagają doprecyzowania.

Sprawdzono **23/23** warianty relacji, **12/12** pytań do lekcji i **10/10** kontroli działającej aplikacji. Obsługa jest podłączona do API lekcji i rozmowy z identyfikatorem wybranej lekcji; wybór lekcji w panelu pozostaje do wykonania. Wagi nie były trenowane. [Zakres i przykłady](docs/PYTANIA_DO_LEKCJI_TSI_2026-10-25.md).

## Trwała pamięć

**Podłączony do lokalnej aplikacji TSI.** Panel „Inkubator pamięci” znajduje się na istniejącej stronie. Nowa rozmowa zachowuje zapisane informacje. Przy sprzeczności lub niejasnym temacie TSI prosi o wybór kontekstu. Można zamknąć temat, cofnąć jedną lub dwie decyzje oraz zatrzymać korzystanie z pamięci.

Bufor rośnie zależnie od wejścia i liczby zapisów: **10 000 → 200 000 wpisów**, **64 MiB → 1 GiB treści**. To limity treści, nie rozmiar całej bazy. Zapis nie uruchamia treningu wag.

Sprawdziany: **18/18** pamięci, **20/20** integracji HTTP, **15/15** przywołań trzech informacji po nowej rozmowie. Mediana pełnej odpowiedzi: **208 ms wcześniej, 215 ms po zmianie** — 15 próbek na wariant. Sam odczyt bazy 50 000 wpisów: **1066 → 14 ms**, 60 zapytań. [Zakres i wyniki](docs/INKUBATOR_PAMIECI_TSI_2026-10-24.md).

## Pamięć i rozwijana rozmowa

W wariancie badawczym połączono trwały zapis T/F/U z rekurencyjną pamięcią roboczą. Kontrole pamięci: **24/24**; ostatni sprawdzian pełnych odpowiedzi tego połączenia: **4/8**. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**. Pełnego połączenia rekurencyjnego nie ustawiono jako domyślnego w panelu. [Zakres i odpowiedzi](docs/PAMIEC_HYBRYDOWA_TSI_2026-10-24.md).

W rozwijanym generatorze dobór kontekstu uwzględnia dostępne miejsce zamiast sztywnego limitu dwóch faktów i czterech tur. Przebieg wcześniejszych treningów znajduje się w [historii](HISTORIA_TSI.md).

## Model i rozmiar

| Zakres | Aktualny stan |
|---|---|
| Wagi działającej aplikacji | Zachowane przy podłączeniu pamięci; inkubator nie zastępuje modelu |
| Rozwijany wspólny model językowy | Dwa enkodery z H512 oraz dekoder transformera; **23 542 811 parametrów**, około **94,67 MB** zapisu wag |
| Model odczytu F/U i badań nad rozmową | **23 843 739 parametrów**, **95,874 MB** zapisu wag; zachowany lokalnie; nowy odczyt w panelu wyłączony |
| Kontrola nowego połączenia | Pamięć **24/24**; pełne odpowiedzi po treningu odczytu **4/8** |
| Katalog aplikacji z kodem i danymi | Pomiar z 25 października: **2 239,85 MB**, bez środowiska Pythona, zapisów użytkownika, treningów i kopii |

Rozmiar modelu nie jest rozmiarem kompletnego portable. Dużego modelu badawczego nie ustawiono jako głównego generatora panelu ani portable. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**. Internetowa pętla uczenia wag pozostaje wyłączona. [Aktualny pomiar katalogu](docs/POMIAR_APLIKACJI_2026-10-25.json).

**Rozmowę i nową pamięć podłączono również do lokalnych MUZ i walidatora.** Każda aplikacja ma własne zapisy. Kontrole połączeń: **10/10**; działające aplikacje przez HTTP: **12/12**. Osobne portable nie zostały w tym etapie przebudowane. W walidatorze rozwijana będzie rola nauczyciela: wskazówki, kontrola kroków i ćwiczenia dobierane do błędów.

## Jak korzystać

Uruchom **URUCHOM_TSI.bat** i otwórz `http://127.0.0.1:8791/`. Aplikację zatrzymuje **ZATRZYMAJ_TSI.bat**.

| Przykład | Zastosowanie |
|---|---|
| `Przeczytaj: Anna daje książkę Markowi.` | Dodanie źródła |
| `Komu Anna daje książkę?` | Pytanie do źródła |
| `słownik: państwo` | Znaczenia offline |
| `Co oznacza zamek?` → `2` | Wybór znaczenia w rozmowie |
| `Co oznacza glipnovar?` → `Glipnovar to lokalna nazwa przycisku startowego.` | Wyjaśnienie nowego słowa |
| `Wyznacz pochodną i całkę: x^2` | Matematyka |
| `logika: NOT (T AND U) OR F` | Logika z krokami |
| `Ola ma niebieski plecak.` → nowa rozmowa → `Jaki kolor ma plecak Oli?` | Przywołanie zachowanego źródła |

## Podgląd

Poniższe zrzuty z 20 października pokazują wcześniejszy układ panelu, sprzed dodania inkubatora.

![Rozmowa TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

[Historia prac](HISTORIA_TSI.md) · [Pamięć i testy](docs/INKUBATOR_PAMIECI_TSI_2026-10-24.md) · [Walidator](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)
