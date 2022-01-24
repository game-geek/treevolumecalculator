from setuptools import setup

APP = ['main2.py']
lol = {
    "argv_emulation": True
}

setup(
    app=APP,
    options={'py2app': lol},
    setup_requires = ['py2app']
    
      )


#https://youtu.be/IIAlkQEw8Gc

