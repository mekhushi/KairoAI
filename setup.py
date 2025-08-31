from setuptools import setup, find_packages

setup(
    name="kairo",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai", "langchain", "chromadb", "rich", "typer", "pypdf", "tiktoken"
    ],
    entry_points={
        "console_scripts": [
            "kairo = kairo.main:app",
        ],
    },
)
