import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="layeutils",
    version="0.1.4",
    author="LayeWang",
    author_email="laye0619@gmail.com",
    description="Private Utils",
    long_description="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)