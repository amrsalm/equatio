import re

def parse_to_latex(raw_notes):
    """
    Convert basic mathematical expressions in plain text to LaTeX format.
    """
    # Convert powers (x^2 -> $x^2$)
    raw_notes = re.sub(r'(\w+)\^(\d+)', r'$\1^{\2}$', raw_notes)

    # Convert square roots (sqrt(x) -> $\sqrt{x}$)
    raw_notes = re.sub(r'sqrt\((.*?)\)', lambda m: f"$\\sqrt{{{m.group(1)}}}$", raw_notes)

    # Convert fractions (1/2 -> $\frac{1}{2}$)
    raw_notes = re.sub(r'(\d+)/(\d+)', lambda m: f"$\\frac{{{m.group(1)}}}{{{m.group(2)}}}$", raw_notes)

    # Convert trigonometric functions (sin(x) -> $\sin(x)$, cos(x) -> $\cos(x)$, etc.)
    raw_notes = re.sub(r'(sin|cos|tan|sec|csc|cot)\((.*?)\)', lambda m: f"${m.group(1)}({m.group(2)})$", raw_notes)

    # Convert summation (sum(x, i=1, n) -> $\sum_{i=1}^{n}x$)
    raw_notes = re.sub(r'sum\((.*?)\s*,\s*i=(\d+)\s*,\s*n\)', lambda m: f"$\\sum_{{i={m.group(2)}}}^{{n}} {m.group(1)}$", raw_notes)

    # Convert integrals (int(x) -> $\int x \, dx$)
    raw_notes = re.sub(r'int\((.*?)\)', lambda m: f"$\\int {m.group(1)} \\, dx$", raw_notes)

    # More mathematical functions and symbols
    raw_notes = re.sub(r'log\((.*?)\)', lambda m: f"$\\log{{{m.group(1)}}}$", raw_notes)
    raw_notes = re.sub(r'(\w+)\((.*?)\)', lambda m: f"${m.group(1)}({m.group(2)})$", raw_notes)
    raw_notes = re.sub(r'limit\((.*?),\s*i=(\d+)\)', lambda m: f"$\\lim_{{i={m.group(2)}}} {m.group(1)}$", raw_notes)
    raw_notes = re.sub(r'ln\((.*?)\)', lambda m: f"$\\ln({m.group(1)})$", raw_notes)
    raw_notes = re.sub(r'floor\((.*?)\)', lambda m: f"$\\lfloor {m.group(1)} \\rfloor$", raw_notes)
    raw_notes = re.sub(r'ceiling\((.*?)\)', lambda m: f"$\\lceil {m.group(1)} \\rceil$", raw_notes)
    raw_notes = re.sub(r'abs\((.*?)\)', lambda m: f"$|{m.group(1)}|$", raw_notes)
    raw_notes = re.sub(r'angle\((.*?)\)', lambda m: f"$\\angle {m.group(1)}$", raw_notes)
    raw_notes = re.sub(r'frac\((.*?)\s*,\s*(.*?)\)', lambda m: f"$\\frac{{{m.group(1)}}}{{{m.group(2)}}}$", raw_notes)
    raw_notes = re.sub(r'det\((.*?)\)', lambda m: f"$\\text{det}({m.group(1)})$", raw_notes)

    # Plain text to LaTeX conversions for descriptive phrases
    raw_notes = re.sub(r'integral from (.*?) to (.*?)', lambda m: f"$\\int_{{{m.group(1)}}}^{{{m.group(2)}}} dx$", raw_notes)
    raw_notes = re.sub(r'limit as (.*?) approaches (.*?)', lambda m: f"$\\lim_{{{m.group(1)}}} {m.group(2)}$", raw_notes)
    raw_notes = re.sub(r'partial derivative of (.*?) with respect to (.*?)', lambda m: f"$\\frac{{\\partial {m.group(1)}}}{{\\partial {m.group(2)}}}$", raw_notes)

    # New mathematical symbols added:
    raw_notes = re.sub(r'alpha', lambda m: "$\\alpha$", raw_notes)
    raw_notes = re.sub(r'beta', lambda m: "$\\beta$", raw_notes)
    raw_notes = re.sub(r'gamma', lambda m: "$\\gamma$", raw_notes)
    raw_notes = re.sub(r'delta', lambda m: "$\\delta$", raw_notes)
    raw_notes = re.sub(r'epsilon', lambda m: "$\\epsilon$", raw_notes)
    raw_notes = re.sub(r'pi', lambda m: "$\\pi$", raw_notes)
    raw_notes = re.sub(r'rho', lambda m: "$\\rho$", raw_notes)
    raw_notes = re.sub(r'sigma', lambda m: "$\\sigma$", raw_notes)
    raw_notes = re.sub(r'tau', lambda m: "$\\tau$", raw_notes)
    raw_notes = re.sub(r'phi', lambda m: "$\\varphi$", raw_notes)
    raw_notes = re.sub(r'psi', lambda m: "$\\psi$", raw_notes)
    raw_notes = re.sub(r'omega', lambda m: "$\\omega$", raw_notes)
    raw_notes = re.sub(r'lambda', lambda m: "$\\lambda$", raw_notes)
    raw_notes = re.sub(r'chi', lambda m: "$\\chi$", raw_notes)

    # Common operators and symbols
    raw_notes = re.sub(r'leq', lambda m: "$\\leq$", raw_notes)
    raw_notes = re.sub(r'geq', lambda m: "$\\geq$", raw_notes)
    raw_notes = re.sub(r'neq', lambda m: "$\\neq$", raw_notes)
    raw_notes = re.sub(r'approx', lambda m: "$\\approx$", raw_notes)
    raw_notes = re.sub(r'eq', lambda m: "$=$", raw_notes)
    raw_notes = re.sub(r'plusminus', lambda m: "$\\pm$", raw_notes)
    raw_notes = re.sub(r'infty', lambda m: "$\\infty$", raw_notes)
    
    return raw_notes
