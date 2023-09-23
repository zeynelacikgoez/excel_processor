
# Excel Data Processing Library

This library offers various functions for data processing in Excel. It was designed to facilitate working with Excel files in Python, especially when it comes to merging, filtering, and processing data from multiple files.

## Main features

- **Comparing data from multiple Excel files**: With the `process_excel_files` function, you can compare data from multiple export and import files and save the results in a single file.
- **Advanced error handling**: The library provides robust error handling and logging to inform you about any potential problems or discrepancies in the data.
- **Flexibility**: Flexibility in specifying column names, key formats, and file paths.
- **(Additional Features)**: As this library is continuously being expanded, more data processing functions will be added in the future.

## Installation

To use this library, simply clone the repository:

```
git clone https://github.com/zeynelacikgoez/excel_processor.git
```

Make sure you have `pandas` and `openpyxl` installed:


```
pip install pandas openpyxl
```

## Usage

### process_excel_files

An example call of the `process_excel_files` function:

```python
from excel_processor import process_excel_files

result = process_excel_files(
    ["export1.xlsx", "export2.xlsx"],
    ["import1.xlsx", "import2.xlsx"],
    ["abc", "def", "ghi"],
    ["123", "456", "789"],
    "{}-{}-{}"
)
print(result)
```
