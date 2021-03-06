from setuptools import setup, find_packages

setup(
    name='socialstalker',
    author='ndouba',
    version='1.0',
    author_email='ndouba@gmail.com',
    description='Social media stalker transforms',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf' ] # list of resources
    },
    install_requires=[
        'canari'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)