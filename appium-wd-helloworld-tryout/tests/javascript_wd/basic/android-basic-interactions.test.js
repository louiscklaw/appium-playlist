import fs from 'fs';

import wd from 'wd';
import chai from 'chai';
import {
  androidCaps, serverConfig, androidApiDemos,
  SAUCE_TESTING, SAUCE_USERNAME, SAUCE_ACCESS_KEY
} from '../helpers/config.js';
const {assert} = chai;

describe('Basic Android interactions', function () {
  let driver;
  let allPassed = true;

  before(async function () {
    // Connect to Appium server
    driver = SAUCE_TESTING
      ? await wd.promiseChainRemote(serverConfig)
      : await wd.promiseChainRemote(serverConfig, SAUCE_USERNAME, SAUCE_ACCESS_KEY);

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

  it('take a screenshot', async function () {
    const base64Image = await driver.takeScreenshot()
    const imageBuffer = Buffer.from( base64Image, 'base64' );
    fs.writeFileSync('./test.png',imageBuffer)
  });

  it( 'click on a button', async function () {
    console.log( 'hello click button' )

    // await driver.setImplicitWaitTimeout(5000);

    const closeDialogButton = await driver.element( "xpath", `//android.widget.TextView[@content-desc="Access'ibility"]` );
    await closeDialogButton.click();

    const base64Image = await driver.takeScreenshot()
    const imageBuffer = Buffer.from( base64Image, 'base64' )
    fs.writeFileSync( './test.png', imageBuffer )
  } );

});
