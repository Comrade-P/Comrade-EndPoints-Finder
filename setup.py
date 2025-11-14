from setuptools import setup, find_packages

setup(
    name="comrade-endpoints",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pyfiglet",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "comrade_endpoints=comrade.cli:main",  # <--- this defines your CLI command
        ],
    },
)
