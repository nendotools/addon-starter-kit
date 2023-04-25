## Introduction

This is a starter repository for creating Blender Add-ons. It includes several
files necessary for building out an Add-on, including a global settings,
preferences UI, and a simple operator.

The repository also includes a bundler for creating distributable .zip files
to share your add-on with others.

## Structure

### \_\_init\_\_.py

This is the entry point for you add-on. It defines your project, provides
details for users to see in the Add-ons preferences, and loads the rest of
your add-on.

### settings.py

This file contains the global settings for your add-on. It is used to store
user preferences and manage the current state of the add-on.

### lib

This folder contains all of the code for your add-on. It can be organized in any
way you like, but it is recommended to keep the code for each feature in its own
file and larger features (such as complex UIs) in their own folder.

### operators

This folder contains all of the operators for your add-on. Operators are
functions that can be called from the UI or other operators. They are
typically used to perform actions on the scene, such as creating objects or
modifying existing ones.

### ui

This folder contains all of the UI code for your add-on. It is recommended to
keep the code for each UI in its own file.


## Requirements

This template utilizes type-hinting for improved code quality and clarity. As
such, add-ons created from this project should target Blender 2.94 and up. I'd
also recommend using a more recent version of python (3.9+) for your editor.

You may use this project as a base for older version of Blender, but all type
declarations will need to be removed.

### IDE language server support

For language servers to properly understand the bpy module structure, you'll
want to install [fake-bpy-module](https://github.com/nutti/fake-bpy-module). Follow the installation guide on the git repo.
I'd stick with the latest version unless you're using specific features not
available in older versions of Blender.

### Linting and Formatting

This template uses [flake8](https://github.com/PyCQA/flake8) to enforce common python standards along with some
Blender-specific tweaks to help get you started. Global changes should be made
using the `.flake8` file. Per-file and per-line exceptions can also be added.

Linting and formatting are optional features, but ideal for open-source or
multi-developer projects. This feature can be ignored if you do not want to
use it.
