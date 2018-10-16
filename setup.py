import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="saber",
    version="0.0.1",
    author="John Giorgi",
    author_email="johnmgiorgi@gmail.com",
    license="MIT",
    description="Saber: Sequence Annotator for Biomedical Entities and Relations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BaderLab/saber",
    python_requires='>=3.6',
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6"
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'scikit-learn>=0.19.1',
        'tensorflow>=1.9.0',
        'Flask>=1.0.2',
        'waitress>=1.1.0',
        'keras>=2.2.0',
        'PTable>=0.9.2',
        'spacy>=2.0.11, <=2.0.15',
        'gensim>=3.4.0',
        'nltk',
    ],
    include_package_data=True,
    # allows us to install + run tests with `python setup.py test`
    # https://docs.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
