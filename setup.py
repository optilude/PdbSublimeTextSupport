from setuptools import setup, find_packages

setup(name = 'PdbSublimeTextSupport',
      version = '0.2',
      description = 'Display source code in Sublime Text 2 while debugging with pdb.',
      keywords = 'sublimetext pdb',
      author = 'Martin Aspeli',
      author_email = 'optilude@gmail.com',
      url = 'http://pypi.python.org/pypi/PdbSublimeTextSupport',
      license = 'GPL',
      py_modules = ['PdbSublimeTextSupport'],
      include_package_data = False,
      platforms = 'Mac OS X',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: MacOS X',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Topic :: Software Development :: Debuggers',
          'Topic :: Text Editors',
      ],
      long_description = """\
          This module is used to hook up``pdb``, the python debugger, with
          Sublime Text 2, enabling it to display the debugged source code during
          a``pdb``session.

          After downloading and unpacking the package, you should install the
          helper module using::

              $ python setup.py install

          You can also do this with ``easy_install``:
          
              $ easy_install -U PdbSublimeTextSupport

          Next you need to hook up ``pdb`` with this module by adding the
          following to your ``.pdbrc`` file, which you can create in your home
          directory if it's not there already::

              from PdbSublimeTextSupport import preloop, precmd
              pdb.Pdb.preloop = preloop
              pdb.Pdb.precmd = precmd
          
          Finally, ensure that you have the ``subl`` command line tool has
          been installed as per `these instructions
          <http://www.sublimetext.com/docs/2/osx_command_line.html>`_.

          Afterwards Sublime Text should get started automatically whenever
          you enter a debug session.  The current source line will be
          displayed simultaneously while stepping through the code.

          This module is based on ``PdbTextMateSupport`` by Andi Zeidler
          and others.
      """,
)
