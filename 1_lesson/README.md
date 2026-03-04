# Automation with PyAutoGUI

This project demonstrates the use of `pyautogui` for automating browser interactions and data entry tasks. Below is an overview of the scripts and their functionality:

## Scripts Overview

### `automation_script.py`
This script automates the following tasks:
1. **Opening the Browser**: Uses `pyautogui` to open Firefox and navigate to a specific URL.
2. **Logging In**: Automates the login process by entering an email and password.
3. **Importing Products**: Reads product data from a CSV file (`products.csv`) and fills out a form on the webpage with the product details. The script:
   - Clicks on specific input fields using pre-determined mouse coordinates.
   - Enters product details such as code, brand, type, category, unit price, cost, and observations.

### `auxiliar.py`
This script is used to capture the mouse pointer's `x` and `y` coordinates. It:
1. Waits for 5 seconds to allow the user to position the mouse over the desired element.
2. Prints the mouse pointer's position, which can then be used in `automation_script.py` for precise clicks.

## How to Use
1. **Run `auxiliar.py`**:
   - Use this script to determine the coordinates of the elements you want to interact with.
   - Replace the coordinates in `automation_script.py` with the captured values.

2. **Prepare the CSV File**:
   - Ensure `products.csv` contains the following columns: `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`.

3. **Run `automation_script.py`**:
   - Execute the script to automate the browser tasks and data entry.

## Requirements
- Python 3.13 or higher
- Libraries: `pyautogui`, `pandas`

## Notes
- The `pyautogui` library simulates mouse and keyboard actions, so ensure the screen resolution and browser layout remain consistent.
- Use `auxiliar.py` whenever the webpage layout changes to update the coordinates.