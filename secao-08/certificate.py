from docx import Document
from docx.shared import Pt


file_word = Document("secao-08\Certificado1.docx")

style_doc = file_word.styles["Normal"]

for i in file_word.paragraphs:

    if "@nome" in i.text:
        i.text = "Rafael Meireles"
        font = style_doc.font
        font.name = "Calibri (Corpo)"
        font.size = Pt(24)


file_word.save("Rafael_meireles.docx")
