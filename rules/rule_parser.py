import json
import re

def load_rules_from_json(file_path):
    with open(file_path, 'r') as file:
        rules_str = json.load(file)

        parsed_rules = []
        for rule in rules_str:
            condition, conclusion = rule.split('=>')
            conditions = [cond.strip() for cond in condition.strip().split('AND')]
            match = re.search(r'Class:\s*(\d)', conclusion)
            class_label = int(match.group(1)) if match else None
            parsed_rule = {
                'conditions': conditions,
                'class': class_label
            }
            parsed_rules.append(parsed_rule)
    return parsed_rules

if __name__ == "__main__":
    rules = load_rules_from_json('rules/rules.json')
    for rule in rules:
        print(f"Conditions: {rule['conditions']}, Class: {rule['class']}")