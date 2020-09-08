from distutils.core import setup

setup(
    name='emailer',
    version='0.2',
    description='Simple emailer',
    author='Ben Thayer',
    author_email='ben@benthayer.com',
    url='https://github.com/benthayer/emailer',
    py_modules=['emailer'],
    entry_points={
        "console_scripts": [
            "send-html=emailer:send_html"
        ]
    }
)
