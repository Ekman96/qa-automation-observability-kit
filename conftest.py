import os
import pytest
from datetime import datetime

ARTIFACTS_DIR = "artifacts"

def pytest_configure(config):
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("/", "_")

            driver.save_screenshot(
                os.path.join(ARTIFACTS_DIR, f"{test_name}_{ts}.png")
            )

            with open(
                os.path.join(ARTIFACTS_DIR, f"{test_name}_{ts}.html"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(driver.page_source)
