import os
from setuptools import setup, find_packages
from typing import List


def readme() -> str:
    """print long description"""
    with open('README.md') as f:
        return f.read()


def get_requirements(req: str) -> List[str]:
    """Load list of dependencies."""
    install_requires = []
    with open(req) as fp:
        for line in fp:
            stripped_line = line.partition('#')[0].strip()
            if stripped_line:
                install_requires.append(stripped_line)

    return install_requires


long_description = (
    "This is a mkdocs plugin that introduces support for markmap."
    "Please follow the instruction in reame to enable this plugin."
)


setup(
    name='mkdocs-markmap',
    version='0.1',
    description='MkDocs plugin and extension to creates mindmaps from markdown using markmap',
    long_description=long_description,
    keywords='mkdocs python markdown mermaid',
    url='https://github.com/neac0der/mkdocs-markmap',
    author='neatc0der',
    author_email='',
    license='MIT',
    python_requires='>=3.6',
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'markmap = mkdocs_markmap.plugin:MarkmapPlugin',
        ],
        'markdown.extensions': [
            'markmap = mkdocs_markmap.extension:MarkmapExtension',
        ]
    },
)
