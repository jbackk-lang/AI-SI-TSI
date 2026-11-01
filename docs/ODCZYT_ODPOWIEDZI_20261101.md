# Odczyt danych i pełne odpowiedzi — 1 listopada 2026

W lokalnej aplikacji włączono ścieżkę: pytanie → odczyt nazwanych pól → kontrola źródła i roli → plan zdania → wykonanie planu przez dekoder TSI → kontrola końcowego tekstu.

Przykład: dodaj w „Dokumenty i tekst źródłowy” tekst `Objętość: 3 l. Gotowanie: 75 min.`, zaznacz pracę z materiałem i zapytaj „Jaka jest objętość?”. Odpowiedź: **Wartość pola „Objętość” wynosi 3 l.** Pytanie „Podaj obie wartości” daje dwa pełne zdania. Zmiana materiału z 3 l na 8 l zmienia odpowiedź na 8 l.

Sprzeczne wartości tego samego pola wymagają uzgodnienia. Niepotwierdzony odczyt nie otrzymuje zmyślonej liczby. Pytanie o zaznaczony materiał nie jest już przejmowane przez domyślne wyszukiwanie w Wikipedii; jawne polecenie wyszukiwania pozostaje osobną operacją.

Zakres: krótkie dane zapisane jako `Nazwa: wartość`. Materiał i pytanie muszą mieścić się w oknie 512 tokenów bajtowych. Dłuższy materiał przechodzi do dotychczasowego czytnika, bez cichego obcinania. Sprawdzono pytania po polsku i polskie lub angielskie brzmienie odpowiedzi. Nazwy pól źródłowych są zachowane.

To generowanie według jawnego planu gramatycznego. Dekoder emituje tekst; błędny tekst jest odrzucany, a nie podmieniany na wzorzec. Surowy generator swobodnej rozmowy nie osiągnął wymaganego poziomu i nie został włączony w tej ścieżce.

Kontrole: 23/23 prób pełnych zdań (w tym nowe etykiety, jednostki i godziny), 10/10 prób całej aplikacji (w tym zmiana danych w tej samej rozmowie), odrzucenie celowo uszkodzonego wyjścia. Wagi nie były zmieniane. Czas po rozgrzaniu w podstawowej próbie aplikacji: około 2–3 s; start procesu jest dłuższy. Te wyniki dotyczą opisanych prób i zakresu.

Dotychczasowe narzędzia matematyczne, powitania i główny rdzeń aplikacji pozostają aktywne. Nowy moduł jest lokalnym dodatkiem o identyfikatorze `TSI-grounded-step-3944`; stan aplikacji pokazuje go oddzielnie od głównego rdzenia. To nie jest pełna wymiana modelu we wszystkich zastosowaniach.
