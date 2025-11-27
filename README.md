# Resume Workflow CLI

Are you tired of the tedious task of tailoring each resume for every job application? Well you still have to do that, but the Resume Workflow CLI tool is here to help make it easier! This tool automates the creation of folders for each company you apply to and copies over template files (if you have a resume template which you prefer to use), allowing you to save time and stay organized. As a best practice, it creates a `job_description.txt` file within the generated directories but also offers customization capabilities. The `_template` folder can be customized with additional template files to be copied during the resume generation process, since you probably have a base resume that you want to start with. Focus on what matters most - the content of your resume, not copy and pasting.

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

## Benefits
- **Time-Saving:** Automates the creation of directory structures and copying of template files, reducing manual effort.
- **Consistency:** Ensures a standardized structure and format for each job application, as well as gracefully handles existing directories
- **Flexibility:** Allows for template customization through the `_template` folder, making it adaptable to different application requirements (Word, LaTeX, Typst, etc)

## For Use

1. **Install `uv`:**
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install the Resume Workflow tool:**
   ```sh
   uv tool install git+https://github.com/oresttokovenko/resume-workflow.git
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

1. **Sync dependencies with `uv`:**
   ```sh
   uv sync --all-extras
   ```

2. **Run the Tool:**
   ```sh
   uv run resume-workflow -c facebook -j "software engineer"
   ```

## Roadmap

- Allow users to use different base resumes for various types of job applications by defining multiple template folders 

   ```sh
   resume-workflow -c Apple -j "platform engineer" -t _infra_engineer
   ```
