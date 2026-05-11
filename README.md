# text-editor
A simple text editor on Windows built with **Python** and the **Tkinter** library. This project was developed as a hands-on learning exercise to master GUI development and file handling in Python.

## ✨ Features

- **File Operations**: 
  - `New File`: Start a fresh document with a safety confirmation dialog.
  - `Open File`: Load existing files from your computer.
  - `Save`: Save your current work to a local directory.
- **Dynamic Styling**: 
  - Change font families (e.g., Arial, Consolas, Courier New) on the fly.
  - Adjust font sizes to suit your preference.
- **User Experience**:
  - `Undo/Redo`: Full support for `Ctrl+Z` and `Ctrl+Y` to manage edit history.
  - `Context Menu`: Right-click functionality for quick access to:
    - **Cut / Copy / Paste**: Standard clipboard operations.
    - **Select All**: Quickly highlight all text.
  - Integrated scrollbar for long documents.
  - Real-time window title updates reflecting the current file path.
## 🚀 Getting Started

### Prerequisites
- **Python 3.x**: Ensure you have Python installed.
- **Tkinter**: Usually included with standard Python installations.

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/ignaxus/text-editor.git](https://github.com/ignaxus/text-editor.git)

```

2. Navigate to the project folder:
```bash
cd text-editor

```

### Running the Editor

Simply run the Python script:

```bash
python text_editor.py

```

## 🛠️ Built With

* [Python](https://www.python.org/) - The programming language used.
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's de-facto standard GUI package.

## 📝 Learning Journey

This project was built step-by-step to understand:

1. GUI Layout management (`pack`, `Frames`).
2. Event-driven programming (binding functions to buttons).
3. File I/O operations and error handling (`try...except`).
4. State management using Tkinter variables (`StringVar`).
