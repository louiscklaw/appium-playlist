// javascript

const wdio = require("webdriverio");
const assert = require("assert");

const opts = {
  path: '/wd/hub',
  port: 4723,
  capabilities: {
    platformName: "Android",
    platformVersion: "8.1",
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

  // const field = await client.$("android.widget.EditText");
  // await field.setValue("Hello World!");
  // const value = await field.getText();
  // assert.equal(value,"Hello World!");

  await client.deleteSession();
}

main();
