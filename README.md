# pdf-creation-python
Program to create a new pdf document usind [FPDF](http://www.fpdf.org/en/doc/index.php) library in PYTHON 3.x

# Installation
Use the package manager pip to install FPDF
```bash
pip install fpdf
```

# Usage
```bash
from fpdf import FPDF

pdf = FPDF() # instantiate the class
pdf.add_page() # add a new page to our pdf document
pdf.set_font("Arial", size=14) # Set our document font
pdf.cell(200, 10, txt={string_variable}, align="C") # create a new cell(line) in our document
pdf.ln() # line break
pdf.multi_cell(180, 10, txt={string_variable}, align="L") # create a new cell, but can it can has more than one line
pdf.output("name_of_doc.pdf") # close our document and generate the pdf file
```
# Documentation
[FPDF](http://www.fpdf.org/en/doc/index.php)
