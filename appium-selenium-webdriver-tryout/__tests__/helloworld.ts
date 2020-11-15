/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License.
 */

import { By2, driver, WebDriver2 } from 'selenium-appium'
import { Builder, until } from 'selenium-webdriver';
import fs from 'fs'

// import { capabilities } from '../Setup'

jest.setTimeout(50000);

const url = 'http://localhost:4723/wd/hub'

const capabilities = {
  browserName: '',
  platformName: "Android",
  platformVersion: "8.1",
  app: "/root/apk_pool/ApiDemos-debug.apk"
}

describe('helloworld selenium-appium', () => {
  test("helloworld selenium-appium", async () => {
    console.log('helloworld')
    const webdriver = await new Builder()
    .usingServer(url)
    .withCapabilities(capabilities)
    .build();

    const element = await webdriver.findElement({"xpath": `//android.widget.TextView[@content-desc="Access'ibility"]`});

    await element.click();

    const base64Image = await webdriver.takeScreenshot()
    const imageBuffer = Buffer.from( base64Image, 'base64' )
    fs.writeFileSync( './test.png', imageBuffer )

    await webdriver.quit();

  })
})
