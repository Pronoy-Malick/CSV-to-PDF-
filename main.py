from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4" )
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Helvetica", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt= row["Topic"], ln=1, align="L")
    pdf.line(10,20,200,20)

pdf.output("output.pdf")