import subprocess

def convert_symbol(text):
    """
    Helper function to replace common symbols with LaTeX equivalents.
    """
    text = re.sub(r'alpha', r"$\\alpha$", text)
    text = re.sub(r'beta', r"$\\beta$", text)
    text = re.sub(r'gamma', r"$\\gamma$", text)
    text = re.sub(r'delta', r"$\\delta$", text)
    text = re.sub(r'epsilon', r"$\\epsilon$", text)
    text = re.sub(r'pi', r"$\\pi$", text)
    text = re.sub(r'rho', r"$\\rho$", text)
    text = re.sub(r'sigma', r"$\\sigma$", text)
    text = re.sub(r'tau', r"$\\tau$", text)
    text = re.sub(r'phi', r"$\\varphi$", text)
    text = re.sub(r'psi', r"$\\psi$", text)
    text = re.sub(r'omega', r"$\\omega$", text)
    text = re.sub(r'lambda', r"$\\lambda$", text)
    text = re.sub(r'chi', r"$\\chi$", text)
    return text

def save_latex(latex_code, title, filename="output.tex"):
    """
    Save the LaTeX code as a full LaTeX document, including title.
    """
    full_latex = f"""
\\documentclass{{article}}
\\usepackage{{amsmath}}
\\title{{{title}}}
\\begin{{document}}

\\maketitle

{latex_code}

\\end{{document}}
    """
    with open(filename, 'w') as file:
        file.write(full_latex)

def compile_latex_to_pdf(latex_filename):
    """
    Compile the LaTeX file into a PDF using pdflatex.
    """
    try:
        subprocess.run(["pdflatex", latex_filename], check=True)
        print(f"PDF generated successfully from {latex_filename}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")
    except FileNotFoundError:
        print("Error: pdflatex not found. Please make sure it is installed and available in the system's PATH.")
