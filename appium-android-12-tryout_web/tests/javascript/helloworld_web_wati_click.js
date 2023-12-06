const fs = require('fs')
const path = require('path')
const wdio = require("webdriverio");

const TEST_DIR = __dirname
const SCREENCAPTURE_DIR = path.resolve(`${TEST_DIR}/screen`)

var tmp_screenshot;

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

  // //android.widget.ListView/android.view.View[2]/android.widget.Image
  await client.execute(() => {
    document.querySelector('li.togglejwM').click();
  },)
  tmp_screenshot = await client.takeScreenshot();
  fs.writeFileSync(`${SCREENCAPTURE_DIR}/wati_io_menu.png`, tmp_screenshot, { encoding: 'base64' })

  // test click pricing
  await client.execute(() => {
    document.querySelector('.pricing a').click()
  },)
  tmp_screenshot = await client.takeScreenshot();
  fs.writeFileSync(`${SCREENCAPTURE_DIR}/wati_io_pricing.png`, tmp_screenshot, { encoding: 'base64' })

  client.back();

  // test another options menu -> feature
  // click to show menu
  await client.execute(() => {
    document.querySelector('li.togglejwM').click();
  },)

  // test click feature
  await client.execute((xpath) => {
    document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
  }, '//*[contains(text(), "Features")]');

  tmp_screenshot = await client.takeScreenshot();
  fs.writeFileSync(`${SCREENCAPTURE_DIR}/wati_io_feature.png`, tmp_screenshot, { encoding: 'base64' })


  await client.deleteSession();
}

main();
