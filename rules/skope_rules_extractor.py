import pickle as pkl
import pandas as pd
import json

def load_model(model_path: str):
    with open(model_path, 'rb') as f:
        model, _ = pkl.load(f)
    return model

def extract_rules_from_tree(model, class_idx):
    rules = []
    for rule, (precision, _, _) in model.rules_:
        rule_conditions = rule.split(' and ')

        rules.append({
            "conditions": rule_conditions,
            "conclusion": {"diagnosis": f"class_{class_idx}"},
            "probability": precision
        })

    return rules

def save_rules_to_json(rules, output_file):
    with open(output_file, 'w') as file:
        json.dump(rules, file, indent=4)

def main():
    model = load_model(model_path='ml/models/skope_rules_model.pkl')
    original_rules = extract_rules_from_tree(model, class_idx=1)
    print(f"Original rules: {len(original_rules)}")

    inverted_model = load_model(model_path='ml/models/skope_rules_model_inverted_target.pkl')
    inverted_rules = extract_rules_from_tree(inverted_model, class_idx=0)
    print(f"Inverted rules: {len(inverted_rules)}")

    combined_rules = original_rules + inverted_rules
    print(f"Combined rules: {len(combined_rules)}")
    save_rules_to_json(combined_rules, output_file="rules/skope_rules.json")

if __name__ == "__main__":
    main()
