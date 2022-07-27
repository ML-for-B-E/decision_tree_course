import setuptools
from pathlib import Path

SRC_DIR = "src"


def get_install_requires():
    requirement_paths = get_requirement_paths()
    return filter_libraries(requirement_paths)


def get_requirement_paths(
    requirement_dir: Path = Path("requirements"),
    included_names: list = ["prod"],
):
    requirement_paths = []
    for file_path in requirement_dir.glob("**/*.txt"):
        if file_path.with_suffix("").name in included_names:
            requirement_paths.append(file_path)
        if file_path.parent.name in included_names:
            requirement_paths.append(file_path)
    return requirement_paths


def filter_libraries(
    requirement_paths,
    operators: list = ["=", "<", ">"],
):
    install_requires = []
    for requirement_path in requirement_paths:
        libs = []
        with open(requirement_path) as fh:
            for lib in fh.read().split("\n"):
                if any((operator in lib) for operator in operators):
                    libs.append(lib)
        install_requires.extend(libs)
    return install_requires


package_name = Path.cwd().name
python_version = "3.8.5"
install_requires = get_install_requires()

setuptools.setup(
    name=package_name,
    version="dev",
    author="Fondation Vallet",
    author_email="adkevinkpakpo@gmail.com",
    packages=setuptools.find_packages(where=SRC_DIR),
    package_dir={"": SRC_DIR},
    classifiers=[
        "Programming Language :: Python :: 3",
        "(c) Fondation Vallet",
        "Operating System :: OS Independent",
    ],
    python_requires=f">={python_version}",
    install_requires=install_requires,
)
