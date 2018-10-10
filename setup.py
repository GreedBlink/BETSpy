from setuptools import setup


setup(name='BETSpy',
      version='0.1',
      description='It provides access to and information about the most important Brazilian economic time series - from the Getulio Vargas Foundation <http://portal.fgv.br/en>, the Central Bank of Brazil <http://www.bcb.gov.br> and the Brazilian Institute of Geography and Statistics <http://www.ibge.gov.br>. It also presents tools for managing, analysing (e.g. generating dynamic reports with a complete analysis of a series) and exporting these time series.',
      url='http://github.com/GreedBlink/BETspy',
      author='Jonatha Costa, Talitha Speranza, Pedro Gruilherme',
      author_email='jonatha.costa@fgv.br',
      license='GPL-3',
      packages=['BETSpy'],
      install_requires=[
          'pandas',
          'requests',
          'datetime',
          'json',
          'time',
          'mysql.connector',
          're'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
