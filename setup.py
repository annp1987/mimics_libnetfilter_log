from distutils.core import setup

setup(name='mimisc_libnetfilter_log',
      version='1.0',
      description='Python libnetfilter_log ctypes',
      author='Nguyen Phuong An',
      author_email='annp.cs51@gmail.com',
      url='https://github.com/annp1987/mimisc_libnetfilter_log',
      packages=['lib', 'lib.netlink', 'lib.log']
)
