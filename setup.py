from setuptools import setup, find_packages

setup(
    name="AttentionNotebookBot",
    version="1.0.5",
    authors=[
        {"name": "Natalia Khodorova", "email": "icxodnik@gmail.com"},
        {"name": "Leskovec Maksim", "email": "leskovecmaksim@gmail.com"},
        {"name": "Oleksandr Romashko", "email": "alex.rmshk@gmail.com"},
        {"name": "Filip Povidernyi", "email": "p.povidernyi@gmail.com"},
    ],
    description="A personal assistant bot for managing contacts and notes.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Filip-Povidernyi/Attention_notebook_bot",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "rich",
        "textual",
        "python-dateutil",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "start-bot=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
