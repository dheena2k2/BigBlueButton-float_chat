from distutils.core import setup
import toml


def get_pipfile_packages():
    """
    This method returns the packages from pipfile
    :return: List of packages with their version
    """
    try:
        with open('Pipfile', 'r') as pipfile:
            content = pipfile.read()
        pipfile_toml = toml.loads(content)
    except FileNotFoundError:
        return []

    try:
        required_packages = pipfile_toml['packages'].items()
    except KeyError:
        return []

    packages = list()
    for pkg, ver in required_packages:
        if ver == '*':
            packages.append(pkg)
        else:
            packages.append('%s%s' % (pkg, ver))

    return packages


if __name__ == '__main__':
    pipfile_packages = get_pipfile_packages()
    setup(
        name='float_chat',
        version='1.0',
        install_requires=pipfile_packages,
        url='',
        license='MIT',
        author='Dheenadhayalan R',
        author_email='dheena2k2@gmail.com',
        description='Float chat application for BigBlueButton'
    )
