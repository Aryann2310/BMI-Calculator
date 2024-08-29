import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")

        self.weight_frame = tk.Frame(root, bg="#f0f0f0")
        self.weight_label = tk.Label(self.weight_frame, text="Weight:", bg="#f0f0f0", font=("Arial", 12))
        self.weight_label.pack(side=tk.LEFT)
        self.weight_entry = tk.Entry(self.weight_frame, font=("Arial", 12))
        self.weight_entry.pack(side=tk.LEFT)
        self.weight_unit_var = tk.StringVar()
        self.weight_unit_var.set("kg")
        self.weight_unit_menu = tk.OptionMenu(self.weight_frame, self.weight_unit_var, "kg", "lbs")
        self.weight_unit_menu.pack(side=tk.LEFT)
        self.weight_frame.pack(pady=10)

        self.height_frame = tk.Frame(root, bg="#f0f0f0")
        self.height_label = tk.Label(self.height_frame, text="Height:", bg="#f0f0f0", font=("Arial", 12))
        self.height_label.pack(side=tk.LEFT)
        self.height_entry = tk.Entry(self.height_frame, font=("Arial", 12))
        self.height_entry.pack(side=tk.LEFT)
        self.unit_var = tk.StringVar()
        self.unit_var.set("m")
        self.unit_menu = tk.OptionMenu(self.height_frame, self.unit_var, "m", "cm")
        self.unit_menu.pack(side=tk.LEFT)
        self.height_frame.pack(pady=10)

        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi, bg="#ffffff",
                                          fg="#0B57D0", font=("Arial", 12))
        self.calculate_button.pack(pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_fields, bg="#0B57D0", fg="#ffffff",
                                      font=("Arial", 12))
        self.clear_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=self.root.destroy, bg="#ffffff", fg="#0B57D0",
                                     font=("Arial", 12))
        self.exit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
        self.result_label.pack()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if self.weight_unit_var.get() == "kg":
                weight_in_kg = weight
            elif self.weight_unit_var.get() == "lbs":
                weight_in_kg = weight / 2.20462

            if self.unit_var.get() == "m":
                height_in_meters = height
            elif self.unit_var.get() == "cm":
                height_in_meters = height / 100

            if weight_in_kg <= 0 or height_in_meters <= 0:
                messagebox.showerror("Invalid input", "Please enter positive values for weight and height.")
                return

            bmi = weight_in_kg / (height_in_meters ** 2)
            category = self.categorize_bmi(bmi)

            self.result_label.config(text=f"Your BMI is: {bmi:.2f}\nYour category is: {category}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def clear_fields(self):
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
  
