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
            self.rule_fired = False
            self.last_rule_fired = None

    for idx, rule_data in enumerate(json_rules):
        conditions = rule_data["conditions"]
        conclusion = rule_data["conclusion"]
        rule_priority = rule_data["probability"]

        def make_rule(conds, concl):
            def rule_method(self):
                fact_values = {}
                for f in self.facts.values():
                    if isinstance(f, Fact):
                         for k, v in dict(f).items():
                            if v is not None:
                                fact_values[k] = v
                try:
                    if eval(" and ".join(conds), {}, fact_values):
                        self.rule_fired = True
                        self.declare(diagnosis(value=concl["diagnosis"]))
                        self.diagnosis = (
                            "No Heart Diseases Detected...😁"
                            if concl["diagnosis"] == "class_0"
                            else "Heart Disease Diagnosed...😞"
                        )
                        self.last_rule_fired = " and ".join(conds)
                        self.diagnosed = True
                except NameError as e:
                    missing = extract_missing_fact(e)
                    if missing:
                        self.missing_facts.add(missing)
            return rule_method

        setattr(
            HeartExpert,
            f"rule_{idx}",
            Rule(salience=rule_priority)(make_rule(conditions, conclusion))
        )

    return HeartExpert()

def main():
    with open("rules/rules.json") as f:
        rules = json.load(f)

    engine = build_dynamic_engine(rules)
    user_input = {}

    while True:
        engine.reset()
        engine.missing_facts = set()
        for fact_name, value in user_input.items():
            fact_class = globals().get(fact_name)
            if fact_class:
                fact_instance = fact_class(**{fact_name: value})
                try:
                    engine.declare(fact_instance)
                except InvalidFact as e:
                    print(f"⚠️ Error declaring fact '{fact_name}': {e}")

            else:
                print(f"⚠️ Unknown fact: {fact_name}")
                
        engine.run()  

        if engine.diagnosed:
            break
        elif engine.missing_facts:
            print("🔍 Missing facts:", engine.missing_facts)
            for fact_name in engine.missing_facts:
                value = input(f"Enter value for '{fact_name}': ")
                try:
                    value = float(value) if '.' in value else int(value)
                except ValueError:
                    pass

                fact_class = globals().get(fact_name)
                if fact_class:
                    user_input[fact_name] = value
                else:
                    print(f"⚠️ Unknown fact: {fact_name}")
        else:
            print("❌ No applicable rule.")
            break

if __name__ == "__main__":
    main()


    with open("rules/rules.json") as f:
        rules = json.load(f)

    engine = build_dynamic_engine(rules)
    
    user_input = {}

    
    
    