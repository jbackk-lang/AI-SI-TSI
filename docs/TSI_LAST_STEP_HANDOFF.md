# TSI — instrukcja wznowienia (nadpisywana)

**Aktualizacja:** 2026-11-11. **Ostatni ukończony etap według rozmowy:** TSI_CURIOSITY_020. **Następny:** 021.

## Kontekst
TSI: lokalny rdzeń H512, pamięć grafowa, kontrolowane eksperymenty diagnostyki/naprawy i wyuczony selektor pytań. Wcześniejsze etapy 017–019 integrowały ciekawość z pamięcią. Etap 020: osobny moduł uczący się preferencji eksploracji z grafu w symulacji; H512 bez zmian.

## Wynik etapu 020 (raportowany w rozmowie)
32 epizody treningowe, 20 oceny. Średnia nagroda: polityka wyuczona 2,8775; prosta kontrolna 1,3050; heurystyka grafowa 4,5800. Polityka przewyższa prostą kontrolną, ale ustępuje heurystyce. Dane i odpowiedzi syntetyczne, pytania składane z szablonów, nie generowane przez H512.

## Artefakty
- Lokalny pakiet rozmowy: `TSI_CURIOSITY_020.zip` (nie zakładać dostępności w nowej sesji; sprawdzić pliki i ewentualnie poprosić o ponowne udostępnienie).
- Wersja v003: https://github.com/jbackk-lang/Belzi/tree/tsi-v003-curiosity — dokumentacja, nie pełne wagi.
- Główny opis: https://github.com/jbackk-lang/AI-SI-TSI/blob/main/README.md

## Następne działanie
1. Odzyskać faktyczne źródła i checkpoint 020; sprawdzić SHA, strukturę i wykonać test uruchomienia.
2. Zbudować 021: przewidywanie wartości informacji; oddzielić zbiory tematów treningowych i testowych, porównać z heurystyką grafową oraz losową przy tym samym budżecie.
3. Zapisać liczby, nasiona losowe, wersje zależności, checkpoint i ograniczenia. Nie twierdzić, że pojawiła się świadomość lub autonomiczne zainteresowania.
4. Po każdym ukończonym etapie **nadpisać ten plik**: numer, wyniki, checkpoint, pliki, komendy, problemy i jeden następny krok. Zachować historię przez commity Git.

## Zasada dla kolejnej rozmowy
Odczytaj ten plik jako pierwsze źródło kontynuacji; zweryfikuj stan kodu i artefaktów, nie zakładaj, że poprzednia sesja lub jej katalog roboczy są dostępne. Nie zmieniaj wag H512 bez osobnej decyzji i testu.
