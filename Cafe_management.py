import tkinter as tk
from tkinter import messagebox

def calculate_total():
    try:
        total = 0
        order_summary = "Your Order:\n"
        for item, price in prices.items():
            qty = int(entries[item].get()) if entries[item].get() else 0
            if qty > 0:
                total += qty * price
                order_summary += f"{item}: {qty} x Rs{price} = Rs{qty * price}\n"

        # Ask the user if they are done ordering before showing the bill
        additional_order = messagebox.askyesno("Order More?", "Do you want to order something else before viewing the bill?")
        if additional_order:
            return

        # Ask the user if they want to proceed to the bill
        proceed = messagebox.askyesno("Confirm Order", "Do you want to see the bill?")
        if proceed:
            order_summary += f"\nTotal Cost: Rs{total}"
            messagebox.showinfo("Order Summary", f"{order_summary}\n\nThank you for visiting Mc Cafe! Your order will be ready soon.")

            # Show the final "Enjoy your meal!!!" popup
            messagebox.showinfo("Enjoy Your Meal", "Enjoy your meal!!!")

            # After "Enjoy your meal", no further questions are asked
            reset_fields()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid quantities.")

def reset_fields():
    for entry in entries.values():
        entry.delete(0, tk.END)

prices = {
    "Icecream": 140,
    "Nugged": 380,
    "Pizza": 230,
    "Burger": 120,
    "Coffee": 85,
    "Tea": 45
}

root = tk.Tk()
root.title("Mc Cafe Management System")
root.geometry("600x400")
root.configure(bg="#a53e06")

# Heading
heading = tk.Label(root, text="Welcome to Mc Cafe", font=("Helvetica", 30, "bold"), bg="#a53e06", fg="#ffffff")
heading.pack(pady=20)

# Frame for Menu
menu_frame = tk.Frame(root, bg="#a53e06")
menu_frame.pack(pady=10)

entries = {}
for item, price in prices.items():
    row = tk.Frame(menu_frame, bg="#ffffff")
    row.pack(fill="x", pady=5)

    label = tk.Label(row, text=f"{item} = Rs{price}", font=("Helvetica", 14), bg="#ffe6e6", fg="#333333")
    label.pack(side="left", padx=10)

    entry = tk.Entry(row, width=5, font=("Helvetica", 14))
    entry.pack(side="right", padx=10)
    entries[item] = entry

# Buttons
button_frame = tk.Frame(root, bg="#ffe6e6")
button_frame.pack(pady=20)

btn_calculate = tk.Button(button_frame, text="Place Order", command=calculate_total, bg="#4caf50", fg="white", font=("Helvetica", 14), width=15)
btn_calculate.pack(side="left", padx=10)

btn_reset = tk.Button(button_frame, text="Reset", command=reset_fields, bg="#f44336", fg="white", font=("Helvetica", 14), width=15)
btn_reset.pack(side="right", padx=10)

# Footer
footer = tk.Label(root, text="Enjoy your meal!", font=("Helvetica", 12, "italic"), bg="#ffe6e6", fg="#555555")
footer.pack(pady=10)

# Start the application
root.mainloop()