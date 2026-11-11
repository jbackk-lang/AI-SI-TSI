# TSI — instrukcja wznowienia

**Aktualizacja 2026-11-11. Ostatni etap: 029. Następny: 030.**

## Obowiązkowa jawność
Przed jakąkolwiek symulacją ogłoś **SYMULACJA** i jej zakres. Nie myl symulacji, inferencji i treningu wag. Użytkownik wyraźnie oczekuje pracy na rzeczywistym H512.

## Etap 029 — RZECZYWISTY TRENING WAG, BEZ SYMULACJI
Archiwum w rozmowie: `TSI_H512_REAL_TRAIN_029.zip` (kod, `h512_candidate_029.pt`, wyniki, log, README). Wymaga sąsiednich katalogów 005, 027, 028 i PyTorch. Uruchom: `python TSI_H512_REAL_TRAIN_029/train.py`.

Punkt startowy: oryginalny H512 z 005, nie checkpoint 027. Trening 63 oznaczone przykłady, walidacja 14, końcowy test 35. Zmiany tylko w `expansion_context` i `expansion_operator`; AdamW 0.0003, 20 epok, najlepsza walidacja w epoce 4.

Walidacja: bazowy 5/14 (35,7%), kandydat 8/14 (57,1%). Test: bazowy 11/35 (31,4%), kandydat 12/35 (34,3%). **Nie promować kandydata do głównego rdzenia.** Różnica testowa to tylko jeden przykład; test jest częścią 70 poleceń wcześniej użytych w 028, a teksty mają tego samego autora. Brak niezależnego benchmarku i testu retencji. Wynik jest wstępny.

## Etap 028
Na 70 ręcznie napisanych instrukcjach bazowy H512 24/70, checkpoint 027 22/70; regresja. Nie wdrażać 027.

## Etap 030
Pozyskać rzeczywiście niezależny zbiór zewnętrzny i zweryfikować jakość, testować retencję oraz inne zdolności H512. Nie używać symulatora bez uprzedniego oznaczenia. Utrzymać niezmieniony checkpoint bazowy.

[Metodologia uczenia](TSI_LEARNING_METHODOLOGY.md).
