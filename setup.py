from pathlib import Path

from setuptools import find_packages, setup

SRC_DIR = "src"

package_name = Path.cwd().name


def get_long_description(filename="README.md"):
    with open(filename, "r") as fh:
        long_description = fh.read()
    return long_description


def extract_description(
    long_description, subsection_title, subsection_indentation="## "
):
    for section in long_description.split(subsection_indentation):
        if section.startswith(subsection_title):
            paragraphs = section.split("\n")[1:]
            return " ".join(paragraphs).strip()
    return "Improper readme for description parsing."


def get_install_requires():
    requirement_paths = get_requirement_paths()
    return filter_libraries(requirement_paths)


def get_requirement_paths(
    package_dir: Path = Path.cwd(),
):
    requirement_paths = []
    for file_path in package_dir.glob("requirements/*.txt"):
        requirement_paths.append(file_path)
    return requirement_paths


def filter_libraries(
    requirement_paths,
) -> list:
    install_requires = []
    for requirement_path in requirement_paths:
        libs = []
        with open(requirement_path) as file_handle:
            for lib in file_handle.read().split("\n"):
                libs.append(lib)
        install_requires.extend(libs)
    return install_requires


long_description = get_long_description()
description = extract_description(long_description, "Description")
install_requires = get_install_requires()

setup(
    name=package_name,
    version="0.0.1",
    author="(c) Fondation Vallet - Benin Excellence",
    author_email="adkevinkpakpo@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where=SRC_DIR),
    package_dir={"": SRC_DIR},
    include_package_data=True,
    install_requires=install_requires,
)
