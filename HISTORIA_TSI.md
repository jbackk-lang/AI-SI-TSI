# Historia rozwoju AI-SI-TSI

Ten plik przechowuje przebieg prac i wcześniejsze pomiary. Aktualne możliwości oraz ograniczenia są opisane w [README](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/README.md). Wyników odmiennych zestawów i modeli nie należy dodawać ani porównywać jak jednego sprawdzianu.

## 27 października — naprawa odczytu, zachowania wiedzy i archiwum AI-SI

Nowy rdzeń ma 17 982 624 parametry. Rozdzielono wpływ zapisu wejścia od utraty wcześniejszych umiejętności podczas treningu. Po nauce OR wcześniejsza negacja odpowiadała stale T, a AND zmieniało odpowiedź po zmianie odstępów. Poprzednie zatwierdzone wagi poprawnie rozpoznawały odczyt, negację i AND w pięciu zapisach.

Dodano ujednolicanie nieistotnych odstępów dla formalnych poleceń LOGIC. Zachowuje ono tryb, operator, argumenty i ich kolejność; nie wylicza odpowiedzi. Trening całej części neuronowej obejmuje wcześniejsze zweryfikowane zależności oraz kontrolę rzeczywistych zmian wag. Odpowiedzi mierzone są przed korektą przez formalne reguły.

| Sprawdzenie | Wynik |
|---|---:|
| Naprawiony rdzeń: główny sprawdzian | **120/120** |
| Oddzielne zapisy | **45/45** |
| Te same naprawione wagi, bez ujednolicania zapisu | **71/75** |
| Z ujednolicaniem | **75/75** |
| 32 kroki z gradientem wcześniejszych lekcji | **75/75** |
| Te same 32 kroki wyłącznie nowego działania | **60/75** |

Krótka kontrola bez projekcji gradientu także osiągnęła 75/75, dlatego nie przypisano poprawy samej projekcji. W dłuższym przebiegu z powtórkami wcześniejsze lekcje po przejściowym 10/11 wróciły do 11/11. Sam retest niezmienionych wag po przerwie nie zmienił odpowiedzi.

Rozpoczęto uczenie krótkich polskich zdań na własnych wagach, z ochroną zaliczonych zależności logicznych. Kolejne bloki kontynuują najnowszy zapis modelu i stan losowania. Naprawiono błąd aktualizacji sumy zapisanego checkpointu; zachowany postęp wznowiono bez cofania wag. Swobodna rozmowa nie osiągnęła wymaganego poziomu. Tego etapu nie wdrożono jeszcze do aplikacji ani portable.

Dla starego AI-SI przygotowano osiem publicznych zestawów o rozmiarze około 8,3 GB: historyczne źródła i modele bazowe Bielik, Qwen, Whisper oraz OPUS. Obecny TSI, prywatne bazy i rozmowy pozostają lokalnie. Szczegóły są w [opisie paczek](docs/PACZKI_STAREGO_AI_SI.md). Poprzedni główny opis zachowano w [archiwum README](docs/archiwum/README_przed_aktualizacja_2026-10-27.md).

## Stan sprzed uporządkowania dokumentacji

- [Poprzedni lokalny README — 21 października 2026](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_before_current_state_2026-10-21.md).
- [Poprzedni roboczy README publikacyjny — 20 października 2026](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_public_before_current_state_2026-10-21.md).
- [Zachowana wcześniejsza historia TSI](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/HISTORIA_TSI_before_2026-10-21.md).
- [Wcześniejsza historia AI-SI](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/HISTORIA_SI_2026-10-11.md).

Kopie README zachowują historyczne opisy i pomiary. Nie oznaczają, że wszystkie wymienione tam eksperymenty są wdrożone. Odnośniki do wcześniejszych lokalnych materiałów w tych kopiach przedstawiono jako zwykły tekst.

## 20 października — wspólny moduł i aplikacja

Wprowadzono wspólny model H512, czytnika, macierzy i uczonych połączeń: runtime 0.6.0, 2 613 105 parametrów i plik wag 10 587 275 B. Integracja dotyczyła jawnych relacji i dowodów; narzędzia oraz pamięć dokumentów pozostały osobnymi częściami aplikacji.

Ówczesne wyspecjalizowane sprawdziany obejmowały 960/960, 720/720 i 640/640 przypadków, 140/140 poleceń językowych, 256/256 operacji wektorowych i 118/118 planów. Były to ograniczone zestawy znanych pojęć i jawnych danych. Nie potwierdzały swobodnej rozmowy.

Uporządkowano panel rozmowy i dokumentów, dodano odczyt kilku źródeł, wersjonowanie, poprawki i cofanie zmian. Analiza sygnałów uzyskała w osobnym sprawdzianie pięciu etykiet 95,32% micro-F1 i 1739/2000 pełnych zestawów. Są to historyczne wyniki innych modułów, a nie ocena obecnego generatora tekstu.

## 21 października — własny generator i odczyt źródeł

Pierwszy generator tekstu miał 1 826 496 parametrów i kontekst 512 tokenów; warstwa uwagi kopiującej dodawała 73 921 parametrów. Na 68 odłożonych zadaniach o fakty i definicje uzyskał 0/68 pełnych odpowiedzi, przy 25/25 odmowach przy braku informacji. Dalszy wspólny trening generatora i wyboru źródła dał 7/68. Wybór źródła potrafił być poprawny, mimo uszkodzonej odpowiedzi.

Model czytający pełną treść połączył własny generator, H512 i role macierzowe. Samo zwiększenie liczby parametrów do około 4,96 mln nie rozwiązało generowania odpowiedzi. Próby impulsów, sekwencji powtórek i zmian wag nie dostarczyły dowodu na fizyczny rezonans poprawiający naukę. Nie stosowano ich jako potwierdzonej metody produkcyjnej.

Podczas wcześniejszych prób wykryto także błędy wyznaczania zakresów źródeł. Wadliwe przebiegi oznaczono i zastąpiono poprawionymi; nie należy ich traktować jako wiarygodnych wyników nauki. Etykiety źródeł w generowanym tekście wymagały osobnej kontroli.

## Dwie połówki i wspólna odpowiedź

Początkowo sklonowano rdzeń i uczono drugą połówkę na błędach, przy zamrożonej pierwszej. Następnie połączono ich reprezentacje. Poprawiono rozdzielenie wyboru źródła od uwagi wewnątrz źródła i wprowadzono role terminu oraz objaśnienia.

Przed wspólnym odblokowaniem obu połówek potwierdzono 7/8 na niezależnych faktach, 8/16 na mieszanych starszych źródłach i 5/7 na wcześniejszych zadaniach językowych. W zestawie mieszanym fakty miały 8/8, a definicje 0/8. Późniejszy trening samych macierzy definicji podniósł starsze definicje do 4/8 i nowe do 10/16.

Wspólny trening 60 kroków odblokował oba generatory i obie pamięci H512. Potwierdzono przepływ gradientów oraz zmianę wag obu połówek. Wariant pojedynczy i dwupołówkowy dostały te same partie danych. Oba uzyskały 23/24 na zestawie doboru i 16/16 na nowych definicjach. Dwupołówkowy uzyskał 49/85 na starszych zadaniach, pojedynczy 48/85. To mała różnica, nie dowód ogólnej przewagi dwóch rdzeni ani szybszego uczenia.

W obu wariantach wystąpiła regresja starszego zestawu faktów: 8/8 → 6/8. Wybrano dwupołówkowy kierunek dalszego rozwoju, zachowując wcześniejsze wagi do cofnięcia. Nie podmieniono działających paneli.

## Eksperyment jednej podpowiedzi

Bez aktualizacji wag podano ogólną wskazówkę o zachowaniu pełnego początku imienia, bez ujawniania imienia, źródła ani odpowiedzi:

| Miejsce podpowiedzi | Pełne odpowiedzi |
|---|---:|
| Bez podpowiedzi | 6/8 |
| Tylko pierwsza połówka | 7/8 |
| Tylko druga połówka | 8/8 |

Nie utracono wcześniejszych sześciu trafień. Był to efekt kontekstu, nie potwierdzone trwałe uczenie. Wynik nie dowodzi, że jedna połówka samodzielnie diagnozuje i uczy drugą.

## Trening z powtórkami i wycofywaniem podpowiedzi

Wykonano 400 kroków. Każda partia zawierała trzy zadania dotyczące faktów i jedną definicję jako powtórkę. Zbiór zawierał 195 różnych treningowych zadań o faktach i 160 definicji; osobny zestaw doboru i nowy test faktów miały po 24 różne zadania. Podpowiedź trafiała tylko do drugiej połówki: początkowo co drugi krok, następnie co czwarty, a w ostatnich 200 krokach była wyłączona.

Ćwiczono macierze uwagi, pozycji i bramki kopiowania. Obie wcześniej wytrenowane sieci bazowe i pamięci H512 zachowano. Trening wspólnego odczytu poprawił fakty, ale zepsuł jedną wcześniej poprawną definicję przez powtórzenie słowa. Rozdzielono więc macierze odczytu definicji i faktów w tym samym modelu; podział wykorzystuje wcześniej istniejące role terminu i objaśnienia, a nie listę konkretnych odpowiedzi.

Po tej ochronie ponowiono pełne sprawdziany bez podpowiedzi:

| Zestaw | Przed | Po |
|---|---:|---:|
| Wcześniejsze błędy faktów | 6/8 | 8/8 |
| Pierwotne źródła | 12/16 | 12/16 |
| Starszy zestaw doboru | 9/14 | 9/14 |
| Starszy zestaw słownikowy | 17/40 | 19/40 |
| Wcześniejsze zadania językowe | 5/7 | 5/7 |
| **Starsze zadania łącznie** | **49/85** | **53/85** |
| Nowy zestaw faktów | 23/24 | 24/24 |
| Osobne proste definicje | 16/16 | 16/16 |

Nie utracono żadnej wcześniej poprawnej odpowiedzi w tych zestawach. Po ponownym wczytaniu zapisanych wag ponowienie ośmiu przypadków nadal dało 8/8. Model po ochronie odczytu ma 10 147 343 parametry, plik 40 944 075 B. Porównanie dotyczy pełnych odpowiedzi, nie tylko etykiet źródeł; historyczne zestawy nie są nowymi ślepymi testami.

## Pozostałe błędy i kolejny etap

W starszych 85 zadaniach wyniki według rodzaju to: fakty 37/40, definicje 7/30, brak informacji 9/13, swobodne pisanie i wyjaśnianie 0/2. Występują ucięte słowa, powtarzanie fragmentów, niezgodność wypisanej etykiety S1/S2 z poprawnie wybranym źródłem i nieuzasadnione odpowiedzi przy braku danych.

Sprawdzono starsze zapisy: etykieta [S1] pojawiała się w odpowiedzi na prośbę o opowiadanie już w pojedynczym rdzeniu bez źródeł. Problem nie został więc zapoczątkowany dopiero przez połączenie połówek. Dokładnego pierwszego kroku jego powstania nie ustalono.

Kolejny trening zakończono po 600 krokach. Rozpoznanie braku informacji wzrosło z 9/13 do 13/13, ale fakty spadły z 37/40 do 31/40, a definicje z 7/30 do 4/30. Łącznie uzyskano 48/85 zamiast 53/85. Wariant odrzucono; poprzednie sprawdzone wagi pozostają zachowane.

## Nauka od solvera i nauczyciela logiki

SymPy przygotował dokładne odpowiedzi dla 768 przykładów treningowych: działania, ułamki i równania liniowe. Zestaw doboru miał 48 przykładów, test 72. Po 800 krokach uczeń uzyskał 2/72. Dodatkowe 1000 kroków uczenia reprezentacji wejścia i ról liczb dało 7/72. Nowy zestaw 48 zadań, wykluczający także wcześniej widziane odwrócenia działań przemiennych, dał 5/48. Zakresy liczb pozostawały znane z treningu. Solver nie był wywoływany podczas odpowiedzi ucznia. Wyniki są nadal niewystarczające do niezawodnego liczenia.

Wprowadzono trening silnej logiki trójstanowej Kleene’a: T — prawda, F — fałsz, U — nieznane. Bezpośredni odczyt tekstu uzyskał 36/39 powtarzanych przypadków podstawowych i 30/48 nowych złożeń. Jeden eksperyment ujawnił błąd wybierania fragmentu wejścia: zamiast wyrażenia wybierano końcową instrukcję „Wynik: T/F/U”. Jego wyników nie traktujemy jako wiarygodnego sprawdzianu wejścia. Po poprawce i powtórkach kolejny wariant uzyskał 38/39 oraz 29/48; problem odczytu złożonych wyrażeń pozostaje.

Osobny wariant formalny łączy parser składni z uczonym modułem operatorów o 483 parametrach. Nauczyciel podał wszystkie 39 elementarnych kombinacji AND, OR, NOT, IMPLIES i EQUIV. Podczas wykonania parser wyznacza kolejność kroków, a sieć przewiduje wynik każdego operatora. Uzyskano 39/39 nauczonych przypadków, 48/48 wcześniejszych złożeń i 100/100 nowych zagnieżdżonych wyrażeń. Nowe są złożenia znanych operatorów; wynik nie dowodzi rozumowania na dowolnym opisie słownym ani samodzielnego odkrywania reguł.

Wagi wcześniejszego odczytu źródeł zachowano bez zmian; kontrola ośmiu wcześniejszych przypadków ponownie dała 8/8. Moduły matematyki i formalnej logiki mają osobne wejścia badawcze. Nie podmieniono działających paneli. Pełny zapis wariantu z tymi modułami ma 11 239 938 parametrów; nie zastępuje zaakceptowanego modelu źródeł opisanego w głównym README.

## Publikacja

### Rozmowa, źródła i lokalny słownik

Sprawdzono rzeczywistą rozmowę o państwach. Starszy czytnik mylił pytanie o państwa z pytaniem o możliwości TSI, prośbę o Wikipedię z wklejaniem dokumentu, a definicję z audytem poprzedniej odpowiedzi. Wytrenowano osobny klasyfikator intencji. Wybrany wariant miał 482 przykłady treningowe i wynik 85/87 na odłożonych przykładach znanych rodzin pytań z innymi tematami. To nie jest wynik swobodnej konwersacji. Dodatkowe parafrazy oraz rzeczywista rozmowa nadal ujawniały błędy, zwłaszcza przy doprecyzowaniu znaczenia i prośbie o prostsze wyjaśnienie. Kolejne warianty badawcze nie zastąpiły wybranego czytnika.

Podłączono pobieranie Wikipedii z wyborem artykułu, zachowaniem źródła i kontekstu. Poprawiono kolizję z włączonym materiałem dokumentowym oraz wybór polskiego języka komunikatów. Szesnaście kontroli HTTP objęło wcześniejszy ciąg pytań, treść artykułu, listę państw, angielskie hasło Gravity, potwierdzanie nowego wyszukania oraz wcześniejsze funkcje matematyki, logiki i dokumentów. Te kontrole poprzedzały dodanie lokalnej bazy słownikowej.

Następnie z publicznego zrzutu polskiego Wikisłownika przez Kaikki/Wiktextract zbudowano lokalną bazę: **114 215 różnych haseł, 125 720 wpisów i 1 437 842 powiązania form odmiany**. Baza zajmuje **157 716 480 B**. Zachowuje znaczenia, przykłady, źródła i informację o pochodzeniu. Jest dostępna przez polecenie `słownik: …`, a rozpoznane pytania definicyjne korzystają z niej przed pobraniem strony. Odrębne znaczenia nie są automatycznie uznawane za równoważne. Sprawdzono lokalny odczyt przy zablokowanym pobieraniu sieciowym. Nie jest to kopia PWN i nie jest to trening wag generatora. NKJP/PELCRA oraz WSJP sprawdzono jako możliwe dalsze zasoby; nie zaimportowano ich pełnych baz.

Rzeczywista próba po podłączeniu słownika poprawnie odpowiedziała na dłuższe pytanie o państwo, lecz doprecyzowanie „chodzi mi o kraj, nie grupę osób” nadal nie zostało poprawnie obsłużone. Pytanie o cechę ciał z definicji grawitacji zwróciło zbyt szerokie fragmenty, także ze starego tematu. Wyszukanie definicji i odczyt konkretnej relacji są oceniane osobno.

Dodano następnie odczyt jawnych relacji z aktywnej definicji. Własny uczony klasyfikator pytania wybiera rolę: cecha, uczestnicy, przeznaczenie, skład, warunek lub inne. Miał 535 przykładów treningowych, 112 do doboru i 112 testowych; uzyskał 109/112 etykiet w teście znanych rodzin pytań. Sam ten wynik nie mierzy trafności pełnych odpowiedzi. Matryca konstrukcji językowych wskazuje dokładny fragment źródła; nie zawiera gotowej odpowiedzi „masę”. W kontroli offline definicja grawitacji dała „masę” dla pytania o cechę i „ciałami mającymi masę” dla uczestników. Brak zapisanego warunku spowodował doprecyzowanie. Kontrole zmiany źródła sprawdziły odczyt różnych cech. To ograniczony odczyt jawnych relacji, nie dowód swobodnego wnioskowania ani opanowania parafrazy przez generator.

### Podłączenie operatorów logiki do panelu

Po powyższych badaniach wdrożono w panelu lokalnym wyłącznie sprawdzony moduł 483 uczonych parametrów operatorów, z parserem formalnych wyrażeń. Zachowano dotychczasowy model rozmowy; nie włączono słabego eksperymentalnego ucznia arytmetyki. Przykłady są dostępne w pomocy. Polecenia `logika: …` i `logic: …` działają w rozmowie i dziale rdzenia; jednoznaczne formalne wyrażenia rozpoznawane są również bez prefiksu. Odpowiedź zawiera wynik T/F/U i kroki, w wybranym języku panelu. Niepełne nawiasy i obce dopiski są odrzucane zamiast pomijania części wejścia.

Kontrola interfejsu HTTP objęła sześć poprawnych wyrażeń PL/EN, trzy błędne zapisy i dwie wcześniejsze funkcje: przywitanie oraz dodawanie. Wszystkie 11 kontroli przeszło. Po uruchomieniu docelowego panelu ponowiono złożone wyrażenie i potwierdzono, że używa nowych wag operatorów. Zachowano kopię poprzedniego koordynatora aplikacji. To wdrożenie formalnej logiki, nie wymiana całego modelu rozmowy.

Ta aktualizacja publikuje dokumentację i dwa wcześniejsze zrzuty panelu z przykładowymi danymi. Nie dodaje kodu obecnego TSI, wag, danych treningowych, prywatnych dokumentów ani lokalnych ścieżek użytkownika. Nie wydano nowego portable. Lokalny panel otrzymał opisany powyżej moduł logiki; pełny wariant badawczy pozostaje oddzielny.


## 22 października 2026 — nauka wypowiedzi i pętla internetowa

Poprzednie główne README zachowano w [archiwum](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_2026-10-21_BEFORE_WEB_LEARNING.md). Główny opis zawiera teraz stan aplikacji, lokalną obsługę nauki i aktualny pomiar rozmiaru.

Pobrano OpenAssistant OASST1 z zachowaniem pochodzenia i licencji Apache-2.0. Rozmowy rozdzielono według całych drzew. Kontrola usunęła całe drzewa z błędami i słabymi odpowiedziami. Po dodaniu autorskich przykładów uzyskano 53 przykłady treningowe, 10 do doboru i 8 testowych. Autorskie zestawy mają wspólne rodziny umiejętności, więc nie dowodzą szerokiej generalizacji. Powtórki obejmowały 1002 wcześniejsze zadania.

Trening obu generatorów wykonał 120 kroków. Wybrany według wskaźnika NLL krok 40 obniżył testowe NLL z 6,2430 do 5,8440, lecz pełne nowe wypowiedzi pozostały niepoprawne (0/8). Fakty zachowano 8/8, ale definicje spadły z 16/16 do 6/16. Wariant odrzucono. Wniosek: spadek błędu przewidywania tokenów nie wystarcza do wyboru dobrego rozmówcy.

Do zachowanej reprezentacji dwóch rdzeni dołączono dwa przyczynowe bloki transformera i odczyt słownika: 1 285 376 uczonych parametrów. Rdzenie bazowe mają 10 147 343 parametry i pozostają zamrożone. Pierwsze ćwiczenia sterowane pełnymi wygenerowanymi odpowiedziami opanowały cztery przykłady. Początkowa zbyt sztywna kontrola wszystkich wypowiedzi odrzuciła dziewięć dalszych rund, choć pierwsza poprawiała liczbę dokładnych odpowiedzi do sześciu, zachowując poprzednie cztery.

W kolejnej pętli dopuszczono zmiany nieopanowanych wypowiedzi przy zachowaniu opanowanych, dodano do 20 kroków naprawczych przed cofnięciem oraz odrębny nadzór każdej zapamiętanej odpowiedzi. Ostatni odczyt do niniejszej publikacji: 11/30 pełnych odpowiedzi uczących, runda 9. Wynik nie jest testem nieznanych rozmów. Zachowywane są migawki wag i historia decyzji. Model nie został automatycznie podmieniony w panelu.

Przygotowano lokalne BAT-y i panel nauki z internetu: checkbox Wikipedii i tematów, dodawanie tematu lub linku polskiej Wikipedii, limity czasu/rund, Start/Stop, kolorowe komunikaty postępu oraz powtórki pamięci. Pętla pobiera fragmenty ze źródłem, rewizją i SHA-256 i uczy odczytu podanej treści. Nie wykonuje instrukcji ani kodu z pobranych stron. Odznaczenie źródła wyłącza nowe uczenie z niego, zachowując powtórki opanowanej pamięci.

Pełna runda w odizolowanej kopii pobrała artykuł „Algorytm”, wykonała krok treningu i prawidłowo cofnęła pogorszenie (błąd 0,181 → 0,184, zachowany 0,181). Sprawdzono inicjalizację panelu z 12 tematami. Dodano sekcję „Nauczyłem się” z rzeczywistymi wygenerowanymi odpowiedziami: tylko zaakceptowana runda może ogłosić nowe opanowanie przykładu; w przeciwnym przypadku pokazywana jest wypowiedź ćwiczona lub zachowana. Sprawdzono rozróżnienie zaakceptowanej i odrzuconej aktualizacji oraz ponownie inicjalizację panelu.

Zmierzono kod, dane, modele i środowisko. [Pomiar z 22 października](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/SIZE_2026-10-22.md) zastępuje historyczne wartości rozmiaru jako bieżący punkt odniesienia. Publikacja zawiera wyłącznie dokumentację; kod, wagi, dane i prywatne ścieżki pozostają poza aktualizacją repozytorium.


### Kontrola zapominania i przekazanie pętli

Po publikacji punktu 11/30 nadzór wykrył utratę jednej wcześniej opanowanej rozmowy o dziewczynce i mapie. Zachowano migawkę rundy 8 (10/30), a następna seria obowiązkowo powtarzała gubioną wypowiedź i chroniła każdą wcześniej opanowaną odpowiedź. Zakończyła 9 rund, zachowując 10/30; błąd odpowiedzi uczących spadł z 0,45820 do 0,45494. Przyjęto 3 rundy, 6 cofnięto. Ostatnie wagi i 10 zapisów pamięci przekazano pętli BAT; model rozmowy w aplikacji pozostał bez zmian.

Panel nauki ma teraz zwartą siatkę tematów, rzeczywiste wypowiedzi po rundach oraz cofnięcie o dwie zaakceptowane wersje. Cofnięcie podczas pracy jest kolejkowane do bezpiecznego zatrzymania i odtwarza zarówno wagi, jak i pamięć. Sprawdzono kolejkowanie przy blokadzie treningu, przywrócenie dwóch wersji oraz odmowę, gdy brak dostatecznej historii.

## 23 października 2026 — wspólny dekoder, źródła i równowaga powtórek

Połączono dwa enkodery z natywnym dekoderem autoregresyjnym przez uwagę krzyżową. Łącznie model ma 14 853 139 parametrów. Kod i pełne wagi pozostają lokalnie. Zapis obejmuje obie części wejściowe i dekoder; nie użyto wag zewnętrznego modelu językowego.

Wykryto brak przekazywania jawnych ról S1/S2 w jednej ścieżce oraz interpretowanie małych odchyleń uczonych flag jako prawdy przez konwersję na bool. Poprawiono przekazywanie ról i odczyt flag z progiem. Nie uznano tych poprawek za automatyczne potwierdzenie poprawności całej rozmowy.

Przyjęty przed ostatnią korektą zapis zachowywał 48/48 odpowiedzi i uzyskiwał 38/69 przypadków odczytu reguł. Sieć miała tendencję do wybierania T lub U, a odczyt F pozostawał błędny. Próba śledzenia wykazała, że zmiana źródła zmienia reprezentacje enkoderów i wyjście uwagi; sygnał docierał, mimo błędnej decyzji dekodera.

W jednej późniejszej, odrzuconej serii popełniono błąd w celu uczenia: lista klas zawierała T/F/F/U, a indeks celu U wskazywał drugie F. Poprawiono ją do unikalnego T/F/U, dodano sprawdzenie identyfikatorów tokenów i kierunku gradientu. Wadliwych wag nie przyjęto. Sama poprawka etykiet nie usunęła pozostałych błędów czytania.

Trening wskazywania fragmentu z wynikiem reguły poprawił odczyt do 46/69 i zachował poprzednie 38 poprawnych przypadków, ale dał 47/48 na chronionych faktach. Pomyłka dotyczyła odwróconej zmiany godziny. Harmonogram powtórek faworyzował 19→9; poprawiono dobór, dodając oba kierunki i obie role czasu.

Zrównoważony program miał 40 przykładów, po 20 z podpowiedzią i bez niej, po 20 pytań o czas aktualny i poprzedni. Wyniki każdej godziny występowały jednakowo często w tym programie. Oddzielono 16 zadań z nowymi parami i inną parafrazą, bez podpowiedzi. Dodatkowe powtórki pary 9/19 były symetryczne.

Punkt po 10 krokach dał 48/48, ale stracił jeden z 46 poprawnych przypadków logiki — U IMPLIES T. Odrzucono go. Przyjęto punkt po 6 krokach: **48/48**, zachowane **46/46**, a pełna kontrola odczytu dała **47/69**. Na nowych opisach czasu uzyskano **3/16**. To przyjęty punkt do dalszych testów, nie podmiana panelu ani potwierdzenie swobodnego rozumienia języka.

Nowa wspólna pętla internetowa rzeczywiście pobrała artykuł „Rekurencja” z Wikipedii (rewizja 80072510), przeprowadziła trening i wykryła pogorszenie: zachowano 23/38 poprzednich przypadków logiki, bez opanowania nowej definicji (0/1). Wagi odrzucono, a pętlę zatrzymano. Materiał zachowano z adresem, rewizją i skrótem treści; nie wykonywano kodu pobranego ze strony.

Pomiar przyjętego modelu: **59,41 MB** parametrów FP32 i **162,82 MB** pełnego zapisu ze stanem treningu. Katalog aplikacji z kodem, danymi, modułami i artefaktami, z wyszczególnionymi wyłączeniami, zajmuje **1 989,89 MB**. Nowy model jest przechowywany oddzielnie. Szczegółowy zakres jest w [pomiarze](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/POMIAR_TSI_2026-10-23.json).

Szczegóły obecnej oceny: [OCENA_TSI_2026-10-23.md](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/OCENA_TSI_2026-10-23.md). Poprzedni README przeniesiono do [archiwum](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_przed_ocena_2026-10-23.md).

## 23 października 2026 — korekta klas i odczytu wyniku ze źródła

Wykonano 16 aktualizacji pierwszej próby oraz 8 aktualizacji drugiej. Uczono oba enkodery i dekoder; reguły formalne pozostały zamrożone. Oceniano ponownie wczytane wagi i pełne odpowiedzi sieci, bez podmiany wyniku przez nauczyciela.

| Zapis | Zachowane wcześniejsze odpowiedzi | Tablica źródłowa | T | F | U | Decyzja |
|---|---:|---:|---:|---:|---:|---|
| Próba 1, krok 8 | 89/98 | 50/69 | 12/23 | 11/19 | 27/27 | Odrzucony |
| Próba 1, krok 16 | 92/98 | 45/69 | 15/23 | 4/19 | 26/27 | Odrzucony |
| Próba 2: wyrównanie i uwaga, krok 8 | 92/98 | 49/69 | 15/23 | 7/19 | 27/27 | Odrzucony |

Chronione 98 przykładów obejmuje 48 wcześniejszych odpowiedzi o faktach i języku, 47 poprawnych wyników logiki oraz 3 poprawne opisy czasu. Podwyższenie łącznego wyniku nie wystarcza do przyjęcia zapisu, jeżeli stracił wcześniej poprawne odpowiedzi.

Audyt pierwszej próby wykazał, że po doliczeniu powtórek udział celów wynosił **T 53, F 32, U 58**, mimo równej liczby nowych ćwiczeń. Druga próba wyrównuje łączny nadzorowany błąd klas: liczby przykładów to T 37, F 16, U 42, a wagi błędu dają każdej klasie taki sam łączny udział. Dodatkowo uwagę sieci uczono kierować na fragment „Wynik reguły”, zamiast na same operandy. Tablica jest materiałem źródłowym dla enkoderów; nie zastępuje wyjścia dekodera.

Pierwsza próba pokazała konkretny błąd: odpowiedź F dla `F NOR F`, chociaż źródło podawało T. Poprawa klasy F kosztem poprawnych odpowiedzi T została rozpoznana jako regresja.

Dodatkowy sprawdzian 16 nowych opisów czasu, z innymi pytaniami i liczbami, dał **0/16** dla bezpiecznych wag oraz **0/16** dla drugiej próby. Te sformułowania nie weszły do treningu. Oddzielnie przygotowano program 72 przykładów czasowych; w tym etapie go nie trenowano. Starszy test 3/16 i nowy sprawdzian stanowią odrębne zbiory. Trzy poprawne przykłady starszego zestawu weszły do chronionych powtórek nowych prób.

**Stan przyjęty pozostaje bez zmian:** 48/48 wcześniejszych odpowiedzi, odczyt źródła logicznego 47/69 (T 21/23, F 0/19, U 26/27), starsze parafrazy czasu 3/16. Nowe próby odrzucono. Panel, MUZ, walidator i paczki portable nie otrzymały tych wag. Nauka internetowa pozostaje zatrzymana.

## 23 października 2026 — większy model i pięć etapów powtórek

Model rozszerzono z 14 853 139 do **23 018 523 parametrów**, a dekoder z 4 do **12 warstw**. Przy samym rozszerzeniu 98/98 wcześniejszych odpowiedzi i ich logity pozostały identyczne.

Następnie odtworzono pięć zapisanych programów nauczania w kolejności od najstarszego do najnowszego. Powtarzano poprawne etykiety, a nie wcześniejsze błędne wypowiedzi sieci. Oryginalne enkodery i cztery warstwy dekodera były zamrożone; uczyło się osiem dodanych warstw.

| Etap | Aktualizacje łącznie | Zachowane odpowiedzi | Logika ze źródłem |
|---|---:|---:|---:|
| 1/5 | 16 | 107/109 | 45/69 |
| 2/5 | 26 | 106/109 | 45/69 |
| 3/5 | 42 | 104/109 | 45/69 |
| 4/5 | 50 | 105/109 | 48/69 |
| 5/5 | 60 | 102/109 | 46/69 |

Końcowa próba: znane opisy czasu **15/40**, nowe opisy bez podpowiedzi **0/16**. Znany zestaw 40 przykładów był materiałem powtórek. Zestaw nowych opisów nie był materiałem treningu tego eksperymentu.

Nie przyjęto nowych wag: zachowano zapis sprzed powtórek.

**Nie osiągnął wymaganego poziomu.** Model badany nie został wdrożony do panelu, MUZ ani walidatora. Internetowy trening wag pozostaje wyłączony.

## 23 października 2026 — dalsze utrwalanie po pięciu etapach

Trening kontynuowano z ostatnich wytrenowanych wag, z mniejszym tempem aktualizacji. Co krok powracano do utraconych odpowiedzi, a zestaw ochronny rozszerzono ze 109 do **117**: dodano osiem nowych poprawnych przypadków. Starsze parametry pozostały zamrożone; uczyły się dodane warstwy.

| Aktualizacje | Zachowane ze 117 | Zachowane z pierwotnych 109 | Logika | Znane godziny |
|---|---:|---:|---:|---:|
| 8 | 106/117 | 104/109 | 44/69 | 15/40 |
| 16 | 109/117 | 107/109 | 46/69 | 15/40 |

Nowe opisy czasu, nieużywane w treningu tej serii: **0/16**. Wynik końcowy T/F/U: **T 20/23**, **F 0/19**, **U 26/27**.

Zachowano wcześniejszy przyjęty zapis; kolejne wytrenowane wagi pozostają materiałem do dalszych badań. Panel, MUZ i walidator nie zostały podmienione. Internetowy trening wag pozostaje wyłączony. **Nie osiągnął wymaganego poziomu.**

## 23 października 2026 — równy udział stanów w całych powtórkach

Audyt poprzedniej serii wykazał nierówny udział stanów po dodaniu materiału ochronnego: **T 46, F 22, U 65** ekspozycji logicznych. Wyrównano cały dobór przykładów, łącznie z powtórkami. Kolejne osiem aktualizacji zawierało dokładnie **T 32, F 32, U 32** ekspozycje. Liczby potwierdzono z faktycznie użytych partii.

Po dodatkowym treningu: **109/118** zachowanych odpowiedzi, w tym **100/109** z pierwotnego zestawu i **48/48** podstawowych. Logika **51/69**; T **16/23**, F **12/19**, U **23/27**. Znane godziny **15/40**, nowe opisy **0/16**.

Najnowszy zapis zachowano do dalszych badań, bez zastąpienia wcześniejszych przyjętych wag. **Nie osiągnął wymaganego poziomu.** Bez podmiany panelu, MUZ i walidatora.

## 24 października 2026 — utrwalanie odczytu źródła

Wykonano osiem aktualizacji od ostatnich wytrenowanych wag. Utrzymano równą liczbę ekspozycji logicznych wraz z powtórkami: **T 32, F 32, U 32**. Uczenie uwagi na właściwy wynik ze źródła objęło również materiał ochronny. Zmniejszono tempo aktualizacji i powtarzano utracone fakty. Enkodery i cztery starsze warstwy dekodera pozostały zamrożone; trenowano osiem dodanych warstw.

Kontrola zapisanych i ponownie wczytanych wag: **113/124** zachowanych odpowiedzi, **104/109** z pierwotnego zestawu, **48/48** podstawowych. Logika **49/69**, znane godziny **16/40**, nowe opisy czasu **0/16**.

Rozkład logiki: **T 16/23**, **F 7/19**, **U 26/27**.

Sprawdzono hipotezę o wymuszaniu dwóch stanów na aktywnej ścieżce: T/F/U mają osobne tokeny w obu tokenizerach, ich reprezentacje w obu enkoderach są różne, a dekoder wybiera z pełnego słownika. Niezależnie zweryfikowano 69 wyników tablic reguł. Nie stwierdzono twardej zamiany U na T/F w tych punktach. Błędne odpowiedzi dla oczekiwanego F: osiem T i cztery U; dla oczekiwanego U: jedno T.

Zachowano nowe wagi do dalszych badań; przyjęty wcześniej zapis pozostaje bez zmian. **Nie osiągnął wymaganego poziomu.** Bez wdrożenia nowych wag do panelu, MUZ i walidatora. Trening internetowy pozostaje wyłączony.



## 2026-10-24 — połączenie wyuczonej macierzy logiki

Naprawiono odczyt wydzielonego wyrażenia w opisach PL/EN i wywołanie macierzy operatorów. Dodano wspólną paczkę badawczą zachowującą jej wagi. Testy: 138/138 poleceń, 148/148 złożeń, 6/6 HTTP, 105/105 pozostałych odpowiedzi identycznych. Nie zmieniono przyjętych wag językowych. [Pełny raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/POLACZENIE_LOGIKI_TSI_2026-10-24.md).


## 2026-10-24 — TIMDR: kontrolowane generowanie i dynamika znaczenia

Dodano kontrolę macierzy znaczenia w uczonym generatorze fraz aplikacji oraz ograniczanie tokenów we wspólnym modelu badanym. Jawne zdarzenia tworzą kolejne stany bez nadpisywania historii. Wyniki: 0/16 → 16/16 na nowych zadaniach czasowych przy dostarczonych macierzach, 3/4 → 4/4 wcześniejszych, 6/6 dynamiki/ról/negacji, 105/105 zachowanych pozostałych odpowiedzi. Polski czytnik: 5/7 prób rozstrzygniętych, 2 nierozstrzygnięte. Bez treningu i podmiany wag, bez nowej portable. [Raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/TIMDR_JEZYK_TSI_2026-10-24.md).

## 2026-10-24 — przebudowa rozmowy, skróty i zdania złożone

Wdrożono wspólny podział zdań oraz obsługę wielu członów z zachowaniem spójników, negacji i kierunku przyczyny. Zlikwidowano globalny wymóg jednej relacji przy generowaniu fraz; zachowano ograniczenia techniczne analizy. Kontrole: 15/15, 116/116, 13/13, generowanie 4/4 i API 3/3.

Próba starego panelu: 12 tur, 9 odmów, dwie nietrafione Wikipedie i jedno nietrafione wyszukanie dokumentu. Osobny nowy przepływ uruchamia rzeczywisty generator, ale jego pierwszy trening zachował 47/48 dawnych odpowiedzi i nie poprawił swobodnej rozmowy do wymaganego poziomu. Wagi odrzucono jako domyślne. Trening na poprawionych wejściach: **52 aktualizacje i 3 aktualizacje powtórki**. Powtórka odzyskała **46/48 → 48/48** wcześniejszych odpowiedzi. W ręcznej ocenie pełnych odpowiedzi: **0/2 powtórek** i **1/4 nowych wypowiedzi**. Poprawna odpowiedź czasowa wymagała kontroli macierzowej podczas ponownego generowania. Nowych wag nie ustawiono jako domyślnych.

Zbadano także zakończenia: EOS sieci w 12/12 odpowiedzi, identyczne wyniki przy 72 i 160 tokenach na dwóch wejściach, zachowanie znaków 54/54. [Szczegóły](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ROZMOWA_I_SKLADNIA_TSI_2026-10-24.md).

## 2026-10-24 — nauka pełnych zdań i osobna warstwa wyjściowa

Przygotowano 514 przykładów oraz 22 odłożone próby. Wariant z osobną warstwą wyjściową zachował przed nauką 48/48 odpowiedzi i identyczne logity. Etap podstaw osiągnął 8/8 pełnych odpowiedzi przy zachowanych 48/48 dawnych. Nowe proste sformułowania: 2/4; nowe role: 0/18. Wybrano zapis po 50 głównych aktualizacjach, odrzucając regresję po 60. Nowy wariant: 23 542 811 parametrów, 94.67 MB wspólnych wag.

Rozszerzono ochronę do 56/56. Próba tej samej wiadomości bez historii i po powitaniu wskazała brak utrwalonej obsługi kontekstu; przygotowano 56 rozmów i 8 odłożonych kombinacji do kolejnego etapu. Domyślnych wag, MUZ, walidatora i portable nie podmieniono. [Szczegółowy raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/PODSTAWY_JEZYKA_TSI_2026-10-24.md).


## 2026-10-24 — wspólna nauka enkoderów, H512 i generatora

Porównano trzy warianty z tego samego zapisu: dodane warstwy generatora, cały generator i oba enkodery z generatorem. Warianty generatora uzyskały 13/56 na uczonych rozmowach i 0/8 na odłożonych kombinacjach; wspólny wariant po 10 aktualizacjach: 8/56 i 1/8, przy zachowanych 56/56 odpowiedziach.

Potwierdzono przepływ gradientu i zapisane zmiany obu enkoderów, w tym obu pamięci H512. Sześć macierzy reguł zachowało wartości. Zapisywany jest zgodny komplet wag źródłowych enkoderów i generatora; podczas uczenia nie buforuje się nieaktualnych reprezentacji ukrytych. Gorszy zapis po 15. aktualizacji odłożono. Model: 23 542 811 parametrów, 94.67 MB wspólnych wag. Domyślnych wag i portable nie podmieniono. [Raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/WSPOLNY_TRENING_KONTEKSTU_TSI_2026-10-24.md).


## 2026-10-24 — odrzucona kontynuacja wspólnego treningu

Kontynuacja ze zgodnego kompletu wag obu enkoderów i generatora: zachowany zapis 56/56, uczone rozmowy 8/56, odłożone kombinacje 1/8 → 0/8. Późniejszy zapis dodatkowo pogorszył chronione odpowiedzi. Zachowano poprzedni model badawczy; wdrożenia nie zmieniono. [Raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/KONTYNUACJA_WSPOLNEGO_TRENINGU_2026-10-24.md).


## 2026-10-24 — odróżnianie bieżącego polecenia od historii

Wspólny trening obu enkoderów i generatora z porównaniem poprawnej odpowiedzi bez historii i odpowiedzi z kontekstem. Chronione 56/56; uczone rozmowy 9/56; porównawcze dwie tury 1/8; dodatkowe trzy tury 0/8. Zachowano poprzedni model badawczy; wynik nie uzasadnia podmiany. [Raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ODROZNIANIE_POLECENIA_OD_HISTORII_2026-10-24.md).


## 2026-10-24 — znaczniki ról rozmowy i zgodność wejścia słownikowego

Naprawiono zachowanie specjalnych znaczników przez warstwę słownikową bez usuwania kontroli zgodności. Dawne wejścia 56/56 identyczne w obu enkoderach. Wspólny trening: 5/56 → 8/56 na uczonych kontekstach; chronione 56/56; dwie tury 0/8, dodatkowe trzy tury 0/8. Zachowano poprzedni model badawczy. [Raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ROLE_ROZMOWY_I_TRENING_TSI_2026-10-24.md).


## 2026-10-24 — rozdzielenie bieżącego polecenia i pamięci rozmowy

Po dwóch rundach treningu bez poprawy odłożonych rozmów porównano przepływy wejścia. Generator dostaje bieżące polecenie, oba enkodery pełną historię. Bez zmiany wag: dwie tury 1/8 → 8/8, trzy tury 0/8 → 8/8, chronione 56/56. Zapisano osobny wariant badawczy; aplikacji i portable nie zmieniono. Następne próby obejmą pytania zależne od wcześniejszych informacji. [Raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/BIEZACE_POLECENIE_I_PAMIEC_TSI_2026-10-24.md).

## 2026-10-24 — inkubator pamięci i trening odczytu historii


## Aplikacja

Do istniejącego panelu TSI podłączono inkubator pamięci. Wagi działającego modelu pozostały te same; dużego modelu badawczego nie podstawiono przy tej operacji. Pamięć jest lokalna i rozdzielona według profili przeglądarki. Nowa rozmowa zmienia historię bieżącego dialogu, zachowując zapisane informacje.

Zapis obejmuje źródło użytkownika, temat, pochodzenie oraz stan informacji. Rozpoznana spójna wypowiedź użytkownika nie jest automatycznie uznawana za fakt o świecie. Nierozstrzygnięta treść może zostać przywołana jako dokładny cytat. Odpowiedzi modelu nie są w tym trybie obserwacjami do zapisu.

Początkowy limit wynosi 10 000 wpisów i 64 MiB treści; może rosnąć do 200 000 wpisów i 1 GiB treści. To limity logiczne, bez rezerwowania od razu takiej przestrzeni. Fizyczna baza z indeksami zajmuje dodatkowe miejsce. Po osiągnięciu limitu nie nadpisuje się po cichu starszych źródeł.

Tematy mają powiązania przez wspólne obiekty. Dostępne są wybór kontekstu, uśpienie i zamknięcie tematu, jawne rozstrzyganie sprzeczności, cofanie jednej lub dwóch decyzji, pauza zapisu i odczytu, eksport oraz potwierdzane wyczyszczenie. Wątpliwość dotycząca kontekstu powoduje pytanie do użytkownika. Zamknięty temat wymaga ponownego otwarcia.

## Sprawdziany na danych przykładowych

| Zakres | Wynik |
|---|---:|
| Zapis, trwałość, profile, konflikty, cofanie, rozmiar i równoległe zapisy | 18/18 |
| Trzy informacje przywołane po nowej rozmowie w aplikacji | 3/3 |
| Integracja HTTP: nowa rozmowa, pamięć, korekty, pauza, tematy i ochrona żądań | 20/20 |
| Powtarzane pytania po nowej rozmowie: przed / po | 0/15 → 15/15 |
| Wyszukiwanie w bazie 50 000 przykładowych wpisów | 60/60 |

Trzy informacje dotyczyły kolorów plecaków i położenia klucza. To ograniczona próba przywoływania podanych źródeł, nie sprawdzian dowolnej rozmowy.

## Czasy odpowiedzi

Pełne lokalne żądanie HTTP, 15 próbek na wariant: mediana **207,872 → 214,525 ms**, p95 **248,870 → 403,770 ms**. Obejmuje aplikację, JSON i lokalne połączenie; bez renderowania przeglądarki. W tej próbie poprawił się dostęp do informacji, a pełna odpowiedź nie przyspieszyła. Przy tak małej liczbie próbek p95 jest bardzo wrażliwe na pojedyncze opóźnienie.

Samo wyszukiwanie w niezmienionej bazie 50 000 wpisów, 60 zapytań: mediana **1066,448 → 14,206 ms**, p95 **1771,614 → 61,333 ms**. Poprawka wybiera najpierw rzadsze słowa z indeksu. Ten pomiar nie obejmuje analizy językowej, generowania ani HTTP.

## Osobny trening językowy

Wytrenowano czytnik ról czasowych i dopasowano do niego oba enkodery, pamięć H512 oraz generator. Sześć macierzy reguł pozostało bez zmian. Pytania wymagające wcześniejszej informacji: **5/12 → 7/12**. Próby stanu i zakresu danych: **28/28**. Chronione odpowiedzi: **56/56**. W rozmowach dwóch i trzech tur wynik ścisłego porównania wyniósł **7/8**; w pozostałym przypadku odpowiedź była krótsza i zachowała sens. Tych wyników nie należy sumować.

Wybrany wspólny zapis badawczy: **23 542 811 parametrów**, około **94,67 MB**. Osobny czytnik i środowisko wykonawcze nie są w tej liczbie uwzględnione. Model nie osiągnął wymaganego poziomu swobodnej rozmowy. Pamięć źródeł w aplikacji jest odrębna od tego treningu.

## Odniesienia i dalsza integracja

Przyjęto duże archiwum oraz niewielką porcję źródeł dobieraną do pytania. Tematy nie są odizolowanymi silosami. Obecny odczyt korzysta z indeksu tekstowego, odmiany słów i jawnych relacji; nie wdrożono tu wyszukiwania przez wektory semantyczne.

Punkty odniesienia: [MemGPT](https://arxiv.org/abs/2310.08560), [bloki pamięci Letta](https://docs.letta.com/v1-sdk/memory/memory-blocks), [pamięć LangGraph](https://docs.langchain.com/oss/python/concepts/memory), [LongMemEval](https://arxiv.org/abs/2410.10813), [zarządzanie kontekstem Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

Adaptacja nowej pamięci do MUZ i walidatora jest kolejnym etapem. Docelowo walidator ma prowadzić naukę z podpowiedziami i kontrolą kroków; samo podłączenie pamięci nie stanowi potwierdzenia tej umiejętności. Osobne README zostaną zaktualizowane po testach integracji. Automatyczne uczenie wag z internetu pozostaje wyłączone.

[README sprzed tej aktualizacji](docs/archiwum/README_before_memory_incubator_2026-10-24.md).


## 2026-10-24 — połączenie pamięci z MUZ i walidatorem


MUZ i walidator korzystają teraz z usługi rozmowy działającej instalacji TSI oraz inkubatora źródeł. Rozmowa nie wymaga uruchomienia osobnego serwera TSI: aplikacja uruchamia lokalny proces przez istniejącą konfigurację wspólnej instalacji. Ten etap nie instaluje dużego modelu badawczego ani nowych wag.

Każda aplikacja ma własną bazę rozmów i inkubatora. Profil przeglądarki jest nadawany po stronie serwera; użytkownik innego profilu nie otrzymuje jego zapisów. Nowa rozmowa zachowuje pamięć. Zapisane wypowiedzi użytkownika nie stają się automatycznie potwierdzonymi faktami o świecie. Przy niepełnym odczycie możliwe jest przywołanie dokładnego źródła.

Na stronach dodano rozwijany panel **TSI · rozmowa i pamięć**. Zawiera polecenia PL/EN, wysyłanie Enterem, nową rozmowę, przegląd źródeł, wybór i zamykanie tematów, pauzę pamięci, zatwierdzanie i odrzucanie informacji oraz cofnięcie jednej lub dwóch decyzji. Dane widoczne jako źródło nie są wykonywanymi poleceniami.

Bufor początkowy: 10 000 wpisów / 64 MiB treści; wzrost do 200 000 / 1 GiB treści. Fizyczny rozmiar bazy obejmuje dodatkowo indeksy. Nie jest to nowy pomiar rozmiaru portable. W ramach tego etapu zaktualizowano katalogi robocze; paczek ZIP i osobnych rozpakowanych portable nie przebudowano.

## Wyniki sprawdzianów

| Zakres | Wynik |
|---|---:|
| Przygotowane połączenie MUZ: pamięć po nowej rozmowie i restarcie procesu, profile, dodawanie, pauza | 5/5 |
| Przygotowane połączenie walidatora: te same kontrole | 5/5 |
| Działający MUZ: panel, pamięć, dodawanie, zarządzanie pamięcią, tabela budżetu, odrzucenie obcego pochodzenia | 6/6 |
| Działający walidator: panel, pamięć, dodawanie, zarządzanie pamięcią, wyznacznik macierzy, odrzucenie obcego pochodzenia | 6/6 |

Próby używały osobnych przykładowych profili: różne kolory plecaka w obu aplikacjach. Nie modyfikowano rachunków ani danych użytkownika. Test tabeli MUZ sprawdził odpowiedź interfejsu danych, nie kompletny plan oszczędnościowy. Test akademicki sprawdził wyznacznik macierzy 2 × 2; nie stanowi sprawdzianu wszystkich tematów.

## Rola nauczyciela i zarządcy

Istniejące obliczenia, geometria, całki i funkcje budżetowe nadal wykonują swoje zadania. Nowy panel rozmowy jest połączony z TSI, ale nie przejmuje automatycznie wszystkich bieżących danych formularzy i finansów. Nie należy zakładać, że pytanie w panelu odwołuje się do aktualnego rysunku bez przekazania jego danych.

Kolejnym etapem dla walidatora jest rozmowa nauczycielska powiązana z aktualnym zadaniem: wskazówki bez zdradzania wyniku, kontrola kroków, wyjaśnienia oraz dobór powtórek. Dla MUZ: rozmowa powiązana z wybranym planem i jawnym stanem budżetu. Swobodna rozmowa TSI nie osiągnęła wymaganego poziomu. Zwykłe używanie pamięci nie trenuje wag; internetowa pętla treningu pozostaje wyłączona.


## 24 października — kontekst i powtórki

Nowe ćwiczenia: 0/36 → 6/36; wcześniejsze odpowiedzi 56/56. Usunięto stały limit 2 faktów i 4 tur w wariancie rozwijanym. [Szczegóły](docs/KONTEKST_I_POWTORKI_TSI_2026-10-24.md).


## 24 października — powtórki, odczyt T/F/U i pamięć rekurencyjna

Wykonano powtórki 59 znanych przykładów przed nowym treningiem. Porównano projekcję statusów do pamięci z uczoną warstwą wyjściową. Następnie podłączono eksperymentalny stan rekurencyjny do generowania i porównano go z bazową siecią oraz ponownym podaniem źródła. [Dokładne wyniki i odpowiedzi](docs/REKURENCJA_I_ODCZYT_TFU_2026-10-24.md). Działających wag nie podmieniono.


## 24 października — trwała pamięć T/F/U i rekurencyjna pamięć robocza

Połączono istniejącą bazę inkubatora z pakowanymi statusami i pomocniczym stanem generatora. Naprawiono przekazywanie F/U bez odrzuconego źródła. Wykonano kontrolowany trening wyłącznie warstwy odczytu oraz sprawdzono pełne odpowiedzi i poprzedni interfejs. [Wyniki, zakres i odpowiedzi](docs/PAMIEC_HYBRYDOWA_TSI_2026-10-24.md). Wdrożone aplikacje i portable pozostały bez zmian.


## 24 października — dalsze powtórki F/U

Trening odczytu na 84 przykładach; kontrola 6/9 → 9/9, nowe imiona 6/6, poprzedni interfejs 1/4 → 1/4. [Odpowiedzi i zakres](docs/PAMIEC_HYBRYDOWA_TSI_2026-10-24.md). Aplikacji i portable nie podmieniono.


## 25 października — powtórki i źródła

Trening odczytu F/U na 148 przykładach. Starszy interfejs: 1/4 → 4/4, nowe źródła 8/8, wcześniejsze kontrole 15/15 → 15/15. [Wyniki i odpowiedzi](docs/TRENING_ODCZYTU_TSI_2026-10-25.md). Działające aplikacje pozostały bez zmian.


## 25 października — podłączenie odczytu F/U w panelu

Wdrożono ocenione wagi jako osobny, ograniczony moduł dla wybranego tematu inkubatora. Zgodność 11/11, uruchomiony panel 6/6 przez HTTP. Dodano wyłączenie i ponowne włączenie plikami BAT, zachowano poprzednie pliki. Głównego rdzenia, pełnej rozmowy ani portable nie podmieniono. [Zakres i wyniki](docs/WDROZENIE_ODCZYTU_FU_2026-10-25.md).

[README sprzed podłączenia odczytu F/U](docs/archiwum/README_before_scoped_readout_2026-10-25.md).


## 25 października — zatrzymanie wymuszania odpowiedzi i audyt

Przerwano wspólny trening po cofnięciu aktualizacji z wynikiem chronionym 80/83. Nowych wag nie wdrożono. Wyłączono podłączony wcześniej odczyt F/U i potwierdzono wcześniejszą odmowę w panelu. Zbadano rozbiór pytania, wybór tematu, słownik i rzeczywiste wywołanie logiki. [Ustalenia i stan](docs/AUDYT_ODMOW_I_ZNACZEN_TSI_2026-10-25.md).


## 25 października — słownik i lekcje tematyczne

Przebudowano zapis znaczeń, zachowując oddzielne gałęzie i źródła. Naprawiono zapętlenie pytania po wyjaśnieniu nowego słowa. Wdrożono zaplecze lekcji, panel odłożono. Wyniki: dialog 13/13, lekcje 10/10, aplikacja 14/14. Bez nowych wag. [Opis i testy](docs/SLOWNIK_I_LEKCJE_TSI_2026-10-25.md). [README przed zmianą](docs/archiwum/README_before_lexicon_2026-10-25.md).


## 25 października — pytania do lekcji

Podłączono matrycę obiekt–właściwość–liczba, istniejący odczyt ról i wyszukiwanie fragmentów przez formy podstawowe. Wyniki: 23/23 relacje, 12/12 pytania do lekcji i 10/10 kontrole HTTP. Wagi bez zmian, panel później. [Zakres](docs/PYTANIA_DO_LEKCJI_TSI_2026-10-25.md).


## 25 października — pytania do znaczeń słownikowych

Podłączono wyszukiwanie fragmentów przypisanych do znaczeń przez formy podstawowe słów, bez wklejania osobnej lekcji. Przykład o sumie kątów pochodzi z istniejącego hasła „trójkąt”; nie dopisano osobnej odpowiedzi z liczbą 180. Zachowano kwalifikator trójkąta płaskiego i źródło. Odczyt 12/12, aplikacja 10/10. Bez treningu wag i bez zmian w walidatorze.

## 26 października 2026 — wspólny model, logika i ciągły trening

Poprzedni główny opis zachowano w [archiwum README](docs/archiwum/README_przed_integracja_2026-10-26.md). Główny README opisuje bieżące możliwości, wyniki, uruchomienie oraz rozmiary.

Przebudowano połączenie odczytu z odpowiedzią. Nowy dekoder otrzymuje miękkie wskazanie źródła, uwagę nad jego reprezentacjami i uczoną bramkę kopiowania. Następnie do tego samego dekodera podłączono oba oryginalne enkodery wraz z H512. Zachowano wcześniejsze nauczone parametry; przeniesiono 89 istniejących stanów parametrów optymalizatora oraz kolejkę danych i losowość. Nowe połączenie otrzymało własne stany optymalizatora.

Sprawdzono rzeczywisty przepływ gradientów i aktualizację wag obu enkoderów, obu H512, czytnika i dekodera. W każdym H512 zmieniło się osiem sprawdzanych tensorów. Próbę aktualizacji cofnięto przed zapisaniem punktu startowego. Chronione sześć macierzy pozostało bez zmian, a ponowne odtworzenie modelu dało identyczne logity. Zintegrowana wersja odniesienia zachowała wszystkie 23 wcześniej poprawne odpowiedzi nowego dekodera.

Pierwszy generator po przebudowie osiągał 11/72 na zestawie rozwojowym, wyłącznie w części relacyjnej; na rzeczywistych tekstach nie dawał wtedy poprawnych odpowiedzi. Wspólny trening czytnika i dekodera dał 22/72 z regresją dawnych odczytów. Po przywróceniu czytnika i zachowaniu nowego dekodera sprawdzono 23/72: 15/24 relacje i 8/48 teksty, przy czym te osiem dotyczyło rozpoznania braku danych. Nie uzyskano wtedy poprawnych pozytywnych odpowiedzi do tych tekstów.

Po połączeniu pełnego układu ostatnia zakończona kontrola wag roboczych dała 55/312 w logice, 143/145 dawnych odczytów i 39/39 odpowiedzi. Wynik ten nie zastąpił automatycznie wersji odniesienia. Przykładowa zakończona runda pełnego układu wykonała 49 aktualizacji w limicie 30 minut nauki; razem z oceną końcową zajęła około 45 minut. Kolejne wznowienia zachowują optymalizator. Oceny niezmienionego modelu odniesienia mogą być użyte ponownie wyłącznie po sprawdzeniu dokładnej równości wag i materiału.

Dodano lekcje bramek T/F/U, negacji, zakresu otwarć „tak”, „nie”, „nie wiem”, wyrażeń złożonych i niewiadomych argumentów. Materiał krzyżuje otwarcia zdań ze wszystkimi wartościami logicznymi. Tryby dwustanowy i trójstanowy mają jawnie różne dziedziny. Sprawdzony moduł operatorów osiągnął 78/78 działań i 132/132 zadań odwrotnych trójstanowych oraz 36/36 i 60/60 dwustanowych. Odmówiono zamiany U na F w dwustanowej. Wyniki te dotyczą tego modułu, nie surowych wypowiedzi nowego generatora.

Czujnik zapisuje zakres formalnego obliczenia, tryb, liczbę wywołań i ślad operatorów. Odróżnia potwierdzenie, sprzeczność i brak rozstrzygnięcia. Dla treningu całego modelu dodatkowo kontroluje gradienty obu enkoderów i H512 oraz niezmienność reguł. Roboczego modułu weryfikacji dowolnych zdań nie włączono; jego interpretacja nie została sprawdzona.

Na prośbę właściciela uruchomiono sterowanie ciągłymi rundami z zachowaniem najlepszej sprawdzonej wersji. Kontynuacje: krótkie pauzy co 10 aktualizacji oraz dwie powtórki z czterokrotnie niższym krokiem. STOP zatrzymuje kolejne rundy; poważna regresja, błąd lub brak potrzebnego zapisu kończy pętlę. Model nie uczy się na własnych niezweryfikowanych odpowiedziach i w tej pętli nie pobiera nowych treści z internetu.

Samodzielna swobodna rozmowa nie osiągnęła wymaganego poziomu. Panel, MUZ, walidator i istniejące portable nie otrzymały tych nowych wag. Historyczne pomiary pozostały w swoich dokumentach. Dane rzeczywistych zadań pochodzą z [CLARIN-PL/PoQuAD](https://huggingface.co/datasets/clarin-pl/poquad), CC BY 4.0.



### 2026-10-28 — grupy wyrazów, czasy i tryb

Dodano grupy rzeczownikowe, liczebniki 0–10 i zbiorowe, uzgodnienie podmiotu liczebnikowego, czas przeszły i przyszły oraz tryb przypuszczający. Odpowiedzi dekodera: 20/20 grup i 18/18 czasów, 5/5 kontroli braków lub sprzeczności. Jedna linia wag, krok 2850, bez dodatkowego treningu. Poprzedni README zachowano w docs/archiwum/README_przed_czasami_2026-10-28.md.

### 2026-10-28 — odniesienia między zdaniami

Dołączono do lokalnego API wiązanie podmiotowych zaimków, kontrolę niejednoznaczności i izolowany kontekst zapytania. 7/7 odpowiedzi dekodera, 4/4 kontroli, 79/79 testów technicznych. Naprawiono utratę rodzaju przy odmianie zaimka i przekazywanie wybranego leksemu. Bez zmian wag i bez podmiany dawnych aplikacji.

### 2026-10-28 — odczyt ról z tekstu

Wprowadzono słownikowo-gramatyczny odczyt całych prostych zdań: przypadki, rekcja, zgodność i pełne pokrycie słów, niezależnie od ich kolejności. Połączono go z rzeczywistym dekoderem planów: 20/20 odpowiedzi, 8/8 kontroli, 82/82 testy techniczne. Baza i wagi bez zmian. Poprzedni README zachowano w docs/archiwum/README_przed_odczytem_zdan_2026-10-28.md.

### 2026-10-28 — tekst połączony z kontekstem

Automatyczny most od zwykłych prostych zdań przez role i rejestr obiektów do odniesień podmiotowych oraz dekodera. 6/6 odpowiedzi, 4/4 kontroli. Zachowano jedną linię wag bez nowego treningu.

### 2026-10-28 — pytania o kontekst

Dodano pytania przypadkowe o podmiot i dopełnienie, źródła odpowiedzi, rozróżnienie negacji i czasu, listy wyników bez powtórzeń i wykrywanie sprzecznych faktów. Rzeczywisty dekoder: 18/18 odpowiedzi, 13/13 kontroli; 90/90 testów technicznych. Bez treningu wag i bez podmiany dawnych aplikacji. Poprzedni README: docs/archiwum/README_przed_pytaniami_2026-10-28.md.

Przy sprawdzaniu pytań kim/czym domknięto obsługę „się” w nowym czytniku i pytaniach. Sprawdzian zdań rozszerzono do 22/22 i 10/10 kontroli.

### 2026-10-28 — polecenia, grzeczności i launcher

Polecenia na kontekście: 9/9 odpowiedzi dekodera i 7/7 kontroli. Źródła znaczeń podłączono do klasyfikacji osób, a nie do zastępowania wyników dekodera. Powitania i grzeczne reakcje PL/EN wdrożono do panelu 8791: 8/8. Przywrócono URUCHOM_TSI.bat. Dodano pełne paradygmaty wskazać i sprzeczność; zmieniono opis liczności na rzeczywistą liczbę unikalnych kluczy lematów. 99/99 testów technicznych, bez treningu wag. Poprzedni README: docs/archiwum/README_przed_poleceniami_2026-10-28.md.

### 2026-10-28 — kalendarz panelu i plan nauczyciela AI

Usunięto dwie blokady routingu pytań o święta i poprawiono rozpoznanie krótkiego zapytania rzeczownikowego. Kalendarz panelu 4/4 PL/EN, ponowione grzeczności 8/8. Obliczenia panelu 4/4, z zachowanym dokładnym 2/7. Przypisano podstawę urzędową. Zapisano plan konsultacji z nauczycielem AI; usługa pozostaje niepodłączona. Bez zmian wag nowego modelu.


## 29 października — nauczyciel AI, źródła i wspólna rozmowa

Dokończono lokalne podłączenie trzech dostawców, wyboru modelu i szyfrowania klucza Windows DPAPI. Brak klucza nie inicjuje połączenia AI. Kolejność po narzędziach lokalnych: konsultacja, Wikipedia, DuckDuckGo Instant Answer, podpowiedź offline. Odpowiedzi i źródła zapisuje się do sprawdzenia; zatwierdzenie wymaga notatki weryfikacyjnej. Eksport nie aktualizuje automatycznie wag. Testy protokołów korzystają z atrap odpowiedzi dostawców, a rzeczywiste połączenie AI wymaga klucza użytkownika. 18/18 testów nauczyciela, 9/9 kontroli panelu, 8/8 reguł grzecznościowych. Rzeczywisty odczyt publicznej Wikipedii potwierdzono na haśle Fotosynteza.

Wykryto brak osadzenia skryptu formularza w HTML oraz pętlę obserwatorów tłumaczenia: ponowne ustawianie niezmienionego lang powodowało aktualizację etykiet i następne odświeżenie. Podłączono skrypt i ograniczono zmianę lang do rzeczywistej zmiany języka. Opisy źródeł kończą się na granicy zdania lub jawnym wielokropku.

Na życzenie użytkownika przebudowano panel: centralna rozmowa około 3/4 szerokości na szerokim ekranie, jedno wspólne pole pytań, pomoc po lewej i narzędzia po prawej. Ustawienia w poziomym menu automatycznie zwijają się po zapisaniu, kliknięciu poza menu lub Escape. Wskaźniki opierają się na oddzielnym endpointcie stanu etapów serwera; po zakończeniu przestają migać. Zachowano obsługę Enter i nowej rozmowy. Wagi pozostają na kroku 2850.


### Utrzymanie kontekstu i naturalne polecenia — korekty 29 października

W rzeczywistej rozmowie polecenie całki i doprecyzowanie X^2 trafiły do Wikipedii jako film X-Men 2. Planer nie zachowywał oczekujących ról; dodano zapis celu, już podanych danych i braków osobno dla sesji oraz bezpieczne uzupełnianie wzoru, granic, próbek i macierzy. Anulowanie usuwa zadanie. Znormalizowano wybrane matematyczne zapisy słowne i wielką literę X. Jawny kontrakt arytmetyczny oraz pytanie o aktywny tekst mają pierwszeństwo przed selektorami słownika / wyszukiwania. Rozszerzono gramatykę opisu cech przez być + przymiotnik z kontrolą przypadku, liczby i rodzaju; nie wyłączano kontroli nieodczytanych fragmentów.

Wykryto równoczesne instancje serwera na tym samym porcie Windows, przez co próby trafiały także do starego kodu. Zatrzymano rozpoznane instancje, wprowadzono SO_EXCLUSIVEADDRUSE i identyfikator wersji aplikacji w odpowiedziach. Launcher korzysta z lekkiego health check. Zamknięcie ostatniej karty panelu daje 10 sekund na odświeżenie lub ponowne otwarcie, potem serwer kończy pracę; testy ostatniej karty, drugiej karty, odświeżenia i konfliktu portu: 4/4.

Pasek narzędzi jest przyklejony u góry. Podpis pola przeniesiono pod wspólne pole pytań. Lokalne autouzupełnianie PL/EN: Tab / kliknięcie wstawia, strzałki wybierają, Escape chowa, Enter wysyła. Sprawdzono rzeczywisty interfejs i zapisano trzy nowe zrzuty do README.

Wyniki kolejnych zestawów: 15/27 przed naprawą kontekstu, 25/29 po pierwszych korektach, 31/32 po rozszerzeniu, końcowa powtórka 32/32. Raporty zachowują pełne odpowiedzi lokalnie. Testy techniczne oczekujących zadań: 9/9; gramatyka cech: 5/5. Rzeczywiste angielskie doprecyzowanie całki i wynik potwierdzono. Wagi modelu pozostają na kroku 2850. Są to poprawki obsługi aplikacji, a nie ponowne wytrenowanie swobodnej rozmowy.


### Kontrola warunku wymiany rdzenia

Po sprawdzianie 32/32 panelu sprawdzono oddzielnie bezpośrednie API nowego modelu plan-decoder-8m-3. Formalna logika T AND U dała U. Dwie naturalne prośby aplikacyjne o całkę i plan oszczędzania zwróciły tylko początek wejścia („Oblicz”, „Przygotuj”), bez wykonania zadania. Nie uznano sprawnego programu otaczającego model za dowód gotowości samodzielnego rdzenia; pełnej wymiany wag / modelu w MUZ i walidatorze nie wykonano. Konfiguracje obu aplikacji wskazują tę samą instalację TSI; poprawione doprecyzowanie całki sprawdzono przez ich rzeczywiste połączenia, przy oddzielnych profilach testowych pamięci.


### Naprawa bezpośredniego API rdzenia — wybór zadania i pojedynczy koordynator

Przyczyną odpowiedzi „Oblicz” i „Przygotuj” był wybór trybu: nierozpoznane wejście auto kierowano do ćwiczenia kopiowania słowa. Próba uruchamiała sam rdzeń, więc nie wynikała z dwukrotnego przekazania przez walidator. Dodano do wspólnego API macierzowy planer zadania, wykonanie lokalnego solvera, niezależne sprawdzenie i emisję przez istniejący dekoder planu. Nie trenowano ponownie ani nie zamieniano wag. Jawne zadanie application z operation / params pomija odczyt polecenia; liczba wykonań i sprawdzeń jest raportowana oddzielnie. Oczekujące dane są zachowywane według identyfikatora rozmowy.

Ponowione obie pierwotne prośby: całka pi daje pi*x + C, plan oszczędzania bez danych powoduje pytanie o nie. W większej próbie sprawdzono rzeczywisty projekt budżetu na danych syntetycznych. Wykryty błąd JSON na granicy solvera dotyczył dat; dodano zapis ISO oraz zachowanie dokładnych wartości Decimal. Opis budżetu jest czytelny w PL/EN, a dane strukturalne pozostają dostępne do sprawdzenia. Kontrola dekodera nie zastępuje jego niepoprawnej emisji poprawnym tekstem referencyjnym.

Sprawdzian nowego API: 14/14 (próby obejmujące inne wzory, uzupełnienie danych, PL/EN, przeczenie, nieznane żądanie, formalną logikę, zadanie już przygotowane oraz budżet). Pełny zestaw techniczny rozszerzono o kontrolę pojedynczego wykonania, sesji, weryfikacji, dat i widoku budżetu. Publikacja runtime zachowuje ten sam checkpoint 2850 i jego SHA. Pełna wymiana modelu w aplikacjach nadal wymaga osobnego potwierdzenia ich obsługiwanych działów.

Końcowy zestaw techniczny po dodaniu kontroli prezentacji budżetu: **117/117**. Ponowiony sprawdzian rzeczywistych odpowiedzi: **14/14**. Checkpoint 2850 i jego suma pozostają takie same; zmienił się opublikowany lokalnie zestaw plików runtime i jego chroniony manifest.
