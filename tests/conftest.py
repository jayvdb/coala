try:
    from pytest_reqs import check_requirements
except ImportError:
    def check_requirements(*args, **kwargs):
        pass


def pytest_collection_modifyitems(config, session, items):
    check_requirements(config, session, items)
