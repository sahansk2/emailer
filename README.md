# emailer
## A utility to send HTML emails.

---

This is emailer, a utility written in Python 3 to send HTML emails.

## Installation Instructions

To install, first, clone the repository: 
```
git clone https://github.com/benthayer/emailer.git
```

Then, `cd` into the repository folder, and install with pip:
```
pip install .
# If you have both pip (Python 2) and pip3 (Python 3), run:
# pip3 install .
```

## Usage
emailer provides the executable `send-html` to send HTML emails.
### Necessary configuration
`send-html` searches environment variables to check for valid email settings:

* `EMAIL_SENDER` - The sender's email address
* `EMAIL_PASSWORD` - The sender's password for the email address
* `SMTP_HOST` - The sender's email provider's SMTP hostname
* `SMTP_PORT` - The sender's email provider's SMTP port

As such, it is recommended to place this information into a plaintext file, and then source it before execution.

`send-instructions.sh`
```
export EMAIL_SENDER="sender@provider.com"
export EMAIL_PASSWORD="password123"
export SMTP_HOST=smtp.provider.com
export SMTP_PORT=587
```

```
source send-instructions.sh
```
### Executing send-html
`send-html` can be called simply like this:
```
send-html recipient@email.org
```

This command must be run in a directory with the necessary files:

```
current_directory
├── email.html # The HTML content of the email.
└── subject.txt # The subject of the email to be sent.
```
