## Selenium test framework that:

- Uses pytest as the runner
- Applies Page Object Model (POM)
- Tests login


### TODO:

1. Product and Cart Functionality
- Test adding and removing products from the cart and verify cart updates accordingly
- Verify product detail pages by clicking individual products and checking their information
- Test product sorting and filtering options (e.g., price low to high, name A-Z)
- Implement the full checkout flow: add multiple products, fill in checkout info, complete purchase, and verify confirmation

2. Test Reporting
- Set up `pytest-html` or similar to generate HTML reports
- Customize reports to include screenshots on failure

3. Data-Driven Tests
- Use external CSV/JSON files to feed login or product data to tests
- Cover more cases efficiently without duplicating code

---

## Extras / things to learn

- Capture screenshots on test failures
- Implement retry logic for flaky tests
- Use `pytest` fixtures for setup and teardown
- Explore visual regression testing tools like Percy or Screener
- Document setup and usage clearly in the README
- Integrate tests with CI/CD pipelines like GitHub Actions
