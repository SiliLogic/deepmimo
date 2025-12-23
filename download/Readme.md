# DeepMIMO Scenario Download

This repository provides tools to **download DeepMIMO scenarios** either **via the web interface** or **programmatically in Python**.

---

## Features

* **Web-based download**: Navigate the scenario page and download datasets manually.
* **Programmatic download**: Use the Python API to download single or multiple scenarios automatically.
* **Automatic extraction**: The API extracts downloaded zip files and organizes them for immediate use with DeepMIMO functions.

---

## Installation

Ensure you have Python 3.7+ and the DeepMIMO package installed:

```bash
pip install deepmimo
```

---

## Usage

### 1. Download via Web

1. Open the DeepMIMO website.
2. Go to a **scenario page** by clicking the scenario name in the database.
3. Scroll to the bottom of the page and click the **Download** button.

---

### 2. Download via Python API

#### Method 1: Download a single scenario

```python
import deepmimo as dm

# Download a specific scenario
dataset = dm.download('asu_campus_3p5')
```

#### Method 2: Download multiple scenarios

1. Perform filtering on the web interface.
2. Copy the list of scenario names from the results table.
3. Use the Python API to download them:

```python
import deepmimo as dm

# List of scenario names copied from clipboard
scenario_names = ['asu_campus_3p5', 'city_0_newyork_3p5']

# Download each scenario
for scen_name in scenario_names:
    dataset = dm.download(scen_name)
```

---

### 3. How `dm.download()` Works

The `dm.download()` function performs **three automatic steps**:

1. **Download**: Saves the scenario zip file to

   ```
   deepmimo_scenarios_downloaded/<scenario_name>.zip
   ```

2. **Extract**: Unzips the scenario automatically.

3. **Organize**: Places the extracted folder under

   ```
   deepmimo_scenarios/<scenario_name>
   ```

The extracted scenario can then be used directly with `dm.load()` and `dm.generate()` functions.

---

## Notes

* Make sure you have **internet access** when downloading scenarios programmatically.
* For **large scenarios**, ensure sufficient disk space for both zip and extracted data.

---

## License

This project is licensed under the MIT License.

---
