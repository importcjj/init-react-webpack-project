from setuptools import setup, find_packages

requires = []

setup(
    name="proton",
    version="0.1",
    description="react develop helper",
    long_description="help you to initial a react webpack project",
    url="https://github.com/importcjj/init-react-webpack-project",
    author="jiaju.chen",
    scripts=['proton/proton'],
    author_email="jiaju.chen@ele.me",
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    packages=find_packages()
)
