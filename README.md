# MyRepo

This repository contains a Python script that utilizes the Weasyprint library.

## Prerequisites

Before running the Python script, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Homebrew (for macOS)

## Getting Started

To set up the project and run the Python script, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/zhukant/toki-pona-cheatsheet-suko.git
   ```

2. Navigate to the project directory:
   ```
   cd toki-pona-cheatsheet-suko
   ```

3. Create a new virtual environment:
   ```
   python3.12 -m venv weasyprintenv
   ```

4. Activate the virtual environment:
   ```
   source weasyprintenv/bin/activate
   ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Navigate to the `src` directory:
   ```
   cd src
   ```

7. Update any files that need updating, such as the font files.

8. Run the Python script:
   ```
   python tp-cheatsheet-suko-generate-pdf.py
   ```

9. Make sure that the venv folder is in the .gitignore list.
10. Update the `requirements.txt` file by running:
    ```
    pip freeze > requirements.txt
    ```

## Virtual Environment

The project uses a virtual environment to isolate the dependencies. The virtual environment is located in the `weasyprintenv` folder. This folder should not be committed to the Git repository.

To activate the virtual environment, run:
```
source weasyprintenv/bin/activate
```

To deactivate the virtual environment, run:
```
deactivate
```

## Dependencies

The project dependencies are listed in the `requirements.txt` file. To install the dependencies, make sure the virtual environment is activated and run:
```
pip install -r requirements.txt
```

If you add new dependencies to the project, update the `requirements.txt` file by running:
```
pip freeze > requirements.txt
```

## Troubleshooting

If you encounter the error "Import weasyprint could not be resolved" in your Python script, ensure that:
- The virtual environment is activated.
- Weasyprint and its dependencies are installed correctly within the virtual environment.
- Your Python script is using the interpreter from the virtual environment.
- The file structure and virtual environment setup are correct.

If you encounter any other issues or have questions, please refer to the project's documentation or contact the maintainer.