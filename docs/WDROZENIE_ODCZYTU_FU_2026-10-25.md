# Podłączenie odczytu F/U do lokalnego panelu — 25 października 2026

**Wdrożone lokalnie w panelu AI-SI-TSI.** Nowy odczyt wykorzystuje ocenione wagi z ostatniego treningu. Obsługuje pytania o odrzuconą albo nierozstrzygniętą informację w wybranym temacie inkubatora. Główny rdzeń i pozostałe zadania nadal korzystają z dotychczasowych modułów.

## Kiedy działa

1. W inkubatorze wybierz temat pamięci.
2. Gdy informacja zostanie odrzucona lub pojawi się nierozstrzygnięty zapis, zapytaj o nią w rozmowie.
3. TSI generuje komunikat F albo U nowym modułem. Szczegóły odpowiedzi zawierają pole `truth_readout` z `used: true` i identyfikatorem wag.

Pytanie musi odnosić się do wybranego źródła. Moduł nie zastępuje kalkulatora, słownika, narzędzi dokumentowych ani obsługi potwierdzonych faktów. Tekst odrzuconego źródła nie jest przekazywany do generatora jako fakt. Odpowiedź modelu nie zapisuje się automatycznie jako nowa wiedza.

## Co uruchomiono

Odczyt zależy od reprezentacji własnego dekodera, dlatego działa w osobnym, lokalnym procesie z wytrenowanym modelem. Wagi są ładowane przy pierwszym odpowiednim pytaniu i pozostają w pamięci do wyłączenia procesu. Użycie GPU jest automatyczne, jeśli dostępny jest CUDA; w wykonanych próbach użyto CPU.

Pakiet lokalny zajmuje **96.58 MB**; plik wag **95,874 MB**. Zawiera kod potrzebny do odczytu i jego wagi. Repozytorium GitHub nadal zawiera tylko dokumentację.

Po wygenerowaniu tekstu sprawdzany jest jego status oraz zakończenie. Nieprawidłowy wynik lub niedostępny proces zachowuje poprzednią odpowiedź aplikacji; nie zastępuje się go udawaną odpowiedzią neuronową. Interfejs angielski tłumaczy dwa obsługiwane komunikaty.

## Sprawdzenie połączenia

Kontrole przygotowanej wersji koordynatora: **11/11**. Panel uruchomiony po zmianie, przez HTTP: **6/6**. Potwierdzono włączenie modułu, F i U po polsku i angielsku oraz poprawny wynik dodawania 2 do 8. Sprawdzono również powrót do wcześniejszego toru po wyłączeniu modułu, zachowanie potwierdzonego źródła, zatwierdzonej korekty i pytania o inną osobę.

| Próba w uruchomionym panelu | Odpowiedź |
|---|---|
| F · polski | Ta informacja została odrzucona. |
| F · angielski | This information has been rejected. |
| U · polski | Potrzebuję potwierdzenia tej informacji. |
| U · angielski | I need confirmation of this information. |
| Dodaj 2 do 8 | 10 |

Pierwsze użycie w wykonanych próbach na CPU trwało około 19–37 sekund razem z ładowaniem wag, kolejne odpowiedzi około 4–12 sekund. To niewielka liczba próbek pełnych żądań, a nie pomiar gwarantowanego czasu odpowiedzi. Przyspieszenia nie potwierdzono.

## Wyłączenie i przywrócenie

W głównym katalogu lokalnej aplikacji są dwa pliki:

- **COFNIJ_ODCZYT_FU.bat** — wyłącza nowy odczyt przy kolejnym pytaniu, bez restartowania panelu.
- **WLACZ_ODCZYT_FU.bat** — ponownie go włącza.

Poprzednie pliki zachowano w `TSI/backups/before-truth-readout-…`. Rozmowy i zapisy pamięci użytkownika pozostawiono. Sprawdziany HTTP używały osobnych profili testowych.

## Zakres pozostający do rozwinięcia

Pełnego modelu swobodnej rozmowy ani rekurencyjnego połączenia pamięci nie przełączono na tor domyślny. MUZ, walidator i osobne portable nie zostały w tym wdrożeniu przełączone ani przebudowane. Wynik ostatniego badawczego sprawdzianu pełnego połączenia pamięci pozostaje 4/8. Swobodna rozmowa nie osiągnęła wymaganego poziomu.
