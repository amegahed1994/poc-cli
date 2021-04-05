from setuptools import setup, find_packages

setup(
    name="poc-cli",
    version="0.0.1",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=["click", "google-cloud-bigquery"],
    entry_points="""
        [console_scripts]
        mvt=mvt-cli.src.cli:root
    """,
)
