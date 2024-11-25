# Djehuty Documentation  

Welcome to the **Djehuty Documentation** repository! 
This repository is used to build the documentation for [**Djehuty**](https://github.com/4TUResearchData/djehuty), 
the repository system powering the [**4TU.ResearchData repository**](https://data.4tu.nl/).  

The documentation is hosted [here](https://leilaicruz.github.io/djehuty-mkdocs/) 
and is created using [MkDocs](https://www.mkdocs.org/). 
The API documentation adheres to the **OpenAPI Documentation Standard**.  

---

## Prerequisites  

Ensure you have Python and `pip` installed on your system before proceeding.

---

## Installation  

Recreate the working environment from the `requirements.txt` file located in the root directory. Follow these steps:

1. Clone the repository:  

   ```bash
   git clone git@github.com:leilaicruz/djehuty-mkdocs.git
   ```

3. Navigate into the repository folder:

   ```bash
     cd djehuty-mkdocs
    ```

4. Create and activate a virtual environment:

a. Install virtualenv if not already installed:
  
   ```bash
    pip install virtualenv
   ```

b. Create a new virtual environment:
   
   ```bash
    djehuty-mkdocs
   ```

c. Activate the virtual environment:

 - On Unix/macOS:

   ```bash
     source djehuty-mkdocs/bin/activate
    ```

 - On Windows (Command Prompt): 

   ```bash
     djehuty-mkdocs\Scripts\activate
    ```

4. Install dependencies from the requirements.txt file:

    ```bash
     pip install -r requirements.txt

    ```
---

## Building the Documentation
The documentation files are located in the `documentation/docs` folder in Markdown (`.md`) format. Each file corresponds to a specific section in the documentation.

The API documentation is generated from the `openapi_spec_model.yml` file.

### Making Changes
To modify the documentation:

1. Edit the relevant Markdown files in `documentation/docs`.
2. If modifying the API documentation, update the `openapi_spec_model.yml` file.

### Previewing Locally
To view the documentation locally, navigate to the documentation folder and run:

    ```
     mkdocs serve
    ```

The documentation will be served locally, usually at `http://127.0.0.1:8000/`.

### Deploying to GitHub Pages
To publish the documentation to GitHub Pages:
   
    ```
     mkdocs gh-deploy
    ```

---

## Building the API
The API documentation is generated from the `openapi_spec_model.yml` file. 
To update it, modify the `.yml` file and rebuild the project. 
Ensure your changes adhere to the OpenAPI standards.

---

## Contributing
We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and submit a pull request.

Please follow standard practices and write clear commit messages.

---

## References
- [MkDocs Documentation](https://www.mkdocs.org/)
- [OpenAPI Specification](https://swagger.io/specification/)

---

## Next Steps
 - Fix rendering issues with tables and figures.
 - Improve styling and accessibility of the documentation.
