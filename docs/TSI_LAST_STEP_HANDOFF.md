# TSI — instrukcja wznowienia (nadpisywana)

**Aktualizacja:** 2026-11-11. **Ostatni ukończony etap:** TSI_CURIOSITY_026. **Następny:** 027.

## Metodologia
[Metodologia uczenia TSI](TSI_LEARNING_METHODOLOGY.md) — osobny dokument opisujący pamięć, politykę ciekawości i ewentualne dostrajanie H512. Traktować jako plan badawczy, nie potwierdzoną zdolność autonomicznego uczenia.

## Etap 026 — wpływ odczytu faktów na pytania
Lokalny artefakt rozmowy: `TSI_CURIOSITY_026.zip` (skrypt `experiment.py`, `result.json`, `run.log`, `README.md`, `METODOLOGIA_UCZENIA_TSI.md`). Wymaga sąsiednich katalogów `TSI_CURIOSITY_025` i `TSI_CURIOSITY_023` z checkpointem `value_predictor_023.pt` oraz PyTorch. Uruchomienie: `python TSI_CURIOSITY_026/experiment.py`.

100 scenariuszy × 5 sesji × 8 pytań; dane i weryfikacja syntetyczne. Trzy strategie: losowa, wyuczona bez odczytu faktów, wyuczona z regułą uwzględniającą fakty.

| Metryka (średnia) | Losowa | Bez odczytu | Z odczytem |
|---|---:|---:|---:|
| Nagroda | 35,7340 | 33,2485 | 32,7590 |
| Różne relacje | 17,07 | 8,55 | 16,83 |
| Poprawne konsensusy | 11,53 | 7,96 | 13,66 |
| Powtórzone pytania | 22,93 | 31,45 | 23,17 |

Różnica nagrody z odczytem minus bez: −0,4895 (bootstrap 95% CI −1,0845..+0,1120). Nie stwierdzono przewagi nagrody. Nie trenowano nowych wag; H512 bez zmian. Historia faktów przechowywana w RAM między sesjami w jednym procesie, nie na dysku. Prawda używana tylko do oceny, nie w selektorze.

## Następny etap 027
Trwały magazyn faktów na dysku między procesami; zapis pochodzenia, wersjonowanie korekt, niepewność i test restartu. Sprawdzić odporność na błędne odpowiedzi i realne wykorzystanie zapisanej wiedzy; nie mylić symulowanej weryfikacji z niezależnym źródłem.

## Procedura powrotu
Odczytaj ten plik i metodologię. Sprawdź faktyczną dostępność ZIP 023, 025, 026 oraz checkpointu 023; pliki lokalne mogą nie być dostępne w nowej sesji. Po etapie 027 nadpisz **ten sam plik** i zachowaj historię Git.
