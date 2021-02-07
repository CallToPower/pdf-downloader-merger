# PDF Downloader/Merger

Options for

- Downloading (PDF) files
- Merging PDF files

## Copyright

Copyright (C) 2021 Denis Meyer

## Prerequisites

### Software

* Python 3 (as "python3")
* Windows
  * Add Python to PATH variable in environment
* Configure `src/settings.yaml`

## Usage

* Start shell
* Create a virtual environment
  * `python -m venv venv`
* Activate the virtual environment
  * Mac/Linux
    * `source venv/bin/activate`
  * Windows
    * `.\venv\scripts\activate`
* Install the required libraries
  * `pip install -r requirements.txt`
* Configure
    * `src/settings.yaml`
* Start
    * `cd src`
    * `python main.py`
