# Pamięć bitowa T/F/U — 24 października 2026

Wariant został podłączony do testowej ścieżki rozmowy rozwijanego modelu TSI. Panel użytkownika, MUZ, walidator i ich wagi pozostają bez zmian.

Zapis przechowuje oryginalne ramki znaczeniowe oraz cztery dwubitowe statusy ról. U=00, F=01, T=10, a 11 jest kodem zarezerwowanym. Adresy 252–255 pozostają kodami sterującymi PC_TIMDR. Kolejne strony po 252 pozycje zapobiegają kolizjom adresów w dłuższej pamięci. Nie zmniejszano precyzji liczb ani ułamków.

Generator otrzymuje odtworzoną, niezależną migawkę pamięci. Zapis następuje po zakończeniu odpowiedzi. Statusów nie podwyższa samo ponowne odczytanie wpisu lub wypowiedź modelu. Nowe ramki bez jawnej oceny ról mają statusy U.

## Sprawdzenia

- Kontrole integracji: **14/14** — w tym 600 ramek na trzech stronach adresowych, zachowanie ułamków, niezmienność migawki, wykrycie zmienionego źródła, odrzucenie kodu 11 oraz zachowanie statusów F/U między turami.
- Cztery porównania z rzeczywistym generatorem TSI i tymi samymi wagami: **4/4 identyczne odpowiedzi** przed i po podłączeniu.
- Poprawność odpowiedzi: **1/4 przed, 1/4 po**. Błąd przypisywania Kubie plecaka Jana nadal występuje. Wagi nie były aktualizowane w tej próbie.

Kodowanie działa bez utraty treści. Samo jego podłączenie nie poprawiło rozmowy. Sieć nie otrzymała w tym etapie nowego uczonego wejścia dla statusów bitowych; statusy służą do zapisu i odtwarzania pamięci. Kolejna integracja musi dotyczyć ich wykorzystania przez odczyt i generowanie, z osobnym sprawdzeniem odpowiedzi.

Model porównania: **23 542 811 parametrów**, kandydat po treningu z powtórkami. Swobodna rozmowa **nie osiągnęła wymaganego poziomu**.
