from setuptools import setup, find_packages


setup(
    name="mochart",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "docutils>=0.3",
        "beautifulsoup4==4.6.3",
        "pytest==3.9.3",
        "pytz==2018.7",
        "requests==2.20.0",
    ],

    package_data={
        '': ['*.txt', '*.rst'],
    },

    author="Hyunchel Kim",
    author_email="hyunchel.inbox@gmail.com",
    description="Music online charts.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="music online chart ranking melon mnet naver gaon oricon",
    url="https://hyunchel.github.io/mochart/",
    project_urls={
        "Bug Tracker": "https://github.com/hyunchel/mochart/issues",
        "Documentation": "https://github.com/hyunchel/mochart/README.md",
        "Source Code": "https://github.com/hyunchel/mochart",
    }
)
