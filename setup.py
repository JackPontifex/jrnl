from setuptools import setup
from jrnl.version import DESCRIPTION, PYPINAME, VERSION

setup(
    name=PYPINAME,
    version=VERSION,
    description=DESCRIPTION,
    url='https://github.com/mwiens91/jrnl',
    author='Matt Wiens',
    author_email='mwiens91@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
    ],
    data_files=[('/usr/local/man/man1', ['man/jrnl.1']),],
    packages=['jrnl'],
    entry_points={
        'console_scripts': ['jrnl = jrnl.jrnl:main'],
    },
    install_requires=[
        'python-dateutil',
        'PyYAML',
    ],
)
