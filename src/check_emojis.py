import csv
import os
import sys
import pandas as pd
import time

os.chdir("C:/GCBA/carga_cognitiva_boti/data/")


"""EDU04CUX06 

No, no es un mito.\r\n\u201cSé el adulto que necesitabas cuando eras niño\u201d. ¿Te suena? ??
El hogar tiene que ser un espacio de *contención y apoyo*. Un lugar donde se enseñe desde
 el *respeto y la empatía*.\r\n¿Viste? Todos los días se aprende algo nuevo. 
 Gracias por romper mitos conmigo. ??\r\n¿Seguimos hablando del tema?

Los unicode son comillas graficas, y el corazon violeta lo transformo como "??"
Luego de "romper mitos conmigo" aparece el emoji 😌 que lo graban como "??"


O sea... hay emojis que se pierden pero aparentemente hay otros ( no se porque )
que se graban como \u99999
"""

emoji = '“'
# Obtener la codificación Unicode del emoji y convertirla a hexadecimal
unicode_codificado = ord(emoji)
unicode_hex = hex(unicode_codificado)
# Formatear la representación Unicode con la notación \u
unicode_repr = f'\\u{unicode_hex[2:]}'
print(f'La representación Unicode del emoji {emoji} es "{unicode_repr}"')

emoji = '”'
unicode_codificado = ord(emoji)
unicode_hex = hex(unicode_codificado)
unicode_repr = f'\\u{unicode_hex[2:]}'
print(f'La representación Unicode del emoji {emoji} es "{unicode_repr}"')

emoji = '📅'
unicode_codificado = ord(emoji)
unicode_hex = hex(unicode_codificado)
unicode_repr = f'\\u{unicode_hex[2:]}'
print(f'La representación Unicode del emoji {emoji} es "{unicode_repr}"')


lista_emojis=["📍","📞","✉️","📅","🔍","👩","📱","🏥","🗓️","💻","🏫","⏰","🇦🇷","📚","🎭","🤖","🌳","🏠","❤️","⚽","🏢","🏛️","🚗","💡","💉","📄","🎨","🖥️","🚘","♻️","⚕️","💳","📝","🎶","🚲","🚍","🌎","👶","🚇","💵","📸","😷","🚚","🎉","🍽️","📧","💸","🎵","💃","🏃","🏆","🧪","🕘","🚴","🔥","👮","🌱","🏍️","☕","🚌","🎧","✏️","💼","🚧","🏙️","💰","☎️","🕛","🖼️","📲","💧","🏗️","🎤","🦾","🌈","🚑","📺","📖","🍿","🗑️","☀️","🧼","🎓","🩺","🔎","🎟","🌿","📬","🚫","🔧","👵","🎟️","📋","🚆","🎬","🏦","🎒","🚖","⚖️","🍳","⌚","♿","🎸","🚀","🚶","🏟️","🍎","🤸","📻","🕺","🌆","🎮","🧹","📽️","🎼","🏋️","🧘","📷","🧾","🛒","🎷","🐶","🥇","🎫","🎥","🌐","👷","👪","🧠","📃","🥤","🚏","🌡️","🥕","🏖️","🛍️","📦","🕒","🦠","🤰","🎙️","🏳️","🗳️","📑","🔋","🩰","💊","⛱️","🏘️","🔬","🍕","🗺️","✴️","🕗","💦","🥟","🏊","🍷","🥩","🏀","🚒","🍗","🎅🏻","🍲","♟️","🥗","🖋️","🏡","🐱","🌃","🚛","🏬","🤹","📜","🐕","📰","🏭","🧩","🇺🇸","🤧","☠️","🕙","⛹️","🍺","✈️","🎾","🔭","🌭","🍔","⌛","🎄","🎲","🧴","🧱","⛪","🥊","🍀","🕵️","🐄","🎪","📓","🚨","🚽","🪪","🌲","🕑","🐾","🍌","❄️","🌇","🚦","🛠️","💍","🏓","🤡","🚉","🛣️","🏪","🤒","🚸","🎩","🐷","🌸","🧉","🔮","🧏","🐎","🔢","🔑","🌾","🤟","🏨","🥶","🐺","🚿","🏅","🌺","🥦","🎆","🌙","🏐","📡","🥐","🎊","💥","⚧️","🦯","🕶️","🔌","🔔","🍴","🥘","🎯","🥁","⚰️","📊","🇫🇷","🩹","🍇","🎁","✊","🥫","🍞","🇬🇧","🌛","🍯","🛬","🦆","✒️","🇧🇷","🎺","🚰","🕚","💲","🏁","👜","🇵🇪","🐦","🕖","🇪🇸","🐩","🌊","🥬","🪗","🗓","📹","🍾","🖨️","🎂","♂","🦮","🚂","🦽","🍃","🕣","🍅","👾","🧺","🥉","🥈","🧓","🕔","🚕","🛹","🔨","🥵","🍂","🚪","🩸","🛵","🍰","💐","🏎️","🌯","🤾","🇨🇱","🐴","🦟","🥝","🇮🇹","💃🏻","🛏️","🧯","🧀","🇲🇽","🥛","🎈","🍊","👕","🍖","🚃","🌧️","🥽","🐟","🦷","🖊️","♀","🕐","🐔","🏛","🗝️","⚗️","🦁","🚔","👓","🎻","🥪","🕓","🥅","🗞️","⛲","🛥️","✝️","🎠","👞","🌡","🌽","🐖","🐓","👂","🧰","🍓","👗","📕","🐮","🚴🏻","🍸","🍻","⛈️","🚴🏽","🌹","🍹","🚙","🕢","🚢","🕕","🧳","🇺🇾","ℹ️","🚈","🕡","🏍","🚓","🐇","🥚","🚬","☄","🚐","🕤","🍆","📗","🗽","📙","🐳","📘","☁️","⛰️","⛸️","🕥","🕰️","🕺🏽","🕹️","🍨","☂️","🦒","💿","🍪","🍣","🇵🇱","🇸🇦","🍁","🕷️","🍦","🇲🇦","🇭🇷","🪑","🇮🇸","💄","⌨️","🥎","🪓","🚯","⛅","🛩️","🏟","🌅","🥣","⏲️","⛏️","🖱️","☔","🏗","🚮","🇯🇵","🇧🇪","🗂️","🌄","〰️","🎢","🐜","🪁","🗺","⚒️","🦻","🛋️","🅿️","🚊","🦊","👁","🧬","🚜","🐐","🐑","🎦","🍽","👠","🕍","🚺","🥖","🧂","🍚","🛫","🏑","💃🏼","📩","🛂","🎞️","🐂","🦗","🇩🇪","🐈","🌂","🦋","🌴","🕊️","🕎","🦎","🐸","🦔","💶","🇵🇹","🐽","⏱","🥑","📼","🇵🇾","🗒","🥡","🍱","🦜","🌻","🇦🇹","🍤","💃🏽","👚","🎇","🇸🇪","⛔","🌞","🍼","🇧🇴","🇨🇳","🐉","🌷","🏕️","🐒","🐍","🤽","🛐","🔸","🔹","✅","👕","🔦","📵","🔄","🔃","⏭","➡","🎽","✔️","🔹","☝️","👇","📍","➖","✅","👉","🙌","😉","📞","💪","👋","✉️","🤔","🤩","📅","🔍","👩","😊","📱","🏥","😕","😎","😅","👍","🗓️","🙂","💻","🏫","☝","⏰","✨","🇦🇷","📚","🎭","🤖","🌳","🧑","👨","","🏠","❤️","🤓","📌","😔","📆","👌","⚽","🏢","🏛️","😍","🚗","❌","💡","💉","📄","🎨","🖥️","🚘","⭐","♻️","⚕️","✍️","💳","📝","🎶","🔒","🚲","😬","😓","🚍","♀️","🌎","🧒","👶","✔","🥰","🚇","💵","🤳","📸","😌","👧","🧐","😷","🤝","🚚","🎉","🍽️","💬","👏","📧","♂️","🤯","💸","🔸","🎵","💃","👦","🏃","🏆","😄","◼️","🙏","🧍","🧪","🕘","🚴","🔥","👮","😋","👆","😀","🌱","🏍️","😃","😮","☕","🚌","🎧","✏️","💼","🚧","🏙️","💰","☎️","🙋","🕛","⏳","🖼️","📲","🙃","💧","🏗️","🎤","⚡","🦾","🌈","🚑","🤞","📺","📖","😞","🍿","👤","🗑️","☀️","👴","😂","🖐️","🧼","🎓","🤤","😱","🥳","🩺","🔎","👐","🎟","🌿","📬","🚫","↔️","🔧","👵","💙","🖌️","🎟️","📋","🚆","🎬","🏦","🎒","🙁","🚖","⚖️","🍳","⌚","♿","😁","🎸","🚀","👊","🚶","🏟️","🍎","🤸","📻","🕺","🌆","🎮","😜","🧹","📽️","🎼","🏋️","🧘","⬅️","📷","🧾","💫","🛒","🎷","🐶","🥇","🎫","😲","🎥","🌐","🤫","🤦","👷","👪","🔊","🧠","⏱️","📃","🥤","🚏","🌡️","🥕","🏖️","✋","😶","🗣️","🛍️","📦","🕒","🦠","🤰","🎙️","💜","🏳️","🗳️","🌟","😟","📑","🔋","🤭","🔄","🩰","💊","⛱️","🏘️","🔬","🍕","🗺️","✴️","🕗","💦","🥟","🏊","🍷","📈","🥩","🏀","🚒","⚠️","🍗","🤛","🎅🏻","🍲","♟️","🥗","🖋️","🤜","🏡","🐱","🌃","▫️","🚛","🏬","🤹","📜","🐕","👉🏼","📰","🏭","🧩","🇺🇸","🤧","☠️","🕙","⛹️","🍺","✈️","🤍","🎾","🔭","🌭","🤲","🍔","⌛","🎄","▪","🔙","🎲","🔗","🧴","🧱","⛪","😏","🥊","🍀","🕵️","🐄","🦰","🎪","☑️","📓","🚨","🚽","🪪","🌲","🕑","🐾","🍌","❄️","🌇","🚦","👀","🛠️","💍","▪️","🏓","🤡","🚉","🛣️","🏪","🤒","💨","🚸","🎩","👱","🦄","🐷","🌸","🧉","🔮","💚","🧏","🐎","◾","🗿","🔢","🤣","🔑","🌾","🤟","🏨","🥶","🐺","🚿","🏅","🌺","🥦","🎆","🌙","🏐","📡","💔","🥐","🎊","➡","💥","⚧️","🟨","🦯","🟢","🕶️","💎","🔌","🔔","🍴","🥘","😥","🎯","🥁","⚰️","👃","📊","🤕","🙄","🇫🇷","🩹","🍇","🎁","✊","🥫","🍞","🇬🇧","🌛","🍯","🔈","👎","🧔","🤐","🛬","📢","🦆","✒️","🇧🇷","🎺","💛","🚰","🕚","💲","🏁","👜","📣","🇵🇪","❇️","🐦","🕖","🇪🇸","👅","🐩","🌊","🥬","🪗","⚕","🗓","📹","🍾","🖨️","🎂","♂","🦮","🚂","➡️","🦽","🍃","🤘","🕣","🍅","👾","🧺","🥉","🥈","🧓","🕔","🚕","🛹","🦸","😵","🔨","⛩️","🥵","🍂","🚪","🩸","🛵","✳️","🍰","🪵","💐","🏺","⚙️","🏎️","🪕","☠","🌯","👥","😧","🤾","🏴","💭","🇨🇱","🛎️","🐴","🦟","🥝","🇮🇹","🤙","💃🏻","🛏️","🔕","😛","💖","🧯","🧀","🇲🇽","🥛","🎈","🍊","🖍️","👕","👨🏻","🍖","🚃","🤷","🌧️","🥽","🧥","▶️","🐟","🦷","🖊️","♀","🕐","🎛️","🐔","🤑","💯","✡️","🏛","🧸","🤪","🗝️","👑","👒","🐛","↖️","⚗️","🦁","👩🏼","🚔","🧢","🦱","👓","🎻","🥪","💩","🫡","🕓","🟧","🥲","🧤","🍄","🫂","🥅","🔦","🤼","🍜","💆","🗞️","⛲","☯️","💞","👭","🌮","🛥️","✝️","🐪","🎠","🚻","👞","🥙","🙈","🔵","🧡","🌡","🌽","🐖","🐓","👂","🧰","🌬️","🙎","💀","🤨","🍓","🔴","🧵","👗","📕","🪐","💗","🐮","🚴🏻","🍸","👁️","🍻","🐙","🖐","⛈️","😒","🚴🏽","🌹","👯","🤱","🔓","🍹","🚙","🥔","🧔🏻","⬆️","😯","🕢","⏯️","🦵","🔜","🚢","🕕","😆","🧳","🇺🇾","ℹ️","🚈","🫶","💤","🕡","🏍","🚓","🐇","✂️","🛢️","🥚","🐞","🚬","☄","🚐","🛸","🏞️","🕤","👹","🍆","🌵","📗","🗽","👽","📙","🐳","📘","☁️","⛰️","⛸️","👈","🪖","🕥","🕰️","🕺🏽","💪🏻","🕹","🙉","🥺","👩🏻","🕹️","🍨","☂️","🦒","💿","🍪","🍣","🥧","🐌","👇🏼","🇵🇱","🇸🇦","🐃","🍁","🕷️","🪆","🛑","🚶🏽","🍦","🇲🇦","🇭🇷","🖖","😪","🪑","🇮🇸","💄","⌨️","⛓️","😑","🥎","🪓","👄","🚯","❓","⛅","⚔️","🛩️","🏟","🌅","😩","🤢","🌀","➰","🥣","🥯","🍛","⏲️","⛏️","💓","🖱️","☔","🤚","🏗","🚮","🇯🇵","🙅","🇧🇪","🗂️","🟥","🙋🏽","👨🏽","🌄","〰️","🎢","🐜","🪁","🗺","⚒️","🙇","🥱","🦻","😣","🔐","🛋️","🪙","🅿️","🚊","🦊","🗃️","👁","🫶🏻","🧬","⚜️","💅🏼","🚜","🔖","🐐","🐣","🥓","🐑","🦲","🎦","🍽","👠","🕍","🚺","🥖","🧂","🍚","🛫","🏑","💃🏼","😝","📩","🛂","📥","🥹","🎞️","🐂","🦗","🇩🇪","🐈","🌂","🧮","☄️","🦋","🌠","🌴","🕊️","🕎","🦎","🐸","🦔","💶","🇵🇹","🐽","✉","⏱","🥑","📼","🇵🇾","😠","👇🏽","🌰","🗒","🥡","🧙","🍱","🧚","🏷️","🦜","🌻","🆗","🇦🇹","🎱","📔","🏰","🧭","🍤","💃🏽","🌉","🔟","🧜","🏎","💅","👚","🔠","😴","🎇","👣","🇸🇪","🙊","🔉","🐭","🏚️","⛔","😢","🆓","🌞","🍼","👶🏾","🆔","👌🏽","🔺","🔶","🦹","👰","🧊","☮️","💟","🇧🇴","🇨🇳","🐉","🌷","🏕️","🐒","🐍","🦅","🃏","🎎","🌗","🥋","🤽","🛐"]

# Lista para almacenar los resultados del proceso
lista_emojis_unicode = []
invalidos = 0
validos   = 0
# Proceso cada emoji y pongo su codigo en una lista
for emoji in lista_emojis:

    try:
        # Obtener el código Unicode del emoji
        unicode_codificado = ord(emoji)
        unicode_hex = hex(unicode_codificado)
        unicode_repr = f'\\u{unicode_hex[2:]}'
        lista_emojis_unicode.append(unicode_repr)
        validos = validos + 1

    except TypeError as e:
        print(f"Error: {e}",emoji )
        invalidos = invalidos + 1


df = pd.DataFrame(lista_emojis_unicode, columns=["Unicode"])

# # Escribo la lista de emojis_unicode en un csv
archivo_csv = "emojis_unicode.csv"
df.to_csv(archivo_csv, index=False)

print(lista_emojis_unicode)
print("validos", validos)
print("invalidos", invalidos)


