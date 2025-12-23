# DeepMIMO Scenario Search

This repository provides tools to search and access DeepMIMO scenarios either **via web interface** or **programmatically in Python**.

---

## Features

* **Web-based search**: Use a simple or advanced interface to filter and find scenarios.
* **Programmatic access**: Query the DeepMIMO database directly in Python using the API.

---

## Installation

Make sure you have Python 3.7+ installed. Then install the DeepMIMO Python package:

```bash
pip install deepmimo
```

---

## Usage

### 1. Web Interface

Open the DeepMIMO website and use the **search interface** to find scenarios:

* **Simple search**: Quickly find scenarios by basic criteria.
* **Advanced search**: Filter by more detailed parameters such as number of antennas, UE distribution, frequency bands, etc.

### 2. Python API

Access the database programmatically:

```python
import deepmimo as dm

# Search for scenarios matching criteria
scenarios = dm.search()

# Print the available scenarios
print(scenarios)
```

You can customize your search by passing arguments to `dm.search()`. For example:

```python
scenarios = dm.search(antenna_count=32, frequency=3.5e9)
```

---

## Contributing

Feel free to submit issues or pull requests to improve the search interface or API features.

---

## License

This project is licensed under the MIT License.

---
