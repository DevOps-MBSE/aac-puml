[![Main branch aac-puml Workflow](https://github.com/DevOps-MBSE/aac-puml/actions/workflows/main-branch.yml/badge.svg)](https://github.com/DevOps-MBSE/aac-puml/actions/workflows/main-branch.yml)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/from-referrer/)

   This plugin implements a conversion from an AaC model definition specified in an .aac file
   to a PlantUML (PUML) file. (see https://plantuml.com)

   Tools exist at the the above website to convert the PUML file to a various types of diagram images.
   These types correspond to some traditional SysML diagram types:
        - Requirement diagram (REQ)
        - Structure Diagrams
        - Block Definition Diagram (BDD)
        - Internal Block Diagram (IBD)
        - Parametric Diagram (PAR)
        - Package diagram (PKG)
        - Behavior Diagrams
        - Activity diagram (ACT)
        - Sequence diagram (SD)
        - State Machine diagram (STM)
        - Use Case diagram (UC)

PYTHON VERSION COMPATIBILITY:
   Currently, Python version 3.9.13 is required to avoid certain dependency version issues.

pyproject.toml vs setup.py
    Previously, this project was built with dependency information kept in a setup.py script.
    However, the preferred method is to use pyproject.toml to set the project-level options.
    Required modules are kept in the requirements.in file, and then the pip-compile command is
    used to add hashes to the requirements.txt file for enhanced security (see additional
    instructions below).

   To coincide with these changes, some changes to tox.ini and the addition of a MANIFEST.ini file were also necessary.

    These lines were added to tox.ini:
    ```
        isolated_build = True
        skipsdist = True
    ```

    A MANIFEST file with these lines was added:
    ```
        graft src
        graft tests
        include tox.ini
        include src/puml/.aac
    ```

TO BUILD FROM TERMINAL:
```
   cd python
   pip install -e .
```

TO TEST FROM TERMINAL:
```
   cd python
   pip install -e .
   python -m unittest
```

To generate a requirements.txt file populated with hashes, use:
```
   pip install pip-tools
   pip-compile --generate-hashes pyproject.toml
```
