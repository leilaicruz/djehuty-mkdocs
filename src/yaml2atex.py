import yaml

# Load the OpenAPI YAML file
with open("C:/Users/linigodelacruz/Documents/4TU.ResearchData/Projects/Djehuty_documentation/documentation/docs/openapi_spec_model.yml", "r") as file:
    api_spec = yaml.safe_load(file)

# Open LaTeX file for writing
with open("api_documentation.tex", "w") as tex_file:
    # Write the document header
    tex_file.write(r"""\documentclass[a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{longtable}
\usepackage{enumitem}
\geometry{a4paper, margin=1in}

\title{API Documentation}
\author{Generated from OpenAPI Specification}
\date{\today}

\begin{document}
\maketitle

\section*{Introduction}
This document provides an overview of the API endpoints for the service.
It was generated from an OpenAPI specification.

\newpage
""")

    # Write API info
    tex_file.write(r"\section*{API Information}\n")
    tex_file.write(f"\\textbf{{Title}}: {api_spec['info']['title']}\\\\\n")
    tex_file.write(f"\\textbf{{Version}}: {api_spec['info']['version']}\\\\\n")
    tex_file.write(f"\\textbf{{Description}}: {api_spec['info'].get('description', 'No description provided')}\\\\\n\n")

    # Write each endpoint
    tex_file.write(r"\section*{Endpoints}\n")
    for path, methods in api_spec.get("paths", {}).items():
        tex_file.write(f"\\subsection*{{Endpoint: {path}}}\n")
        for method, details in methods.items():
            tex_file.write(f"\\subsubsection*{{Method: {method.upper()}}}\n")
            tex_file.write(f"\\textbf{{Summary}}: {details.get('summary', 'No summary provided')}\\\\\n")
            tex_file.write(f"\\textbf{{Description}}: {details.get('description', 'No description provided')}\\\\\n\n")

            # Write parameters
            parameters = details.get("parameters", [])
            if parameters:
                tex_file.write(r"\textbf{Parameters:}\n")
                tex_file.write(r"\begin{longtable}{|p{3cm}|p{3cm}|p{6cm}|}\hline\n")
                tex_file.write(r"Name & Location & Description \\\hline\n")
                for param in parameters:
                    name = param.get("name", "N/A")
                    location = param.get("in", "N/A")
                    description = param.get("description", "No description provided")
                    tex_file.write(f"{name} & {location} & {description} \\\\\n")
                tex_file.write(r"\end{longtable}\n\n")

            # Write responses
            responses = details.get("responses", {})
            if responses:
                tex_file.write(r"\textbf{Responses:}\n")
                tex_file.write(r"\begin{longtable}{|p{3cm}|p{8cm}|}\hline\n")
                tex_file.write(r"Status Code & Description \\\hline\n")
                for code, response in responses.items():
                    description = response.get("description", "No description provided")
                    tex_file.write(f"{code} & {description} \\\\\n")
                tex_file.write(r"\end{longtable}\n\n")

    # Write the document footer
    tex_file.write(r"\end{document}")
