# Przepływ i wewnętrzna kontrola TSI — 1 listopada 2026

Ostatni zakończony trening: zapis **4677**, **4/8** małych kontroli generacji. Wcześniejszy zapis **4497** miał **6/8**. Swobodna rozmowa nie osiągnęła wymaganego poziomu. Obecny etap to diagnoza i korekta; kolejny identyczny długi trening nie został uruchomiony.

## Co wykazały próby

1. **Dekoder czeka na analizę.** W kontrolowanej próbie CPU zakończenie analizy nastąpiło po 0,272 s, start dekodera po 0,276 s. Przy sztucznym zatrzymaniu analizy przez 0,2 s nie pojawił się żaden krok dekodera. Pytania A → B → A i opóźnienie analizy nie zmieniły odpowiedzi A. Wagi nie były zmieniane.
2. **K nie jest kontrolerem gotowej odpowiedzi.** W tym przepływie stan modalny powstaje z wejścia. Trzy pary poprawna/błędna odpowiedź, sprawdzone na dwóch zapisach, dawały identyczny stan K dla tego samego wejścia. Wygenerowana odpowiedź nie wraca do niego do oceny. Kontrola stałych tablic logiki nie weryfikuje automatycznie semantyki każdej swobodnej wypowiedzi.
3. **Część pozornej utraty wiedzy wynika z wyboru przebiegu dekodera.** Na tych samych wagach 4677 zwykły wybór kolejnego znaku dał 4/8, a przeszukiwanie sześciu przebiegów odpowiedzi 6/8. Generator nie otrzymał odpowiedzi wzorcowych. To wynik zmiany wnioskowania, nie dodatkowego treningu.
4. **Nowe słowa pozostają problemem.** Zdanie „Iga ogląda mapę” nadal było przekręcane. Przeszukiwanie potrafiło też wybrać płynną, ale niezwiązaną odpowiedź. Ocena prawdopodobieństwa nie zastępuje sprawdzenia zgodności z pytaniem i źródłem. Nowy sposób wyboru odpowiedzi nie został włączony w aplikacji jako uniwersalne rozwiązanie.

| Pytanie | Wybór pojedynczego przebiegu | Wybór spośród sześciu |
|---|---|---|
| Jak się nazywasz? | Poznaj jego znaczenie i użyj go w kilku zda. | Cześć! Nazywam się TSI. |
| Ola czyta list. Co robi Ola? | Ola czyta list. | Ola czyta list. |
| Iga ogląda mapę. Co robi Iga? | Igaaa odada�ę. | Igaaa ogla�ę. |

## Poprawki kontroli

- Kontroler treningu sprawdza teraz utratę wcześniej poprawnych odpowiedzi dialogowych, niezależnie od wyników czytnika. Test na zapisach 4497 i 4677 wykrył dwie utracone odpowiedzi, wcześniej niewidoczne w liście regresji.
- Podgląd nauki odróżnia oczekiwanie na nową kontrolę od poprzedniej próbki. Wyniki dostają identyfikator oceny i krok wag; stara lub niezgodna paczka nie jest pokazywana jako nowa. Sprawdzono stan oczekiwania, niezgodne identyfikatory i komplet ośmiu odpowiedzi.
- Nie dodano sztucznego oczekiwania do generowania. Test nie potwierdził wyścigu czasowego w badanym lokalnym przepływie CPU.

## Metody dobrane do błędów

| Problem TSI | Metoda do osobnej, kontrolowanej próby |
|---|---|
| Przekręcanie nowych słów | Odtwarzanie brakujących fragmentów na poziomie bajtów, inspirowane [ByT5](https://arxiv.org/html/2105.13626v3). To adaptacja zadania uczenia, nie podmiana TSI na ByT5. |
| Utrata wcześniejszych odpowiedzi | Powtórki i ochrona rozkładów odpowiedzi zachowanego modelu, inspirowana [Learning without Forgetting](https://arxiv.org/abs/1606.09282). Poprawność odpowiedzi nauczyciela wymaga wcześniejszego sprawdzenia. |
| Powtarzające się fragmenty | Kontrola pokrycia źródła z [pointer-generator networks](https://aclanthology.org/P17-1099/) albo [unlikelihood training](https://arxiv.org/abs/1908.04319). |
| Poprawne litery przy podanym prefiksie, błędna cała odpowiedź | Porównanie pełnych kandydatów, a następnie nauka całych odpowiedzi, m.in. inspiracja [sequence-level distillation](https://arxiv.org/abs/1606.07947). Sam wybór kandydata nie jest sprawdzeniem prawdziwości. |

Wspólny mechanizm tych propozycji to dodatkowy sygnał dotyczący konkretnej zależności: źródło → odpowiedź, wcześniejsza → nowa wiedza lub poprzedni → następny fragment. W TSI potrzebna jest również ocena gotowej odpowiedzi względem pytania i źródła. Obecny stan K i sama średnia strata znaków nie zapewniają takiej kontroli.

Wyniki dotyczą opisanych prób. Działający moduł aplikacyjny odpowiedzi na nazwane dane nadal korzysta z przypiętego zapisu 3944. Kod, wagi i prywatna pamięć pozostają lokalnie.
