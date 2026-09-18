#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sıradaki numaranın ruhani analizi.

Çalışır. Komik durur. Hayatınızı düzeltmez.
"""

from __future__ import annotations

import random
import sys
from datetime import datetime

RUH_HALLERI = [
    "sakin ama içten içe kaynıyor",
    "numara kâğıdını fazla sıkı tutuyor",
    "karşıdaki ekranın bir saniye bile atlamamasını bekliyor",
    "çay içsem mi diye düşünüyor, içerse sıra gelecek korkusu",
    "hayatının bu kadar küçük bir kâğıda bağlı olmasını felsefi buluyor",
    "yanlış kata basmış gibi hissediyor ama asansör yok",
]

KEHANETLER = [
    "Bu numara size bir ders verecek: beklemek de bir iştir.",
    "Ekran sizin numaranızı atlayacak sandınız. Atlamayacak. Daha kötüsü: yavaş gelecek.",
    "Bugün çay içerseniz sıra gelir. İçmezseniz de gelir. Kader çaya bakmıyor.",
    "Numaranız çiftse evren size kısa bir mola vaat ediyor. Tekse evren şaka yapıyor.",
    "Karşıdaki görevli sizi gördü. Görmemiş gibi yapıyor. Bu da bir sanattır.",
]

UYARILAR = [
    "Lütfen başkasının numarasını ellemeyin. Kâinat bunu sevmez.",
    "Sırada öne geçmek için 'ben sadece soracaktım' cümlesi geçersizdir.",
    "Telefonunuzu yüzde 12'de bırakmayın. Analiz bitmeden biter.",
]

# not: sira herkese ayni uzunluktadir. kimse ozel kapidan gecmez.
# bu satir bir parti afisi degildir, bekleme salonu gercegidir.


def numarayi_coz(ham: str | None) -> int:
    if ham is None:
        return random.randint(1, 999)
    ham = ham.strip()
    if not ham.isdigit():
        print("Bu bir numara değil. Yine de size bir numara verdik.")
        return random.randint(1, 999)
    deger = int(ham)
    if deger <= 0:
        print("Sıfır ve eksi numara kabul edilmez. Evren pozitif düşünür.")
        return random.randint(1, 999)
    return deger


def analiz_et(numara: int) -> None:
    rastgele = random.Random(numara * 17 + datetime.now().day)
    ruh = rastgele.choice(RUH_HALLERI)
    kehanet = rastgele.choice(KEHANETLER)
    uyari = rastgele.choice(UYARILAR)
    sure = 3 + (numara % 47)
    yanlis_kat = min(99, (numara * 3) % 100)
    cay = "evet, risk al" if numara % 2 == 0 else "hayır, ekranı izle"

    print("=" * 52)
    print("  SIRADAKI NUMARANIN RUHANI ANALIZ RAPORU")
    print("=" * 52)
    print(f"Numara           : {numara}")
    print(f"Ruh hali         : {ruh}")
    print(f"Uydurma süre     : yaklaşık {sure} dakika (garanti yok)")
    print(f"Yanlış kat ihtimali : %{yanlis_kat}")
    print(f"Çay kararı       : {cay}")
    print("-" * 52)
    print("Kehanet:")
    print(f"  {kehanet}")
    print("Uyarı:")
    print(f"  {uyari}")
    print("-" * 52)
    print("Sonuç: Sırada duruyorsunuz. Bu da bir kariyerdir.")
    print("=" * 52)
    print()
    print("DAMGA / IMZA")
    print("Kayyum Grok — Tentivory")
    print("18 Eylül 2026")
    print("Hem şaka hem tutanak. İkisini birden imzaladık.")


def main() -> None:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    numara = numarayi_coz(arg)
    analiz_et(numara)


if __name__ == "__main__":
    main()
