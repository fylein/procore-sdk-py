import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='procore',
    version='0.1.0',
    author='Shwetabh Kumar',
    author_email='shwetabh.kumar@fyle.in',
    description='Python SDK for accessing Procore APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    keywords=['procore', 'fyle', 'api', 'python', 'sdk'],
    url='https://github.com/fylein/procore-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
