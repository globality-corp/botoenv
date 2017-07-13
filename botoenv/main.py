"""
Capture and export AWS credentials.

"""
from sys import stdout

from argparse import ArgumentParser
from botocore.session import Session


DEFAULT_TEMPLATE = "export {key}={value}\n"


def parse_args():
    session = Session()
    parser = ArgumentParser()
    parser.add_argument("-p", "--profile", choices=session.available_profiles)
    parser.add_argument("-t", "--template", default=DEFAULT_TEMPLATE)
    return parser.parse_args()


def build_credentials_map(session, credentials):
    if credentials.token is None:
        return dict(
            AWS_DEFAULT_REGION=session.get_config_variable("region"),
            AWS_ACCESS_KEY_ID=credentials.access_key,
            AWS_SECRET_ACCESS_KEY=credentials.secret_key,
        )
    else:
        return dict(
            AWS_DEFAULT_REGION=session.get_config_variable("region"),
            AWS_ACCESS_KEY_ID=credentials.access_key,
            AWS_SECRET_ACCESS_KEY=credentials.secret_key,
            AWS_SESSION_TOKEN=credentials.token,
        )


def render_template(template, credential_map):
    for key, value in credential_map.items():
        stdout.write(template.format(key=key, value=value))
    stdout.flush()


def main():
    args = parse_args()
    session = Session(profile=args.profile)
    credentials = session.get_credentials()
    credentials_map = build_credentials_map(session, credentials)
    render_template(args.template, credentials_map)
    return 0
