import glob
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansys.pyensight.core import Session


def test_basic(launch_app_and_ensight):
    session: "Session"
    app, session = launch_app_and_ensight
    session.load_example("waterbreak.ens")
    app.dsg_export()
    if not hasattr(session._launcher, "_enshell"):
        app._server_process.wait()
    app.on_shutdown()
    assert os.path.isfile(os.path.join(app.destination, "dsg_scene.usd"))
    assert len(glob.glob(os.path.join(app.destination, "Parts", "*.usd"))) == 5
    session.close()
