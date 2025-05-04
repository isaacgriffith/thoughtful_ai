# Thoughtful Sort

A Python package for categorizing packages based on their dimensions and mass.

## Installation

```bash
pip install -e .
```

## Usage

### Python API

The `sort` function categorizes packages into three categories based on their dimensions and mass:

- **STANDARD**: Neither bulky nor heavy
- **SPECIAL**: Either bulky or heavy
- **REJECTED**: Both bulky and heavy

A package is considered:
- Bulky if its volume (width * height * length) exceeds 1,000,000
- Bulky if any dimension (width, height, or length) exceeds 150
- Heavy if its mass exceeds 20

#### Example

```python
from thoughtful_sort.sort import sort

# Standard package
result = sort(10, 10, 10, 10)  # Returns "STANDARD"

# Special package (bulky due to volume)
result = sort(100, 100, 100, 10)  # Returns "SPECIAL"

# Special package (bulky due to dimension)
result = sort(151, 10, 10, 10)  # Returns "SPECIAL"

# Special package (heavy)
result = sort(10, 10, 10, 21)  # Returns "SPECIAL"

# Rejected package (both bulky and heavy)
result = sort(100, 100, 100, 21)  # Returns "REJECTED"
```

### Command Line Interface

The package provides a command-line interface for easy use:

```bash
# Basic usage
python -m thoughtful_sort.cli 10 10 10 10

# Example outputs:
# Package category: STANDARD
# Package category: SPECIAL
# Package category: REJECTED
# Error: All dimensions must be positive
```

The CLI accepts four arguments in order:
1. Width
2. Height
3. Length
4. Mass

All arguments must be positive numbers.

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the package in development mode:
   ```bash
   pip install -e .
   ```
4. Install development dependencies:
   ```bash
   pip install pytest
   ```

## Testing

The project uses pytest for testing. To run the tests:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=thoughtful_sort
```

## Project Structure

```
thoughtful_sort/
├── __init__.py
├── sort.py          # Core sorting logic
├── cli.py           # Command-line interface
└── test/
    ├── test_sort.py # Unit tests for sort function
    └── test_cli.py  # Unit tests for CLI
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 