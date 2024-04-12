from pathlib import Path
import $pkgname

def pytest_report_header(config):
    """Add information on the package version used in the tests.
    """
    modpath = Path($pkgname.__file__).resolve().parent
    return [ "$distname: %s" % ($pkgname.__version__),
             "           %s" % (modpath)]
