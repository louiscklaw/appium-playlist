const fs = require('fs')
const path = require('path')
const wdio = require("webdriverio");

const TEST_DIR=__dirname
const SCREENCAPTURE_DIR=path.resolve(`${TEST_DIR}/screen`)

const opts = {
  path: '/wd/hub',
  port: 4723,
  capabilities: {
    platformName: "Android",
    platformVersion: "9.0",
    app: "/root/apk_pool/ApiDemos-debug.apk",
    // fullReset: true
    // deviceName: "nexus_5_7.1.1",
    // appPackage: "io.appium.android.apis",
    // appActivity: ".view.TextFields",
    // automationName: "UiAutomator2"
  }
};

async function main () {
  const client = await wdio.remote(opts);

  let screenshot = await client.takeScreenshot();
  fs.writeFileSync(`${SCREENCAPTURE_DIR}/capture_using_javascript.png`,screenshot,{encoding:'base64'})

  await client.deleteSession();
}

main();
