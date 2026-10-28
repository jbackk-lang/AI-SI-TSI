# AI-SI-TSI — własny model TSI

**Stan: 28 października 2026.** Lokalny model **plan-decoder-8m-3** ma **8 081 032 parametry**. Repozytorium udostępnia dokumentację; bieżący kod, wagi, słowniki i prywatna pamięć pozostają lokalnie.

## Co działa obecnie

- **Odczyt prostych zdań** ze słownika i reguł: podmiot, czynność, dopełnienie, przypadki i zaprzeczenie. Zmieniona kolejność słów nie wyznacza automatycznie ich ról.
- **Odmiana i uzgadnianie form**: osoba, liczba, rodzaj, przypadek, przymiotniki, liczebniki 0–10 i zbiorowe, czas teraźniejszy, przeszły i przyszły oraz tryb przypuszczający. Obsługiwane są wybrane konstrukcje z „się”.
- **Kontekst kilku prostych zdań** i odniesienia podmiotowych zaimków „on/ona”. Niejednoznaczność powoduje doprecyzowanie. Konteksty zapytań są oddzielone.
- **Pytania o treść**: kto, co, kogo, komu, czego, kim, czym. Odpowiedź uwzględnia czas i zaprzeczenie oraz wskazuje zdania źródłowe.
- **Polecenia na kontekście**: wypisywanie potwierdzonych osób i czynności, porównanie dwóch zdań oraz wskazanie sprzecznych faktów. Osoby są rozpoznawane z cech słownikowych i lokalnej bazy znaczeń; nierozstrzygnięta klasyfikacja wymaga doprecyzowania.
- **Chroniona logika dwu- i trójstanowa** oraz wykonanie dynamicznego planu przez dekoder sieciowy, również dla dłuższych odpowiedzi i znaków UTF-8.
- **Kalendarz świąt w istniejącym panelu**: przywrócone połączenie z modułem dat, lista polskich świąt oraz wybrane pytania o daty; obsługa PL/EN.
- **Reguły grzecznościowe PL/EN**: powitania, podziękowania, pożegnania oraz spokojna reakcja na obrażanie. Cytat albo zadanie zawierające przekleństwo nie jest automatycznie blokowane.

Odczyt ról i wybór faktów korzystają z chronionych reguł oraz słowników. Treść przygotowanego planu emituje dekoder sieciowy; jego błędny wynik nie jest zastępowany poprawnym gotowcem. Powitania i pozostałe akty grzecznościowe mają osobną, jawną ścieżkę regułową, zgodnie z ich przeznaczeniem.

**Swobodna rozmowa nie osiągnęła wymaganego poziomu.** Nowe odczyty, pytania i polecenia działają w lokalnym API i CLI. Panel na porcie 8791 otrzymał reguły grzecznościowe i naprawione kierowanie pytań o święta; jego dotychczasowy rdzeń pozostaje bez podmiany. MUZ, walidator i istniejące portable wymagają osobnej aktualizacji.

## Przykłady rzeczywistych wyników

| Dane lub tekst | Zadanie | Wynik |
|---|---|---|
| Książkę czyta Ola. | Odczytaj i ułóż zdanie | **Ola czyta książkę.** |
| Uczeń czyta książkę. On śpi. | Powiąż odniesienie | **Uczeń czyta książkę. On śpi.** |
| Ola czyta książkę. | Kto czyta książkę? | **Ola.** |
| Ewa pomaga dziecku. | Komu pomaga Ewa? | **dziecku.** |
| Ola interesuje się książką. | Czym interesuje się Ola? | **książką.** |
| Ola nie czyta książki. | Czego nie czyta Ola? | **książki.** |
| Ola śpi. Ona czyta książkę. | Wypisz czynności | **Ola śpi. / Ola czyta książkę.** |
| Ola czyta książkę. Ola nie czyta książki. | Wskaż sprzeczności | **Zdania 1 i 2**, wraz z ich treścią |

`Porównaj zdania 1 i 2` pozwala wskazać parę w dłuższym kontekście. Porównanie rozróżnia podmiot, czynność, dopełnienie, czas i zaprzeczenie. Nieobsługiwanych dodatkowych warunków nie pomija się.

## Sprawdzenie obecnej wersji

| Kontrola | Wynik |
|---|---:|
| Odczyt prostych zdań / kontrole niejednoznaczności i braków | **22/22 / 10/10** |
| Automatyczny kontekst kilku zdań / kontrole | **6/6 / 4/4** |
| Pytania o kontekst / kontrole | **18/18 / 13/13** |
| Polecenia na kontekście / kontrole | **9/9 / 7/7** |
| Reguły grzecznościowe w działającym panelu PL/EN | **8/8** |
| Kalendarz świąt w działającym panelu PL/EN | **4/4** |
| Sprawdzone obliczenia panelu: dodawanie, odejmowanie, 2/7 | **4/4** |
| Grupy wyrazów / czasy i tryb | **20/20 / 18/18** |
| Wykonanie nowych planów odpowiedzi / braki i sprzeczne zalecenia | **24/24 / 4/4** |
| Wpisy słownika / próby brzegowe | **32/32 / 20/20** |
| Chroniona logika: dawne polecenia / pełne tablice | **15/15 / 57/57** |
| Testy techniczne | **99/99** |

Wyniki dotyczą wymienionych zakresów. Ostatnie rozszerzenia dodają reguły, połączenia i pełne paradygmaty dwóch haseł; wagi sieci pozostały na zatwierdzonym kroku **2850**.

Kalendarz opiera się na [oficjalnym tekście ustawy o dniach wolnych od pracy](https://api.sejm.gov.pl/eli/acts/DU/2025/296/text.pdf), sprawdzonym 28 października 2026. Matematyka panelu kieruje obliczenia do solvera, z niezależną kontrolą numeryczną. Ułamek 2/7 jest zachowany wraz z przybliżeniem dziesiętnym.

## Słowniki i wielkość

Własna baza odmiany SQLite zawiera **43 847 unikalnych kluczy lematów** i **1 874 187 rekordów form z cechami**. Zachowuje identyfikatory leksemów, homonimię i źródła. Odczyt działa bez importu Morfeusza. Dane SGJP pochodzą z częściowego lokalnego eksportu; zachowano [autorów i licencję BSD-2-Clause](https://morfeusz.sgjp.pl/doc/license/en). To nie jest pełny SGJP.

Klasyfikacja znaczeń korzysta również z istniejącej lokalnej sieci słownikowej, z zachowaniem odnośników do źródeł i znaczeń. Rozbieżne lub brakujące znaczenia nie stają się automatycznie pewną informacją.

| Składnik | Wielkość |
|---|---:|
| Sieć tekstowa: enkoder, dekoder, TIMDR i kanały planu | **8 081 032 parametry** |
| Chroniony moduł operatorów logicznych | **483 parametry** |
| Wagi sieci tekstowej FP32 | **30,83 MiB** |
| Checkpoint z optymalizatorem i stanem losowania | **92,71 MiB** |
| Aktywna własna baza odmiany | **353,25 MiB** |

1 MiB = 1 048 576 bajtów. Python, PyTorch, kod, pozostałe słowniki, dane i kopie bezpieczeństwa są dodatkowymi składnikami instalacji; tabela nie podaje wielkości kompletnego portable.

## Uruchomienie i dalsza praca

Istniejący panel uruchamia **URUCHOM_TSI.bat** w głównym katalogu lokalnej instalacji. Adres: `http://127.0.0.1:8791/`. BAT został odtworzony. Dla nowych funkcji lokalnego modułu dostępne są m.in. zadania CLI `compose_text`, `compose_context`, `ask_context`, `context_command` i `courtesy`.

Następny krok: rozmowa z utrzymaniem tematu, krótkie pytania uzupełniające i doprecyzowanie odniesień. Zaplanowano również nauczyciela AI: odpowiedź ze źródłem → weryfikacja → zatwierdzona wiedza → trening. Dostawca AI nie jest jeszcze podłączony. Zachowywana jest jedna linia wag, optymalizatora i losowania. [Szczegóły aktualnego stanu](docs/STAN_TSI_2026-10-28.md).

## Istniejący panel

Poniższe zrzuty z 20 października przedstawiają wcześniejszy panel, a nie podgląd nowego modułu API.

![Rozmowa TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

## Historia i archiwum

[Historia prac](HISTORIA_TSI.md) · [README sprzed ostatniego rozszerzenia](docs/archiwum/README_przed_poleceniami_2026-10-28.md) · [Uczestnicy](CONTRIBUTORS.md)

[Historyczne paczki starego AI-SI — 8 zestawów ZIP, około 8,3 GB](https://github.com/jbackk-lang/AI-SI-TSI/releases/tag/archive-ai-si-2026-10-18) · [Spis i odtworzenie](docs/PACZKI_STAREGO_AI_SI.md)

[Walidator](https://github.com/jbackk-lang/TSI-math-validator-5) · [MUZ](https://github.com/jbackk-lang/TSI-MUZ)
