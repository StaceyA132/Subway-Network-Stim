"""Minimal setup script to make the package installable.

This lets users run the simulator with ``python -m subway_sim`` after
installing the package in editable mode (`pip install -e .`).
"""

from setuptools import setup, find_packages

setup(
    name="subway_sim",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # no external dependencies yet
    entry_points={
        "console_scripts": ["subway-sim=subway_sim.main:run"],
    },
    description="Small-scale subway network simulation and monitoring dashboard",
    author="",
    author_email="",
    url="",
)
