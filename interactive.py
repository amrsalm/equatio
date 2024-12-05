from latex_parser import parse_to_latex
from latex_helper import save_latex, compile_latex_to_pdf

def interactive_input():
    """
    Handle interactive user input and process LaTeX generation.
    """
    print("Enter mathematical expressions (or type 'save' to save and generate PDF):")
    notes = []
    while True:
        line = input()
        if line.strip().lower() == 'save':
            break
        notes.append(line)

    raw_notes = ' '.join(notes)
    latex_code = parse_to_latex(raw_notes)
    title = input("Enter a title for the document: ")
    filename = input("Enter a filename for the LaTeX document (default: output.tex): ") or "output.tex"
    
    save_latex(latex_code, title, filename)
    compile_latex_to_pdf(filename)
