from setuptools import setup

def readme():
  with open('README.md') as f:
    return f.read()

setup(
    name='comment_parser',
    version='1.0.3',
    description='Parse comments from various source files.',
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Documentation',
      'License :: OSI Approved :: MIT License'
    ],
    url='http://github.com/jeanralphaviles/comment_parser',
    author='Jean-Ralph Aviles',
    author_email='jeanralph.aviles+pypi@gmail.com',
    license='MIT',
    packages=['comment_parser', 'comment_parser.parsers'],
    install_requires=['python-magic>=0.4'],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False)
