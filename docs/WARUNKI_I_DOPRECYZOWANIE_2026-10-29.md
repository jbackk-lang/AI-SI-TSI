# Warunki zadania i doprecyzowanie — 29 października 2026

Usunięto wykryte gubienie granic całki w istniejącym panelu TSI i w nowym lokalnym API. Czytnik wiąże dosłowny wzór, dolną i górną granicę niezależnie od zapisu przed lub po wzorze. Dwukropek nie jest wymagany dla obsługiwanych pełnych konstrukcji. Działanie, rozpoznanie danych, wykonanie solvera i sprawdzenie wyniku zachowują oddzielne role.

Pamięć trwającego zadania przechowuje rozpoznane wartości i nazwy brakujących pól. Podanie wzoru nie usuwa wcześniej podanych granic. Para granic w odpowiedzi może uzupełnić lub zmienić zakres przed wykonaniem; zmiana jest zachowana także przy kolejnym doprecyzowaniu. Poszczególne rozmowy mają oddzielny stan. Anulowanie usuwa zadanie oczekujące; kompletne nowe polecenie nie dziedziczy granic poprzedniego.

| Wpis użytkownika | Sprawdzony wynik |
|---|---|
| Oblicz całkę z x^2 od 0 do 3 | Całka oznaczona: **9** |
| Calculate integral from 0 to 3 of x^2 | Definite integral: **9** |
| Oblicz całkę z sin(x) od 0 do pi | Całka oznaczona: **2** |
| Oblicz całkę od 0 do 3 → x^2 | Prośba o wzór → **9** |
| Oblicz całkę od 0 → od 1 do 3 → x^2 | Doprecyzowanie granic i wzoru → **26/3** |
| Oblicz całkę nieoznaczoną z x^2 od 0 do 3 | Prośba o wybór rodzaju całki; warunki nie są pomijane |

Odczyt sprawdzono także dla brakującej jednej granicy, ułamków, liczb ujemnych, dziesiętnego przecinka w granicy oraz stałej pi. Sprzeczne zakresy, nierozpoznane dodatkowe warunki i granice przypisane niejednoznacznie do działania wymagają doprecyzowania. To rozszerzenie obsługi danych matematycznych i kontynuacji zadania; swobodna rozmowa nie osiągnęła wymaganego poziomu.

Kontrole: **12/12** nowych testów jednostkowych z wieloma wariantami, **19/19** dotychczasowych testów, **10/10** scenariuszy przez rzeczywisty solver i obie ścieżki wykonania oraz **6/6** scenariuszy uruchomionej aplikacji HTTP. Wyniki nie są sumowane w jedną ogólną ocenę inteligencji. Zachowano sprawdzenie stałych reguł logicznych, surowe odpowiedzi i poprzednie pliki źródłowe. Kod nowego czytnika objęto manifestem chronionej wersji API.

W tym etapie nie trenowano ani nie podmieniano wag. Najnowszy stan dalszego uczenia pozostaje na kroku **2869**; zatwierdzona wersja wykonawcza korzysta z kroku **2850**. ZIP-y, wydania demo i portable nie zostały przebudowane. Poprawiony wspólny moduł istniejącej aplikacji jest dostępny również dla konsumentów korzystających z tej instalacji TSI, bez wymiany modelu.
