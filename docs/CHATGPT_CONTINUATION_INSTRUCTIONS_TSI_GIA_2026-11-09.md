# Instrukcja kontynuacji pracy z ChatGPT — TSI i GIA-TIMDR

**Data:** 9 listopada 2026. **Konto GitHub:** jbackk-lang. **Cel:** zachować kontekst, zasady pracy, wymagane źródła i kolejność dalszych działań w kolejnych rozmowach.

Odczytaj ten dokument na początku nowej rozmowy dotyczącej TSI, helisy, Chronoprocesu lub GIA-TIMDR. Aktualizuj go po ważnych decyzjach, audytach i zmianach stanu.

## 1. Projekty i repozytoria — nie mieszać ich

Dostępna lista konta jbackk-lang zawiera 72 repozytoria. Główne repozytoria rozpoznane 9.11.2026:

- jbackk-lang/AI-SI-TSI — centralna dokumentacja TSI, architektura rdzenia, roadmapa i historia.
- jbackk-lang/TSI-math-validator-5 — aplikacja/walidator matematyczny, jeden z konsumentów wspólnej obsługi.
- jbackk-lang/TSI-MUZ — aplikacja MUZ, jeden z konsumentów wspólnej obsługi.
- jbackk-lang/TSI-Predikt-Motor — osobny kierunek analizy sygnałów i diagnostyki.
- jbackk-lang/GIA-TIMDR — osobny projekt matematyczny: geometria odbić, mobilność graniastosłupa rombowego i osie śrubowe. Może dostarczać hipotez badawczych, ale nie jest rdzeniem TSI.

**Zasada:** nie utożsamiać modeli, zmiennych, operatorów, checkpointów ani wyników tylko dlatego, że występują nazwy helisa/TSI/GIA/Chronoproces. Każde przeniesienie wyniku z GIA-TIMDR do TSI wymaga formalnego mapowania i oddzielnego testu w kodzie TSI.

## 2. Źródło prawdy dla TSI

Zawsze najpierw sprawdzić aktualny stan i historię w tej kolejności:

1. docs/TSI_CORE_ROADMAP_AND_ARCHITECTURE.md — nadrzędny, żywy plan konstrukcyjny. To jedno miejsce rozstrzyga kierunek architektury i kolejność prac.
2. README.md — skrót aktualnego stanu, działających funkcji i ograniczeń.
3. HISTORIA_TSI.md — chronologia decyzji, treningów, regresji i wyników.
4. docs/HELIX_CHRONOPROCESS_TSI_RESEARCH_20261108.md — hipotezy dotyczące helisy i Chronoprocesu oraz protokół ich walidacji.
5. docs/INTEGRACJA_TSI_20261103.md i dokumenty wymienione w roadmapie — szczegóły integracji i testów.

Nie tworzyć równoległej roadmapy. Raporty historyczne zachować jako dowody, nie traktować ich jako aktualnego stanu bez sprawdzenia daty.

## 3. Aktualny stan TSI udokumentowany w GitHub (9.11.2026)

- TSI jest lokalnym systemem: własna sieć enkoder–dekoder, słowniki, pamięć, reguły logiczne i narzędzia matematyczne.
- Wspólna obsługa 2026-11-03-consumers-11 jest podłączona do walidatora i MUZ; rozmowy i pamięć aplikacji pozostają rozdzielone.
- Repozytoria publiczne publikują dokumentację. Aktualny kod źródłowy, wagi/checkpointy, pamięć i dane użytkownika pozostają lokalnie.
- Moduł odpowiedzi aplikacji opisano jako krok 5217 i 9 074 672 parametrów.
- Większa sieć treningowa: 21 731 408 parametrów, ostatni zapis opisany w README jako 5664; nie jest wdrożona do aplikacji.
- Swobodna rozmowa nie osiągnęła wymaganego poziomu. Wyniki testów dotyczą konkretnych zestawów i ścieżek z narzędziami; nie sumować ich w jeden ogólny wynik.
- Helisa i Chronoproces są kierunkiem badawczym, nie potwierdzoną funkcją produkcyjną ani dowodem samonaprawy.
- Nie twierdzić, że asystent przeprowadził pełny audyt kodu, dopóki lokalne źródła nie zostaną udostępnione i przeanalizowane.

## 4. Zasady pracy asystenta

1. Najpierw sprawdź pliki i stan repozytoriów. Jeśli pytanie zależy od kodu, dokumentu lub wcześniejszej decyzji, odczytaj źródło przed wnioskowaniem.
2. Rozróżniaj fakty, wyniki testów, hipotezy i plany. Oznaczaj je wprost.
3. Nie zgaduj zawartości lokalnego dysku. Ścieżka C:\Users\jback\Downloads\a jest folderem użytkownika. Asystent nie ma automatycznego dostępu do dysku C: ani do całej zawartości komputera.
4. Nie uznawaj publicznego GitHuba za pełne źródło kodu TSI. Repozytoria TSI zawierają dokumentację; kod i wagi są lokalne.
5. Nie modyfikuj wag, checkpointów, pamięci trwałej ani działającej instalacji bez osobnej, jawnej decyzji. Najpierw audyt, kopia, baseline, testy i plan rollbacku.
6. Nie publikuj sekretów ani prywatnych danych. Nie proś o klucze API, hasła, tokeny, dane bankowe, prywatne rozmowy ani bazy użytkowników.
7. Dla zmian w GitHub: sprawdź plik przed edycją, zachowaj styl i zależności, wykonaj małą zmianę, uruchom właściwe CI, sprawdź wynik i podaj link do commita/workflow. Nie deklaruj sukcesu, gdy workflow jest jeszcze w toku.
8. Nie sumuj wyników różnych zestawów. Podawaj wersję kodu, checkpoint, zakres, liczbę przypadków, warunki i ograniczenia.
9. Eksperymenty GIA-TIMDR prowadź odwracalnie i oddzielnie. Nie przenoś ich automatycznie do TSI.
10. Kontynuuj od ostatniego potwierdzonego stanu, a nie od najbardziej optymistycznej hipotezy.

## 5. Jakie pliki są potrzebne do rzeczywistego audytu lokalnego TSI

Użytkownik wskazał, że pozostałe kody znajdują się w C:\Users\jback\Downloads\a. Asystent nie może sam otworzyć tej ścieżki z poziomu czatu. Użytkownik musi dodać pliki jako załącznik albo przekazać archiwum ZIP w rozmowie. Zalecana nazwa: TSI_SOURCE_AUDIT_2026-11-09.zip.

### Pakiet minimalny — potrzebny jako pierwszy

- kod źródłowy aktywnego rdzenia TSI;
- moduł wejścia/enkodera, dekodera i generatora odpowiedzi;
- definicje H512, czytnika, kanałów relacji, matryc i adapterów;
- koordynator/narzędzia: pamięć, solver, walidator, obsługa kontekstu i korekt;
- pliki konfiguracji i manifesty określające aktywny model;
- testy jednostkowe, integracyjne i regresyjne;
- skrypty uruchomieniowe oraz requirements.txt, pyproject.toml lub odpowiedniki;
- dokument wskazujący, która wersja kodu i który checkpoint są aktualnie używane przez TSI, walidator i MUZ.

### Pakiet do badania helisy / Chronoprocesu

- pliki, w których helisa jest faktycznie definiowana i obliczana;
- wzory, operatory, parametry, warunki brzegowe i definicje pętli/kanałów;
- kod historii czasowej, pamięci epizodycznej i rekonstrukcji;
- testy zaburzeń, odtwarzania, synchronizacji i integralności danych;
- przykładowe syntetyczne dane testowe oraz oczekiwane wyniki;
- powiązanie implementacji z odpowiednim checkpointem i ścieżką wykonania.

### Wagi i checkpointy — dopiero po audycie kodu

Na pierwszym etapie nie trzeba wysyłać wszystkich dużych wag. Wystarczy manifest checkpointu: nazwa, krok, architektura, format, rozmiar, hash SHA-256, konfiguracja i informacja, który proces go ładuje. Jeśli analiza będzie wymagała wag, poprosić o konkretny plik i uzasadnić potrzebę.

### Czego nie dołączać

- .venv, venv, __pycache__, cache i tymczasowych buildów;
- logów z prywatnymi danymi, historii rozmów użytkowników i baz produkcyjnych;
- haseł, kluczy API, tokenów, certyfikatów prywatnych i plików .env z sekretami;
- danych bankowych, danych uczniów i innych danych osobowych;
- kopii zapasowych, które nie są potrzebne do konkretnego audytu.

Przed spakowaniem zamień sekrety na placeholdery, np. REDACTED. Nie zmieniaj kodu ani nazw interfejsów potrzebnych do analizy.

## 6. Procedura pracy po otrzymaniu ZIP

1. Potwierdzić listę plików i strukturę katalogów; nie uruchamiać od razu nieznanego kodu.
2. Rozpoznać entrypointy, konfiguracje, zależności, checkpointy i aktywne ścieżki.
3. Zbudować mapę przepływu: wejście → kontekst → reprezentacja → pamięć → plan → narzędzie/model → walidacja → odpowiedź.
4. Wskazać, co jest siecią neuronową, co regułą, co adapterem, co solverem, a co tylko dokumentacją.
5. Zweryfikować, które moduły rzeczywiście wywołuje aplikacja, a które są nieużywane lub eksperymentalne.
6. Sporządzić inwentarz testów i uruchomić bezpieczne testy bez modyfikowania danych użytkownika.
7. Wykonać baseline na wskazanym checkpointcie; zachować wyniki i wersję kodu.
8. Zmapować formalizm helisy TSI na model GIA-TIMDR wyłącznie wtedy, gdy zmienne i operatory mają wykazaną równoważność.
9. Zaprojektować izolowany eksperyment porównujący wariant statyczny, wariant z historią/sprzężeniem i kontrolę bez sprzężenia.
10. Przedstawić raport z dowodami, ograniczeniami, ryzykami i proponowanym kolejnym krokiem. Nie wdrażać automatycznie eksperymentalnego mechanizmu do produkcyjnego TSI.

## 7. Kontynuacja bieżącego czatu — GIA-TIMDR

Bieżący wątek dotyczy badania geometrii całej rodziny osi izometrii w jbackk-lang/GIA-TIMDR, a nie wyłącznie widma kątów ani samych osi śrubowych.

### Stan wykonanych zmian

- Dodano experiments/rhombic_prism_axis_geometry_limit_audit.py.
- Dodano .github/workflows/rhombic-prism-axis-geometry-audit.yml.
- Dopisano sekcję 29 do docs/geometry/TIMDR_Rhombic_Prism_Mobility_Domain_2026-11-09.md.
- Audyt reprezentuje osie w przestrzeni Plückera: L=(a,m), m=p×a.
- Uwzględnia osie obrotu o zerowym skoku i osie śrubowe o niezerowym skoku; translacje nie mają skończonej osi.
- Porównuje zbiory kumulacyjne dla parzystych długości słów 2, 4, 6 i 8, odległości najbliższych sąsiadów, zajętość komórek przy wspólnej normalizacji oraz wrażliwość na próg kąta.
- Badane konfiguracje: centrum, bliska centrum gałąź symetrii, konfiguracja ogólna umiarkowana i ogólna diagonalna.
- Ograniczenie: zajętość komórek nie jest wymiarem Hausdorffa; mała odległość nowych osi od starych nie dowodzi zbieżności granicznej.

### Ostatni potwierdzony CI

Dedykowany workflow przeszedł pomyślnie:
https://github.com/jbackk-lang/GIA-TIMDR/actions/runs/42647816412

Commit zawierający poprawkę składni i uruchomienie audytu: c37300befa32caff972ea2f62a040363438beda8.

Pierwsze uruchomienie miało błąd składni f-string; poprawiono go i ponowiony workflow zakończył się success. Nie używać pierwszego nieudanego przebiegu jako wyniku naukowego.

### Następne kroki GIA-TIMDR

1. Pobrać logi udanego workflow i zapisać rzeczywiste wyniki liczbowe audytu.
2. Sprawdzić, czy zbiór kumulacyjny jest poprawnie zbudowany: klucz mapy, deduplikacja, tolerancja numeryczna i brak niezamierzonych kolizji.
3. Zbadać, czy metryka euklidesowa w sześciu współrzędnych Plückera jest używana konsekwentnie i czy wyniki są stabilne względem normalizacji.
4. Porównać ogony rozkładów odległości i średnicę zbioru; nie opierać wniosku o granicy tylko na medianie.
5. Wykonać analizę czułości progu kąta i precyzji deduplikacji.
6. Jeśli koszt obliczeń pozwala, rozszerzyć głębokość lub zastosować stabilniejsze obliczenia/arytmetykę dokładną dla wybranych konfiguracji.
7. Dopiero po walidacji danych rozważyć estymację wymiaru pudełkowego jako osobny eksperyment; nie nazywać go wymiarem Hausdorffa.
8. Wyniki i interpretację dopisać do dokumentacji GIA-TIMDR, oddzielając obserwacje od hipotez.

## 8. Jak rozpocząć następną rozmowę

Użytkownik może napisać:

> Kontynuuj TSI zgodnie z instrukcją CHATGPT_CONTINUATION_INSTRUCTIONS_TSI_GIA_2026-11-09.md. Najpierw odczytaj tę instrukcję, nadrzędną roadmapę TSI i aktualne repozytoria. Nie zgaduj zawartości lokalnego kodu. Jeśli potrzebny jest ZIP z C:\Users\jback\Downloads\a, wskaż dokładnie, które pliki mam dołączyć. Kontynuuj od ostatniego potwierdzonego stanu.

Jeśli rozmowa dotyczy tylko GIA-TIMDR, kontynuować od sekcji 7 i najpierw pobrać wyniki udanego workflow.

---
**Najważniejsza zasada:** najpierw odczyt źródeł i audyt rzeczywistego kodu, następnie hipoteza i eksperyment, na końcu dopiero ewentualna integracja. Nie zamieniać hipotez w fakty i nie zmieniać działającego TSI bez wyraźnej decyzji użytkownika.
