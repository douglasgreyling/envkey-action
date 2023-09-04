import os, envkey

secrets = envkey.fetch_env(os.getenv('ENVKEY'), cache_enabled=False)

bash_lines = ['#!/usr/bin/env bash', '']
env_lines = []
for k, v in secrets.items():
  bash_lines.append(f"""echo '{k}={v}' >> $GITHUB_ENV""")
  env_lines.append(f"""{k}='{v}'""")

with open('/tmp/secrets.sh', 'w') as file:
  file.write('\n'.join(bash_lines))

if os.getenv('DOTENV') == 'true':
  with open('.env', 'w') as file:
    file.write('\n'.join(env_lines))