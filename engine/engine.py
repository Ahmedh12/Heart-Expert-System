from experta import KnowledgeEngine, Fact, Rule
from .facts import *
import json

def extract_missing_fact(error_msg):
    if "name '" in str(error_msg):
        return str(error_msg).split("name '")[1].split("'")[0]
    return None

def build_dynamic_engine(json_rules):
    class HeartExpert(KnowledgeEngine):
        def __init__(self):
            super().__init__()
            self.missing_facts = set()
            self.diagnosed = False
            self.diagnosis = None

    for idx, rule_data in enumerate(json_rules):
        conditions = rule_data["conditions"]
        conclusion = rule_data["conclusion"]

        def make_rule(conds, concl):
            def rule_method(self):
                fact_values = {}
                for f in self.facts.values():
                    if isinstance(f, Fact):
                        fact_values.update(dict(f))
                try:
                    if eval(" and ".join(conds), {}, fact_values):
                        self.rule_fired = True
                        self.declare(diagnosis(value=concl["diagnosis"]))
                        self.diagnosis = "No Heart Diseases Diagnosed" if concl["diagnosis"] == "class_0" else "Heart Disease Diagnosed"
                except NameError as e:
                    missing = extract_missing_fact(e)
                    if missing:
                        self.missing_facts.add(missing)
            return rule_method

        setattr(
            HeartExpert,
            f"rule_{idx}",
            Rule()(make_rule(conditions, conclusion))
        )

    return HeartExpert()

def main():
    with open(f"rules/rules.json") as f:
        rules = json.load(f)


    engine = build_dynamic_engine(rules)
    engine.reset()

    engine.declare(cp(cp=45))
    engine.declare(ca(ca=45))

    engine.run()

    if engine.diagnosed:
        print(engine.diagnosis)
    elif engine.missing_facts:
        print("Ask for:", engine.missing_facts)
    else:
        print("No applicable rule.")

if __name__ == "__main__":
    main()