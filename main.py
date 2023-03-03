""""
from gtts import gTTS
import os
from os import path
dosya = open("seslendirme1.txt",encoding="utf-8")
yazi = dosya.read()
cikti = gTTS(text = yazi  , lang = "tr",slow = False)
cikti.save("kamyon2.mp3")
os.system("kamyon2.mp3")
dosya.close()
"""
from gtts import gTTS
import os
mytext = 'Yalnızca fiyata bakarak karar vermek ise başka büyük bir hatadır. Unutmayın doğru kişisel korunma donanımı seçimi hem çalışan, hem şirket, hem ülke için en doğru, karlı ve verimli seçenektir.Yanlış korunma donanımı seçimi sizi karşılanması zor, belki de hiç telafi edilemeyecek risklere karşı korunmasız bırakır.Gürültüden koruyucu kulak seçimi yapılırken ilk bakılacak nokta SNR değeri olmalıdır. Her iş kulaklığının ambalajında SNR değeri açık bir şekilde yazar.Satın alma biriminizin mutlaka İSG uzmanınızın tavsiye ettiği eşik değerin üzerinde bir SNR değeri olan bir kulaklık seçmesini sağlayınız.'
language = 'tr'
isim  = 'kulaklık8.3.mp3'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(isim)
os.system(isim)
