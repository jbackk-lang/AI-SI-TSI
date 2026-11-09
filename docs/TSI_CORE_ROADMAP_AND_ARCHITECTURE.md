# TSI — architektura rdzenia i skomasowany plan rozwoju

**Status dokumentu:** nadrzędny, żywy plan konstrukcyjny  
**Stan wiedzy:** 9 listopada 2026  
**Zakres:** architektura, kolejność rozwoju, integracja, walidacja i granice deklarowanych możliwości.

Ten dokument jest jednym punktem odniesienia dla kierunku budowy TSI. Zastępuje rozproszone plany rozwoju i powtarzające się opisy architektury. Szczegółowe raporty, wyniki testów i wcześniejsze decyzje pozostają w historii jako materiał źródłowy; nie są równoległymi roadmapami.

## 1. Cel konstrukcyjny

Budować jeden spójny rdzeń TSI, który:
- reprezentuje znaczenia, role, relacje i stan rozmowy;
- korzysta z uporządkowanej pamięci i zachowuje pochodzenie informacji;
- rozdziela rozpoznanie polecenia, plan działania, wykonanie narzędzia i kontrolę wyniku;
- potrafi jawnie odmówić rozstrzygnięcia, gdy brakuje danych albo wejście wykracza poza sprawdzony zakres;
- może być współdzielony przez aplikacje bez mieszania ich pamięci użytkownika;
- rozwija się bez naruszania działających ścieżek, checkpointów i regresji.

Priorytetem jest **produktywność pod warunkiem zachowania bezpieczeństwa i poprawności**. Nowy mechanizm nie trafia do aktywnego rdzenia tylko dlatego, że jest interesujący. Musi wykazać przewagę nad prostszą kontrolą, nie zwiększać ryzyka i przejść testy regresyjne.

## 2. Zasady niezmienne

1. **Jedno źródło prawdy:** ten dokument opisuje aktualny kierunek; README jest skrótem projektu; historia zapisuje chronologię.
2. **Oddzielaj stan od hipotezy:** działający kod, eksperyment, plan i przypuszczenie muszą być oznaczone osobno.
3. **Nie utożsamiaj podobnych nazw:** helisa TSI, modele GIA-TIMDR i mechanizmy Helix-Lock wymagają formalnego mapowania przed przeniesieniem wniosków.
4. **Pochodzenie informacji:** pamięć i adaptacja nie mogą po cichu nadpisywać źródła, historii korekt ani danych wejściowych.
5. **Niezależna kontrola:** solver, walidator, źródła i testy sprawdzają wynik poza samym generatorem odpowiedzi.
6. **Bezpieczne niepowodzenie:** niepełne, sprzeczne lub nieznane wejście daje pytanie, status nierozstrzygnięty albo odmowę — nie zgadywanie.
7. **Kompatybilność:** nowe moduły są najpierw adapterami lub eksperymentami poza ścieżką produkcyjną. Wymiana rdzenia wymaga osobnej bramki.
8. **Mierzalność:** każda zmiana ma hipotezę, punkt odniesienia, metryki, zestaw odłożony i kryterium wycofania.
9. **Minimalizm:** nie dodawać modułu, jeśli istniejąca reguła lub prostszy mechanizm rozwiązuje problem równie dobrze i bezpieczniej.

## 3. Architektura docelowa

Poniższy podział jest docelowym kontraktem odpowiedzialności. Nie oznacza, że wszystkie warstwy są już scalone w jeden model lub checkpoint.

### A. Wejście i kontekst
- normalizacja tekstu i dokumentów;
- identyfikacja języka, zakresu wypowiedzi, korekt i odwołań do wcześniejszego kontekstu;
- wydobycie kandydatów: pojęć, ról, obiektów, czasu, negacji, warunków i brakujących danych;
- zachowanie identyfikatorów źródeł oraz granic bieżącego zadania.

### B. Reprezentacja i rdzeń relacyjny
- enkoder–dekoder oraz reprezentacje pojęć;
- H512 i istniejące kanały czytnika;
- transformer relacji, słownik pojęć, macierz wymagań i przejścia ról;
- jawne reguły dwu-/trójstanowe tam, gdzie wymagają deterministycznej kontroli.

H512, czytnik i matryce mają już udokumentowane etapy integracji. Nie wolno jednak opisywać ich jako jednego w pełni zunifikowanego modelu, jeśli kod lub checkpoint tego nie potwierdza.

### C. Pamięć i ciągłość
Pamięć powinna mieć jawne zakresy:
- kontekst aktywnego zadania/rozmowy;
- pamięć epizodyczna: zdarzenia, kolejność, czas i korekty;
- pamięć semantyczna: zatwierdzona wiedza z pochodzeniem;
- stan trwały i checkpointy, wersjonowane oraz możliwe do odtworzenia.

Nowa informacja nie staje się wiedzą zatwierdzoną automatycznie. Adaptacja nie może nadpisywać surowego źródła. Trzeba odróżniać odzyskanie relacji od odtworzenia treści.

### D. Koordynacja i planowanie
- klasyfikacja celu i zakresu;
- wiązanie celu z wymaganymi danymi;
- plan kroków i wybór narzędzi;
- wykrywanie konfliktów, braków i niepewności;
- kontrolowane przekazanie do solvera, źródła lub modułu domenowego.

### E. Wykonanie i niezależna weryfikacja
- solvery matematyczne i przeliczniki;
- parsery oraz narzędzia dokumentów;
- źródła zewnętrzne z kontrolą trafności i pochodzenia;
- audyt odpowiedzi, jednostek, dziedziny, ograniczeń i kompletności;
- status wyniku: potwierdzony, częściowy, wymagający danych albo nierozstrzygnięty.

### F. Interfejsy i aplikacje konsumenckie
Walidator, MUZ i panel TSI korzystają ze wspólnej obsługi rdzenia, ale zachowują odrębne profile, rozmowy i pamięć użytkowników. Warstwa aplikacji nie powinna kopiować logiki rdzenia ani omijać jego walidacji.

## 4. Stan potwierdzony na 9 listopada 2026

| Obszar | Stan udokumentowany | Granica deklaracji |
|---|---|---|
| H512 + czytnik | Wspólny checkpoint i sprzężenie czterech kanałów relacji opisane w raporcie z 20 października | Nie jest to scalenie całej aplikacji ani dowód wzrostu swobodnej rozmowy |
| Matryce relacji | Transformer relacji, słownik i macierz wymagań oraz uczona tablica przejść | Reguły wiązania, audyt i solvery pozostają jawne poza tym checkpointem |
| Koordynacja narzędzi | Wspólna obsługa jednostek, audytu równań i zadań o ruchu jednostajnym | Zakres jest ograniczony do opisanych typów zadań |
| Integracja aplikacji | Wspólna obsługa dla walidatora i MUZ; osobne pamięci aplikacji | Nie oznacza identyczności wszystkich ścieżek ani wymiany wszystkich modeli |
| Język i kontekst | Wybrane konstrukcje polskie/angielskie, korekty, odczyt zdań, pytania o fakty i kontekst | Swobodna rozmowa nadal nie osiągnęła wymaganego poziomu |
| Helisa / Chronoproces | Istnieje notatka badawcza i plan walidacji | Nie jest to wdrożona funkcja TSI ani dowód samonaprawy |
| Kod i wagi | Publiczne repozytorium zawiera dokumentację; kod, wagi i pamięć pozostają lokalne | Wyników testów dokumentacyjnych nie wolno przedstawiać jako publicznego audytu kodu |

Wdrożony moduł odpowiedzi jest opisany jako krok 5217 i 9 074 672 parametrów. Większa sieć treningowa (21 731 408 parametrów, zapis 5664) nie jest wdrożona do aplikacji. Aktualizacja integracyjna z 3 listopada nie zmieniała wag.

Szczegółowe wyniki testów i ograniczenia są w [README](../README.md), [historii](../HISTORIA_TSI.md), [raporcie wspólnego rdzenia](TSI_UNIFIED_CORE_2026-10-20.md), [raporcie matryc](TSI_MATRIX_CORE_2026-10-20.md) i [integracji](INTEGRACJA_TSI_20261103.md). Te raporty są dowodami historycznymi, nie osobnymi planami.

## 5. Kolejność dalszej budowy

### Etap 0 — zamrożenie punktu odniesienia
- wskazać dokładny kod, konfigurację i checkpoint aktywny w każdej aplikacji;
- zachować kopie, sumy kontrolne i możliwość rollbacku;
- uruchomić jeden wspólny zestaw regresji dla wszystkich konsumentów;
- oddzielić wyniki rdzenia od wyników całej aplikacji z narzędziami.

**Warunek wyjścia:** powtarzalny baseline i jednoznaczna identyfikacja wersji.

### Etap 1 — audyt rzeczywistej architektury
- prześledzić wywołania od wejścia do odpowiedzi;
- sporządzić mapę modułów, zależności, formatów danych i granic pamięci;
- potwierdzić, które elementy są sieciami, regułami, adapterami i narzędziami;
- wykryć duplikaty logiki i niejawne ścieżki omijające walidację.

**Warunek wyjścia:** mapa architektury potwierdzona kodem, nie tylko opisem dokumentacji.

### Etap 2 — stabilny kontrakt reprezentacji i pamięci
- ustalić format reprezentacji relacji, ról, czasu, negacji i źródeł;
- zdefiniować identyfikatory, wersjonowanie i pochodzenie pamięci;
- rozdzielić stan bieżący, historię zdarzeń i wiedzę zatwierdzoną;
- przygotować testy korekt, restartu, konfliktów, utraty fragmentów i odtwarzania.

**Warunek wyjścia:** deterministyczny zapis/odczyt i brak utraty pochodzenia danych.

### Etap 3 — koordynator z kontrolą wyniku
- utrzymać rozdział rozpoznania celu, planu, wykonania i weryfikacji;
- dodać jawne statusy braków i nierozstrzygnięcia;
- rozszerzać zadania kompozycyjne tylko po testach odłożonych;
- mierzyć skuteczność całego przepływu, liczbę błędnych akceptacji, fałszywych odmów i koszt wykonania.

**Warunek wyjścia:** poprawa względem baseline bez pogorszenia bezpieczeństwa i regresji.

### Etap 4 — badanie helisy i Chronoprocesu poza rdzeniem produkcyjnym
1. Odszukać w kodzie TSI faktyczną definicję helisy, stanów, operatorów, pętli i osi czasu.
2. Porównać ją formalnie z modelem badanym w GIA-TIMDR; nie mapować zmiennych na podstawie samej nazwy.
3. Zbudować mały eksperyment izolowany od checkpointów i pamięci produkcyjnej.
4. Porównać wariant statyczny, wariant z historią oraz kontrolę bez sprzężenia.
5. Wprowadzać kontrolowane zakłócenia pojedynczych kanałów i całej struktury.
6. Mierzyć osobno: zachowanie relacji, synchronizację, rekonstrukcję treści, integralność payloadu, czas i pamięć.
7. Użyć danych odłożonych i niezależnej kontroli.

**Warunek wyjścia:** powtarzalna przewaga nad kontrolą i brak regresji. Synchronizacja faz nie jest dowodem odzyskania danych ani samonaprawy pamięci.

### Etap 5 — integracja warunkowa
- dopiero po przejściu bramki przenieść zatwierdzony mechanizm do adaptera;
- nie zmieniać od razu aktywnych wag ani trwałej pamięci;
- wykonać testy zgodności wszystkich aplikacji i próbę wycofania;
- aktualizować checkpoint dopiero po osobnej kwalifikacji i kopii bezpieczeństwa.

**Warunek wyjścia:** wdrożenie odwracalne, mierzalne i bez pogorszenia istniejących funkcji.

## 6. Wspólny protokół pomiarowy

Każda zmiana powinna raportować co najmniej:
- trafność na danych znanych i odłożonych;
- błędne akceptacje i błędne odmowy;
- kompletność wymaganych danych i poprawność źródeł;
- odporność na zmianę kolejności, formy językowej i korekty;
- zachowanie po restarcie oraz zgodność odtworzenia;
- opóźnienie, RAM, rozmiar checkpointu i koszt obliczeń;
- wynik regresji wszystkich aplikacji konsumenckich;
- porównanie z prostszym baseline'em.

Zestawów częściowo nakładających się nie sumować w jeden ogólny procent. Raportować dokładne zakresy, liczbę przypadków, warunki i wersję kodu.

## 7. Decyzje architektoniczne i kryteria odrzucenia

- Nie trenować wszystkich wag naraz bez wykazania, że mniejszy adapter lub reguła nie wystarczy.
- Nie integrować mechanizmu, którego korzyści nie da się zmierzyć.
- Nie zwiększać powierzchni ataku ani zakresu uprawnień modułu dla niewielkiej poprawy wygody.
- Nie używać pamięci eksperymentalnej jako źródła prawdy.
- Nie nazywać synchronizacji, korelacji lub powrotu do stanu nominalnego samonaprawą.
- Nie przenosić wyników GIA-TIMDR lub Helix-Lock na TSI bez oddzielnego testu TSI.
- Jeśli nowy moduł nie poprawia mierzalnie wyniku lub pogarsza bezpieczeństwo, pozostaje poza rdzeniem albo zostaje usunięty.

## 8. Rejestr otwartych pytań

1. Jaka jest dokładna implementacja helisy w aktywnym kodzie TSI i czy odpowiada modelowi trzech sprzężonych pętli?
2. Które kanały H512 i czytnika są faktycznie wykorzystywane w bieżącym przepływie, a które są tylko dostępne w checkpointcie?
3. Jaki jest kanoniczny schemat pamięci epizodycznej i semantycznej oraz gdzie przebiega granica między nimi?
4. Czy historia czasowa daje mierzalną przewagę nad samym stanem bieżącym na nowych danych?
5. Które części koordynatora można ujednolicić bez naruszenia specjalistycznych narzędzi aplikacji?
6. Jakie są aktualne pomiary czasu, RAM i rozmiaru pełnego uruchomienia na docelowym sprzęcie?

Odpowiedzi wymagają audytu kodu i pomiarów; nie należy zastępować ich założeniami.

## 9. Powiązane dokumenty źródłowe

- [Wspólny model H512 i czytnika — 20.10.2026](TSI_UNIFIED_CORE_2026-10-20.md)
- [Wspólny moduł matryc TSI — 20.10.2026](TSI_MATRIX_CORE_2026-10-20.md)
- [Integracja wspólnego TSI — 03.11.2026](INTEGRACJA_TSI_20261103.md)
- [Badania helisy i Chronoprocesu — 08.11.2026](HELIX_CHRONOPROCESS_TSI_RESEARCH_20261108.md)
- [Historia zmian](../HISTORIA_TSI.md)

Dokumenty powyżej zachowują szczegóły i surowe wyniki. Nowe decyzje dotyczące architektury, priorytetów i kolejności prac należy dopisywać tutaj, a nie tworzyć kolejnej roadmapy.
