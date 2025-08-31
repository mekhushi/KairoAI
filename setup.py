from setuptools import setup, find_packages

setup(
    name="kairoAI",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai", "langchain", "chromadb", "rich", "typer", "pypdf", "tiktoken"
    ],
    entry_points={
        "console_scripts": [
            "kairoAI = kairoAI.cli:app",
        ],
    },
    python_requires=">=3.8",
)
   
