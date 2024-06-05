# Resume Workflow Tool

#### Please note: This tool focuses on Typst - if you wish to use it for LaTeX please fork and edit as you wish

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
   resume_workflow -c facebook -j "software engineer"
   ```

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