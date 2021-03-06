import time
import sys
import getopt
import subprocess
import os

def guess():
    print("--> Analyzing")
    toprint = ""
    files = []
    py = 0
    njs = 0
    rb = 0
    el = 0
    other = 0
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(f"{os.getcwd()}/{file}"):
            files.append(file)
            if file.endswith(".py"):
                py += 1
            if file.endswith(".js"):
                njs += 1
            if file.endswith(".rb"):
                rb += 1
            if file.endswith(".el"):
                el += 1
            if file.endswith(".js") == False and file.endswith(".py") == False and file != "pyproject.toml" and file != "package.json" and file != "Gemfile":
                other += 1
    if "Gemfile" in files:
        rb += 1
    if "pyproject.toml" in files:
        py += 1
    if "package.json" in files:
        njs += 1
    if "Cask" in files:
        el += 1
    if py != 0:
        percentage = py / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        toprint += f"Python: {percentage}%\n"
    if njs != 0:
        percentage = njs / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        toprint += f"Nodejs: {percentage}%\n"
    if rb != 0:
        percentage = rb / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        toprint += f"Ruby: {percentage}%\n"
    if el != 0:
        percentage = el / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        toprint += f"Elisp: {percentage}%\n"
    percentage = other / len(files)
    percentage = percentage * 100
    percentage = round(percentage)
    toprint += f"Other: {percentage}%\n"
    print(toprint)
    print(f"--> {len(files)} files scanned")

def alz():
    pcs = []
    toprint = ""
    files = []
    py = 0
    njs = 0
    rb = 0
    el = 0
    largest = [0,0]
    other = 0
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(f"{os.getcwd()}/{file}"):
            files.append(file)
            if file.endswith(".py"):
                py += 1
            if file.endswith(".js"):
                njs += 1
            if file.endswith(".rb"):
                rb += 1
            if file.endswith(".el"):
                el += 1
            if file.endswith(".js") == False and file.endswith(".py") == False and file != "pyproject.toml" and file != "package.json" and file != "Gemfile":
                other += 1
    if "Gemfile" in files:
        rb += 1
    if "pyproject.toml" in files:
        py += 1
    if "package.json" in files:
        njs += 1
    if "Cask" in files:
        el += 1
    if py != 0:
        percentage = py / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        py = percentage
        toprint += f"Python: {percentage}%\n"
    if njs != 0:
        percentage = njs / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        njs = percentage
        toprint += f"Nodejs: {percentage}%\n"
    if rb != 0:
        percentage = rb / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        rb = percentage
        toprint += f"Ruby: {percentage}%\n"
    if el != 0:
        percentage = el / len(files)
        percentage = percentage * 100
        percentage = round(percentage)
        toprint += f"Elisp: {percentage}%\n"
    pcs.append(f"ruby {rb}")
    pcs.append(f"python {py}")
    pcs.append(f"nodejs {njs}")
    pcs.append(f"elisp {el}")
    for item in pcs:
        item = item.split()
        if int(item[1]) > int(largest[1]):
            largest = item
    return largest[0]
