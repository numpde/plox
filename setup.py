import setuptools

with open("README.md", 'r') as fd:
    long_description = fd.read()

# python setup.py sdist bdist_wheel
# twine upload dist/* && rm -rf build dist *.egg-info

setuptools.setup(
    name="plox",
    version="0.0.3",
    author="RA",
    author_email="numpde@null.net",
    keywords="development matplotlib figure context",
    description="Context manager for matplotlib figures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/numpde/plox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['matplotlib'],

    test_suite="nose.collector",
    tests_require=["nose"],
)
