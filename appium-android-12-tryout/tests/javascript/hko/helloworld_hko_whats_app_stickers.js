const fs = require('fs');
const path = require('path');
const greetings = require('./utils/greetings');
const {
  TOP_LEFT_MENU_BUTTON,
  MENU_BUTTON_WEATHER_TIPS,
  TOP_LEFT_BACK_BUTTON,
  MENU_BUTTON_WHATSAPP_STICKERS,
} = require('./utils/XPATHS');

const TEST_DIR = __dirname;
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`);

const opts = {
  path: '/',
  port: 4723,
  capabilities: {
    platformName: 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:app': '/workspace/appium-playlist/appium-android-12-tryout/apk_pool/observatory.apk',
    'appium:fullReset': true,
  },
};

async function main() {
  var driver, screenshot_raw;
  try {
    driver = await greetings(opts);

    console.log('start click menu button');
    element = await driver.$(TOP_LEFT_MENU_BUTTON);
    await element.click();

    element = await driver.$(MENU_BUTTON_WHATSAPP_STICKERS);
    await element.click();

    await driver.pause(1 * 1000);

    screenshot_raw = await driver.takeScreenshot();
    fs.writeFileSync(`${SCREENCAPTURE_DIR}/whatsapp_stickers.png`, screenshot_raw, { encoding: 'base64' });

    console.log('done, back to home');
    element = await driver.$(TOP_LEFT_BACK_BUTTON);
    await element.click();
  } finally {
    // screenshot_raw = await driver.takeScreenshot();
    // fs.writeFileSync(`${SCREENCAPTURE_DIR}/capture_using_javascript.png`, screenshot, { encoding: 'base64' })
    await driver.pause(1 * 1000);
    await driver.deleteSession();
  }
}

main();
