from engine.engine import build_dynamic_engine
from engine.facts import *
import json

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
                engine.declare(fact_instance)
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
