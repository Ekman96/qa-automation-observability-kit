![tests](https://github.com/Ekman96/qa-automation-observability-kit/actions/workflows/test.yml/badge.svg)
# QA Automation Observability Kit

A production-style QA automation project focused on **test observability and debuggability**, not just execution.

## 🚀 What this project demonstrates

### UI Automation
- Selenium + Pytest
- Page Object Model (POM)
- Headless browser execution (CI-friendly)
- Automatic artifacts on failure:
  - Screenshots
  - Page HTML source

### API Automation
- Pytest + Requests
- Smoke/health checks
- Graceful handling of blocked environments (skip on 401/403)

### Reporting & CI
- Pytest HTML report (self-contained)
- GitHub Actions CI pipeline
- Test artifacts uploaded from CI runs

---

## 🧪 Run tests locally

### Install dependencies
```bash
pip install -r requirements.txt
