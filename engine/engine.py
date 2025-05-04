from experta import KnowledgeEngine, Fact, Rule
from rules.rule_parser import load_rules_from_json
from facts import HeartFacts

def build_expert_engine(rules_data):
    methods = {}

    for idx, rule_data in enumerate(rules_data):
        condition_str = " and ".join(rule_data["conditions"])
        conclusion = rule_data["class"]

        def make_rule(condition=condition_str, conclusion=conclusion):
            def rule(self):
                if eval(condition, {}, self.facts[1]):
                    self.declare(Fact(diagnosis=conclusion))
            return rule

        rule_func = Rule()(make_rule())
        methods[f"rule_{idx}"] = rule_func

    ExpertClass = type("HeartDiseaseExpertSystem", (KnowledgeEngine,), methods)
    return ExpertClass()



def main():
    
    rules_str = load_rules_from_json('rules/rules.json')

    Expert = build_expert_engine(rules_str)
    Expert.reset()

    Expert.declare(HeartFacts(age=60, sex=1, cp=3, trestbps=140,
                              chol=289, fbs=0, restecg=1,
                              thalach=172, exang=0,oldpeak=0.0, 
                              slope=2, ca=0.0,thal=2.0))
    
    Expert.run()

    print(Expert.facts)

if __name__ == "__main__":
    main()


