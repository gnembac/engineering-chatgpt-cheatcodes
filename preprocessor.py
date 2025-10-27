# src/preprocessor.py
import re
from taglib import TagDefs, DEFAULT_PROMPT_TEMPLATE
from typing import List, Tuple

TAG_PATTERN = re.compile(r"@([A-Za-z0-9_]+)(?:\(([^)]*)\))?")


def extract_tags(prompt: str) -> Tuple[List[Tuple[str, str]], str]:
    """Extrahiere Tags (mit optionalen Parametern) und den Kernprompt."""
    matches = list(TAG_PATTERN.finditer(prompt))
    parsed = []
    for m in matches:
        tag = m.group(1)
        param = m.group(2) or None
        parsed.append((tag, param))
    core = TAG_PATTERN.sub("", prompt).strip(" :\n")
    return parsed, core


def build_instructions(parsed_tags: List[Tuple[str, str]]) -> str:
    """Baue die Instruktions‑Textpassage basierend auf TagDefs.
    Priorität wird berücksichtigt; doppelte Tags werden entfernt (erstes Vorkommen bleibt).
    """
    # Sortiere nach priority (höher zuerst) — wir behalten ursprüngliche Reihenfolge bei Tags mit gleicher Priority
    resolved = []
    seen = set()
    # map tag to priority for sorting
    enriched = []
    for tag, param in parsed_tags:
        if tag in TagDefs:
            prio = TagDefs[tag].get("priority", 0)
            enriched.append((prio, tag, param))
        else:
            enriched.append((0, tag, param))
    enriched.sort(key=lambda x: -x[0])

    for _, tag, param in enriched:
        if tag in seen:
            continue
        seen.add(tag)
        if tag in TagDefs:
            entry = TagDefs[tag]["instruction_de"]
            if param:
                entry += f" (Parameter: {param})"
            resolved.append(entry)
        else:
            # unbekannter Tag: informiere kurz
            resolved.append(f"Tag '{tag}' ist nicht bekannt; ignoriere oder behandle als normaler Text.")
    return " ".join(resolved)


def preprocess_prompt(user_prompt: str) -> str:
    """Hauptfunktion: erzeugt das finale Prompt, das an das Modell geschickt werden soll."""
    parsed, core = extract_tags(user_prompt)
    instructions = build_instructions(parsed)
    final = DEFAULT_PROMPT_TEMPLATE.format(instructions=instructions, core_prompt=core)
    return final


# CLI Support (einfach)
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = input("Prompt: ")
    print(preproces
