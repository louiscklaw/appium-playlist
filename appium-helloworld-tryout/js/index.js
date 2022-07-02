const wdio = require("webdriverio");

const opts = {
  hostname: "http://192.168.10.21",
  path: "/wd/hub",
  port: 4444,
  capabilities: {
    platformName: "Android",
    app: "apk_pool/ApiDemos-debug.apk",
    // uiautomator2ServerLaunchTimeout: 60 * 1000,
  },
};

async function main() {
  const client = await wdio.remote(opts);

  await client.deleteSession();
}

main();
