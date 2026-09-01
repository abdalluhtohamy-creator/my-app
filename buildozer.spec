[app]
title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,arabic_reshaper,python-bidi
orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0
android.permissions = INTERNET
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
