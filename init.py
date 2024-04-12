#! python3

import argparse
from pathlib import Path
import string
import subprocess


argparser = argparse.ArgumentParser(description="Initialize the repository.")
argparser.add_argument("distname", help="name of the package")
args = argparser.parse_args()


tags = subprocess.check_output(["git", "tag"], universal_newlines=True)
if tags:
    subprocess.check_call(["git", "tag", "-d"] + tags.split())


distname_files = (
    Path("doc/Makefile"),
    Path("doc/src/conf.py"),
    Path("doc/src/index.rst"),
    Path("python-skel.spec"),
    Path("setup.py"),
    Path("tests/conftest.py"),
    Path("tests/test_00.py"),
)
distname = args.distname
pkgname = args.distname.replace('-', '_')

for path in distname_files:
    with path.open("rt") as f:
        s = string.Template(f.read())
    with path.open("wt") as f:
        f.write(s.safe_substitute(distname=distname, pkgname=pkgname))
    subprocess.check_call(["git", "add", str(path)])

Path("src/%s" % pkgname).mkdir()
subprocess.check_call(["git", "mv",
                       "python-skel.spec", "python-%s.spec" % distname])
subprocess.check_call(["git", "mv",
                       "src/distname/__init__.py",
                       "src/%s/__init__.py" % pkgname])
subprocess.check_call(["git", "rm", "init.py"])
subprocess.check_call(["git", "commit", "-m", "Set the name of the package"])
Path("src/distname").rmdir()

print("""Name of the package set.

Next steps: fix the url in setup.py and adapt the description of the
package in the doc string in setup.py and in the README.rst.

Also have a look into the documentation sources in doc/src""")
