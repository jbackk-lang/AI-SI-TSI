# Paczki starego AI-SI

Archiwum dotyczy historycznych źródeł i bazowych modeli z instalacji AI-SI z 18 października 2026. Zestaw przygotowano 27 października. Obecny TSI nie jest częścią paczek.

## Zawartość

| Paczka | Liczba części | Rozmiar części łącznie |
|---|---:|---:|
| AI-SI-legacy-code-2026-10-18 | 1 | 0.001 GB |
| AI-SI-base-Bielik-1.5B-v3.0-Instruct-GGUF | 2 | 1.700 GB |
| AI-SI-base-faster-whisper-small | 1 | 0.486 GB |
| AI-SI-base-opus-mt-pl-en | 1 | 0.222 GB |
| AI-SI-base-Qwen3-4B-Instruct-2507-GGUF | 3 | 2.497 GB |
| AI-SI-base-Qwen3-Embedding-0.6B-GGUF | 1 | 0.639 GB |
| AI-SI-base-Qwen3-Reranker-0.6B | 2 | 1.196 GB |
| AI-SI-base-Qwen3-VL-2B-Instruct-GGUF | 2 | 1.552 GB |

Łącznie około **8,3 GB**. Kod obejmuje 574 wybrane pliki źródłowe i konfiguracyjne. Modele należą do ich autorów; nazwy oraz odnośniki do źródeł są w MODEL-NOTICES.md. Licencje są dołączone w LICENSES.zip.

## Pobieranie i odtworzenie

1. Otwórz [Releases](https://github.com/jbackk-lang/AI-SI-TSI/releases) i odszukaj wydanie **AI-SI — archiwum kodu i modeli 2026-10-18**. Wydanie staje się publiczne po zakończeniu przesyłania wszystkich plików.
2. Pobierz wszystkie części wszystkich ośmiu paczek. Każda część ma nie więcej niż 900 MiB.
3. Do tego samego katalogu pobierz MANIFEST.json, RESTORE.py, RESTORE.bat, archive_split_io.py, README.md, SHA256SUMS.txt, MODEL-NOTICES.md i LICENSES.zip.
4. Przy zainstalowanym Pythonie 3 uruchom RESTORE.bat. Skrypt tworzy nowy katalog **AI-SI-restored** i nie nadpisuje istniejącego katalogu o tej nazwie.

Pliki .zip.001 i .zip.002 nie są osobnymi archiwami; są kolejnymi częściami jednego ZIP-a. Nie zmieniaj ich nazw ani kolejności. Narzędzie RESTORE obsługuje podział bez instalowania dodatkowych bibliotek. Odtworzenie wymaga całego zestawu.

Automatyczne pozycje GitHuba **Source code (zip)** i **Source code (tar.gz)** zawierają migawkę repozytorium dokumentacji. Historyczny kod AI-SI jest w paczce **AI-SI-legacy-code-2026-10-18**, a modele — w osobnych paczkach AI-SI-base.

## Zakres

- Wybrane historyczne źródła AI-SI oraz bazowe modele zewnętrzne.
- Bez obecnego kodu, wag, pamięci i treningów TSI.
- Bez prywatnych baz, dokumentów, historii rozmów, danych dostępowych i historii Git.
- Bez dawnych środowisk wykonawczych i zainstalowanych zależności. Wymagania trzeba odtworzyć osobno z plików projektu.
- Bez prywatnych lub nieprzejrzanych dostrojeń modeli ze starych eksperymentów.

To nie jest kompletna kopia dawnej prywatnej instalacji ani wydanie portable. Usunięcie lokalnych plików dotyczy wyłącznie zawartości objętej opublikowanymi paczkami. Pozostałe prywatne pliki i obecny TSI zostają lokalnie.

[Powrót do aktualnego stanu](../README.md) · [Historia](../HISTORIA_TSI.md)

## Uzupełnienie archiwum — 3 listopada 2026

[Wydanie archiwalne z 3 listopada](https://github.com/jbackk-lang/AI-SI-TSI/releases/tag/archive-cleanup-2026-11-03) zawiera:

| Zestaw | Zawartość |
|---|---|
| AI-SI-legacy-Qwen3-output-2026-10-05 | Stary wariant Qwen3 z odrębnym wyjściem; 3 części ZIP, około 2,82 GB |
| AI-SI-legacy-NLI | Dwie historyczne kopie modelu DeBERTa NLI; 1 część ZIP, około 0,76 GB |
| AI-SI-legacy-public-code | Dawne publiczne pliki aplikacji AI-SI i licencja, bez katalogu data/ |

Pobierz komplet części oraz MANIFEST.json, RESTORE.py i archive_split_io.py. Uruchom `python RESTORE.py NOWY_KATALOG`. Skrypt weryfikuje SHA-256 i odtwarza pliki do nowego katalogu. Dołączono licencje, opis pochodzenia i SHA256SUMS.txt. Poszczególne części .001/.002/.003 nie są niezależnymi ZIP-ami.

To uzupełnienie poprzedniego wydania. Aktualny TSI, jego treningi, pamięć, prywatne bazy i dokumenty nie są publikowane. Lokalne usunięcie dotyczy wyłącznie plików objętych opublikowanym manifestem.
