import PyPDF2

with open('./scripting/pdf-playground/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    print(page.extract_text())

    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('./scripting/pdf-playground/dummy-output.pdf', 'wb') as output:
        writer.write(output)