# Copilot Instructions for AI Agents

## Project Overview
This is a simple Python CLI application for managing restaurants. The main logic is in `app.py` and currently supports basic menu-driven user interaction.

## Architecture & Workflow
- **Single-file structure:** All logic resides in `app.py`. There are no modules, packages, or external dependencies.
- **CLI Menu:** The application displays a menu with options to register, list, activate restaurants, or exit. User input is handled via `input()`.
- **No persistent storage:** Data is not saved between runs. There are no database or file operations.
- **No tests or build scripts:** There are no automated tests, build, or deployment workflows. Run the app directly with Python.

## Developer Workflow
- **Run the application:**
  ```powershell
  & C:/Users/nator/AppData/Local/Programs/Python/Python313/python.exe "app.py"
  ```
  Or use the default Python interpreter for your environment.
- **Debugging:**
  - Errors will appear in the terminal. There is no custom error handling or logging.
  - The last line in `app.py` currently contains a syntax error (an extra `1` after the print statement).

## Project-Specific Patterns
- **Menu options:** All user interaction is via numbered menu options. Extend by adding new options and handling them with conditional logic.
- **No external libraries:** Only built-in Python functions are used.
- **ASCII art banner:** The app prints a stylized banner at startup.

## Key File
- `app.py`: Main entry point and contains all logic.

## Example: Adding a New Menu Option
```python
print('5. Consultar restaurante')
# ...existing code...
opcao_escolhida = input('Escolha uma opção: ')
if opcao_escolhida == '5':
    print('Consultar restaurante selecionado')
```

## Recommendations for AI Agents
- Focus on expanding `app.py` with new features using simple CLI patterns.
- Fix syntax errors before adding new logic.
- If introducing persistence or modularity, document new conventions here.

---
*Update this file if project structure or conventions change.*
