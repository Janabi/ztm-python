import PyPDF2

template = PyPDF2.PdfReader(open('./scripting/pdf-playground/super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('./scripting/pdf-playground/wtr.pdf', 'rb'))

output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

output.write('./scripting/pdf-playground/watermarked_output.pdf')