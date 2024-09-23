import os
import pytest
from omni.kit_app import KitApp
from ansys.pyensight.core import DockerLauncher, LocalLauncher



os.environ["OMNI_KIT_ACCEPT_EULA"] = "yes"

EXTS_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exts", "ansys.tools.omniverse.core")
CONFIG_PATH = os.path.join(EXTS_FOLDER, "config", "extension.toml")


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    This let's you specify the install path when you run pytest:
    $ pytest tests --install-path "/ansys_inc/v231/CEI/bin/ensight"
    TODO: Default must be set to the one on the CI/CD server.
    """
    parser.addoption(
        "--install-path",
        action="store",
    )
    parser.addoption("--use-local-launcher", default=False, action="store_true")


def on_startup(app):
    from ansys.tools.omniverse.core import AnsysToolsOmniverseCoreServerExtension
    instance = AnsysToolsOmniverseCoreServerExtension._service_instance
    return instance

@pytest.fixture
def launch_ensight(tmpdir, pytestconfig: pytest.Config):
    data_dir = tmpdir.mkdir("datadir")
    use_local = pytestconfig.getoption("use_local_launcher")
    if use_local:
        launcher = LocalLauncher()
    else:
        launcher = DockerLauncher(data_directory=data_dir, use_dev=True)
    session = launcher.start()
    return session, use_local, data_dir

@pytest.fixture
def create_app(launch_ensight):
    app = KitApp()
    # Launch Kit
    session, use_local, data_dir = launch_ensight
    commands = [
            CONFIG_PATH, 
            "--ext-path", 
            EXTS_FOLDER, 
            "--enable", 
            "ansys.tools.omniverse.core",
        ]
    app.startup()
    additional = []
    export_location = data_dir.mkdir("dsg_export")
    if use_local:
        additional =  [
            f"--/exts/ansys.tools.omniverse.core/omniUrl={export_location}",
        ]
    else:
        additional =  [
            "--/exts/ansys.tools.omniverse.core/omniUrl=/data/dsg_export/",
        ]   
    additional.extend([
        f"--/exts/ansys.tools.omniverse.core/dsgUrl=grpc://127.0.0.1:{session._grpc_port}",
        f"--/exts/ansys.tools.omniverse.core/securityCode={session._secret_key}"
    ])
    commands.extend(additional)
    app.startup(commands)
    instance = on_startup(app)
    if not use_local:
        container_name = session._launcher._container.name
        version = session._launcher._enshell.ansys_version()
        instance.create_container(container_name, version, session._launcher._data_directory)
    return instance, session
    

