from engine.engine import build_dynamic_engine
from engine.facts import *

import ttkbootstrap as tb
from GUI import ExpertSystemGUI

import json

engine = None
GUI = None

def diagnose(engine, success_handler):
    engine.reset()
    GUI.clear_facts_area()
    GUI.reset_fields_state()
    engine.missing_facts = set()
    for fact_name, value in GUI.get_fields_dict().items():
        fact_class = globals().get(fact_name)
        if fact_class:
            fact_instance = fact_class(**{fact_name: value})
            try:
                engine.declare(fact_instance)
                GUI.append_facts({fact_name: value})
            except InvalidFact as e:
                GUI.notify_validation_error(fact_name, str(e))
                return
        else:
            GUI.report_warning(f"⚠️ Unknown fact: {fact_name}")
            return
            
    engine.run()  

    if engine.rule_fired:
        GUI.append_rules(engine.last_rule_fired)
        engine.last_rule_fired = None
        engine.rule_fired = False

    if engine.diagnosed:
        success_handler(engine.diagnosis)
    elif engine.missing_facts:
        for fact_name in engine.missing_facts:
            fact_class = globals().get(fact_name)
            if fact_class:
                GUI.highlight_field_needed(fact_name)
            else:
                GUI.report_warning(f"⚠️ Unknown fact: {fact_name}")
    else:
        GUI.report_error("❌ No applicable rule.")

def success_handler(diagnosis):
    global GUI, engine
    GUI.Messagebox("Diagnosis Result", diagnosis)


def diagnose_handler():
    global engine, GUI

    if engine.diagnosed:
        GUI.report_warning("⚠️ Diagnosis already completed, Resetting the system...")
        engine.reset()
        engine.missing_facts = set()
        engine.diagnosed = False
        engine.rule_fired = False
        GUI.clear_all()
        return

    diagnose(engine, success_handler)


def main():
    with open("rules/skope_rules.json") as f:
        rules = json.load(f)

    global engine
    engine = build_dynamic_engine(rules)
    root = tb.Window(themename="solar")

    global GUI
    GUI = ExpertSystemGUI(root, fact_names_description, engine, diagnose_handler)

    root.mainloop()

if __name__ == "__main__":
    main()
