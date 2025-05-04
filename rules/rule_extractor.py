import joblib
import pandas as pd
from sklearn.tree import _tree
import json

def load_model(model_path: str):
    with open(model_path, 'rb') as file:
        model = joblib.load(file)
    return model

def extract_rules_from_tree(model):
    tree_ = model.tree_
    feature_names = model.feature_names_in_

    rules = []

    def recurse(node, rule):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            feature_name = feature_names[tree_.feature[node]]
            threshold = tree_.threshold[node]
            left_child = tree_.children_left[node]
            right_child = tree_.children_right[node]
            
            rule_left = rule + [f"{feature_name} <= {threshold:.2f}"]
            rule_right = rule + [f"{feature_name} > {threshold:.2f}"]
            
            recurse(left_child, rule_left)
            recurse(right_child, rule_right)
        else: #leaf node
            value = tree_.value[node]
            predicted_class = value.argmax()
            rule_str = " AND ".join(rule) + f" => Class: {predicted_class} ({value[0][predicted_class]:.2f} probability)"
            rules.append(rule_str)

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

    # Print extracted rules for inspection
    for rule in rules:
        print(rule)

if __name__ == "__main__":
    main()
