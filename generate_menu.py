import json

# LaTeX-Template laden
with open("template/last_resort_template.tex", "r", encoding="utf-8") as f:
    template = f.read()

# JSON-Daten
with open("drinks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def section(title, items):
    output = f"\\textbf{{\\large {title}}}\\\\\n\\rule{{\\linewidth}}{{0.4pt}}\n\\vspace{{0.5em}}\n\n"
    output += "\\begin{tabularx}{\\linewidth}{>{\\raggedright\\arraybackslash}X r}\n"
    for drink in items:
        output += f"\\textbf{{{drink['name']}}} & €\\,{drink['price']} \\\\\n"
        output += f"\\small\\textit{{{drink['ingredients']}}} & \\\\[0.6em]\n"
    output += "\\end{tabularx}\n\n\\vspace{1em}\n"
    return output

# Gruppenweise zusammenbauen
left_col = section("Cocktails \& Longdrinks", data["cocktails"])
left_col += section("Cocktail der Woche", data["specials"])
right_col = section("Softdrinks \& Alkoholfreies", data["softdrinks"])
right_col += section("Shots", data["shots"])
right_col += section("Bier", data["beer"])

latex_content = (
    "\\noindent\n"
    "\\begin{minipage}[t]{0.48\\textwidth}\n"
    + left_col +
    "\\end{minipage}\n\\hfill\n"
    "\\begin{minipage}[t]{0.48\\textwidth}\n"
    + right_col +
    "\\end{minipage}\n"
)

# delete and create folder pdf
import os
if os.path.exists("pdf"):
    for file in os.listdir("pdf"):
        file_path = os.path.join("pdf", file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# In finaler Datei speichern
with open("pdf/last_resort_generated.tex", "w", encoding="utf-8") as f:
    f.write(template.replace("{content}", latex_content))
