from distutils.core import setup

setup(
    name='lightcrafter',
    author='Martin Privat',
    version='0.1.0',
    packages=['lightcrafter','lightcrafter.tests'],
    license='MIT',
    description='configure Lightcrafter DMD using the USB HID protocol',
    long_description=open('README.md').read(),
    install_requires=[
        'hidapi',
        'numpy'
    ]
)
