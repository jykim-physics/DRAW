from setuptools import setup, find_packages
from pkg_resources import resource_filename
from pathlib import Path


with (Path(__file__).parent / 'readme.md').open() as readme_file:
    readme = readme_file.read()

setup(
    name='DRAW',
    packages=find_packages(),
    url="",
    author='Jaeyoung Kim',
    author_email='jaeyoung97@yonsei.ac.kr',
    description='''
Tools.
''',
    install_requires=[
        'numpy<1.23',  # Remove this when numba becomes compatible with numpy>=1.23
        'scipy',
        'numba',
        'matplotlib', 
        'jupyterlab', 
        'uncertainties',
        'iminuit',
        'gvar',
        'numdifftools',
    ],
    extras_require={
        "examples":  [],
    },
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: jykim License "
    ],
    license='jykim',
)
