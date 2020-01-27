# -*- encoding: utf-8 -*-

from fpdf import FPDF

TITULO = ("Example creation pdf document in python").decode("utf-8")

text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pretium turpis sem, in porttitor sapien bibendum tincidunt. "
+ "Vestibulum laoreet, justo quis luctus porttitor, felis tellus rhoncus nunc, volutpat pulvinar magna justo ut lorem. "
+" Proin urna mi, dictum id vestibulum feugiat, feugiat a orci. Aliquam convallis facilisis orci, ut feugiat diam tempus a. "
+"Suspendisse commodo ornare felis, sit amet tincidunt metus egestas id. Maecenas commodo, eros in convallis egestas, lacus nisl interdum arcu, "
+"id facilisis ex tellus eget libero. Suspendisse potenti. Proin tincidunt est ac urna posuere commodo. Fusce vitae bibendum sapien.").decode("utf-8")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt=TITULO, align="C")
pdf.ln()
pdf.ln()
pdf.multi_cell(180, 10, txt=text, align="L")
pdf.ln()

pdf.output("PDF_CREATED.pdf")
print("PDF gerado")