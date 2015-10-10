from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='insights.py',
      version='1.0',
      description='A Python package for reading, storing, & analyzing data from Public Data APIs.'
                  'It provides modules for reading & parsing data from URL, storing data using a wrapper for SQLite, and performing some statistics.',
      long_description = readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='insights, analysis, statistics',
      url='http://github.com/OmarElGabry/Insights.py',
      author='Omar El Gabry',
      author_email='omar.elgabry.93@gmail.com',
      license='MIT',
      packages=['insights.py'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False)

