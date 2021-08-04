from unittest.mock import Mock

import pytest

from .requester import Connection, Requester


@pytest.fixture
def connection() -> Mock:
    """
    Classes externas, bibliotecas, repositórios, etc.
    Todos esses itens que vão "fugir" do escopo da classe
    testada, idealmente devem ser um "mockados".
    """
    return Mock(Connection)


@pytest.fixture
def requester(connection: Mock) -> Requester:
    """
    A classe foco do teste deve ser instanciada de verdade.
    """
    return Requester(connection=connection)


@pytest.fixture
def item() -> dict:
    return {
        "id": 1,
        "name": "Felipe",
        "team": "jarvis",
    }


def test_get(connection, requester, item):
    connection.select.return_value = item

    response = requester.get(id=1)

    assert response == item

    connection.select.assert_called_once_with(id=1)


def test_create(connection, requester):
    response = requester.create(data={"name": "Berna", "team": "jarvis"})

    assert response.get("status") == "OK"

    connection.insert.assert_called_once_with({"name": "Berna", "team": "jarvis"})


def test_create_with_error(connection, requester):
    connection.insert.side_effect = TypeError

    response = requester.create(data={"name": "Berna", "team": "jarvis"})

    assert response.get("status") == "Error"

    connection.insert.assert_called_once_with({"name": "Berna", "team": "jarvis"})


def test_get_as_string():
    pass


def test_delete():
    pass


def test_update():
    pass