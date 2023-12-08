const fs = require('fs');
const path = require('path');

const TEST_DIR = __dirname;
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`);

const {
  TOP_LEFT_MENU_BUTTON,
  MENU_BUTTON_WEATHER_TIPS,
  TOP_LEFT_BACK_BUTTON,
  MENU_BUTTON_WHATSAPP_STICKERS,
  LEFT_DRAWER,
  MENU_BUTTON_9_DAY_FORECAST,
} = require('./utils/XPATHS');
const { KEYCODE_PAD_DOWN } = require('./utils/unicodeKey');

const opts = {
  path: '/',
  port: 4723,
  capabilities: {
    platformName: 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:app': '/workspace/appium-playlist/appium-android-12-tryout/apk_pool/observatory.apk',
    'appium:fullReset': true,
  },
  waitforTimeout: 15000,
};

const greetings = require('./utils/greetings');

async function main() {
  var driver, screenshot_raw;
  try {
    driver = await greetings(opts);
    await driver.pause(1000);

    console.log('start click menu button');
    element = await driver.$(TOP_LEFT_MENU_BUTTON);
    await element.click();

    element = await driver.$(LEFT_DRAWER);
    for (i = 0; i < 14; i++) {
      await driver.pressKeyCode(parseInt(KEYCODE_PAD_DOWN));
    }

    element = await driver.$(MENU_BUTTON_9_DAY_FORECAST);
    await element.click();

    await driver.pause(1 * 500);
    screenshot_raw = await driver.takeScreenshot();
    fs.writeFileSync(`${SCREENCAPTURE_DIR}/9_day_forecast_enter.png`, screenshot_raw, { encoding: 'base64' });
  } catch (error) {
    tmp_xml = await driver.getPageSource();
    fs.writeFileSync('./troubleshoot.xml', tmp_xml, { encoding: 'utf-8' });

    screenshot_raw = await driver.takeScreenshot();
    fs.writeFileSync(`./troubleshoot.png`, screenshot_raw, { encoding: 'base64' });

    throw error;
  } finally {
    console.log('done');
  }
}

main();
