#!/bin/sh
# https://www.google.com/search?ei=NeS_X-iPCO6Xr7wPu6GFyAM&q=mac+npm+install+appium&oq=mac+npm+install+appium&gs_lcp=CgZwc3ktYWIQAzIJCAAQyQMQFhAeOgQIABBHOggIABDJAxCRAjoFCAAQkQI6CgguEMcBEKMCEEM6BAgAEEM6CggAELEDEIMBEEM6AggAOggILhDHARCjAjoICC4QsQMQgwE6CAgAELEDEIMBOgUIABCxAzoNCAAQsQMQgwEQyQMQQzoHCAAQsQMQQzoHCC4QsQMQQzoQCC4QsQMQgwEQxwEQowIQQzoECC4QQzoFCAAQyQM6BggAEBYQHjoICAAQCBANEB5QxhRYqDlg8jpoAXAEeACAAYcBiAH6C5IBBDIyLjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwio_q6_3KDtAhXuy4sBHbtQATkQ4dUDCA0&uact=5

set -ex

echo '1'
adb devices -l


echo '2'
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo '3'
brew install node

echo '4'
npm i -g npm@latest
npm install -g appium
npm install -g appium-doctor

echo '5'
npm install wd

echo '6'
appium --port 4724 --address 10.10.1.40