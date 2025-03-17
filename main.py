from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.webview import WebView
from kivy.utils import platform
from jnius import autoclass

class WebApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.webview = WebView()
        self.add_widget(self.webview)

        self.webview.url = "https://topthanawy.blogspot.com"

        if platform == 'android':
            self.load_admob()

    def load_admob(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        AdView = autoclass('com.google.android.gms.ads.AdView')
        AdSize = autoclass('com.google.android.gms.ads.AdSize')
        AdRequest = autoclass('com.google.android.gms.ads.AdRequest')

        activity = PythonActivity.mActivity
        banner_ad = AdView(activity)
        banner_ad.setAdSize(AdSize.BANNER)
        banner_ad.setAdUnitId("ca-app-pub-8837657678086847/2113650729")
        ad_request = AdRequest.Builder().build()
        banner_ad.loadAd(ad_request)

        self.add_widget(banner_ad)

class MyApp(App):
    def build(self):
        return WebApp()

if __name__ == '__main__':
    MyApp().run()