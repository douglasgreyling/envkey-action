import os, envkey

secrets = envkey.fetch_env(os.getenv('ENVKEY'), cache_enabled=False)

bash_lines = ['#!/usr/bin/bash', '']
mask_lines = ['#!/usr/bin/bash', '']
env_lines = []
for k, v in secrets.items():
  v = v.replace("'", """'"'"'""") # escape single quote
  bash_lines.append(f"""echo '{k}={v}' >> $GITHUB_ENV""")
  env_lines.append(f"""{k}='{v}'""")

   # so the value is masked
  if '\n' in v:
    for l in v.splitlines():
      mask_lines.append(f"""echo '::add-mask::{l}'""")
  else:
      mask_lines.append(f"""echo '::add-mask::{v}'""")
  

# replace re-used env vars
for k, val in secrets.items():
  key = '${' + k + '}'
  for i, _ in enumerate(bash_lines):
    bash_lines[i] = bash_lines[i].replace(key, val)
  for i, _ in enumerate(env_lines):
    env_lines[i] = env_lines[i].replace(key, val)

with open('/tmp/secrets.sh', 'w') as file:
  file.write('\n'.join(bash_lines))

with open('/tmp/masks.sh', 'w') as file:
  file.write('\n'.join(mask_lines))

if os.getenv('DOTENV') == 'true':
  with open('.env', 'w') as file:
    file.write('\n'.join(env_lines))
