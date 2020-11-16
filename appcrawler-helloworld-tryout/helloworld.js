
var wd = require('wd')

var driver = wd.remote({
  hostname: '127.0.0.1',
  port: 4444
});


driver.elementByAccessibilityId('Graphics')
driver.