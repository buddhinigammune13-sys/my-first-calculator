# Simple GUI Calculator

A responsive, interactive graphical calculator built with Python and Tkinter. It supports standard arithmetic operations, precise BODMAS (Order of Operations) evaluation, decimal inputs, and backspace functionality.

## Features
* **BODMAS Support:** Accurately evaluates complex expressions (e.g., `5(6)` automatically converts to `5*(6)`).
* **Responsive Design:** The grid layout automatically scales and stretches when you resize the window.
* **Error Handling:** Gracefully handles division by zero and invalid inputs.

## Prerequisites
* Python 3.x installed on your system.

## Setup and Running the Application

Follow these steps to set up an isolated virtual environment and run the calculator.

### 1. Create a Virtual Environment
It is best practice to run Python projects inside a virtual environment. Open your terminal or command prompt, navigate to the folder containing your project, and run the following command to create a folder named `venv`:

**Windows:**
```bash
python -m venv venv
```

**macOS and Linux:**
```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment
Before running the application, you must activate the environment. You will know it is activated when `(venv)` appears at the beginning of your terminal prompt.

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```
*(Note: If you are using PowerShell, run `venv\Scripts\Activate.ps1`. You may need to bypass execution policies if it is your first time).*

**macOS and Linux:**
```bash
source venv/bin/activate
```

### 3. Run the Application
With the virtual environment active, ensure the `gui_calculator.py` file is in your current directory and run:

```bash
python gui_calculator.py
```
*(On macOS/Linux, you might need to use `python3 gui_calculator.py` depending on your setup).*

The graphical calculator window should now open on your screen!

### 4. Deactivate the Environment (Optional)
When you are completely finished using the calculator and want to return your terminal to its normal state, simply type:

```bash
deactivate
```