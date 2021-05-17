from pathlib import Path
import $distname

def pytest_report_header(config):
    """Add information on the package version used in the tests.
    """
    modpath = Path($distname.__file__).resolve().parent
    return [ "$distname: %s" % ($distname.__version__),
             "           %s" % (modpath)]
