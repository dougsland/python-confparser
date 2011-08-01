from distutils.core import setup

setup(name='python-confparser', version='1.0.1',
      description='Parser for *nix config files',
      author='Douglas Schilling Landgraf',
      author_email='dougsland@redhat.com',
      url='https://github.com/dougsland/python-confparser/wiki',
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: LGPLv2+',
          'Programming Language :: Python',
          ],
      license= 'LGPLv2+' ,
      py_modules = ['confparser']   
           
)
