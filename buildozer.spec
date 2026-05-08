[app]
title = Matrix PassGen
package.name = matrixpassgen
package.domain = org.luigimarzetti
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 1.0

# Dipendenze necessarie per AdMob
requirements = python3,kivy==2.3.0,android,kivmob,pyjnius

orientation = portrait
fullscreen = 0
icon.filename = icon.png

# Permessi obbligatori per caricare annunci
android.permissions = INTERNET, ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True
android.archs = arm64-v8a
android.enable_androidx = True

# Tuo ID APP REALE nei metadati
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-2537033671132924~2402224670

# Librerie Google Play Services
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:23.0.0'

[buildozer]
log_level = 2
warn_on_root = 1
