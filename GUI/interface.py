import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame, ScrolledText


class ExpertSystemGUI:
    def __init__(self, root, Fields, engine):
        self.root = root
        self.root.title("Heart Disease Diagnosis Expert System")
        self.engine = engine
        self.Fields = Fields

        self.root.geometry("800x600")
        self.style = tb.Style()

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tb.Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.main_label = tb.Label(self.main_frame, text="Heart Disease Diagnosis", font=("Segoe UI", 16, "bold"))
        self.main_label.pack(pady=20)

        self.input_frame = ScrolledFrame(self.main_frame, autohide=True)
        self.input_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.input_frame_label = tb.Label(self.input_frame, text="Examination Parameters", font=("Segoe UI", 12, "bold"))
        self.input_frame_label.pack(anchor=W)

        for _, field_val in self.Fields.items():
            label = tb.Label(self.input_frame, text=field_val, font=("Segoe UI", 10))
            label.pack(anchor=W, pady=5, padx=20)

            entry = tb.Entry(self.input_frame, font=("Segoe UI", 10))
            entry.pack(fill=X, pady=2, padx=20)
            # self.entries[field_key] = {'entry': entry, 'validator': lambda x, y: (True, "")}  # Default validator

        self.diagnose_button = tb.Button(self.input_frame, text="Diagnose", bootstyle="success", command=self.diagnose)
        self.diagnose_button.pack(pady=20)

        self.info_frame = ScrolledFrame(self.main_frame, autohide=True)
        self.info_frame.pack(side=RIGHT, fill=BOTH)

        self.facts_label = tb.Label(self.info_frame, text="Entered Facts:", font=("Segoe UI", 12, "bold"))
        self.facts_label.pack(anchor=W)

        self.facts_listbox = ScrolledText(self.info_frame, height=12, width=40, font=("Consolas", 10))
        self.facts_listbox.pack(pady=10, padx=20)

        self.rules_label = tb.Label(self.info_frame, text="Fired Rules:", font=("Segoe UI", 12, "bold"))
        self.rules_label.pack(anchor=W)

        self.rules_listbox = ScrolledText(self.info_frame, height=10, width=40, font=("Consolas", 10))
        self.rules_listbox.pack(pady=10, padx=20)

    def diagnose(self):
        pass
        

# Example Usage:
if __name__ == "__main__":
    root = tb.Window(themename="solar")
    
    #Dummy field for testing UI
    fields = {}

    for i in range(13):
        fields[f"field_{i}"] = f"Field {i}"

    gui = ExpertSystemGUI(root, fields, engine=None)  # Replace None with actual engine instance
    root.mainloop()
