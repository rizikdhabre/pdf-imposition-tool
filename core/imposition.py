import fitz  

def impose_2up(input_path, output_path):
    source = fitz.open(input_path)
    output = fitz.open()

    page_width, page_height = source[0].rect.width, source[0].rect.height

    for i in range(0, len(source), 2):
        new_page = output.new_page(width=page_width * 2, height=page_height)
        new_page.show_pdf_page(
            fitz.Rect(0, 0, page_width, page_height),
            source,
            i
        )
        if i + 1 < len(source):
            new_page.show_pdf_page(
                fitz.Rect(page_width, 0, page_width * 2, page_height),
                source,
                i + 1
            )

    output.save(output_path)
    output.close()
    source.close()
