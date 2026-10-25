# Pytania do lekcji TSI — 25 października 2026

## Co wdrożono

Zaplecze lokalnego TSI obsługuje pytania do wskazanej lekcji. Połączenie rozmowy używa identyfikatora lekcji; panel wyboru nie został jeszcze przygotowany. Każde wyszukiwanie jest ograniczone do materiału i profilu użytkownika.

Odczyt korzysta z trzech mechanizmów:

1. Matryca obiektu, właściwości i liczby dla prostych zdań z czasownikiem „mieć”. Analizuje odmianę, przypadki, zgodność liczby oraz liczebniki z istniejącego modułu liczb. Obsługuje np. „Pająk ma osiem nóg”, „Pudełko ma 6 ścian” i „Pudełko ma dwadzieścia trzy ściany”. Nie zawiera osobnych zapisanych odpowiedzi dla figur.
2. Dotychczasowy odczyt ról i warunków, np. „Komu Anna daje książkę?” oraz wersja z przeczeniem.
3. Wyszukiwanie fragmentów przez wspólne formy podstawowe słów. Ten tryb przedstawia cytat; samo podobieństwo słów nie jest oznaczane jako potwierdzona odpowiedź.

Odpowiedź zawiera identyfikator lekcji, skrót kontrolny materiału, źródło oraz wykorzystane fragmenty. Dotyczy treści materiału, a nie niezależnej oceny jego prawdziwości. Przy kilku znaczeniach lub sprzeczności TSI zachowuje rozróżnienie.

## Rzeczywista rozmowa przez aplikację

Materiał: „Trójkąt ma trzy boki. Kwadrat ma cztery boki.”

| Pytanie | Odpowiedź |
|---|---|
| Ile boków ma trójkąt? | trzy boki. |
| Ile boków ma kwadrat? | cztery boki. |
| Ile waży trójkąt? | Prośba o brakującą informację; brak wymyślonej masy |

Po podaniu materiału z dwiema różnymi liczbami boków TSI poprosiła o wybór wariantu. Zachowano działanie wyjaśnień nowych słów, rachunku 2 + 8 oraz odmowy podania nieznanego terminu spotkania.

## Sprawdziany

| Sprawdzian | Wynik |
|---|---:|
| Pytania do lekcji, izolacja profili, brak danych, przeczenie i fragmenty list | 12/12 |
| Zmiana obiektu, liczby, szyku; sprzeczności; pytanie w źródle; ujemna liczba; błędna odmiana | 23/23 |
| API i rozmowa działającej aplikacji | 10/10 |

Formy „koła/kół” mają w analizatorze kilka dopuszczalnych znaczeń. Ten przypadek pozostawiono nierozstrzygnięty; nie wybierano znaczenia na siłę. Pełne złożone zdania i dowolne parafrazy wymagają dalszego rozwinięcia.

W krótkim sprawdzianie pierwsze wywołanie wraz z inicjalizacją zajęło około 2,5 s, kolejne około 2–24 ms. To pomiar modułu na krótkich materiałach, nie czas pełnej rozmowy ani dużej lekcji.

Wagi i panel pozostały bez zmian. Nie wznowiono internetowej pętli treningu gotowych odpowiedzi.
