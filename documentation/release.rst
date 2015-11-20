Release
=======

Steps to make a release:

1. Update version number in setup.py
2. Build with ``python setup.py sdist``
3. Upload to PyPi with ``twine upload dist/humblewx-x.y.z.tar.gz``
4. Tag ``git tag x.y.z``
