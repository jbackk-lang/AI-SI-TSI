# Sprawdzian modułu sygnałów TSI — 29 października 2026

Badany składnik: **TSI-SIGNALS-TURNING-f3792b5d**, 44 357 parametrów, 131 cech wejściowych, 181 681 bajtów pliku wag. Jest to osobny klasyfikator cech sygnału; wyniki nie są oceną całego rdzenia plan-decoder-8m-3 ani swobodnej rozmowy. Nie zmieniano wag, kalibracji, aplikacji ani progów po obejrzeniu wyników.

## Zakres i protokół

Nowy generator z zapisanym ziarnem przygotował 216 okien kontrolnych: stała, szum, trend, skok, impuls, okresowość, minimum/maksimum oraz dwie mieszanki. Dodano 54 pochodne próby zmiany skali, znaku i przesunięcia: razem 270 prób, nie 270 niezależnych zjawisk. Długości: 64, 128 i 256 próbek. Metoda odniesienia to jawne, proste reguły statystyczne o ustalonych progach, bez dostrajania do wyników. Nie jest reprezentacją najlepszych metod branżowych.

Realne dane: [Numenta NAB — temperatura maszyny](https://github.com/numenta/NAB/blob/master/data/realKnownCause/machine_temperature_system_failure.csv), 22 695 pomiarów. Oceniono 177 kolejnych, niepokrywających się pełnych okien po 128 próbek; ostatnie 39 próbek nie tworzy pełnego okna. 22 okna przecinają cztery [przedziały oznaczone przez NAB](https://github.com/numenta/NAB/blob/master/labels/combined_windows.json). Alarm TSI: skok poziomu lub impuls; osobno liczono wszystkie wskazania i wskazania przy stanie pattern_candidate. Metoda odniesienia: odchylenie w drugiej połowie okna większe niż sześć odpornych skal MAD z pierwszej połowy. Etykieta obejmuje całe okno; nie jest to punktowa ocena czasu wykrycia ani oficjalny wynik NAB.

## Wyniki

| Pomiar | TSI | Proste reguły |
|---|---:|---:|
| Pełny zestaw surowych cech zgodny z etykietą | 253/270 (93,7%) | 119/270 (44,1%) |
| Micro-F1 rozpoznawania cech | 0,953 | 0,605 |
| Nierozstrzygnięte okna kontrolne | 19/270 | brak mechanizmu odmowy |
| Te same wskazania po zmianie jednostek/offsetu/znaku | 52/54 | 54/54 |
| Realne okna: trafione alarmy przy zaakceptowanym odczycie | 3/22 | 5/22 |
| Realne okna: fałszywe alarmy poza oznaczonymi przedziałami | 38/155 | 25/155 |
| Oznaczone przedziały z przynajmniej jednym takim alarmem | 3/4 | 4/4 |
| Nierozstrzygnięte realne okna | 56/177 | brak mechanizmu odmowy |

Dla wszystkich surowych alarmów TSI, również przy odczycie nierozstrzygniętym: 6 trafień, 56 fałszywych alarmów i 16 pominiętych okien dodatnich. Wariant zaakceptowany: 3 trafienia, 38 fałszywych alarmów i 19 pominiętych. Wynik 253/270 dotyczy wskazań cech przed odrzucaniem odczytów niepewnych.

Na tej maszynie mediana pełnego odczytu TSI wyniosła **43,43 ms** dla realnego okna, p95 **159,36 ms**; prosta metoda odpowiednio **0,35 ms** i **4,27 ms**. Szczyt pamięci całego oddzielnego procesu Python: TSI **258,54 MiB**, odniesienie **34,29 MiB**. Obejmuje biblioteki i dane, nie samą sieć. Pojedynczy pomiar inicjalizacji TSI: 29,86 s, bez czasu uruchamiania interpretera i początkowego importu NumPy. Czasów nie należy traktować jako gwarancji dla innych komputerów.

## Wniosek i następny krok

Moduł dobrze rozpoznaje badane kształty, ale **nie osiągnął wymaganego poziomu diagnostyki awarii**. Na tym rzeczywistym szeregu ustępuje prostej metodzie odniesienia. Nie ma podstaw do deklarowania przewagi rynkowej, najmniejszego systemu inteligentnego ani gotowości autonomicznego diagnosty.

Kolejny etap powinien dodać model normalnej pracy konkretnego urządzenia, historię odniesienia, jednostki i kontekst czujnika, a następnie przeprowadzić kalibrację na wydzielonych danych oraz sprawdzian na innych urządzeniach bez dostrajania do testu. Obecna normalizacja okna zachowuje kształt, ale nie wystarcza do wykrywania np. bezwzględnego przekroczenia temperatury. Należy także wyjaśnić dwie rozbieżności po transformacji jednostek. Portal może służyć do dzielenia się zastosowaniami eksperymentalnymi; płatna obietnica diagnostyki wymaga dalszych dowodów.

Zachowano skrypt, protokół, sumy SHA-256 danych i modułu, wejścia oraz surowe odpowiedzi. Bieżący kod i wagi TSI pozostają lokalnie. Dzisiejsza aktualizacja dokumentacji nie przebudowuje ZIP-ów i nie podmienia modeli w MUZ ani Math Validatorze.
