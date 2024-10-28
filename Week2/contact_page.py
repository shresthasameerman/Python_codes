import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Contact")

# Labels for Name and Address
tk.Label(root, text="Name").grid(row=1, column=0, columnspan=4)
tk.Label(root, text="Address").grid(row=1, column=8, columnspan=4)

# Entry fields for Name and Address
name = tk.Entry(root, width=16)
address = tk.Entry(root, width=16)

name.grid(row=1, column=4, columnspan=4)
address.grid(row=1, column=12, columnspan=4)

# Treeview widget to display contact details
tree = ttk.Treeview(root, columns=("Name", "Address"), show='headings')
tree.heading("Name", text="Name")
tree.column("Name", anchor=tk.CENTER)
tree.heading("Address", text="Address")
tree.column("Address", anchor=tk.CENTER)
tree.grid(row=4, column=0, columnspan=16)

data = []

# Function to save data
def saveData():
    nameEntry = name.get()
    addressEntry = address.get()
    if nameEntry and addressEntry:
        data.append({"name": nameEntry, "address": addressEntry})
        tree.insert("", tk.END, values=(nameEntry, addressEntry))
        name.delete(0, tk.END)
        address.delete(0, tk.END)
        print(data)

# Function to delete selected item
def deleteData():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            # Get the item index in 'data' list
            values = tree.item(item, "values")
            data_index = next((i for i, d in enumerate(data) if d["name"] == values[0] and d["address"] == values[1]), None)
            if data_index is not None:
                del data[data_index]  # Remove from data list
            tree.delete(item)  # Remove from Treeview
            print(data)

# Function to edit selected item
def editData():
    selected_item = tree.selection()
    if selected_item:
        item = selected_item[0]
        values = tree.item(item, "values")
        
        # Pre-fill entries with selected data
        name.delete(0, tk.END)
        address.delete(0, tk.END)
        name.insert(0, values[0])
        address.insert(0, values[1])

        # Update button
        def updateData():
            new_name = name.get()
            new_address = address.get()
            if new_name and new_address:
                # Update the 'data' list
                data_index = next((i for i, d in enumerate(data) if d["name"] == values[0] and d["address"] == values[1]), None)
                if data_index is not None:
                    data[data_index] = {"name": new_name, "address": new_address}
                # Update the Treeview item
                tree.item(item, values=(new_name, new_address))
                name.delete(0, tk.END)
                address.delete(0, tk.END)
                update_button.grid_forget()
                print(data)

        # Show update button
        update_button.grid(row=2, column=8, columnspan=4)

# Buttons
tk.Button(root, text="Save", command=saveData).grid(row=2, column=0)
tk.Button(root, text="Delete", command=deleteData).grid(row=2, column=4)
tk.Button(root, text="Edit", command=editData).grid(row=2, column=8)

# Update button for editing, hidden initially
update_button = tk.Button(root, text="Update", command=None)
update_button.grid_forget()

root.mainloop()

