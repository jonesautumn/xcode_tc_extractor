## Introduction

This repo will extract all test case (name, id, and jira link) from a test case file in Tokopedia iOS Xcode repo.

The purpose of extracting all test cases in Xcode is to help you to identify which corresponding TC need to be migrated over Katalon.

## How to Use

```bash
python main.py [--input-file {INPUT_FILE}] [--output-file {OUTPUT_FILE}]
```

You need to install several dependencies first. You can run the following code.

```bash
pip install -r requirements.txt
```

#### INPUT_FILE

By default, the **INPUT_FILE** is referred in the file `constants.py`.

To override the input file in `constants.py`, you could use arguments in running the file.

Kindly check the argument example on the file `constants.py`

#### OUTPUT_FILE

By default, the **OUTPUT_FILE** is referred in the file `constants.py`.

To override the output file in `constants.py`, you could use arguments in running the file.

By default, the output is in the form of CSV. This choice is to make it easier when you are copying the file over Google sheets.
