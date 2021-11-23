import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='returns_json_deco',
    version='0.0.1',
    author='Momspresso',
    author_email='rakesh.khulbe@mycity4kids.com',
    description='response formatter decorator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    project_urls = {
        "Bug Tracker": ""
    },
    license='MIT',
    packages=['returns_json_deco'],
    install_requires=['Flask==1.1.1'],
)
