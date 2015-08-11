from setuptools import setup


setup(
    name='flix',
    version='0.1.0',
    py_modules=['cli'],
    install_requires=[
        'Click', 'BeautifulSoup4', 'lxml'
        ],
        entry_points='''
        [console_scripts]
        flix=cli:main
        '''
)
