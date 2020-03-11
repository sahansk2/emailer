from distutils.core import setup

setup(
    name='emailer',
    version='0.1',
    description='Simple emailer',
    author='Ben Thayer',
    author_email='ben@benthayer.com',
    url='https://github.com/benthayer/emailer',
    modules=['emailer'],
    entry_points={
        "console_scripts": [
            "send-html=emailer:send_html"
        ]
    }
)
