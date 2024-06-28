from Parser import Parser
from Scanner import Scanner
from IntRep import IntRep

from markdown_pdf import MarkdownPdf
from markdown_pdf import Section

if __name__ == '__main__':
    scanner = Scanner()
    parser = Parser()
    intRep = IntRep()

    tokens = scanner.scan("Ejm2", debug=True)
    print(parser.parse(tokens))
    text = intRep.translate(tokens)
    print(text)
    
    # Asegúrate de tener las dependencias correctas para MarkdownPdf y Section.
    pdf = MarkdownPdf(toc_level=2)
    pdf.add_section(Section(text))
    pdf.meta["title"] = "User Guide"
    pdf.meta["author"] = "Vitaly Bogomolov"
    pdf.save("output2.pdf")