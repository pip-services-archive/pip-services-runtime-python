# Development and Testing Guide <br/> Pip.Services Runtime for Python

This document provides high-level instructions on how to build and test the microservice.

* [Environment Setup](#setup)
* [Installing](#install)
* [Building](#build)
* [Testing](#test)
* [Release](#release)
* [Contributing](#contrib) 

## <a name="setup"></a> Environment Setup

This is a Python 2.7 project and you have to install Python tools. 
You can download them from official Python website: https://www.python.org/downloads/

After node is installed you can check it by running the following command:
```bash
python --version
```

Install **pip** package manager folling the instructions https://pip.pypa.io/en/latest/installing/ 

If you are using Windows, you may need to install Cygwin tools from https://cygwin.com/install.html

To work with GitHub code repository you need to install Git from: https://git-scm.com/downloads

## <a name="install"></a> Installing

After your environment is ready you can check out source code from the Github repository:
```bash
git clone git@github.com:pip-services/pip-services-runtime-python.git
```

Then go to the project folder and install dependent modules:
```bash
pip install -r requirements.txt
```

Register the package in Python to be able to use it in tests and other microservices locally
```bash
pip install -e .
```

## <a name="build"></a> Building

Since Python is a scripting language there is no building required

## <a name="test"></a> Testing

Before you execute tests you need to set configuration options in config.yaml file.
As a starting point you can use example from config.example.yaml:

```bash
copy config/config.example.yaml config/config.yaml
``` 

After that check all configuration options. Specifically, pay attention to connection options
for database and dependent microservices. For more information check [Configuration Guide](Configuration.md) 

Command to run unit tests:
```bash
py.test test -s
```
or
```bash
make test
```

## <a name="release"></a> Release

Formal release process consistents of few steps. 
First of all it is required to tag guthub repository with a version number:

```bash
git tag vx.y.y
git push origin master --tags
```

Then the release can be pushed to the global PiPy repository. 
To be able to make the release contributor must have an account with proper
permissions at npm site.

```bash
pip setup.py register
```

Place in your user home folder file **.pypirc** with PiPy user credentials
```text
[server-login]
username:<username>
password:<password>
```

Now publish the Python package
```bash
pip setup.py sdist register upload
```

Microservice releases additionally require generation and publishing 
binary packages at http://downloads.pipservices.org


## <a name="contrib"></a> Contributing

Developers interested in contributing should read the following instructions:

- [How to Contribute](http://www.pipservices.org/contribute/)
- [Guidelines](http://www.pipservices.org/contribute/guidelines)
- [Styleguide](http://www.pipservices.org/contribute/styleguide)
- [ChangeLog](../CHANGELOG.md)

> Please do **not** ask general questions in an issue. Issues are only to report bugs, request
  enhancements, or request new features. For general questions and discussions, use the
  [Contributors Forum](http://www.pipservices.org/forums/forum/contributors/).

It is important to note that for each release, the [ChangeLog](../CHANGELOG.md) is a resource that will
itemize all:

- Bug Fixes
- New Features
- Breaking Changes
