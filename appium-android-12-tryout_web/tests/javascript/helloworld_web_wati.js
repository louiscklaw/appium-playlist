const fs = require('fs')
const path = require('path')
const wdio = require("webdriverio");

const TEST_DIR = __dirname
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`)

const opts = {
  path: '/',
  port: 4723,
  capabilities: {
    platformName: "Android",
    browserName: "chrome",
    "appium:automationName": "UiAutomator2",
  }
};

async function main() {
  const client = await wdio.remote(opts);
  await client.url("https://www.wati.io");

  let screenshot = await client.takeScreenshot();
  // fs.writeFileSync(
  //   `${SCREENCAPTURE_DIR}/capture_using_javascript.png`,
  //   screenshot,
  //   { encoding: 'base64' }
  // )

  await client.deleteSession();
}

main();
