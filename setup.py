from setuptools import setup

setup(
    name = "helloWorldApp",
    version = "1.0",
    author = "Fritz Geib",
    author_email = "github-f@standland.org",
    description = "A hello world app",
    license = "MIT",
    url = "https://github.com/Fr1tzBot/helloWorldApp",
    long_description=open('README.md').read(),
    entry_points = {
        'console_scripts' : ['helloWorldApp = helloWorldApp.helloWorldApp:main']
    },
    data_files = [
        ('share/applications/', ['helloWorldApp.desktop'])
    ]
)