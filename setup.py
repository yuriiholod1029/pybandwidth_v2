from distutils.core import setup


setup(
  name='pybandwidth_v2',
  packages=['pybandwidth_v2'],
  version='0.0.1',
  license='MIT',
  description='Bandwidth API for v2 messaging',
  author='Yurii Holodnyi',
  author_email='holodnyijurii@gmail.com',
  url='https://github.com/yuriiholod1029/pybandwidth_v2',
  download_url='https://github.com/yuriiholod1029/pybandwidth_v2/archive/v_001.tar.gz',
  keywords=['python', 'bandwidth', 'v2', 'api', 'client'],   # Keywords that define your package best
  install_requires=[
      'requests',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
