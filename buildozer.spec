[app]
title = Matrix PassGen
package.name = matrixpassgen
package.domain = org.luigimarzetti
source.dir = .
# Fondamentale aggiungere mp3 qui!
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 1.0

requirements = python3,kivy==2.3.0,android

orientation = portrait
fullscreen = 0
icon.filename = icon.png

android.api = 33
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True
android.archs = arm64-v8a
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
