import os, envkey

secrets = envkey.fetch_env(os.getenv('ENVKEY'), cache_enabled=False)

bash_lines = ['#!/usr/bin/env bash', '']
for k, v in secrets.items():
  bash_lines.append(f"""echo '{k}={v}' >> $GITHUB_ENV""")

with open('/tmp/secrets.sh', 'w') as file:
  file.write('\n'.join(bash_lines))
