from setuptools import setup, find_packages

setup(
    name='comex',
    version='0.1.4',
    description='Generate combined multi-code view graphs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IBM/tree-sitter-codeviews',
    license='Apache-2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'networkx==2.6.3',
        'tree-sitter==0.20.1',
        'deepdiff==5.8.1',
        'pydot==1.4.1',
        'typer==0.4.1',
        'loguru==0.6.0',
        'setuptools>=69.0; python_version>="3.12"'
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'comex=comex.cli:app',
        ],
    },
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'tqdm',
            'pqdm',
            'loguru',
            'GitPython',
            'pandas',
        ],
    },
)