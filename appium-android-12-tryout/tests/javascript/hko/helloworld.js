const fs = require('fs');
const path = require('path');
const wdio = require('webdriverio');

const TEST_DIR = __dirname;
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`);

const opts = {
  path: '/',
  port: 4723,
  capabilities: {
    platformName: 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:app': '/workspace/appium-playlist/appium-android-12-tryout/apk_pool/ApiDemos-debug.apk',
    'appium:fullReset': true,
  },
};

const greetings = require('./utils/greetings');

async function main() {
  var driver, screenshot_raw;
  try {
    const driver = await wdio.remote(opts);
    await driver.pause(1000);

    screenshot_raw = await driver.takeScreenshot();
    fs.writeFileSync(`${SCREENCAPTURE_DIR}/helloworld_done.png`, screenshot_raw, { encoding: 'base64' });
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
