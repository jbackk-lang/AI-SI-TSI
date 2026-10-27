# AI-SI-TSI — własny model TSI i lokalny asystent

**Stan: 27 października 2026.** Rozwijamy własny rdzeń TSI oraz jego współpracę z aplikacjami. Kod, wagi i prywatna pamięć **obecnego TSI pozostają lokalnie**. Publiczne paczki dotyczą wyłącznie **starego AI-SI i używanych w nim modeli zewnętrznych**.

## Aktualny stan TSI

| Obszar | Potwierdzony stan |
|---|---|
| Nowy rdzeń | **17 982 624 parametry**; enkoder inspirowany TIMDR i dekoder Transformer |
| Odczyt i podstawy logiki | **120/120** zadań oraz **45/45** oddzielnych zapisów: odczyt T/F/U i dwustanowe BUF, NOT, AND, OR |
| Sposób pomiaru | Odpowiedzi samej sieci, przed korektą przez tablicę reguł |
| Rozmowa | Trwa nauka krótkich polskich zdań i dopytywania o brakujące dane; **swobodna rozmowa nie osiągnęła wymaganego poziomu** |
| Trening | Cała część neuronowa uczy się wspólnie; kolejne bloki kontynuują najnowsze wagi i stan losowania |
| Zachowanie wiedzy | Zweryfikowane wcześniejsze lekcje, kontrolowane zmiany wag i zachowane kopie do odtworzenia |
| Reguły i rachunki | Osobna, stała kontrola formalnej logiki, zbiorów i dokładnej arytmetyki |

Czytnik ujednolica nieistotne odstępy w jawnych poleceniach logicznych, zachowując operator, argumenty i ich kolejność. Zmiana liczby spacji lub zapis w kilku wierszach nie tworzy już innego wejścia do tej części sieci.

**Zaliczony zakres dotyczy nowego rdzenia, nie całej matematyki ani dowolnej rozmowy.** Wagi rozwijane w treningu nie zostały jeszcze wdrożone do MUZ, walidatora ani wcześniejszych paczek portable. Bieżący trening i kopie do odtworzenia są kolejnymi zapisami jednej linii rozwoju modelu.

## Aplikacja lokalna

Dotychczasowy panel zawiera pracę z tekstem i dokumentami, słownik offline, pamięć notatek i źródeł, narzędzia matematyczne oraz analizę wybranych sygnałów. Dostępne są PL/EN, wysyłanie Enterem i nowa rozmowa. To działająca aplikacja z wcześniejszą integracją; trening nowego rdzenia jest prowadzony osobno od jej wdrożenia.

Uruchomienie istniejącej instalacji: **URUCHOM_TSI.bat**, panel `http://127.0.0.1:8791/`. Zatrzymanie: **ZATRZYMAJ_TSI.bat**. Przykładowe polecenia panelu: `Przeczytaj: …`, `Streść: …`, `słownik: państwo`.

## Paczki starego AI-SI

Przygotowano **8 zestawów ZIP, łącznie około 8,3 GB**: historyczne źródła AI-SI oraz bazowe modele Bielik, Qwen, Whisper i OPUS. Są to dawne zależności AI-SI, a nie wagi obecnego TSI.

<!-- AI_SI_ARCHIVE_STATUS -->
**Paczki są opublikowane.** Pobieranie: [archiwum starego AI-SI](https://github.com/jbackk-lang/AI-SI-TSI/releases/tag/archive-ai-si-2026-10-18).
<!-- /AI_SI_ARCHIVE_STATUS -->

- Każda paczka ma części do **900 MiB** (około 944 MB): `.zip.001`, `.zip.002` itd.
- Do odtworzenia całego archiwum pobierz wszystkie części wszystkich paczek oraz `MANIFEST.json`, `RESTORE.py`, `RESTORE.bat` i `archive_split_io.py` do jednego katalogu. Uruchom **RESTORE.bat**; wymagany jest Python 3.
- `SHA256SUMS.txt` zawiera sumy części, a `MODEL-NOTICES.md` i `LICENSES.zip` — pochodzenie i licencje modeli.
- Publikacja nie obejmuje obecnego TSI, prywatnych baz, dokumentów ani historii rozmów. To **archiwum historyczne**, nie gotowy portable i nie aktualna wersja aplikacji.

[Dokładny spis paczek i instrukcja](docs/PACZKI_STAREGO_AI_SI.md).

## Rozmiar obecnego rdzenia

MB = 1 000 000 bajtów.

| Składnik | Rozmiar |
|---|---:|
| Parametry nowego rdzenia w FP32 | około **71,93 MB** |
| Plik wag z konfiguracją i metadanymi | około **72 MB** |

Pełna instalacja zajmuje więcej: obejmuje również kod, Pythona, biblioteki, słowniki i dane. Nie przygotowano jeszcze nowego kompletnego portable z tym rdzeniem. Historyczne ZIP-y AI-SI są odrębnym zestawem i nie wyznaczają rozmiaru TSI.

## Podgląd aplikacji

Zrzuty z 20 października przedstawiają istniejący panel, nie nowy rdzeń podczas treningu.

![Rozmowa TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

[Historia prac](HISTORIA_TSI.md) · [Poprzedni README](docs/archiwum/README_przed_aktualizacja_2026-10-27.md) · [Uczestnicy](CONTRIBUTORS.md) · [Walidator](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)
