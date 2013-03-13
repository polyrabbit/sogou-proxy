from distutils.core import setup
import py2exe

setup(
    console=['bootstrap.py'],
    zipfile=None,
    options={
        "py2exe": {
            "optimize": 2,
            "compressed": True,
            "bundle_files": 1,
            "ascii": True,
            "includes": [
                "__future__",
                "logging",
                "os",
                "pyuv",
                "select",
                "socket",
                "struct",
                "time",
                "ConfigParser",
                ],
            "excludes": [
                "_ssl",
                "bdb",
                "calendar",
                "difflib",
                "doctest",
                "email",
                "gettext",
                "hashlib",
                "httplib",
                "inspect",
                "locale",
                "mimetools",
                "mimetypes",
                "optparse",
                "pdb",
                "pickle",
                "pyuv",
                "rfc822",
                "ssl",
                "subprocess",
                "tempfile",
                "threading",
                "tokenize",
                "tornado",
                "tornado-pyuv",
                "unittest",
            ]
        }
    }
)