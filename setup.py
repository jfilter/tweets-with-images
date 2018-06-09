from setuptools import setup

setup(name='tweets-with-images',
      version='0.1.0',
      description='Get All Tweets with Images from a User',
      url='https://github.com/jfilter/tweets-with-images',
      author='Johannes Filter',
      author_email='hi@jfilter.de',
      license='MIT',
      packages=['tweets_with_images'],
      install_requires=[
          'twint==1.1.3.1', 'lxml', 'requests'
      ],
      zip_safe=False)
