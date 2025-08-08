# ISO 8601 to Milliseconds Converter (Python)

This simple Python script converts an **ISO 8601 datetime string** (e.g., `2020-02-27T15:24:17.123Z`) to **milliseconds since the Unix epoch** (January 1, 1970).

## 📂 File

- `iso8601_to_millis.py` – Main script to perform the conversion

## 🧠 How It Works

The script:
1. Replaces the `'Z'` (Zulu time) with `+00:00` to ensure proper UTC parsing.
2. Parses the ISO 8601 string into a `datetime` object.
3. Converts the datetime to a Unix timestamp.
4. Multiplies by 1000 to convert seconds to milliseconds.

## ✅ Requirements

- Python 3.7+

No external libraries are needed. It uses the built-in `datetime` module.

## 🚀 Usage

### 1. Clone or Download

Save the script `iso8601_to_millis.py`.

### 2. Run the Script

```bash
python iso8601_to_millis.py
