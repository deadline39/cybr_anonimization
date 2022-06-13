### Badania modeli klasyfikacji złośliwych połaczeń na zanonimizowanych danych.
Kroki:
- pobierz zbiór ([CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)) i wypakuj pliki do folderu `CSVs` w tym folderze
- uruchom komórki w pliku `01_preprocessing.ipynb` - gdzie pliki są wstępnie przetwarzane, anonimizowane i zapisywane do pojedynczego pliku
- uruchom komórki w pliku `03_attack_filter.ipynb`. gdzie plik dzielony jest na pliki odpowiadające poszczególnym atakom
- uruchom komórki w pliku `04_1_feature_selection_for_attack_files.ipynb` - gdzie wybierane są najważniejsze cechy dla modeli klasyfikacji
- uruchom komórki w pliku `05_1_machine_learning_implementation_for_attack_files .ipynb`, gdzie losowo powstaje podział na zbiór testowy oraz uczone i tesowoane są modele klasyfikacji