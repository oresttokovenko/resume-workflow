# Resume Workflow Tool

The Resume Workflow tool automates the creation of customized resume directories and files for specific job applications, and gracefully handles existing directories. At a minimum, this tool creates a `job_description.txt` file, but has the capacity for much more. The _template folder can be used to include additional template files, and it can either be empty or contain files to be copied over during the resume generation process.

## For Use

1. **Install `pipx`:**
   ```sh
    brew install pipx
    pipx ensurepath
   ```

2. **Install the Resume Workflow tool:**
   ```sh
   pipx install git+https://github.com/oresttokovenko/typst-resume-workflow.git --python 3.11
   ```

3. **Run the tool from anywhere on your machine, no virtual environment required:**
   ```sh
   resume_workflow -c Facebook -j "software engineer"
   ```

### Using the `-t/-T` Flag and the `_template` Folder

The `resume_workflow` tool includes an optional `-t/-T` flag to specify whether to use the `_template` folder. If the `_template` folder is present and contains files, those files will be copied over to the new job directory. 

- To use the template folder (default behavior):
   ```sh
   resume_workflow -c Facebook -j "software engineer" -t
   ```
- To run without using the template folder:
   ```sh
   resume_workflow -c Facebook -j "software engineer" -T
   ```

If the `_template` folder is empty or not present, the tool will still function as expected, creating the necessary directories and files for your resume workflow.


## For Contributors

1. **Create a Virtual Environment and Activate it:**
   ```sh
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install the Tool in Editable Mode:**
   ```sh
   pip install --editable .
   ```

3. **Run the Tool from Within the Virtual Environment:**
   ```sh
   resume_workflow -c facebook -j "software engineer"
   ```

Make sure to replace `"facebook"` and `"software engineer"` with the desired company name and job title respectively.