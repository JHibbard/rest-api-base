# Standard Libraries
from unittest import mock

# External Libraries
from click.testing import CliRunner

# Internal Libraries
from rab.cli import server


def test_server_static_prefix_validation():
    with mock.patch("rab.cli._run_server") as run_server_mock:
        CliRunner().invoke(server)
        run_server_mock.assert_called_once()
