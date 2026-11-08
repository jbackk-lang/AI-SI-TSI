# Notatka badawcza TSI: helisa, Chronoproces i ciągłość informacji

**Data:** 8 listopada 2026  
**Status:** kierunek badawczy / hipotezy do walidacji  
**Powiązany projekt źródłowy:** [GIA-TIMDR](https://github.com/jbackk-lang/GIA-TIMDR)  
**Uwaga:** ta notatka nie opisuje wdrożonej funkcji TSI ani potwierdzonej właściwości samonaprawy.

## 1. Dlaczego temat dotyczy TSI

Rdzeń TSI jest oparty na koncepcji helisy. Z tego powodu badania nad pełnym przejściem trójpętlowym, relacjami fazowymi i rolą czasu nie powinny pozostać wyłącznie w kontekście Helix-Lock. Mogą mieć znaczenie dla sposobu, w jaki TSI reprezentuje, wiąże i zachowuje relacje pomiędzy informacjami.

Nie należy jednak przenosić wyników z modelu demonstracyjnego bezpośrednio do twierdzeń o działaniu rdzenia TSI. Najpierw trzeba ustalić, czy formalizm helikalny używany w TSI ma te same zmienne, operator i warunki brzegowe co badany model GIA-TIMDR.

## 2. Hipoteza robocza

Możliwa zależność:

\[
\text{spójność relacji informacji}
=F(\text{sprzężenie trzech pętli},\text{czas},\text{pełny obieg})
\]

Hipoteza zakłada, że ewolucja całej struktury trójpętlowej może zachować lub odzyskać relacje pomiędzy składowymi po zaburzeniu. „Odzyskanie synchronizacji” nie jest równoznaczne z odzyskaniem pierwotnej treści ani z odtworzeniem utraconych danych.

## 3. Co dotychczas zbadano w GIA-TIMDR

1. **Domknięcie cyklu:** dla kandydującej permutacji cyklicznej \(P^3=I\). Po trzech przejściach wraca kolejność kanałów, ale zaburzenie nie znika.
2. **Operator liniowy:** dla różnicy trajektorii \(\delta\Psi\) zachodzi \(\delta\Psi_{n+1}=J(\Lambda)\delta\Psi_n\). Sama liniowa transformacja nie ma mechanizmu selektywnego usuwania zaburzenia.
3. **Historia czasowa:** chwilowy powrót częstotliwości nominalnej nie musi usuwać skumulowanego przesunięcia fazowego.
4. **Sprzężony model dynamiczny:** w odrębnym, zaproponowanym modelu Kuramoto relacje fazowe mogą relaksować w czasie po zaburzeniu, gdy istnieje sprzężenie. Jest to wynik modelu kandydującego, nie dowód, że taka dynamika wynika z aksjomatów TIMDR lub aktualnego kodu TSI.

Szczegóły i ograniczenia: [protokół walidacji przejść fazowych w GIA-TIMDR](https://github.com/jbackk-lang/GIA-TIMDR/blob/main/docs/theory/PHASE_RECOVERY_VALIDATION_PROTOCOL.md).

## 4. Znaczenie dla architektury TSI — możliwe obszary

- **Reprezentacja relacji:** sprawdzić, czy helikalna struktura TSI koduje relacje, które pozostają stabilne przy zmianie kolejności lub postaci reprezentacji.
- **Pamięć:** sprawdzić, czy historia przejść wnosi informację, której nie ma w pojedynczym stanie wejściowym.
- **Rekonstrukcja:** odróżnić ponowne dopasowanie reprezentacji od odtworzenia źródłowej informacji.
- **Odporność:** badać, czy zaburzenie jednej części struktury może być wykryte dzięki relacjom z pozostałymi częściami.
- **Ciągłość:** zachować identyfikowalny łańcuch pochodzenia danych i korekt, aby adaptacja nie nadpisywała źródła.

Na tym etapie nie proponuje się zmiany wag, checkpointów, pamięci trwałej ani ścieżki odpowiedzi TSI.

## 5. Plan walidacji równoległej

### Etap A — zgodność formalizmów
- Odszukać w kodzie i dokumentacji TSI dokładną definicję helisy, liczby pętli, operatorów, stanu i osi czasu.
- Zmapować zmienne TSI na \(\Psi=(\psi_1,\psi_2,\psi_3)^T\) tylko wtedy, gdy istnieje uzasadniona równoważność.
- Zapisać różnice i nie utożsamiać nazw o podobnym brzmieniu.

### Etap B — testy reprezentacji
- Przygotować znane struktury danych z jawnymi relacjami między trzema kanałami.
- Zaburzać jeden, dwa i wszystkie kanały.
- Mierzyć zachowanie relacji, a nie tylko podobieństwo wyjściowego tekstu.
- Porównać pełną strukturę z kontrolą bez sprzężenia.

### Etap C — rola czasu
- Porównać statyczny odczyt z odczytem uwzględniającym uporządkowaną historię przejść.
- Zmieniać długość i intensywność zaburzenia.
- Sprawdzać, czy historia poprawia rekonstrukcję na danych odłożonych od kalibracji.

### Etap D — test informacji
- Zachować oryginalny payload poza mechanizmem adaptacji.
- Mierzyć integralność skrótem kryptograficznym.
- Oddzielnie oceniać rekonstrukcję treści, odtworzenie relacji i synchronizację.
- Nie uznawać niezmienionego payloadu za dowód jego samonaprawy.

## 6. Kryteria uczciwego wniosku

Wynik pozytywny w koherencji fazowej uprawnia wyłącznie do stwierdzenia, że w danym modelu relacje fazowe wracają do ustalonego progu. Nie dowodzi samonaprawy pamięci, odzyskania danych ani poprawy jakości odpowiedzi TSI.

Wpływ na TSI można uznać dopiero wtedy, gdy:
1. formalna zgodność z helikalnym rdzeniem TSI zostanie wykazana;
2. testy przejdą na odłożonych danych;
3. wynik przewyższy kontrolę bez historii/sprzężenia;
4. nie pogorszą się dotychczasowe testy regresyjne TSI;
5. kod, wagi i pamięć zostaną zmienione dopiero po osobnej decyzji i audycie.

## 7. Zasada projektu

**Helisa jest wspólnym kierunkiem badawczym dla GIA-TIMDR, Helix-Lock i TSI, ale wyniki eksperymentów pozostają przypisane do konkretnego modelu, w którym je uzyskano.**

Tożsamość źródła, relacji i historii musi być zachowana niezależnie od adaptacji reprezentacji.


## 8. Nowy artefakt badawczy w Helix-Lock (2026-11-08)

W Helix-Lock powstała pierwsza implementacja ograniczonej pamięci cech historycznych: `helix_pro/airp_history_memory.py` (`AIRPHistoryMemory`). Przetwarza ona metadane zdarzeń w stałych oknach, wymaga ciągłości sekwencji, emituje deterministyczne podsumowania powiązane z hashem checkpointu i nie zachowuje payloadów ani identyfikatorów. Stan roboczy jest ograniczony do jednego niepełnego okna; gotowe podsumowania przekazywane są do zewnętrznego magazynu.

To **nie jest implementacja TSI** i nie stanowi dowodu samonaprawy helisy. Jest to kontrolowany prototyp pamięci historii, który może posłużyć do sformułowania testów dla TSI po audycie kodu źródłowego. Szczegóły i ograniczenia: [Helix-Lock: CHRONOPROCESS_MEMORY_BOUNDARIES.md](https://github.com/jbackk-lang/Helix-Lock/blob/main/docs/CHRONOPROCESS_MEMORY_BOUNDARIES.md), [moduł](https://github.com/jbackk-lang/Helix-Lock/blob/main/helix_pro/airp_history_memory.py).

CI Helix-Lock dla Python 3.11 i 3.12 przeszło dla testów nowego modułu. Nie należy przenosić tego wyniku na rdzeń TSI bez osobnej integracji i walidacji.
