const wdio = require('webdriverio');

async function greetings(opts) {
  const driver = await wdio.remote(opts);
  var element;

  return new Promise(async (res, rej) => {
    try {
      element = await driver.$('//*[@text="Agree"]');
      await element.click();

      element = await driver.$('//*[@text="Agree"]');
      await element.click();

      element = await driver.$('//*[@text="OK"]');
      await element.click();

      await driver.pause(3 * 1000);
      element = await driver.$('//*[@text="While using the app"]');
      await element.click();

      element = await driver.$('//*[@text="Allow all the time"]');
      await element.click();

      element = await driver.$('//*[@content-desc="Back"]');
      await element.click();

      // steady to wait greeting slide pop-up
      await driver.pause(5 * 1000);

      // proceed tour -> page 1
      // '//*[@content-desc="Next page"]'
      element = await driver.$('//*[@content-desc="Next page"]');
      await element.click();

      // // proceed tour -> page 2
      // // '//*[@content-desc="Next page"]'
      element = await driver.$('//*[@content-desc="Next page"]');
      await element.click();

      // // proceed tour -> page 3 -> done
      // // '//*[@content-desc="Close"]'
      element = await driver.$('//*[@content-desc="Close"]');
      await element.click();

      res(driver);
    } catch (error) {
      rej(driver);
    } finally {
      console.log('greeting done');
    }
  });
}

module.exports = greetings;
