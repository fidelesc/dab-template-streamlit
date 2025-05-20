# Databricks Streamlit Asset Bundle Template

This is a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for creating a [Databricks Asset Bundle](https://docs.databricks.com/en/dev-tools/bundles/index.html) that includes:

- A **Streamlit app** configured for deployment on Databricks
- An optional **job** to create or prepare data before the app is used
- Clean folder structure and examples for easy bootstrapping

---

## Template Contents

This template is organized as follows:

```

{{ project\_name }}/
├── app/
│   ├── app.py               # Streamlit app entry point
│   ├── app.yml              # Asset bundle config for Streamlit app
│   └── requirements.txt     # Streamlit dependencies
├── resources/
│   ├── app.yml              # Streamlit deployment config
│   └── job.yml              # Optional job config for data creation
├── scratch/
│   └── scratch\_notebook.py  # Example notebook for testing (placeholder)
├── src/
│   └── job\_notebook.py      # Notebook or script logic for the job
├── databricks.yml           # Main Databricks asset bundle configuration
└── README.md

````

---

## Usage

### Prerequisites

- Python 3.12+
- [Databricks CLI v0.200+](https://docs.databricks.com/en/dev-tools/cli/index.html)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

### Generate a New Project

```bash
# Create a new directory for your project
mkdir my_new_project
cd my_new_project

# Initialize the project using this cookiecutter template
databricks bundle init https://github.com/fidelesc/dab-template-streamlit.git
````

You will be prompted to enter:

| Prompt                | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `project_name`        | Name of your project. Used in folder and file names.                     |
| `databricks_username` | Your Databricks user email (used in job config).                         |
| `sql_warehouse_id`    | SQL Warehouse ID used by the Streamlit app to connect to Databricks SQL. |

---

## Development and Deployment

### Validate

```bash
databricks bundle validate
```

> The main configuration file is `databricks.yml`.

### Deploy (Job and App)

```bash
databricks bundle deploy --profile my_profile -t dev
```

---

## 💻 Local Development (Streamlit)

You can test your Streamlit app locally with:

```bash
cd app/
streamlit run app.py
```

Note: Connecting to a real SQL Warehouse requires valid credentials.

---

## 🧰 Customization Tips

* You can remove the `resources/job.yml` file and its reference in `databricks.yml` if you only need the app.
* The `scratch/` folder is optional and can be used for quick testing or development.
* Use `src/` to organize job-related logic cleanly, separating it from the Streamlit UI code.

---