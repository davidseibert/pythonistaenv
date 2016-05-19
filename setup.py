from setuptools import setup, find_packages

setup(name='pythonistaenv',
      version='0.1',
      description='Trying to short circuit package issues on Pythonista iOS',
      url='http://github.com/davidseibert/pythonistaenv',
      author='David Seibert',
      author_email='dave@davidseibert.me',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'jinja2',
      ],
      zip_safe=False,
      )
