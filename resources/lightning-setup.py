#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Silakan masuk ke my.telegram.org
Masuk menggunakan akun Telegram Anda
Klik pada Alat Pengembangan API
Buat aplikasi baru, dengan memasukkan detail yang diperlukan
Untuk TeleBot"""
)
print("")

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    tele = client.send_message("me", client.session.save())
    tele.reply(
        "Di atas adalah STRING_SESSION untuk sesi Anda saat ini.\n@buzzasistenbot""
    )
    print("")
    print(
        "Di bawah ini adalah STRING_SESSION. Anda juga dapat menemukannya di Pesan Tersimpan Telegram Anda."
    )
    print("")
    print("")
    print(client.session.save())
