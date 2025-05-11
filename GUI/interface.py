import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame, ScrolledText
from ttkbootstrap.dialogs import Messagebox


class ExpertSystemGUI:
    def __init__(self, root, Fields, engine, diagnose_handler=None):
        self.root = root
        self.root.title("Heart Disease Diagnosis Expert System")
        self.engine = engine
        self.Fields = Fields
        self.diagnose_handler = diagnose_handler if diagnose_handler else self.diagnose
        self.entries = {}

        self.root.geometry("800x600")
        self.style = tb.Style()

        self.create_widgets()

    def scroll_to_entry(self, entry):
        for child in self.input_frame.winfo_children():
            if isinstance(child, tb.Entry) and child == entry:
                self.input_frame.yview_moveto((child.winfo_y() / self.input_frame.winfo_height()) * 0.75) 
                break


    def create_widgets(self):
        self.main_frame = tb.Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.main_label = tb.Label(self.main_frame, text="Heart Disease Diagnosis", font=("Segoe UI", 16, "bold"))
        self.main_label.pack(pady=20)

        self.input_frame = ScrolledFrame(self.main_frame, autohide=True)
        self.input_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.input_frame_label = tb.Label(self.input_frame, text="Examination Parameters", font=("Segoe UI", 12, "bold"))
        self.input_frame_label.pack(anchor=W)

        for field_key, field_description in self.Fields.items():
            label = tb.Label(self.input_frame, text=field_description, font=("Segoe UI", 10))
            label.pack(anchor=W, pady=5, padx=20)

            entry = tb.Entry(self.input_frame, font=("Segoe UI", 10))
            entry.pack(fill=X, pady=2, padx=20)
            self.entries[field_key] = entry

        self.bottom_frame = tb.Frame(self.root)
        self.bottom_frame.pack(side=BOTTOM, fill=X, pady=10)

        self.diagnose_button = tb.Button(self.bottom_frame, text="Diagnose", bootstyle="success", command=self.diagnose_handler)
        self.diagnose_button.pack(pady=20, padx=20, fill=X, expand=True)

        self.status_bar = tb.Label(self.bottom_frame, text="Welcome to the Heart Disease Diagnosis Expert System")
        self.status_bar.pack(pady=10, padx=5, side=BOTTOM, fill=X)

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

    def Messagebox(self, title, message):
        Messagebox.show_info(title=title, message=message)

    def get_fields_dict(self):
        fields_dict = {}
        for key, entry in self.entries.items():
            value = entry.get()
            if value:
                try:
                    fields_dict[key] = float(value) if '.' in value else int(value)
                except ValueError:
                    fields_dict[key] = value
        return fields_dict
    

    def format_entry_field(self, field_name, format_type, message=None):
        if field_name in self.entries:
            entry = self.entries[field_name]
            entry.configure(bootstyle= format_type)
            entry.focus_set()
            self.scroll_to_entry(self.entries[field_name])
            self.status_bar.configure(text= message)

        for field in self.entries:
            if field != field_name:
                self.entries[field].configure(bootstyle="default")

    def highlight_field_needed(self, field_name):
        self.format_entry_field(field_name, "danger", f"Missing field: : {self.Fields[field_name]}") 

    def notify_validation_error(self, field_name, message):
        self.format_entry_field(field_name, "warning", f"Validation Error: {message}")

    def reset_fields_state(self):
        for field in self.entries:
            self.entries[field].configure(bootstyle="default")
        self.status_bar.configure(text="Welcome to the Heart Disease Diagnosis Expert System")

    def report_warning(self, message):
        self.status_bar.configure(text=message)
        self.Messagebox("Warning", message)

    def report_error(self, message):
        self.status_bar.configure(text=message)
        self.Messagebox("Error", message)
    
    def append_facts(self, facts):
        self.facts_listbox.text.configure(state=NORMAL)
        self.facts_listbox.text.insert(END, facts)
        self.facts_listbox.text.insert(END, "\n")
        self.facts_listbox.text.yview(END)
        self.facts_listbox.text.configure(state=DISABLED)

    def append_rules(self, rules):
        self.rules_listbox.text.configure(state=NORMAL)
        self.rules_listbox.text.insert(END, rules)
        self.rules_listbox.text.yview(END)
        self.rules_listbox.text.insert(END, "\n")
        self.rules_listbox.text.configure(state=DISABLED)

    def clear_facts_area(self):
        self.facts_listbox.text.configure(state=NORMAL)
        self.facts_listbox.text.delete(1.0, END)
        self.facts_listbox.text.configure(state=DISABLED)

    def clear_rules_area(self):
        self.rules_listbox.text.configure(state=NORMAL)
        self.rules_listbox.text.delete(1.0, END)
        self.rules_listbox.text.configure(state=DISABLED)

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, END)

    def clear_all(self):
        self.clear_facts_area()
        self.clear_rules_area()
        self.clear_entries()
        self.reset_fields_state()

# Example Usage:
if __name__ == "__main__":
    root = tb.Window(themename="solar")
    
    #Dummy field for testing UI
    fields = {}

    for i in range(14):
        fields[f"field_{i}"] = f"Field {i}"

    gui = ExpertSystemGUI(root, fields, engine=None)  # Replace None with actual engine instance
    root.mainloop()
