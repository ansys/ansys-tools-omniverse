import pytest

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansys.pyensight.core import Session


def test_basic(create_app):
    session: "Session"
    app, session = create_app
    app.dsg_export()