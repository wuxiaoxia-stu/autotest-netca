from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from .config import read_config
import poplib

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg, indent=0):
    content = None
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            content = print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
    return content

def getEmailContent():
    email = read_config('getemail', 'email')
    password = read_config('getemail', 'password')
    pop3_server = read_config('getemail', 'pop3_server')
    server = poplib.POP3_SSL(pop3_server, 995)
    server.user(email)
    server.pass_(password)
    resp, mails, octets = server.list()
    index = len(mails)
    resp, lines, octets = server.retr(index)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    content = print_info(msg)
    server.quit()
    return content
