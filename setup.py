from distutils.core import setup

setup(name='python-rdnbrd',
      version="1.3",
      description = "Redistribute Neighbor",
      author='Dinesh G Dutt',
      author_email='ddutt@cumulusnetworks.com',
      url='cumulusnetworks.com',
      scripts=['rdnbrd'],
      data_files=[
          ('/usr/sbin/', ['rdnbrd']),
          ('/usr/share/rdnbrd/', ['contrib/netplug', 'contrib/dhclient-hooks-example']),
          ('/lib/systemd/system', ['lib/systemd/system/rdnbrd.service']),
          ('/etc/', ['etc/rdnbrd.conf']),
          ('/etc/logrotate.d/', ['logrotate.d/rdnbrd']),
          ('/etc/rsyslog.d/', ['rsyslog.d/35-rdnbrd.conf'])
      ]
)
