from setuptools import setup, find_packages
import os

current_folder = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_folder, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup( 
    name='Example Project',
    version='0.2.1',
    description='An example Python project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Hakonmh/example-project',
    author='Håkon Magne Holmen',
    author_email='haakonholmen@outlook.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='sample development',
    packages=find_packages(exclude='tests'),
    python_requires='>=3.6',
    project_urls={
        'Funding': 'https://donate.pypi.org',
        'Documentation': r'https://an-example-project.readthedocs.io/en/latest/index.html'
    },
)
