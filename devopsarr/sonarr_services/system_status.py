from datetime import datetime
from devopsarr.adapter import RestAdapter
from devopsarr.models import ArrModel


class SystemStatus(ArrModel):
    appName: str
    instanceName: str
    version: str
    buildTime: datetime
    isDebug: bool
    isProduction: bool
    isAdmin: bool
    isUserInteractive: bool
    startupPath: str
    appData: str
    osName: str
    osVersion: str
    isMonoRuntime: bool
    isMono: bool
    isLinux: bool
    isOsx: bool
    isWindows: bool
    mode: str
    branch: str
    authentication: str
    sqliteVersion: str
    urlBase: str
    runtimeVersion: str
    runtimeName: str
    startTime: datetime
    packageVersion: str
    packageAuthor: str
    packageUpdateMechanism: str


class SystemStatusClient():
    base_path = '/system/status/'

    def __init__(self, adapter: RestAdapter):
        self._adapter = adapter

    # get the system status
    def get(self) -> SystemStatus:
        response = self._adapter.get(f'{self.base_path}')
        return SystemStatus(**response.data)
