# 🤝 Contributing to IPTEL ANVIZ Desktop

First off, thank you for considering contributing to this project! Your help is greatly appreciated.

---

## 📋 Table of Contents

- [Getting Started](#-getting-started)
- [How to Contribute](#-how-to-contribute)
- [Development Workflow](#-development-workflow)
- [Coding Standards](#-coding-standards)
- [Testing Guidelines](#-testing-guidelines)
- [Documentation](#-documentation)
- [Pull Request Process](#-pull-request-process)
- [Community](#-community)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Basic understanding of Python and PyQt6

### Setting Up Development Environment

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/your-username/IPTEL_ANVIZ_Desktop.git
cd IPTEL_ANVIZ_Desktop

# Add upstream remote
git remote add upstream https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Run the application
python main.py
```

---

## 🎯 How to Contribute

### Types of Contributions

| Type | Description |
| :--- | :--- |
| 🐛 **Bug Reports** | Report issues you encounter |
| 💡 **Feature Requests** | Suggest new features or improvements |
| 📝 **Documentation** | Improve or update documentation |
| 🧪 **Testing** | Write and run tests |
| 💻 **Code** | Fix bugs or add features |
| 🎨 **UI/UX** | Improve design and user experience |

### Finding Issues to Work On

1. Browse [open issues](https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop/issues)
2. Look for labels like `good-first-issue`, `help-wanted`, or `bug`
3. Comment on the issue to let others know you're working on it

---

## 🔄 Development Workflow

### 1. Create a Branch

```bash
# Always branch off from main
git checkout main
git pull upstream main

# Create your feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix-name
```

**Branch Naming Convention:**
- `feature/` – For new features
- `fix/` – For bug fixes
- `docs/` – For documentation changes
- `refactor/` – For code refactoring
- `test/` – For test additions

### 2. Make Your Changes

- Write clean, readable code
- Add comments where necessary
- Update documentation if needed
- Write tests for new features

### 3. Test Your Changes

```bash
# Run the application
python main.py

# Run tests (once implemented)
pytest tests/
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "type(scope): brief description of changes"
```

**Commit Message Format:**
```
type(scope): brief description

Detailed description of what changed and why.
Fixes #issue-number
```

**Types:**
- `feat` – New feature
- `fix` – Bug fix
- `docs` – Documentation
- `style` – Code style (formatting, no logic change)
- `refactor` – Code refactoring
- `test` – Tests
- `chore` – Maintenance

**Example:**
```bash
git commit -m "feat(user): add bulk import from CSV"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then:
1. Go to GitHub and open a Pull Request
2. Target the `main` branch
3. Fill out the PR template
4. Request review from maintainers

---

## 📝 Coding Standards

### Python Style

- Follow **PEP 8** guidelines
- Use **4 spaces** for indentation
- Maximum line length: **79 characters** for code, **72** for docstrings
- Use **type hints** (Python 3.9+)
- Write **docstrings** for all public functions/classes

### PyQt6 Standards

- Use **proper parent-child relationships** for widgets
- Follow **MVC pattern** where appropriate
- Use **Signals and Slots** for communication
- Use **Qt Designer** for complex UIs when possible

### Example

```python
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class ExampleWidget(QWidget):
    """Widget for demonstrating coding standards."""

    def __init__(self, parent: QWidget | None = None) -> None:
        """Initialize the example widget."""
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Set up the user interface components."""
        layout = QVBoxLayout(self)
        button = QPushButton("Click Me", self)
        button.clicked.connect(self._handle_click)
        layout.addWidget(button)

    def _handle_click(self) -> None:
        """Handle button click event."""
        print("Button clicked!")
```

---

## 🧪 Testing Guidelines

### Write Tests

```python
# tests/test_example.py
import pytest
from src.example import ExampleClass

def test_example_function():
    """Test that example function returns expected output."""
    result = ExampleClass().do_something()
    assert result == expected_value
```

### Run Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_example.py

# Run with coverage
pytest --cov=src tests/
```

---

## 📚 Documentation

### File Naming

- `docs/README.md` – Documentation index
- `docs/TECHNICAL.md` – Technical documentation

### Docstring Format

```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description of what the function does.

    Longer description with additional details.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When an invalid parameter is passed
    """
    pass
```

---

## 🔍 Pull Request Process

### Before Submitting PR

1. ✅ Ensure all tests pass
2. ✅ Update documentation
3. ✅ Follow coding standards
4. ✅ Write a clear PR description
5. ✅ Link any related issues

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added for new functionality
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Commit messages follow guidelines
- [ ] PR description is clear and detailed

## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Refactor

## Testing
Describe how you tested your changes.

## Related Issues
Closes #issue-number

## Screenshots (if applicable)
Add screenshots to demonstrate the changes.

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests added
- [ ] Documentation updated
- [ ] Commit messages are clear


---

## 🌟 Community

- **GitHub Issues** – Bug reports and feature requests
- **Discussions** – General questions and ideas
- **Pull Requests** – Code contributions

---

## 📧 Contact

If you have any questions, feel free to reach out:

- **Email:** moeez.raza.dev@gmail.com
- **GitHub Issues:** [Create an issue](https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop/issues)

---

**Thank you for contributing! 🎉**
