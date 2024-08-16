# keyDoc: Keyword Detection in PDF and Word Documents
[![keyDoc badge](https://img.shields.io/badge/keyDoc-ready%20to%20use-brightgreen)](https://github.com/yvoawk/keyDoc)
[![licence](https://img.shields.io/badge/Licence-MIT%20%2B%20file%20LICENSE-blue)](https://github.com/yvoawk/keyDoc/blob/master/LICENSE.md)

This Python script allows you to search for specific keywords in a batch of PDF and Word documents. It takes a `.txt` file containing the keywords and a folder with the documents as input. The script will output the names of files that contain any of the keywords and save the results in a CSV file.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Features

- Extracts text from `PDF` and `Word` documents.
- Searches for specified keywords in the text.
- Outputs the names of files containing the keywords.
- Saves the output in a `CSV` file.

## Requirements

- Python 3.x
- The following Python libraries:
  - `PyPDF2`
  - `python-docx`
  - `pandas`

## Installation

1. **Clone the repository** (or download the script):

   ```bash
   git clone https://github.com/yvoawk/keyDoc.git
   cd keyDoc
   ````

2. **Install the required Python libraries:**

```bash
pip install PyPDF2 python-docx pandas
```
## Usage

1. **Prepare the Keywords File:**
Create a text file (`keywords.txt`) with each keyword on a new line. For example:

```
keyword1
keyword2
keyword3
```

2. **Prepare the Documents Folder:**
Place all the **PDF** and **Word** documents you want to search in a single folder (e.g., documents_folder).

3. **Run the Script:**
Use the following command to run the script:

````bash
python3 detect.py keywords.txt documents_folder output.csv
````

- keywords.txt: Path to the text file containing the keywords.
- documents_folder: Path to the folder containing the `PDF` and `Word` documents.
- output.csv: Path where the output `CSV` file will be saved.

## Example

Assume you have:

    - A file named `keywords.txt` with the following content:

```
molestie
lorem
ipsum
```

    - A folder named `docs` containing the following files:
        - sample.pdf
        - sample.docx

To search for the keywords in these documents, run the script:

```bash
python detect.py keywords.txt docs output.csv
```

The script will output the names of files containing the keywords to the console and save them to `output.csv`.
