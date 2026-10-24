# Pamięć trwała T/F/U i rekurencyjna pamięć robocza — 24 października 2026

## Co połączono

Istniejący inkubator SQLite pozostaje jedynym trwałym magazynem. Most odczytuje wybrany temat i profil, dołącza pakowane statusy T/F/U, a następnie zasila rekurencyjną pamięć roboczą reprezentacjami potwierdzonych źródeł. Generator korzysta z niezmiennego widoku do końca odpowiedzi. Jego wypowiedzi nie są automatycznie zapisywane jako fakty.

T/F/U opisuje status zapisu, interpretacji i decyzji użytkownika. Trwałość wynika z zapisu na dysku. Rekurencja pracuje na pomocniczych stanach w RAM; przyspieszenia odpowiedzi nie potwierdzono.

## Zasady aktualizacji

- Konflikt lub nowy nierozstrzygnięty zapis blokuje użycie starszej wartości w danym miejscu pamięci.
- Odrzucenie usuwa ślad roboczy; treść odrzuconego źródła nie trafia do generatora jako potwierdzony fakt.
- Zatwierdzona poprawka odtwarza stan z nowej wersji, bez mieszania sprzecznych wartości.
- Powtórka użytkownika może podtrzymać stan; samo pytanie lub odczyt nie zwiększa liczby powtórek.
- Pauza, zamknięcie tematu, cofanie decyzji i czyszczenie pamięci są respektowane przez nowy tor.
- Pamięć robocza ma osobne zakresy profilu, tematu i wersji enkodera. Wyrzucenie starego zakresu z RAM pozostawia zapis na dysku.

Nowy tor badawczy wymaga jawnie wybranego tematu. Nie sprawdzano automatycznego rozpoznawania tematów. Wariant ma konfigurowalne granice: 4096 rekordów widoku tematu, 64 potwierdzone miejsca robocze i 16 zakresów w RAM. Przekroczenie granic widoku wymaga zawężenia tematu; nie ucina źródeł po cichu.

## Sprawdzenie połączenia

Kontrole SQLite, statusów i pamięci roboczej: **24/24**. Sprawdzono ponowne uruchomienie, konflikty, poprawki, odrzucenia, cofanie, izolację tematów i profili, niezmienny widok odpowiedzi, ograniczanie RAM oraz odświeżenie po zmianie enkodera.

Pierwszy przebieg wykrył błąd: wejście statusu wymagało źródła S2 także wtedy, gdy źródło celowo wycofano. Rozdzielono status warstwy wyjściowej od podawania treści źródła. Zachowano dotychczasowy interfejs źródeł.

## Trening i pełne odpowiedzi

Uczono tylko istniejącą warstwę odczytu statusu, na 52 przykładach: 16 z treścią źródła wyłączoną oraz 36 powtórek poprzedniego interfejsu F/U. Enkodery, pozostały generator i sześć macierzy reguł zachowano. Liczba parametrów pozostała **23,843,739**, plik wag **95.874 MB**. Potwierdzony T i brak statusu nadal omijają tę warstwę; ich wagi pozostały identyczne.

Pod prawidłowym początkiem odpowiedzi: **36/52 → 52/52**. Oddzielne, pełne odpowiedzi F/U dla trzech imion: **6/9**. Wyniku przy podanym początku nie traktujemy jako swobodnej rozmowy.

| Próba całego połączenia | Przed treningiem odczytu | Po treningu odczytu |
|---|---:|---:|
| Z pamięcią roboczą | 2/8 | 4/8 |
| Z samą pamięcią trwałą | 2/8 | 4/8 |

W każdym przebiegu sprawdzono dobór i wycofywanie źródeł w **16/16** odpowiedziach obu wariantów. Osobny sprawdzian poprzedniego interfejsu, z nadal podanym źródłem F/U: **1/4** poprawnych pełnych odpowiedzi.

## Rzeczywiste odpowiedzi nowego połączenia

| Przypadek | Przed treningiem | Po treningu |
|---|---|---|
| known_source | Plecak Ewy jest czerwony. | Plecak Ewy jest czerwony. |
| user_repetition | Plecak Ewy jest czerwony. | Plecak Ewy jest czerwony. |
| approved_correction | Plecak Eus jest niebieski. | Plecak Eus jest niebieski. |
| after_other_topic | Plecak Eus jest niebieski. | Plecak Eus jest niebieski. |
| rejected_source | Potrzebuję potwierdzenia tej informacona. | Ta informacja została odrzucona. |
| unknown_source | Potrzebuję potwierdzenia tej informacja została odrzucja została odrzucja została odrzucona. | Potrzebuję potwierdzenia tej informacji. |
| new_name | Plecak Jana jest czerwony. | Plecak Jana jest czerwony. |
| restart | Plecak Jana jest czerwony. | Plecak Jana jest czerwony. |

## Oddzielne pytania F/U

| Imię | Status wartości / pozostałych ról | Odpowiedź |
|---|---|---|
| Ewy | F / T | Ta informacja została odrzucona. |
| Ewy | U / T | Potrzebuję potwierdzenia tej informacji. |
| Ewy | U / U | Potrzebuję potwierdzenia tej informacji. |
| Kuby | F / T | Ta informacja została odrzucona. |
| Kuby | U / T | Potrzebuję potwierdzenia tej informacji. |
| Kuby | U / U | Potrzebuję potwierdzenia tej informacji. |
| Heleny | F / T | Ta informacji. |
| Heleny | U / T | Potrzebuję potwierdzenia tej informacja została odrzucja została odrzucja została odrzucona. |
| Heleny | U / U | Potrzebuję potwierdzenia tej informacja została odrzucja została odrzucja została odrzucona. |

**Wniosek:** połączono trwały zapis ze stanem roboczym i poprawiono odczyt F/U w części prób. Pomyłki dotyczące osób i odmiany pozostają. W tym zestawie sama rekurencja nie podniosła poprawności ponad wariant z pamięcią trwałą. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**.

Nowe połączenie oraz wytrenowany odczyt pozostają w wariancie badawczym. Panel, MUZ, walidator i portable zachowują dotychczasowe wagi i obsługę pamięci. Publikacja zawiera dokumentację, bez kodu i wag.


## Kolejne powtórki odczytu F/U — 24 października

Kontynuowano trening tej samej warstwy odczytu na **84 przykładach**, z zachowaniem wcześniejszych ćwiczeń i dodaniem różnych imion oraz pytań. Treści testowych dla Ewy, Kuby, Heleny, Ireny i Leona nie dodano do treningu. Pierwsze trzy imiona to powtórzona kontrola, ostatnie dwa to nowe próby. Wagi enkoderów, pozostałego generatora i macierzy reguł pozostały identyczne.

Pełne, samodzielne odpowiedzi:

- Powtórzona kontrola: **6/9 → 9/9**.
- Nowe imiona: **6/6**.
- Poprzedni interfejs ze źródłem: **1/4 → 1/4**.

Kandydat zachowany do dalszych badań bez spadku liczby poprawnych odpowiedzi w tych kontrolach. Wyniki dotyczą odpowiedzi na statusy F/U. Ostatni sprawdzian całego połączenia pamięci pozostaje **4/8**; nie powtórzono go w tej krótkiej turze. Panel i portable pozostały bez zmian.

| Imię | Status wartości / pozostałych ról | Pełna odpowiedź |
|---|---|---|
| Ewy | F / T | Ta informacja została odrzucona. |
| Ewy | U / T | Potrzebuję potwierdzenia tej informacji. |
| Ewy | U / U | Potrzebuję potwierdzenia tej informacji. |
| Kuby | F / T | Ta informacja została odrzucona. |
| Kuby | U / T | Potrzebuję potwierdzenia tej informacji. |
| Kuby | U / U | Potrzebuję potwierdzenia tej informacji. |
| Heleny | F / T | Ta informacja została odrzucona. |
| Heleny | U / T | Potrzebuję potwierdzenia tej informacji. |
| Heleny | U / U | Potrzebuję potwierdzenia tej informacji. |
| Ireny | F / T | Ta informacja została odrzucona. |
| Ireny | U / T | Potrzebuję potwierdzenia tej informacji. |
| Ireny | U / U | Potrzebuję potwierdzenia tej informacji. |
| Leona | F / T | Ta informacja została odrzucona. |
| Leona | U / T | Potrzebuję potwierdzenia tej informacji. |
| Leona | U / U | Potrzebuję potwierdzenia tej informacji. |
