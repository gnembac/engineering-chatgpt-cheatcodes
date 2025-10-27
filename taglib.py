
---

# src/taglib.py

```python
# src/taglib.py
# Maschinelle Tag-Definitionen

TagDefs = {
    "ELI5": {
        "instruction_de": "Erkläre in einfacher Sprache, ohne Fachjargon.",
        "priority": 10
    },
    "TLDR": {
        "instruction_de": "Fasse die Kernaussage in 1–3 Sätzen zusammen.",
        "priority": 9
    },
    "StepByStep": {
        "instruction_de": "Gib eine Schritt-für-Schritt Herleitung oder Anleitung.",
        "priority": 9
    },
    "SWOT": {
        "instruction_de": "Erstelle eine SWOT-Analyse: Stärken, Schwächen, Chancen, Risiken.",
        "priority": 8
    },
    "Compare": {
        "instruction_de": "Vergleiche die genannten Objekte systematisch und nach Kriterien.",
        "priority": 8
    },
    "ProsCons": {
        "instruction_de": "Liste strukturierte Vorteile und Nachteile auf.",
        "priority": 8
    },
    "Derive": {
        "instruction_de": "Führe eine vollständige mathematische Herleitung durch und zeige Zwischenschritte.",
        "priority": 9
    },
    "Equation": {
        "instruction_de": "Gib relevante Gleichungen an und erkläre alle Variablen.",
        "priority": 9
    },
    "UnitsCheck": {
        "instruction_de": "Prüfe Einheiten auf Konsistenz (Dimensionsanalyse).",
        "priority": 9
    },
    "Simulate": {
        "instruction_de": "Beschreibe den Simulationsaufbau: Randbedingungen, Anfangsbedingungen, Gitter/Time‑Step Hinweise.",
        "priority": 8
    },
    "MonteCarlo": {
        "instruction_de": "Schlage einen Monte‑Carlo Ansatz vor und gib Beispielparameter (Anzahl Samples, Verteilungen).",
        "priority": 7
    },
    "Optimize": {
        "instruction_de": "Formuliere Zielfunktion und Restriktionen; skizziere Optimierungsverfahren.",
        "priority": 8
    },
    "Sensitivity": {
        "instruction_de": "Analysiere die Sensitivität gegenüber wichtigen Parametern.",
        "priority": 8
    },
    "LaTeX": {
        "instruction_de": "Formatiere mathematische Ausdrücke in LaTeX.",
        "priority": 6
    },
    "Refs": {
        "instruction_de": "Gib relevante Literaturhinweise, Normen oder Papers an (sofern bekannt).",
        "priority": 5
    },
    "Summary": {
        "instruction_de": "Fasse am Ende kompakt zusammen.",
        "priority": 5
    }
}

DEFAULT_PROMPT_TEMPLATE = (
    "Du bist ein sachkundiger wissenschaftlich-technischer Assistent. {instructions} Aufgabe: {core_prompt}"
)
