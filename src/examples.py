# src/examples.py

"""Beispieldatei für Engineering ChatGPT Cheat Codes.
Dieses Modul zeigt, wie man mit der Tag‑Bibliothek und dem Preprocessor arbeitet.
"""

from src.preprocessor import preprocess_prompt

# Beispiel 1: Vereinfachte Erklärung (ELI5)

def example_eli5():
prompt = "@ELI5: Erkläre die Funktionsweise eines Wechselrichters in einer PV‑Anlage."
result = preprocess_prompt(prompt)
print("\n--- Beispiel: ELI5 ---")
print(result)

# Beispiel 2: Vergleichsanalyse (Compare)

def example_compare():
prompt = "@Compare(Wärmepumpe, Gasheizung): Welche Technologie ist effizienter im Winterbetrieb?"
result = preprocess_prompt(prompt)
print("\n--- Beispiel: Vergleich ---")
print(result)

# Beispiel 3: SWOT‑Analyse

ndef example_swot():
prompt = "@SWOT(Solarthermie): Bewertung für Wohngebäude in Bayern."
result = preprocess_prompt(prompt)
print("\n--- Beispiel: SWOT‑Analyse ---")
print(result)

# Beispiel 4: TLDR‑Zusammenfassung

def example_tldr():
prompt = "@TLDR: Technische Zusammenfassung des IPCC‑Berichts 2024 zur industriellen Dekarbonisierung."
result = preprocess_prompt(prompt)
print("\n--- Beispiel: TLDR ---")
print(result)

# Beispiel 5: Kombination von Tags

def example_combo():
prompt = (
"@ELI5 @SWOT(Quantencomputer‑Chips): Vorteile und Risiken in der Halbleiterfertigung."
)
result = preprocess_prompt(prompt)
print("\n--- Beispiel: Kombinierte Tags ---")
print(result)

if **name** == "**main**":
example_eli5()
example_compare()
example_swot()
example_tldr()
example_combo()

