# rivescript-python setup.py

import rivescript
from setuptools import setup

setup(
    name             = 'rivescript',
    version          = rivescript.__version__,
    description      = 'A rivescript bot specializing in password generation',
    long_description = 'A scripting language to make it easy to write responses for a chatterbot.',
    author           = 'Kaza Razat',
    author_email     = 'kaza@ego.network',
    url              = 'https://github.com/aichaos/rivescript-python',
    license          = 'MIT',
    packages         = ['rivescript'],
    keywords         = ['bot', 'chatbot', 'chatterbot', 'ai', 'aiml',
                        'chatscript', 'buddyscript'],
    classifiers      = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    install_requires = [ 'setuptools', 'six' ],
)

# vim:expandtab
