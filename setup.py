from setuptools import setup, find_packages

setup(
    name='datasciencetoolbox',
    version='0.1.0-dev',
    url='https://github.com/DTU-DABAI/datasciencetoolbox',
    author='Philip J. H. Jørgensen',
    author_email='philipjhj@gmail.com',
    description='Toolbox with high-level functions for data science tasks',
    packages=find_packages(),
    install_requires=[
        'numpy >= 1.12.1',
        'matplotlib >= 2.2.2',
        'scikit-learn >= 0.19.1',
        'pandas >= 0.23.0',
        'requests >= 2.18.4'
    ],
)
