from setuptools import setup, find_namespace_packages

APP_NAME = "rab"
VERSION = "0.1.0"
LICENSE = "MIT"
AUTHOR = "James Hibbard"
DESCRIPTION = (
    "REST API Base"
)

setup(
    name=APP_NAME,
    version=VERSION,
    license=LICENSE,
    author=AUTHOR,
    description=DESCRIPTION,
    install_requires=[
        "connexion[swagger-ui]==2.7.0",
        "PyYAML==5.3.1",
        "Flask==1.1.2",
        "click==7.1.2",
        "Flask-Cors==3.0.9",
        "gunicorn==20.0.4",
    ],
    extras_require={
        "docs": ["Sphinx==3.3.1", "sphinx-click==2.5.0", ],
        "quality": ["black==20.8b1", "pyflakes==2.2.0", "radon==4.3.2", ],
    },
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.yaml"], },
    entry_points="""
    [console_scripts]
        rab=rab.cli:cli
    """,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
