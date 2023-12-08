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
  },
};

// app: "/root/apk_pool/ApiDemos-debug.apk",
// platformVersion: "12.0",
// fullReset: true
// deviceName: "nexus_5_7.1.1",
// appPackage: "io.appium.android.apis",
// appActivity: ".view.TextFields",
// automationName: "UiAutomator2"

async function main() {
  const driver = await wdio.remote(opts);

  try {
    const batteryItem = await driver.$('//*[@text="App"]');
    await batteryItem.click();

    // let screenshot = await client.takeScreenshot();
    // fs.writeFileSync(`${SCREENCAPTURE_DIR}/capture_using_javascript.png`, screenshot, { encoding: 'base64' })
  } finally {
    await driver.pause(1000);
    await driver.deleteSession();
  }
}

main();
