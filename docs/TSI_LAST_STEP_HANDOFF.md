# TSI — instrukcja wznowienia (nadpisywana)

**Aktualizacja:** 2026-11-11. **Ostatni ukończony etap:** TSI_H512_REAL_TRAIN_027. **Następny:** 028.

## Ważna korekta kierunku
Etapy 020–026 dotyczyły głównie syntetycznych symulatorów ciekawości, **nie treningu H512**. Nie należy przedstawiać ich jako dowodu autonomicznego uczenia TSI. Etap 027 to pierwszy w tej sekwencji rzeczywisty nadzorowany trening parametrów H512, ale nie trening ciekawości.

## Etap 027 — trening rzeczywistego H512
Lokalny artefakt rozmowy: `TSI_H512_REAL_TRAIN_027.zip`, zawiera `train.py`, `README.md`, `result.json`, `h512_finetuned_027.pt`. Bazowy checkpoint `TSI_H512_RUN_005/src/h512.pt`, SHA-256 `23e7c2f208129776705ea075f855c1afd5d26caf2bd7f1620fdae96b16c48851`. Zmienione warstwy: `expansion_context.*`, `expansion_operator.*`; pozostałe parametry porównano z checkpointem bazowym i zachowano.

42 ręcznie oznaczone polskie instrukcje treningowe (7 operatorów), 21 odłożonych przykładów. Trafność na odłożonych: **6/21 (28,57%) przed**, **11/21 (52,38%) po**. Kod i etykiety jawne w skrypcie. Trening nadzorowany, bez symulowanych odpowiedzi. Mały, ręcznie przygotowany zbiór; brak niezależnego zewnętrznego benchmarku i brak dowodu ogólnego uczenia lub ciekawości.

Uruchomienie: katalogi `TSI_H512_RUN_005` i `TSI_H512_REAL_TRAIN_027` obok siebie; PyTorch; `python TSI_H512_REAL_TRAIN_027/train.py`. Wyniki i checkpoint w katalogu 027. **Nie zastępować oryginalnego H512.**

## Następny krok 028
1. Zbudować większy niezależny zbiór rzeczywistych instrukcji, z rozdzieleniem autorów i szablonów między treningiem i testem.
2. Sprawdzić retencję dotychczasowych możliwości i regresje po fine-tuningu.
3. Dopiero potem badać wybór pytań przez H512 na sprawdzalnych źródłach, bez generowania sztucznej prawdy.
4. Raportować także porażki i ograniczenia.

## Powrót
Odczytaj ten plik oraz [metodologię uczenia](TSI_LEARNING_METHODOLOGY.md). Zweryfikuj dostępność ZIP i checkpointów w nowej sesji. Po kolejnym etapie **nadpisz ten sam plik**.
