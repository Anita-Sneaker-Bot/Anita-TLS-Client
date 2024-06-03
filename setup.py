from setuptools import setup, find_packages

setup(
    name="anita_tls_client",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
     package_data={
        'anita_tls_client': ['*.dll', "*.so"],  # Include the .dll file
    },
    install_requires=[
        'typing_extensions'
    ],
    author="",
    author_email="",
    description="A modified TLS client.",
    url="https://github.com/grinchify/Modified-TLS-Client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
