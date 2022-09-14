from setuptools import setup, find_packages

setup(name="django-redis",
      description="django-redis",
      long_description="django-redis",
      packages=find_packages(exclude=["*tests*"]),
      package_data={'': ['*.yaml']},
      version="1.0.0",
      install_requires=[
          'django==4.1.1',
          'djangorestframework==3.13.1',
          'redis==4.3.4',
      ],
      extras_require={
          'dev': [
              'pycodestyle==2.9.1',
              'flake8==5.0.4',
          ],
      }
      )
