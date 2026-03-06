import os
import re
import pytest
from playwright.sync_api import sync_playwright


def _sanitize_filename(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", name)
    return name[:150]


@pytest.fixture(scope="function")
def page():
    running_in_ci = os.getenv("GITHUB_ACTIONS", "false").lower() == "true"

    headless = running_in_ci

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            test_name = _sanitize_filename(item.nodeid)
            page.screenshot(path=f"screenshots/{test_name}.png", full_page=True)