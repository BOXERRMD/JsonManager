import setuptools

with open("README.md", "rt") as file:
    long_description = file.read()

setuptools.setup(
    name='json-manager2.0',
    version='0.0.1',
    author='BOXERRMD',
    author_email='vagabonwalybi@gmail.com',
    description='An json manager',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BOXERRMD/JsonManager',
    project_urls={
        'Documentation': 'https://github.com/BOXERRMD/JsonManager/wiki',
        'GitHub': 'https://github.com/BOXERRMD/JsonManager',
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows :: Windows 11"
    ],
    install_requires=[
        'json'
    ],

    packages=['json_manager'],
    python_requires=">=3.7",
    include_package_data=True,
)