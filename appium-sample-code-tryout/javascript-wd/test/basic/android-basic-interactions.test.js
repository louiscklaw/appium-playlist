import fs from 'fs';

import wd from 'wd';
import chai from 'chai';
import {
  androidCaps, serverConfig, androidApiDemos,
  SAUCE_TESTING, SAUCE_USERNAME, SAUCE_ACCESS_KEY
} from '../helpers/config.js';
const {assert} = chai;


const PACKAGE = 'io.appium.android.apis';
const SEARCH_ACTIVITY = '.app.SearchInvoke';
const ALERT_DIALOG_ACTIVITY = '.app.AlertDialogSamples';

describe('Basic Android interactions', function () {
  let driver;
  let allPassed = true;

  before(async function () {
    // Connect to Appium server
    driver = SAUCE_TESTING
      ? await wd.promiseChainRemote(serverConfig)
      : await wd.promiseChainRemote(serverConfig, SAUCE_USERNAME, SAUCE_ACCESS_KEY);

    // add the name to the desired capabilities
    const sauceCaps = SAUCE_TESTING
      ? {
        name: 'Android Basic Interactions Test',
      }
      : {};

    // merge all the capabilities
    const caps = {
      platformName: "Android",
      platformVersion: "8.1",
      app: "/root/apk_pool/ApiDemos-debug.apk"
    }

    // Start the session, merging all the caps
    await driver.init(caps);
  });

  afterEach(function () {
    // keep track of whether all the tests have passed, since mocha does not do this
    allPassed = allPassed && (this.currentTest.state === 'passed');
  });

  after(async function () {
    await driver.quit();
    if (SAUCE_TESTING && driver) {
      await driver.sauceJobStatus(allPassed);
    }
  });

  it('helloworld',function () {
    return driver.takeScreenshot().then((base64Image) => {
      const imageBuffer = Buffer.from( base64Image, 'base64' );
      fs.writeFileSync('./test.png',imageBuffer)
    });

  });

});
