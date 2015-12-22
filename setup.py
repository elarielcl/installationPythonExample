from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='prueba',
      version='0.1.1',
      description='Test',
      long_description=readme(),
      url='http://www.onlinereyes.com',
      author='Ariel',
      author_email='el.ariel.cl@gmail.com',
      license='MIT',
      packages=['prueba'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False,
      test_suite='prueba.tests',)
