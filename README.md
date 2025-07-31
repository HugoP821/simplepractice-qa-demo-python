# SimplePractice QA Demo - Python + Selenium + CI/CD

This project is a technical demonstration of interface test automation for the [SimplePractice](https://www.simplepractice.com/) site, using:

- Python 3.9
- Selenium WebDriver
- Pytest
- GitHub Actions para CI/CD
- Pytest HTML report
- Behave para pruebas BDD con Gherkin

---
# Errors in Sing Up
During automation and manual testing of the signup page (https://www.simplepractice.com → Start for free), the following behavior was observed:

- API call to signupSubmit returns a 422 Unprocessable Entity, blocking account creation.
- Response message: "You are not allowed to open an SP account at this time."
- Google reCAPTCHA fails to load due to CORS policy violations.
- Network trace and screenshots available under /docs/errors/.

### Error 422 in API SingUp

  <img width="2524" height="1262" alt="6286642d571913968bc3a09ee4b437e8184d53a08e12b1bcf2af54fdd86f8d88" src="https://github.com/user-attachments/assets/92605a62-b380-4e03-b853-589e50d3a7c7" />
