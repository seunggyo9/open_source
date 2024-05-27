from setuptools import find_packages, setup

install_requires = [
    'beautifulsoup4',
    'requests',
    'tqdm',
]

setup(
    name='test',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    author='seunggyo',
    author_email='wxcv47@naver.com',
    description='Naver News Crawler',
)
