# Resume Workflow CLI

The Resume Workflow CLI tool automates the tedious parts of creating folders for each company you intend on applying to and copying over template files. This tool, as a best practice, creates a `job_description.txt` file within the generated directories but offers the capability for more customization. The `_template` folder can be used to include additional template files, which can either be empty or contain files to be copied over during the resume generation process.

## Benefits
- **Time-Saving:** Automates the creation of directory structures and copying of template files, reducing manual effort.
- **Consistency:** Ensures a standardized structure and format for each job application, as well as gracefully handles existing directories
- **Flexibility:** Allows for customization through the `_template` folder, making it adaptable to different application requirements (Word, LaTex, Typst, etc)

Here is an example of basic structure using LaTeX and leveraging the `_template` option

```
_template/
├── font
│   └── font.otf
└── main.tex
```

A generated directory for a Software Engineer role at Facebook

```
Facebook
└── software_engineer
    ├── font
    │   └── font.otf
    ├── job_description.txt
    └── main.tex
```

## For Use

1. **Install `pipx`:**
   ```sh
    brew install pipx
    pipx ensurepath
   ```

2. **Install the Resume Workflow tool:**
   ```sh
   pipx install git+https://github.com/oresttokovenko/resume-workflow.git --python 3.11
   ```

3. **Run the tool from anywhere on your machine, no virtual environment required:**
   ```sh
   resume-workflow -c Facebook -j "software engineer"
   ```

### Using the `-t/-T` Flag and the `_template` Folder

The `resume_workflow` tool includes an optional `-t/-T` flag to specify whether to use the `_template` folder. If the `_template` folder is present and contains files, those files will be copied over to the new job directory. 

- To use the template folder (default behavior):
   ```sh
   resume-workflow -c Facebook -j "software engineer" -t
   ```
- To run without using the template folder:
   ```sh
   resume-workflow -c Facebook -j "software engineer" -T
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
   resume-workflow -c facebook -j "software engineer"
   ```