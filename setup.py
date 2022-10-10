from setuptools import setup, find_packages


setup(
    name                          = 'DSToolkit',
    version                       = '0.0.2',
    description                   = 'Data Science practical methods collection',
    author                        = 'Andrea Ferrante',
    author_email                  = 'andreaferrante1986@gmail.com',
    classifiers                   = ['Development Status :: 3 - Alpha',
                                     'Intended Audience :: Developers',
                                     'Topic :: Software Development :: Build Tools',
                                     'License :: OSI Approved :: MIT License',
                                     'Programming Language :: Python :: 3.6',
                                     'Programming Language :: Python :: 3.7',
                                     'Programming Language :: Python :: 3.8',
                                     'Programming Language :: Python :: 3.9',
                                     'Programming Language :: Python :: 3 :: Only'],
    keywords                      = 'datetime, setuptools',
    packages                      = find_packages(where='src'),
    python_requires               = '>=3.6, <4',
    install_requires              = ['pandas', 'numpy'],
    py_modules                    = ['pyutils']
    
)
