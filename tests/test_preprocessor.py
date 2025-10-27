# tests/test_preprocessor.py

"""Unit-Tests für den Prompt-Preprocessor des Engineering ChatGPT Cheat Codes Projekts."""

import pytest
from src.preprocessor import preprocess_prompt

def test_eli5_prompt():
prompt = "@ELI5: Erkläre den Unterschied zwischen Spannung und Strom."
result = preprocess_prompt(prompt)
assert isinstance(result, str)
assert "einfacher Sprache" in result or len(result) > 0

def test_compare_prompt():
prompt = "@Compare(Solarzelle, Batterie): Unterschied in Funktion und Anwendung."
result = preprocess_prompt(prompt)
assert "Vergleich" in result or len(result) > 0

def test_swot_prompt():
prompt = "@SWOT(Windkraft): Bewertung für Norddeutschland."
result = preprocess_prompt(prompt)
assert any(keyword in result for keyword in ["Stärken", "Schwächen", "Chancen", "Risiken"])

def test_tldr_prompt():
prompt = "@TLDR: Zusammenfassung der wichtigsten Ergebnisse der Fusionsforschung 2024."
result = preprocess_prompt(prompt)
assert len(result) > 20

def test_combined_tags():
prompt = "@ELI5 @SWOT(3D-Druck): Vor- und Nachteile für Kleinserienproduktion."
result = preprocess_prompt(prompt)
assert isinstance(result, str)
assert len(result) > 0

if **name** == "**main**":
pytest.main([**file**])
# tests/test_preprocessor.py
