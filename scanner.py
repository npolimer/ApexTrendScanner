import yfinance as yf
import pandas as pd

symbols = [
    "ADANIENSOL.NS",
    "ADANIENT.NS",
    "ADANIGREEN.NS",
    "ADANIPORTS.NS",
    "ADANIPOWER.NS",
    "ALKEM.NS",
    "AMBUJACEM.NS",
    "ANGELONE.NS",
    "APOLLOHOSP.NS",
    "APLAPOLLO.NS",
    "ASHOKLEY.NS",
    "ASIANPAINT.NS",
    "ASTRAL.NS",
    "AUBANK.NS",
    "AUROPHARMA.NS",
    "AXISBANK.NS",
    "BAJAJ-AUTO.NS",
    "BAJAJFINSV.NS",
    "BAJAJHLDNG.NS",
    "BAJFINANCE.NS",
    "BANDHANBNK.NS",
    "BANKBARODA.NS",
    "BANKINDIA.NS",
    "BDL.NS",
    "BEL.NS",
    "BHARATFORG.NS",
    "BHARTIARTL.NS",
    "BIOCON.NS",
    "BLUESTARCO.NS",
    "BOSCHLTD.NS",
    "BPCL.NS",
    "BRITANNIA.NS",
    "BSE.NS",
    "CAMS.NS",
    "CANBK.NS",
    "CDSL.NS",
    "CGPOWER.NS",
    "CHOLAFIN.NS",
    "CIPLA.NS",
    "COALINDIA.NS",
    "COFORGE.NS",
    "COLPAL.NS",
    "CONCOR.NS",
    "CUMMINSIND.NS",
    "DABUR.NS",
    "DALBHARAT.NS",
    "DIVISLAB.NS",
    "DLF.NS",
    "DMART.NS",
    "DRREDDY.NS",
    "EICHERMOT.NS",
    "ETERNAL.NS",
    "EXIDEIND.NS",
    "FEDERALBNK.NS",
    "FORTIS.NS",
    "GLENMARK.NS",
    "GMRAIRPORT.NS",
    "GODREJCP.NS",
    "GODREJPROP.NS",
    "GRASIM.NS",
    "HCLTECH.NS",
    "HDFCAMC.NS",
    "HDFCBANK.NS",
    "HDFCLIFE.NS",
    "HEROMOTOCO.NS",
    "HINDALCO.NS",
    "HINDPETRO.NS",
    "HINDUNILVR.NS",
    "HINDZINC.NS",
    "ICICIBANK.NS",
    "ICICIGI.NS",
    "ICICIPRULI.NS",
    "IDFCFIRSTB.NS",
    "INDHOTEL.NS",
    "INDIANB.NS",
    "INDIGO.NS",
    "INDUSINDBK.NS",
    "INFY.NS",
    "INOXWIND.NS",
    "IOC.NS",
    "IREDA.NS",
    "IRFC.NS",
    "ITC.NS",
    "JIOFIN.NS",
    "JINDALSTEL.NS",
    "JSWENERGY.NS",
    "JSWSTEEL.NS",
    "JUBLFOOD.NS",
    "KALYANKJIL.NS",
    "KAYNES.NS",
    "KOTAKBANK.NS",
    "KPITTECH.NS",
    "LAURUSLABS.NS",
    "LICHSGFIN.NS",
    "LICI.NS",
    "LODHA.NS",
    "LT.NS",
    "LUPIN.NS",
    "M&M.NS",
    "MANKIND.NS",
    "MARICO.NS",
    "MARUTI.NS",
    "MAXHEALTH.NS",
    "MAZDOCK.NS",
    "MOTHERSON.NS",
    "MPHASIS.NS",
    "MUTHOOTFIN.NS",
    "NATIONALUM.NS",
    "NBCC.NS",
    "NESTLEIND.NS",
    "NHPC.NS",
    "NMDC.NS",
    "NTPC.NS",
    "NUVAMA.NS",
    "NYKAA.NS",
    "OBEROIRLTY.NS",
    "OFSS.NS",
    "OIL.NS",
    "ONGC.NS",
    "PAGEIND.NS",
    "PATANJALI.NS",
    "PAYTM.NS",
    "PETRONET.NS",
    "PERSISTENT.NS",
    "PFC.NS",
    "PHOENIXLTD.NS",
    "PIIND.NS",
    "PNB.NS",
    "PNBHOUSING.NS",
    "POLICYBZR.NS",
    "POLYCAB.NS",
    "POWERGRID.NS",
    "POWERINDIA.NS",
    "PREMIERENE.NS",
    "PRESTIGE.NS",
    "RECLTD.NS",
    "RELIANCE.NS",
    "RBLBANK.NS",
    "RVNL.NS",
    "SAIL.NS",
    "SAMMAANCAP.NS",
    "SBICARD.NS",
    "SBILIFE.NS",
    "SBIN.NS",
    "SHREECEM.NS",
    "SHRIRAMFIN.NS",
    "SOLARINDS.NS",
    "SONACOMS.NS",
    "SUZLON.NS",
    "SUNPHARMA.NS",
    "SUPREMEIND.NS",
    "SWIGGY.NS",
    "TATACONSUM.NS",
    "TATAELXSI.NS",
    "TATAPOWER.NS",
    "TATASTEEL.NS",
    "TCS.NS",
    "TECHM.NS",
    "TIINDIA.NS",
    "TITAN.NS",
    "TMPV.NS",
    "TORNTPHARM.NS",
    "TRENT.NS",
    "TVSMOTOR.NS",
    "ULTRACEMCO.NS",
    "UNITDSPR.NS",
    "UNIONBANK.NS",
    "UNOMINDA.NS",
    "UPL.NS",
    "VBL.NS",
    "VEDL.NS",
    "VOLTAS.NS",
    "WAAREEENER.NS",
    "WIPRO.NS",
    "ZYDUSLIFE.NS"
]

results = []

for symbol in symbols:

    try:

        df = yf.download(
            symbol,
            period="10d",
            interval="5m",
            auto_adjust=True,
            progress=False
        )

        if len(df) < 50:
            continue

        close = df["Close"].iloc[:, 0]
        volume = df["Volume"].iloc[:, 0]

        first_high = df["High"].iloc[0, 0]
        first_low = df["Low"].iloc[0, 0]

        recent_low = df["Low"].tail(50).min()
        recent_high = df["High"].tail(50).max()

        if hasattr(recent_low, "iloc"):
            recent_low = recent_low.iloc[0]

        if hasattr(recent_high, "iloc"):
            recent_high = recent_high.iloc[0]

        bull_structure = 0
        bear_structure = 0

        if recent_low > first_low:
            bull_structure = 20

        if recent_high < first_high:
            bear_structure = 20

        ema9 = close.ewm(span=9).mean()

        ema_side = close > ema9

        cross_count = (
            ema_side != ema_side.shift(1)
        ).tail(50).sum()# Trend Persistence
        bars_above = int(
            (close > ema9).tail(50).sum()
        )

        # EMA Efficiency
        ema_efficiency = (
            bars_above / 50
        ) * 100

        # EMA Slope
        ema_slope = (
            (ema9.iloc[-1] - ema9.iloc[-20])
            / ema9.iloc[-20]
        ) * 100

        # Trend Strength
        trend_strength = (
            (close.iloc[-1] - close.iloc[-20])
            / close.iloc[-20]
        ) * 100

        # Volume
        avg_vol = volume.tail(20).mean()
        curr_vol = volume.iloc[-1]

        vol_ratio = (
            curr_vol / avg_vol
            if avg_vol > 0
            else 0
        )

        # Pullback Quality
        pullback_count = (
            (close > ema9)
            &
            (close.shift(1) <= ema9.shift(1))
        ).tail(50).sum()

        # EMA Cross Count
        ema_side = close > ema9

        cross_count = (
            ema_side != ema_side.shift(1)
        ).tail(50).sum()

        # Consecutive Trend Candles
        green_count = (
            close > close.shift(1)
        ).tail(20).sum()

        # Trend Smoothness
        smoothness = (
            green_count / 20
        ) * 100

        # EMA Discipline
        distance_from_ema = (
            abs(close - ema9) / ema9
        ).tail(20).mean()

        ema_discipline = max(
            0,
            100 - (distance_from_ema * 1000)
        )

        # Maximum Drawdown
        rolling_high = close.cummax()

        drawdown = (
            (rolling_high - close)
            / rolling_high
        ) * 100

        max_drawdown = drawdown.tail(50).max()

        # Trend Quality
        trend_quality = (
            ema_efficiency
            + smoothness
            - (cross_count * 5)
        )

        # Final Score
        score = 0

        score += ema_efficiency * 0.50
        score += smoothness * 0.30
        score += ema_discipline * 0.10
        score += min(vol_ratio * 5, 10)
        score += max(0, ema_slope * 20)
        score += max(0, trend_strength * 10)

        score -= cross_count * 5
        score -= max_drawdown * 8

        # Direction Logic

        bars_below = 50 - bars_above

        bear_efficiency = (
            bars_below / 50
        ) * 100

        if (
            ema_efficiency >= 65
            and cross_count <= 8
            and ema_slope > 0.10
            and trend_strength > 0.10
        ):
            direction = "BULL"

        elif (
            bear_efficiency >= 65
            and cross_count <= 8
            and ema_slope < -0.15
            and trend_strength < -0.15
        ):
            direction = "BEAR"

        else:
            direction = "SIDEWAYS"

        results.append([
            symbol,
            direction,
            round(score, 2),
            round(trend_quality, 2),
            round(ema_efficiency, 2),
            round(smoothness, 2),
            round(ema_discipline, 2),
            round(max_drawdown, 2),
            int(cross_count),
            round(ema_slope, 2),
            round(trend_strength, 2),
            bars_above,
            round(vol_ratio, 2)
        ])

    except Exception as e:
        print(symbol, e)

rank = pd.DataFrame(
    results,
    columns=[
        "Stock",
        "Direction",
        "Score",
        "TrendQuality",
        "Smoothness",
        "EMADiscipline",
        "MaxDrawdown",
        "CrossCount",
        "EMA_Slope%",
        "Trend%",
        "BarsAboveEMA",
        "VolRatio",
        "EMA_Efficiency"
    ]
)

bull_rank = rank[
    rank["Direction"] == "BULL"
].sort_values(
    by=["Score", "TrendQuality"],
    ascending=False
)

bear_rank = rank[
    rank["Direction"] == "BEAR"
].sort_values(
    by="Score",
    ascending=False
)

sideways_rank = rank[
    rank["Direction"] == "SIDEWAYS"
].sort_values(
    by="Score",
    ascending=False
)

print("\nTOP 10 BULLISH STOCKS\n")
print(bull_rank.head(10))

print("\nTOP 10 BEARISH STOCKS\n")
print(bear_rank.head(10))

print("\nTOP 10 SIDEWAYS STOCKS\n")
print(sideways_rank.head(10))

rank.to_csv(
    "output.csv",
    index=False
)

print("\nResults saved to output.csv")