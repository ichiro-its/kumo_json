from setuptools import setup

package_name = 'kumo_json'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools'
    ],
    zip_safe=True,
    maintainer='Alfi Maulana',
    maintainer_email='alfi.maulana.f@gmail.com',
    description='ROS 2 interface to JSON serialization for Kumo package',
    license='MIT License',
    tests_require=['pytest'],
)