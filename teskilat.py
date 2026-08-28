#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Diş Macunu Orta Kısım Planlama Teşkilatı — çalışan resmi yazılım.

Tüpün neresinden sıkıldığını ölçer, sapmayı kalkınma endeksine çevirir,
beş yıllık planla karşılaştırır ve tutanak basar.
"""
from __future__ import annotations

import argparse
import base64
import datetime
import random
import sys
from dataclasses import dataclass

SURUM = "1.0.2026-ORTA"
TESKILAT = "T.C. Diş Macunu Orta Kısım Planlama Teşkilatı"
MARKALAR = [
    "İleri Macun",
    "Beyaz Devrim",
    "Mint Cumhuriyeti",
    "Florür Belediyesi",
    "Kalsiyum Kooperatifi",
    "Diş Eti Vakfı",
]
RENKLER = [
    "klasik mint",
    "resmi beyaz",
    "karanfil genelgesi",
    "gece kömürü",
    "çocuk çileği",
    "anason tebliği",
]

# Arşiv dipnotu (base64). Çözmek isteyen çözer. Siyasi değil, planlıdır.
_ARIV = "QmXFnyB5xLFsbMSxayBwbGFuIGhlciB6YW1hbiBiaXRlciwgaGVyIHR1dGFuYWsga2FsxLFyLg=="


@dataclass
class Tutanak:
    marka: str
    renk: str
    orta_orani: float
    sapma_puani: float
    karar: str
    ceza: str
    plan_yili: int


def sapma_hesapla(orta_orani: float) -> float:
    """0.0 = mükemmel uçtan sıkma, 1.0 = tümüyle ortadan sıkma."""
    o = max(0.0, min(1.0, orta_orani))
    return round((o ** 1.35) * 100.0, 2)


def karar_uret(puan: float) -> tuple[str, str]:
    if puan < 8:
        return (
            "UYGUN — Beş yıllık plan çizgisinde uçtan sıkılmıştır.",
            "Takdir yazısı ve bir adet yedek kapak.",
        )
    if puan < 25:
        return (
            "HAFİF SAPMA — Tüpün beline yaklaşılmış, henüz kriz yok.",
            "Sözlü uyarı ve ayna karşısında eğitim.",
        )
    if puan < 50:
        return (
            "ORTA SAPMA — Kalkınma ekseni tüpün göbeğine kaymıştır.",
            "Yazılı ihtar ve 3 gün fırça yasağı (sembolik).",
        )
    if puan < 75:
        return (
            "AĞIR SAPMA — Orta kısım fiilen yeni başkent ilan edilmiştir.",
            "Tüpün toplatılması ve ucundan sıkma semineri.",
        )
    return (
        "OLAĞANÜSTÜ HAL — Tüp kendi anayasasını yazmıştır.",
        "Genel kurul, kelepçeli kapak ve halka açık itiraf.",
    )


def ascii_tup(orta_orani: float) -> str:
    n = 16
    pos = int(round(orta_orani * (n - 1)))
    govde = ["="] * n
    govde[pos] = "X"
    return "kapak]" + "".join(govde) + "[kuyruk"


def bas(t: Tutanak) -> str:
    simdi = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    cizgi = "=" * 62
    return f"""{cizgi}
{TESKILAT}
SÜRÜM {SURUM}  |  TUTANAK TARİHİ {simdi}
{cizgi}
Marka / renk      : {t.marka} / {t.renk}
Orta sıkma oranı  : %{t.orta_orani * 100:.1f}
Sapma puanı       : {t.sapma_puani} / 100
Plan dönemi       : {t.plan_yili}–{t.plan_yili + 5}
Tüp şeması        : {ascii_tup(t.orta_orani)}
                      (X = basılan yer)

KARAR
{t.karar}

YAPTIRIM
{t.ceza}

Not: Macun milli servettir. Ortadan sıkmak israftır,
uçtan sıkmak medeniyettir. Bu cümle tartışmaya kapalıdır.
{cizgi}
"""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=TESKILAT,
        epilog="Örnek: python teskilat.py --orta 0.62 --marka 'Mint Cumhuriyeti'",
    )
    p.add_argument(
        "--orta",
        type=float,
        default=None,
        help="0.0 (uç) ile 1.0 (tam orta) arası sıkma oranı. Boşsa rastgele.",
    )
    p.add_argument("--marka", type=str, default=None)
    p.add_argument("--renk", type=str, default=None)
    p.add_argument(
        "--gizli",
        action="store_true",
        help="Arşiv dipnotunu çözer (meraklılar için).",
    )
    args = p.parse_args(argv)

    if args.gizli:
        try:
            print(base64.b64decode(_ARIV).decode("utf-8"))
        except Exception:
            print("(dipnot okunamadı, teşkilat arşivi nem kapmış)")
        return 0

    orta = args.orta if args.orta is not None else random.random()
    orta = max(0.0, min(1.0, orta))
    puan = sapma_hesapla(orta)
    karar, ceza = karar_uret(puan)
    t = Tutanak(
        marka=args.marka or random.choice(MARKALAR),
        renk=args.renk or random.choice(RENKLER),
        orta_orani=orta,
        sapma_puani=puan,
        karar=karar,
        ceza=ceza,
        plan_yili=random.choice([1963, 1968, 1973, 1979, 1985, 2024]),
    )
    print(bas(t))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
