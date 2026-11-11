# TSI — instrukcja wznowienia (nadpisywana)

**Data:** 2026-11-11. **Ostatni ukończony etap:** TSI_CURIOSITY_025. **Następny:** 026.

## Etap 025 — reset pamięci, nowe obiekty i retencja
Archiwum rozmowy: `TSI_CURIOSITY_025.zip`, zawiera `experiment.py`, `result.json`, `run.log`, `README.md`. Do uruchomienia wymagany checkpoint `TSI_CURIOSITY_023/value_predictor_023.pt` oraz PyTorch. Komenda: `python TSI_CURIOSITY_025/experiment.py`. 100 środowisk na wariant, pięć sesji na środowisko; nowe identyfikatory obiektów w każdej sesji, niezmienione abstrakcyjne tematy.

| Strategia | Zgodne warunki | Odwrócona zależność |
|---|---:|---:|
| Losowa | 19,2177 | 20,0535 |
| Wyuczona bez pamięci | 37,3083 | 22,3325 |
| Reset pamięci co sesję | 37,3083 | 22,3325 |
| Wyuczona + trwała pamięć | 37,5830 | 23,7637 |

Persistent−reset: zgodne +0,2747 (95% bootstrap CI −0,1155..+0,7167), odwrócone +1,4312 (CI +0,7939..+2,1157). Średnia liczba zachowanych wcześniej faktów w ostatniej sesji: 21,28 i 14,98. Zapis JSON ponownie odczytany i sprawdzony.

**Ograniczenia:** odpowiedzi i weryfikacja są symulowane, nie niezależne; trwałe fakty nie wpływają na wybór pytań; te same abstrakcyjne tematy występują we wszystkich sesjach; H512 bez zmian. To test pamięci, nie dowód autonomicznej ciekawości.

## Następny etap 026
Włączyć odzyskaną wiedzę do selekcji pytań; przeprowadzić ablation z wyłączonym odczytem pamięci; sprawdzić nowe relacje, błędne odpowiedzi i odporność na zmiany środowiska. Mierzyć rzeczywistą poprawę predykcji i poprawność wiedzy, nie tylko syntetyczną nagrodę.

## Powrót
Odczytać ten plik, zweryfikować dostępność ZIP 025 i checkpointu 023, odtworzyć wyniki. Po kolejnym etapie nadpisać **ten sam plik**, zachowując historię Git.
