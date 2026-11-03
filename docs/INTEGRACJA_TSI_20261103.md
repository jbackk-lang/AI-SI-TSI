# Podłączenie wspólnego TSI — 3 listopada 2026

Aktualna lokalna obsługa: **2026-11-03-consumers-11**. Moduł odpowiedzi pozostaje na kroku 5217 (9 074 672 parametrów). Większa sieć treningowa nie jest wdrażana tą aktualizacją.

Walidator i MUZ czytają ten sam lokalny kod TSI; przechowują rozmowy i pamięć osobno. Jawne polecenia matematyczne trafiają do wspólnej obsługi zamiast do starszych przechwyceń aplikacji. Kontekst panelu i jawne działania nauczyciela zachowują swoje odrębne ścieżki.

Podpis wersji obejmuje teraz również przelicznik w rozmowie, zadania łączone, ramki danych, odzyskiwanie odpowiedzi i moduły źródeł. Ich zmiana przeładowuje proces rozmowy przy kolejnym żądaniu. Rozmowa jest zapisana lokalnie i odtwarzana po przeładowaniu. Zmiana kontekstu panelu usuwa aktywne dane poprzedniego zadania matematycznego.

## Co sprawdzono

W każdej aplikacji **15/15 prób podłączenia**: jednostki, zadanie ruchu, korekta czasu, audyt błędnego podstawienia ucznia, kontynuacja po zamknięciu i ponownym uruchomieniu procesu rozmowy, inny profil, zmiana zakresu panelu, audyt samodzielny, kąty podawane osobno, angielska konwersja, odczyt zdania i pytanie o przyczynę. Dodatkowa kontrola walidatora sprawdziła wyznacznik −2, a MUZ brak danych potrzebnych do planu budżetu.

W każdym działającym panelu dodatkowo **7/7 prób HTTP**. Profile testowe były osobne od kont użytkownika. Nie używano rachunków ani prywatnych kwot jako danych sprawdzianu. Odczyt panelu budżetu i narzędzia finansowe MUZ nie zostały zastąpione modelem ruchu.

Podczas integracji wykryto, że ogólne „Dlaczego?” po przeczytanym zdaniu było przechwytywane przez wyjaśnianie obliczeń. Naprawiono wybór zakresu i ponowiono testy w obu aplikacjach. Zweryfikowano również, że podpis wykrywa dodanie i zmianę nowego modułu zadań.

## Zakres możliwości

Jednostki zachowują dokładne ułamki i sprawdzają wymiary. Audyt obejmuje jedną zmienną x i porównanie 2–10 równań, z dokładnymi zbiorami rozwiązań równań wymiernych do stopnia 6. Jedna równość może być sprawdzana jako tożsamość. Dostępne dziedziny: rzeczywiste, całkowite, x≠0, x>0 i x≥0.

Zadania łączone obejmują ruch jednostajny i trzy wielkości: drogę, czas i prędkość. Kolejność narzędzi: role ilości → jednostki → model relacji → solver → audyt równania → wyjaśnienie. Rozwiązanie ucznia jest porównywane z modelem zadania i jego dziedziną, nie tylko z następnym wierszem rachunku.

## Historia obecnej aktualizacji

1. W rozmowie znaleziono gubienie kontekstu trójkąta, błędny wybór narzędzia dla czasu i wyszukiwanie treści pytania o źródło zamiast wskazania źródła poprzedniej odpowiedzi.
2. Dodano zbieranie danych, korekty, powroty do zadań i odczyt zatwierdzonej wiedzy przy odmianie słów i innym sformułowaniu pytania.
3. Sprawdzono podobne zadania. Pierwszy zestaw: 448/504; po naprawie wyboru początku/końca zdarzenia: 568/568 rozszerzonych wariantów.
4. Podłączono istniejący przelicznik do rozmowy. Wyniki: 36/36 przypadków i 7/7 w panelu.
5. Następnie podłączono audyt równań. Wyniki: 20/20 przypadków i 8/8 w panelu. Zachowano znak ≠ w nagłówkach z założeniami.
6. Połączono narzędzia w zadaniach o ruchu jednostajnym. Wyniki: 19/19 przypadków i 13/13 kroków w panelu.
7. Podłączono wspólną obsługę do walidatora i MUZ oraz ponowiono sprawdzenia między aplikacjami.

To wyniki wybranych zestawów aplikacji z narzędziami. Swobodna rozmowa nie osiągnęła wymaganego poziomu. Kod, wagi i pamięć pozostają lokalnie; publiczna aktualizacja zawiera dokumentację. Istniejące wydania demo i ZIP-y portable pozostają w dotychczasowych wersjach.
