# Kontekst i powtórki TSI — 24 października 2026

Prace dotyczą rozwijanego wspólnego modelu **23 542 811 parametrów**. Wagi domyślnego panelu, MUZ i walidatora pozostawiono bez zmian.

## Sprawdzenie bufora

W dwóch krótkich próbach informacja użytkownika docierała w całości do obu enkoderów i generatora. Skrót zawartości pamięci i maski uwagi był identyczny od pierwszego do ostatniego kroku odpowiedzi. Model mimo tego odpowiadał „Nie znam” lub „Proszę bardzo”. W tych przypadkach problemem było wykorzystanie dostępnych danych, a nie usunięcie bufora.

Znaleziono osobne ograniczenie składania kontekstu: stałe dwa ostatnie fakty i cztery tury. Starszy fakt o Oli znikał po dopisaniu dwóch niezwiązanych informacji. W rozwijanym wariancie zastąpiono te limity doborem całych wpisów do rzeczywistego budżetu tokenów. Gdy brakuje miejsca, uwzględniana jest zbieżność słów pytania i wpisu; pominięcia są jawnie liczone. Nie usuwa to zapisu źródeł. Za długie bieżące pytanie z dowodem wywołuje informację o przekroczeniu pojemności, zamiast obcinać je po cichu.

Próby potwierdziły zachowanie trzech faktów i siedmiu tur, wybór starszego pasującego faktu przy mniejszym budżecie oraz niezmienność zapisu rozmowy.

Trwały inkubator aplikacji nie ma automatycznego terminu wygasania wpisów. Osiągnięcie pojemności nie nadpisuje starszych zapisów. Ten mechanizm jest odrębny od okna kontekstu rozwijanego modelu.

## Trening wag

Ćwiczenia: **36** przykładów pytań o informacje użytkownika, z historią rozmowy i bez rozbudowanej historii. Uczą się oba enkodery, ich pamięć H512 i cały generator. Zachowano sześć jawnych macierzy reguł. Zestaw kontrolny zawiera **56** wcześniejszych odpowiedzi, w tym godziny, kolory i podstawową rozmowę.

Pierwszy przebieg poprawiał nowe ćwiczenia kosztem części wcześniejszych odpowiedzi; jego zmian nie przyjęto. W drugim przeplatano nowe ćwiczenia z powtórkami, częściej wracając do utraconych odpowiedzi. Mniejszy krok i powtórki pozwoliły zachować:

| Kontrola | Wynik |
|---|---:|
| Wcześniejsze odpowiedzi | **56/56** |
| Nowe ćwiczenia — przed | **0/36** |
| Nowe ćwiczenia — po | **6/36** |
| Osobne pytania i imiona — przed | **0/8** |
| Osobne pytania i imiona — po | **1/8** |
| Niezależne sprawdzenie działającego modułu T/F/U | **82/82** |

Wynik generatora liczy pełne dopasowanie do wzorcowej odpowiedzi wraz z zakończeniem. Oddzielne pytania nie wchodziły do funkcji straty ani wyboru kroku treningu. Są próbą porównawczą; nie określają ogólnej sprawności językowej.

Sprzęt tego przebiegu: **CPU**, bez dostępnego CUDA. Internetowa nauka wag pozostaje wyłączona. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**.


## Kolejna hipoteza — historyczna koncepcja pamięci TIMDR

Źródłem jest dawny opis, a nie aktualny formalizm: [historia README, sekcja 4](https://github.com/jbackk-lang/GIA-TIMDR/blob/main/HISTORIA_README.md), [Model AG, sekcja 9 „TIMDR a pamięć AI”](https://github.com/jbackk-lang/GIA-TIMDR/blob/main/docs/theory/Model_AG_AI_Theory.md) oraz historyczny `TIMTopoGeneratorDoubleMem` w archiwum koncepcji.

Opis wiąże pamięć ze stabilizacją reprezentacji, czasowym zapisem zmiany i podtrzymywanym obiegiem. Dawny kod zawiera dwie sprzężone, rekurencyjne pamięci h1 i h2. Następna próba ma sprawdzić podtrzymanie śladu i stabilny odczyt podczas generowania odpowiedzi. Nie jest to wdrożona zmiana architektury w tym przebiegu treningowym.


Kontrola zapisanych wag potwierdziła zmiany w obu enkoderach (po 71 tensorów), obu pamięciach H512 (po 8) i generatorze (246), przy niezmienionych sześciu macierzach reguł. Plik kandydata: **97,80 MB**; liczba parametrów pozostaje **23 542 811**.


## PC_TIMDR / KHIPU i zapis T/F/U

Po wskazaniu PC_TIMDR sprawdzono historyczny `TransitionMemory`, adresowanie 252 stanów i cztery zarezerwowane kody sterujące oraz rozwinięcie w KHIPU (`Rope256`, `Rope48`, `Node256`). Obecny `Node256` jest strukturą Pythona, a nie gotowym, fizycznie spakowanym słowem 256-bitowym.

Przygotowano osobny wariant badawczy słowa 16-bitowego: 8-bitowy adres stanu i cztery dwubitowe statusy ról — wykonawcy, relacji, obiektu i wartości. Kody: U=00, F=01, T=10; 11 zarezerwowano, a nie potraktowano jako czwartą wartość logiczną. Adresy RESET/NULL/OVER_TAU/OVER_DELTA_S zachowano i rozdzielono od faktów. Wartości liczbowe, treść źródła i powiązania encji pozostają w osobnym zapisie, bez kwantyzacji.

Test objął całe 65 536 słów: 20 412 poprawnych kombinacji danych, cztery niezmienione kody sterujące i odrzucenie 45 120 pozostałych zapisów. To sprawdzenie kodowania; wariant nie jest podłączony do działającego TSI i nie zmierzono jego wpływu na rozmowę.

Osobny szkic pamięci dwóch sprzężonych śladów przeszedł 32 sekwencje sprawdzające odczyt bez wygaszania, izolację nazwanych tematów oraz stałą migawkę przez czas odpowiedzi. Pozostaje wariantem badawczym; nie zastępuje pamięci aplikacji.
