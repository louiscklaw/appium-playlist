const fs = require('fs');
const path = require('path');

const TEST_DIR = __dirname;
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`);
const {
  TOP_LEFT_MENU_BUTTON,
  MENU_BUTTON_WEATHER_TIPS,
  TOP_LEFT_BACK_BUTTON,
  MENU_BUTTON_MY_WEATHER_OBSERVATION,
} = require('./utils/XPATHS');

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

    element = await driver.$(MENU_BUTTON_MY_WEATHER_OBSERVATION);
    await element.click();

    element = await driver.$('//*[@text="Agree"]');
    await element.click();

    await driver.pause(1 * 1000);

    screenshot_raw = await driver.takeScreenshot();
    fs.writeFileSync(`${SCREENCAPTURE_DIR}/my_weather_observation_done.png`, screenshot_raw, { encoding: 'base64' });
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
