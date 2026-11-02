# saucedemo-playwright

[![Tests](https://github.com/MufazaMajeed09/saucedemo-playwright/actions/workflows/tests.yml/badge.svg)](https://github.com/MufazaMajeed09/saucedemo-playwright/actions)

## About
Automated end-to-end UI tests for saucedemo.com, a demo e-commerce site.
Built with Playwright (Python) and pytest using the Page Object Model, and run automatically with GitHub Actions on every push and pull request.

## Tech stack
- Python 3.14
- Playwright (Python)
- pytest
- pytest-html (HTML test reports)
- GitHub Actions (CI)

## What's tested (12 tests)

| Area | Test |
|---|---|
| Login | Valid login |
| Login | Invalid login: wrong password, locked-out user, empty fields (parametrized) |
| Login | Logout |
| Products | 6 products are shown |
| Products | Sort by price: low to high |
| Products | Sort by price: high to low |
| Cart | Adding a product shows the cart badge |
| Cart | Removing the product hides the badge |
| Checkout | Full checkout completes with a confirmation message |
| Checkout | Missing first name shows an error |

## Project structure
```
saucedemo-playwright/
├── .github/workflows/tests.yml     # CI: runs tests, uploads HTML report
├── pages/                          # Page Object Model: one class per page
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py            # checkout information form
│   ├── finish_checkout_page.py     # checkout overview (Finish)
│   └── checkout_complete.py        # order confirmation
├── tests/
│   ├── conftest.py                 # shared fixtures (login, checkout form)
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
└── requirements.txt
```

## Design highlights
- **Page Object Model:** locators and actions live in page classes, so a UI change is fixed in one place
- **pytest fixtures:** a login fixture, plus a chained fixture that starts tests directly on the checkout form
- **Parametrization:** one test function covers several invalid-login cases
- **Stable locators:** `data-test` attributes
- **Auto-waiting assertions:** Playwright's `expect` instead of fixed waits

## How to run locally
```bash
git clone https://github.com/MufazaMajeed09/saucedemo-playwright.git
cd saucedemo-playwright
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install --with-deps chromium
pytest -v --html=report.html --self-contained-html
```

## Continuous integration
Every push and pull request to `main` runs the full suite on GitHub Actions.
The HTML report is uploaded as an artifact on each run (Actions tab → a run → Artifacts → test-report).