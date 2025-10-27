# Engineering ChatGPT Cheat Codes


**Kurzbeschreibung**
Sammlung von Prompt‑"Cheat Codes" (Tag‑Bibliothek) für Ingenieur‑ und Wissenschaftsanwendungen. Enthält eine maschinenlesbare Tagliste, einen einfachen Prompt‑Preprocessor in Python, Beispiel‑Prompts und Unit‑Tests. Ziel: schnelle Integration in Custom GPTs, Workflows oder CLI‑Utilities.


## Enthaltene Dateien
- `tags.csv` — maschinenlesible Liste der Tags (deutsch + Kurzbeschreibung)
- `src/taglib.py` — Tag‑Definitionen (Dict / Metadaten)
- `src/preprocessor.py` — Parser und Prompt‑Template‑Builder
- `src/examples.py` — typische Use Cases und Beispielprompts
- `tests/test_preprocessor.py` — Unit‑Tests
- `docs/integration.md` — Hinweise zur Integration in Custom GPTs / Pipelines
- `requirements.txt` — Python‑Abhängigkeiten
- `LICENSE` — MIT


## Installation (lokal)
1. Repository klonen
```bash
git clone <dein-repo-url>
cd engineering-chatgpt-cheatcodes
