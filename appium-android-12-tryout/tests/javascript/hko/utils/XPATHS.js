module.exports = {
  TOP_LEFT_MENU_BUTTON:
    '//*[@content-desc="‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‏‏‏‏‏‎‏‎‎‎‏‏‎‏‎‎‎‏‏‎‎‎‏‏‏‏‎‏‎‎‎‎‏‏‎‏‏‎‏‎‎‏‎‎‏‎‎‎‎‎‎‏‎‏‎‎‎‎‏‏‏‎‎‎‎‎Navigate up‎‏‎‎‏‎"]',
  TOP_LEFT_BACK_BUTTON:
    '//*[@content-desc="‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‏‏‏‏‏‎‏‎‎‎‏‏‎‏‎‎‎‏‏‎‎‎‏‏‏‏‎‏‎‎‎‎‏‏‎‏‏‎‏‎‎‏‎‎‏‎‎‎‎‎‎‏‎‏‎‎‎‎‏‏‏‎‎‎‎‎Navigate up‎‏‎‎‏‎"]',

  LEFT_DRAWER: '//android.widget.ListView[@resource-id="hko.MyObservatory_v1_0:id/left_drawer"]',
  LEFT_DRAWER_HOME_BUTTON:
    '//androidx.drawerlayout.widget.DrawerLayout[@resource-id="hko.MyObservatory_v1_0:id/drawer_layout"]/android.widget.LinearLayout/android.widget.LinearLayout[1]',

  MENU_BUTTON_MY_WEATHER_OBSERVATION: '//*[@text="My Weather Observation"]',

  MENU_BUTTON_WEATHER_TIPS: '//*[@resource-id="hko.MyObservatory_v1_0:id/text" and @text="Weather Tips"]',
  MENU_BUTTON_WHATSAPP_STICKERS: '//*[@resource-id="hko.MyObservatory_v1_0:id/text" and @text="WhatsApp Stickers"]',
  MENU_BUTTON_9_DAY_FORECAST: '//*[@resource-id="hko.MyObservatory_v1_0:id/text" and @text="9-Day Forecast"]',

  // HOME
  REGIONAL_WEATHER_BUTTON: '//*[@content-desc="Select Regional Weather"]',

  // regional_weather_tab
  ADD_LOCATION_BUTTON: '//*[@resource-id="hko.MyObservatory_v1_0:id/add_location_btn"]',
  SEARCH_LOCATION_INPUT_BOX: '//*[@resource-id="hko.MyObservatory_v1_0:id/search_src_text"]',

  // first item in the list
  FIRST_ITEM_IN_THE_LIST: '//*[@resource-id="hko.MyObservatory_v1_0:id/location_add_layout"]',
  ADD_BUTTON: '//*[@content-desc="Add"]',

  // 9-forecast
  NINE_DAY_FORECAST_BODY: '//androidx.viewpager.widget.ViewPager[@resource-id="hko.MyObservatory_v1_0:id/viewpager"]',
};
