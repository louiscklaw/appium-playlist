const fs = require('fs');
const path = require('path');
const greetings = require('./utils/greetings');
const { TOP_LEFT_MENU_BUTTON } = require('./utils/XPATHS');

const TEST_DIR = __dirname;
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`);

const opts = {
  path: '/',
  port: 4723,
  capabilities: {
    platformName: 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:app': '/workspace/appium-playlist/appium-android-12-tryout/apk_pool/observatory.apk',
  },
};

async function main() {
  var driver, screenshot_raw;
  try {
    driver = await greetings(opts);

    console.log('start click menu button');
    element = await driver.$(TOP_LEFT_MENU_BUTTON);
    await element.click();
  } finally {
    // screenshot_raw = await driver.takeScreenshot();
    // fs.writeFileSync(`${SCREENCAPTURE_DIR}/capture_using_javascript.png`, screenshot, { encoding: 'base64' })
    // await driver.pause(999 * 1000);
    // await driver.deleteSession();
  }
}

main();
