import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    setattr(item, "rep_" + result.when, result)

@pytest.fixture(scope="function", autouse=True)
def capture_screenshot_on_failure(request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        with allure.step("Taking screenshot on failure"):
            pass  # Extend if Playwright fixture available
