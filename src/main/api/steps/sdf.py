# Проанализируйте код, расскажите в каком порядке будут вызваны фикстуры. В тесте test_order напишите assert для списка order.

order = []


@pytest.fixture(scope="session")
def session_fixture():
    order.append("session_fixture")


@pytest.fixture(scope="module")
def module_fixture():
    order.append("module_fixture")


@pytest.fixture
def fixture_1(fixture_3, fixture_4):
    order.append("fixture_1")


@pytest.fixture(scope="function")
def fixture_3():
    order.append("fixture_3")


@pytest.fixture(autouse=True)
def autouse_fixture():
    order.append("autouse_fixture")


@pytest.fixture
def fixture_2():
    order.append("fixture_2")


@pytest.fixture
def fixture_4():
    yield
    order.append("fixture_4")


def test_order(fixture_1, module_fixture, fixture_2, session_fixture):
    assert order == [
        'session_fixture', 'module_fixture', 'autouse_fixture', 'fixture_3', 'fixture_1', 'fixture_2'
    ]