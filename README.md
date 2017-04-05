# botoenv

Manage AWS environment variables using botocore

## Installation

    pip install botoenv


## Usage

By default, `botoenv` prints out environment variable assignments for the current AWS credentials.

The expected usage is to **eval** its output:

    eval $(botoenv)


## Profiles

AWS supports role assumption via profiles in your `~/.aws` configuration.

For example, in `~/.aws/config`:

    [default]
    region = us-east-1

    [profile development]
    region = us-east-1
    source_profile = default

    [profile production]
    region = us-west-2
    source_profile = default

Then, in `~/.aws/credentials`:

    [default]
    aws_access_key_id = <redacted>
    aws_secret_access_key = <redacted>

    [development]
    role_arn = arn:aws:iam::account_id:role/development

    [production]
    role_arn = arn:aws:iam::account_id:role/production

If you have both the `source_profile` and `role_arn` configured, you can use `botoenv`
to automtically invoke the STS Assume Role function:

    eval $(botoenv --profile development)


## Template Customization

The template output can be configured. For example:

    eval $(botoenv --template $'unset {key}\n')
