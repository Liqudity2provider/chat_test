from pathlib import Path

from setuptools import find_packages, setup


def read_requirements(path):
    try:
        with path.open(mode="rt", encoding="utf-8") as fp:
            # allows to comment in for debugging purposes
            _install_requires = (line.split("#")[0].strip() for line in fp)
            return list(filter(None, _install_requires))
    except (IOError, IndexError):
        raise RuntimeError(f"{path} is broken")


setup_py = Path(__file__)
cwd = setup_py.parent
requirements = cwd / "requirements"
requirements_prod = requirements / "prod.txt"
readme = cwd / "README.md"
package_name = "chat_test"
src = "src"


setup(
    install_requires=read_requirements(requirements_prod),
    python_requires=">=3.8.0",
    # setup_requires=["setuptools_scm"],
    # use_scm_version={
    #     "version_scheme": "post-release",
    #     "local_scheme": "no-local-version",
    #     "write_to": f"{src}/{package_name}/_version.py",
    #     "write_to_template": '_version = "{version}"\n',
    #     "relative_to": str(setup_py),
    # },
    include_package_data=True,
    package_data={
        "": [],
    },
    packages=find_packages(where=src),
    package_dir={"": src},
    name=package_name,
    long_description=readme.read_text(),
    long_description_content_type="text/markdown",
)
