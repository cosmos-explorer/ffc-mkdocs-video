from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="ffc-mkdocs-video",
    version="1.0.1",
    author="Cosmos Explorer",
    author_email="lian.yang@gmail.com",
    url="https://github.com/cosmos-explorer/ffc-mkdocs-video",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "mkdocs>=1.1.0,<2"
    ],
    include_package_data=True,
    python_requires='>=3.6',
    entry_points={
        'mkdocs.plugins': [
            'ffc-mkdocs-video = ffc_mkdocs_video.plugin:Plugin',
        ]
    }

)
