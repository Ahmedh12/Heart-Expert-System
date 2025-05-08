import pickle as pkl
import pandas as pd
from sklearn.tree import _tree
import json

def load_model(model_path: str):
    with open(model_path, 'rb') as file:
        model = pkl.load(file)
    return model

def extract_rules_from_tree(model):
    tree_ = model.tree_
    feature_names = model.feature_names_in_

    rules = []

    def recurse(node, conditions):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            feature_name = feature_names[tree_.feature[node]]
            threshold = tree_.threshold[node]

            left_conditions = conditions + [f"{feature_name} <= {threshold:.2f}"]
            right_conditions = conditions + [f"{feature_name} > {threshold:.2f}"]

            recurse(tree_.children_left[node], left_conditions)
            recurse(tree_.children_right[node], right_conditions)
        else:
            # Leaf node
            class_idx = tree_.value[node].argmax()
            rules.append({
                "conditions": conditions,
                "expression": " and ".join(conditions),
                "conclusion": {"diagnosis": f"class_{class_idx}"}
            })

    recurse(0, [])
    return rules

def save_rules_to_json(rules, output_file="rules/rules.json"):
    with open(output_file, 'w') as file:
        json.dump(rules, file, indent=4)

def main():
    model_path = 'ml/heart_model.pkl'
    model = load_model(model_path)
    
    rules = extract_rules_from_tree(model)
    
    save_rules_to_json(rules)

    for rule in rules:
        print(rule)

if __name__ == "__main__":
    main()
