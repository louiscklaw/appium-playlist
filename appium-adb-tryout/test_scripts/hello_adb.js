const ADB = require('appium-adb');

(async () =>{

  const adb = await ADB.createADB();
  console.log(await adb.getPIDsByName('com.android.phone'));

})();