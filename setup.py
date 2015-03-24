from setuptools import setup

setup(
    name='jenkins-jobs-artifactory',
    version='0.1',
    description='Jenkins Job Builder Artifactory wrapper',
    url='https://github.com/xiii/jenkins-jobs-artifactory',
    author='Efstathios Xagoraris',
    author_email='efstathios.xagoraris@itv.com',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.wrappers': [
            'artifactory = jenkins_jobs_artifactory.artifactory:artifactory_wrapper']
    },
    packages=['jenkins_jobs_artifactory'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
