# 🧠 PDF Imposition Tool

This tool transforms any A4-sized PDF into a print-ready booklet in A5, A6, or A7 format by automatically calculating page arrangements, signature grouping, and fold-based layouts.

Features
Accepts any standard A4 PDF file

Supports booklet creation in:

A5 format (1 fold – 4 pages per sheet)

A6 format (2 folds – 8 pages per sheet)

A7 format (3 folds – 16 pages per sheet)

Intelligent signature planning to reduce blank pages

Automatically scales and rearranges pages into correct print order

## How to Run

### 1. Clone the project
```bash
git clone https://github.com/rizikdhabre/pdf-imposition-tool.git
cd pdf-imposition-tool
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
