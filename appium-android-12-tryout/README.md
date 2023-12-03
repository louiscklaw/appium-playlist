# README.md

```bash
# download apk from https://app.zhipin.com/
$ wget <boss_11.220_c0.apk>

# down container if running
$ scripts/down_docker.sh

# re-create container
$ scripts/start_docker.sh

# expecting appium docker were up
$ pipenv run python3 ./zhipin_helloworld.py

```

