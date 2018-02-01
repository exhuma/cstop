from setuptools import setup, find_packages
VERSION = open('cstop/version.txt').read()
setup(
    name="cstop",
    version=VERSION.strip(),
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    include_package_data=True,
    author="Michel Albert",
    author_email="michel@albert.lu",
    description="Simple CLI stopwatch",
    entry_points={
        'console_scripts': [
            'cstop=cstop.core:main'
        ]
    },
    license="BSD",
    url="https://exhuma.github.com/cstop",
)
