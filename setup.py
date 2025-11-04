from setuptools import find_packages, setup

setup(
    name='tmrl',
    version="69",
    description='Network-based framework for real-time robot learning',
    long_description_content_type='text/markdown',
    keywords='reinforcement learning, robot learning, trackmania, self driving, roborace',
    license='MIT',
    install_requires=install_req,
    extras_require={},
    scripts=[],
    packages=find_packages(exclude=("tests", )))
