const fs = require('fs');
const path = require('path');

const TEST_DIR = __dirname;
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`);
const {
  TOP_LEFT_MENU_BUTTON,
  MENU_BUTTON_WEATHER_TIPS,
  TOP_LEFT_BACK_BUTTON,
  REGIONAL_WEATHER_BUTTON,
  ADD_LOCATION_BUTTON,
  SEARCH_LOCATION_INPUT_BOX,
  FIRST_ITEM_IN_THE_LIST,
  ADD_BUTTON,
  LEFT_DRAWER_HOME_BUTTON,
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

    element = await driver.$(REGIONAL_WEATHER_BUTTON);
    await element.click();

    element = await driver.$(ADD_LOCATION_BUTTON);
    await element.click();

    // click search
    element = await driver.$(SEARCH_LOCATION_INPUT_BOX);
    await element.keys('Kwun Tong');
    await driver.pause(1 * 1000);
    screenshot_raw = await driver.takeScreenshot();
    fs.writeFileSync(`${SCREENCAPTURE_DIR}/type_search_kwun_tong.png`, screenshot_raw, { encoding: 'base64' });

    element = await driver.$(ADD_BUTTON);
    await element.click();

    await driver.pause(1000);

    element = await driver.$(TOP_LEFT_MENU_BUTTON);
    await element.click();

    element = await driver.$(LEFT_DRAWER_HOME_BUTTON);
    await element.click();

    screenshot_raw = await driver.takeScreenshot();
    fs.writeFileSync(`${SCREENCAPTURE_DIR}/regional_weather_kwun_tong_done.png`, screenshot_raw, {
      encoding: 'base64',
    });
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
