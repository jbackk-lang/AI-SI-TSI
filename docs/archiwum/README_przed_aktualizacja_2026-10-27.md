# AI-SI-TSI — lokalny asystent TSI

**Stan: 26 października 2026.** Własny model TSI, słownik, pamięć i narzędzia do pracy z tekstem, dokumentami oraz obliczeniami. Repozytorium publikuje dokumentację. Kod, wagi i dokumenty użytkownika pozostają lokalnie.

## Co działa w aplikacji

| Obszar | Możliwości |
|---|---|
| Tekst | Pytania do podanej treści, skróty, listy, wiadomości i obsługiwane korekty |
| Dokumenty | Wklejanie treści, TXT, MD, CSV, PDF, DOCX i DOC; do 10 plików, 8 MB na plik i 32 MB łącznie; DOC wymaga Worda, skany OCR |
| Słownik offline | 114 215 haseł i 172 772 znaczenia, formy odmiany, źródła, pytania do definicji i wyjaśnianie nowych słów |
| Pamięć | Notatki i źródła między rozmowami, tematy, konflikty, cofanie decyzji oraz eksport |
| Matematyka | Działania, równania, pochodne, całki, macierze i wykresy przez narzędzia obliczeniowe |
| Sygnały | Serie liczbowe, wykresy oraz uczona ocena wybranych trendów, anomalii i okresowości |
| Obsługa | PL/EN, Enter wysyła, Shift+Enter dodaje wiersz, nowa rozmowa, pomoc i przykłady |

Uruchomienie lokalnej instalacji: **URUCHOM_TSI.bat**, panel `http://127.0.0.1:8791/`; zatrzymanie: **ZATRZYMAJ_TSI.bat**. Przykłady: `Przeczytaj: …`, `Streść: …`, `słownik: państwo`, `logika: NOT (T AND U) OR F`.

## Aktualny model i nauka

**Połączono oba oryginalne enkodery, obie pamięci H512, czytnik i nowy dekoder z kopiowaniem informacji ze źródła.** Uczą się wspólnie i są zapisywane w jednym pliku modelu. Zachowano słownik odmiany i chronione macierze reguł. Rozmowa jest rozwijana na własnych wagach TSI.

| Ostatnia zakończona kontrola wag roboczych | Wynik |
|---|---:|
| Logika: bramki, negacja, zakres zdania i niewiadome | **55/312**, początkowo 0/312 |
| Zachowane wcześniejsze odczyty | **143/145** |
| Zachowane sprawdzane odpowiedzi językowe | **39/39** |
| Niezmienione chronione macierze reguł | **6/6** |

**Swobodna rozmowa nie osiągnęła wymaganego poziomu.** Wynik wag roboczych nie oznacza ich przyjęcia: najlepsza sprawdzona wersja jest zachowywana osobno. Nowego modelu nie podmieniono w głównym panelu, MUZ, walidatorze ani istniejących portable.

Nauka pracuje lokalnie w kolejnych rundach, ze wznowieniem wag, optymalizatora i kolejki danych. Kontynuacje dodają **3-sekundową pauzę co 10 aktualizacji i dwie powtórki z czterokrotnie mniejszym krokiem**. Poważna regresja lub błąd przerywa ciągłą pracę. Podgląd: **PODGLAD_TRENINGU_TSI.bat**; zatrzymanie całej pętli: **ZATRZYMAJ_CIAGLY_TRENING_TSI.bat**. Zwykła rozmowa nie uruchamia samoczynnie treningu.

Materiał: 25 505 przygotowanych zadań do odczytu tekstów oraz 328 lekcji logiki; osobno 312 kontroli innych sformułowań i 125 odłożonych przypadków logicznych. Pracujemy na CPU. Ostatnie tempo wynosiło około 39–42 s na aktualizację, z dodatkowym czasem ocen i zapisu.

## Logika i zakres czujnika

W lokalnej wersji testowej formalne obliczenia obowiązkowo korzystają z zamrożonego uczonego modułu operatorów TSI. **Tryb dwustanowy: T/F. Tryb trójstanowy: T/F/U, silna logika Kleene’a.** U nie jest automatycznie zamieniane na F.

| Kontrola modułu operatorów | Wynik |
|---|---:|
| Działania trójstanowe | **78/78** |
| Niewiadomy argument — trójstanowo | **132/132** |
| Działania dwustanowe | **36/36** |
| Niewiadomy argument — dwustanowo | **60/60** |

Zadania odwrotne rozróżniają jedną możliwość, kilka możliwości i brak rozwiązania. Przykład: `X AND F = F` dopuszcza {T,F} w dwustanowej oraz {T,F,U} w trójstanowej.

Czujnik podaje **zakres, tryb, wywołane operatory i zgodność wyniku**. Potwierdza formalne obliczenie; sprzeczna zgłoszona wartość jest błędem, a nierozpoznane znaczenie pozostaje niepotwierdzone. Te wyniki modułu operatorów są odrębne od wyników generatora. Kontrola dowolnej swobodnej wypowiedzi nie jest ukończona.

## Wielkość na dysku

MB = 1 000 000 B. Poniższe zakresy częściowo się zawierają.

| Składnik | Rozmiar |
|---|---:|
| Aktualny zintegrowany model | **15 981 366 parametrów** |
| Same parametry przy zapisie FP32 | około **63.93 MB** |
| Sprawdzony wspólny plik modelu, z metadanymi odtworzenia | **124.73 MB** |
| Zapis roboczy z optymalizatorem, ostatni pomiar | **236.89 MB** |
| Aplikacja z kodem i danymi — pomiar z 25 października | **2 239,85 MB**, bez środowiska Pythona, treningów i kopii |

Rozmiar pliku modelu nie jest rozmiarem kompletnego portable. Portable z nową integracją nie zostało w tej rundzie przygotowane. [Zakres pomiaru aplikacji](../POMIAR_APLIKACJI_2026-10-25.json).

## Podgląd panelu

Zrzuty z 20 października pokazują panel aplikacji; nie przedstawiają nowego treningu.

![Rozmowa TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

[Historia i archiwum](../../HISTORIA_TSI.md) · [Uczestnicy projektu](../../CONTRIBUTORS.md) · [Walidator](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)
