# 🐍 Python Virtual Environment & Package Management

---

## 🔹 1. What is a Virtual Environment?

A **virtual environment** is an isolated workspace where you can install and manage packages without affecting the global Python installation.  
It’s essential for working on multiple projects with different dependencies.

---

## 🔹 2. Creating and Activating a Virtual Environment

### Create Project Folder
```bash
mkdir myproject
cd myproject
```
## Create a Virtual Environment
```bash
python -m venv myvenv
```
## Activate the Environment
### ▶ On Windows:
```bash
myvenv\Scripts\activate
```
### ▶ On macOS/Linux:
```bash
source myvenv/bin/activate
```
### Deactivate
```bash
deactivate
```
### ✅ When activated, your terminal prompt will show something like:
```bash
(myvenv) C:\Users\Alireza\myproject>
```
### 🔹 3. Managing Packages with pip
#### Install a Package
```bash
pip install requests
```
### Install a Specific Version
```bash
pip install requests==4.8.0
```
### Search for a Package
```bash
pip search requests
```
**⚠️ Note: pip search might be deprecated in some versions of pip.
Instead, search directly on PyPI.org
.**
### Show Package Information
```bash
pip show requests
```
### pip show requests
```bash
pip freeze
```
### 🔹 4. Saving and Reusing Dependencies
#### Save All Dependencies to a File
```bash
pip freeze > requirements.txt
```
### Install Dependencies from a File
```bash
pip install -r requirements.txt
```
**✅ This ensures that anyone cloning your project can recreate the same environment easily.**
## 🔹 5. Good Practices

**Always use a virtual environment for each project.**

**Keep your dependencies in requirements.txt.**

**Before committing, deactivate the environment (deactivate) so you don’t push environment files.**

**Add /myvenv/ to .gitignore to prevent uploading virtual environments to GitHub.**

### 🧾 Example .gitignore
```bash
# Ignore virtual environment folder
myvenv/

# Ignore Python cache files
__pycache__/
*.pyc
```
