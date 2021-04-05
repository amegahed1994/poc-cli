from setuptools import setup

setup(
    name="mvt-cli",
    version="0.0.1",
    python_requires='>=3.6',
    install_requires=["click", "google-cloud-bigquery"],
    entry_points="""
        [console_scripts]
        mvt=__main__:main
    """,
)