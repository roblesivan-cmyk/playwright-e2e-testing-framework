![Python](https://img.shields.io/badge/Python-3.x-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-yellow)

# QA Playwright Framework (Python) – Saucedemo

Mini end-to-end (E2E) automation framework using **Playwright and Pytest** applied to the **Saucedemo** website.  
The goal of this project is to demonstrate a clean automation structure using **Page Object Model (POM)**, maintainable test design, and automated UI testing practices.

---
## Tech Stack
- Python
- Playwright (sync)
- Pytest
- pytest-html (reportes)
---
## Features

- Page Object Model (POM) architecture
- End-to-End UI testing
- Positive and negative test scenarios
- HTML test reporting
- Modular and maintainable test structure
---
## Project Structure
```
qa-playwright-framework/
├── pages/
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── tests/
│ ├── test_login.py
│ ├── test_inventory.py
│ └── test_checkout.py
└── conftest.py
```
---
## Test Coverage

This project includes automated tests covering the following flows:

---
### Login
- Successful login
- Locked user
- Invalid password
- Empty credentials validation
---
### Inventory
- Add products to cart
- Remove products from cart
- Cart persistence after page refresh
- Logout functionality
---
### Checkout
- Complete checkout flow (happy path)
- Required fields validation
---
## Setup

Create a virtual environment:

```
python -m venv .venv 
```
---
Activar entorno virtual:

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```
---
Install dependencies:

```bash
pip install -r requirements.txt
```
---
Install Playwright browsers:

```bash
playwright install
```
---

## Run Tests

Run all tests:

```bash
pytest
```
Generate HTML report:

```bash
pytest --html=report.html --self-contained-html
```
---
## Notes

This project follows the **Page Object Model (POM)** pattern to separate UI interaction logic from test cases, improving maintainability and scalability of the automation suite.