### Waterproofing Inspections

Waterproofing inspection management

### Goals

- Provide a **Waterproofing Inspection form** for waterproofing project leads and inspection scope
- Capture **contact details**, **phone**, **email**, **dates**, **responsible user**, **value**, and **tags**
- Status: **New** → **In Progress** → **Done**
- Attach a **primary image**
- **Waterproofing tab** with:
  - **Interior**: Checkbox, Area (Bathroom / Ensuite / Laundry), Length, Width, New Text
  - **Exterior**: Checkbox, Area (Balcony / Stairs / Planter Box / Jacuzzi / Spa)

### What's included

- `Waterproofing Inspection` DocType with details and Waterproofing tab (Interior/Exterior sections)
- Desk shortcut at `/app/waterproofing-inspection`

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app waterproofing_inspections
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/waterproofing_inspections
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
