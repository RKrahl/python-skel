"""A skeleton for a Python package
"""

from distutils.core import setup
try:
    import distutils_pytest
except ImportError:
    pass

doclines = __doc__.strip().split("\n")


setup(
    name = "skel",
    version = "0.0",
    description = doclines[0],
    long_description = "\n".join(doclines[2:]),
    author = "Rolf Krahl",
    author_email = "rolf@rotkraut.de",
    license = "Apache-2.0",
    requires = [],
    packages = [],
    classifiers = [
        "Development Status :: 1 - Planning",
        # "Intended Audience :: ?",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        # "Topic :: ?",
    ],
)

