# Rekurencyjna pamięć i odczyt T/F/U — 24 października 2026

## Powtórki i odczyt statusów

Przed nowym uczeniem wykonano rzeczywiste powtórki 59 znanych przykładów. Zachowano 59/59 odpowiedzi. Sama projekcja statusów do pamięci enkoderów nie poprawiła odpowiedzi F/U. Następnie uczono dodatkową warstwę wyjściową przy zachowanych wagach pozostałej sieci.

Przy podawaniu prawidłowego początku odpowiedzi nowa warstwa uzyskała 3/54 → 39/54 ćwiczeń treningowych oraz 0/24 → 9/24 oddzielnych przykładów. Pełne, samodzielnie wygenerowane odpowiedzi w rozmowie: **1/6**. To odrębne pomiary; wynik przy prawidłowym początku nie jest wynikiem swobodnej rozmowy.

Chronione odpowiedzi: **59/59**. Kandydat: **23,843,739 parametrów**, **95.874 MB** pliku wag (MB dziesiętne). Sześć macierzy reguł zachowano. Model pozostaje lokalnym wariantem badawczym.

## Próba pamięci rekurencyjnej podczas generowania

W historycznym TIMDR odnaleziono generator z dwiema pamięciami aktualizowanymi jako 0,5 × poprzedni stan + 0,5 × nowy stan. Oryginał używa także losowych projekcji, tanh i pętli topologicznej. W tej próbie podłączono adaptację mechanizmu podtrzymywania stanu do reprezentacji istniejących enkoderów TSI; nie jest to przeniesienie całego historycznego generatora.

Adaptacja: h1 = a·h1 + (1−a)·x; h2 = a·h2 + (1−a)·h1. Dwa stany na źródło są dodatkowymi tokenami pamięci dekodera. Sprawdzono a=0,5 oraz a=0,8. Przez cały czas generowania odczytywany jest ten sam, zamrożony stan.

Tematy i miejsca zapisu wskazuje program sprawdzający. Automatyczne rozpoznawanie tematów oraz wyszukiwanie w dużej pamięci nie były przedmiotem tego testu. Dane aktualne są nadal dostępne w zwykłym kontekście. Wagi nie były trenowane ani zmieniane.

Dziesięć przypadków: dwie osoby × pojedynczy fakt, trzykrotne powtórzenie, zmiana tematu, poprawienie faktu oraz trzykrotne powtórzenie poprawki. Oceniono całą wygenerowaną odpowiedź, włącznie z osobą, kolorem i poprawnością zapisu. Dodatkowa kontrola podaje ponownie bieżące reprezentacje źródła bez rekurencji, z taką samą liczbą tokenów.

| Wariant | Pełne poprawne odpowiedzi | Poprawione względem bazowego | Pogorszone | Średni czas generowania |
|---|---:|---:|---:|---:|
| Bez dodatkowej pamięci | 3/10 | 0 | 0 | 4.781 s |
| Rekurencja 0,5 | 4/10 | 1 | 0 | 5.279 s |
| Rekurencja 0,8 | 4/10 | 1 | 0 | 4.392 s |
| Ponowne źródło bez rekurencji | 4/10 | 1 | 0 | 4.914 s |

**Wniosek:** odpowiedzi rekurencji 0,5 i zwykłego ponownego źródła były identyczne w **10/10** przypadków. Ta próba nie wykazała przewagi rekurencji nad dodatkowym kontekstem. Mechanizm wymaga nauczenia odczytu, zanim będzie można ocenić jego przydatność w szerszej rozmowie.

Czasy dotyczą tylko generowania odpowiedzi, bez wcześniejszego zbudowania pamięci. Mała, sekwencyjna próba na CPU nie jest miarodajnym porównaniem szybkości.

## Rzeczywiste odpowiedzi

| Przypadek | Wariant | Odpowiedź |
|---|---|---|
| Ewa:single | Bez dodatkowej pamięci | Plecak Ewć jest czerwony. |
| Ewa:single | Rekurencja 0,5 | Plecak Ewy jest czerwony. |
| Ewa:single | Rekurencja 0,8 | Plecak Ewy jest czerwony. |
| Ewa:repeated | Bez dodatkowej pamięci | Plecak Ewy jest czerwony. |
| Ewa:repeated | Rekurencja 0,5 | Plecak Ewy jest czerwony. |
| Ewa:repeated | Rekurencja 0,8 | Plecak Ewy jest czerwony. |
| Ewa:topic_change | Bez dodatkowej pamięci | Nie. |
| Ewa:topic_change | Rekurencja 0,5 | Nie. |
| Ewa:topic_change | Rekurencja 0,8 | Nie. |
| Ewa:correction | Bez dodatkowej pamięci | Plecak Ewy jest czerwony. |
| Ewa:correction | Rekurencja 0,5 | Plecak Ewy jest czerwony. |
| Ewa:correction | Rekurencja 0,8 | Plecak Ewy jest czerwony. |
| Ewa:correction_rehearsed | Bez dodatkowej pamięci | Plecak Ewy jest czerwony. |
| Ewa:correction_rehearsed | Rekurencja 0,5 | Plecak Ewy jest czerwony. |
| Ewa:correction_rehearsed | Rekurencja 0,8 | Plecak Ewy jest czerwony. |
| Kuba:single | Bez dodatkowej pamięci | Plecak Jana jest czerwony. |
| Kuba:single | Rekurencja 0,5 | Plecak Jana jest czerwony. |
| Kuba:single | Rekurencja 0,8 | Plecak Jana jest czerwony. |
| Kuba:repeated | Bez dodatkowej pamięci | Plecak Jana jest czerwony. |
| Kuba:repeated | Rekurencja 0,5 | Plecak Jana jest czerwony. |
| Kuba:repeated | Rekurencja 0,8 | Plecak Jana jest czerwony. |
| Kuba:topic_change | Bez dodatkowej pamięci | Nie. |
| Kuba:topic_change | Rekurencja 0,5 | Nie. |
| Kuba:topic_change | Rekurencja 0,8 | Nie. |
| Kuba:correction | Bez dodatkowej pamięci | Plecak Jana jest czerwony. |
| Kuba:correction | Rekurencja 0,5 | Plecak Jana jest czerwony. |
| Kuba:correction | Rekurencja 0,8 | Plecak Jana jest czerwony. |
| Kuba:correction_rehearsed | Bez dodatkowej pamięci | Plecak Jana jest czerwony. |
| Kuba:correction_rehearsed | Rekurencja 0,5 | Plecak Jana jest czerwony. |
| Kuba:correction_rehearsed | Rekurencja 0,8 | Plecak Jana jest czerwony. |
| Ewa:single | Ponowne źródło bez rekurencji | Plecak Ewy jest czerwony. |
| Ewa:repeated | Ponowne źródło bez rekurencji | Plecak Ewy jest czerwony. |
| Ewa:topic_change | Ponowne źródło bez rekurencji | Nie. |
| Ewa:correction | Ponowne źródło bez rekurencji | Plecak Ewy jest czerwony. |
| Ewa:correction_rehearsed | Ponowne źródło bez rekurencji | Plecak Ewy jest czerwony. |
| Kuba:single | Ponowne źródło bez rekurencji | Plecak Jana jest czerwony. |
| Kuba:repeated | Ponowne źródło bez rekurencji | Plecak Jana jest czerwony. |
| Kuba:topic_change | Ponowne źródło bez rekurencji | Nie. |
| Kuba:correction | Ponowne źródło bez rekurencji | Plecak Jana jest czerwony. |
| Kuba:correction_rehearsed | Ponowne źródło bez rekurencji | Plecak Jana jest czerwony. |

**Swobodna rozmowa nie osiągnęła wymaganego poziomu.** Wynik dotyczy tej adaptacji i tych dziesięciu przypadków. Pamięć pozostawała stała podczas odpowiedzi; pomyłki dotyczące osób i zmiany tematu wymagają dalszego uczenia odczytu. Działających aplikacji, ich wag i portable nie podmieniono.
