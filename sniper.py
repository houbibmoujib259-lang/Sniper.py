import os
import aiohttp
import asyncio

SESSION_ID = os.getenv("TIKTOK_SESSION_ID")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

USERNAMES_TO_CHECK = [
    "bx9_", "z7q_", "k3m_", "v2w_", "j5x_", "p8n_", "d4l_", "h6s_", "f1t_", "m9r_",
    "q2z_", "w5k_", "x8j_", "c3v_", "b7h_", "n4f_", "l6d_", "t1p_", "s9m_", "r2x_",
    "9xx2", "7kk7", "3mm3", "5ff5", "8zz8", "4ll4", "2hh2", "6pp6", "1nn1", "0cc0",
    "x_z_9", "k_m_8", "j_l_7", "v_w_6", "b_n_5", "h_t_4", "f_r_3", "d_s_2", "p_q_1", "m_c_0",
    "qax9", "zsw7", "edc3", "rfv4", "tgb5", "yhn6", "ujm7", "ikl8", "olp9", "aqz1"
]

async def send_telegram_alert(username):
    if not BOT_TOKEN or not CHAT_ID:
        return
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"Available username found: @{username}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            pass

async def check_username(session, username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": f"sessionid={SESSION_ID}" if SESSION_ID else ""
    }
    try:
        async with session.get(url, headers=headers, allow_redirects=False) as response:
            if response.status == 404:
                await send_telegram_alert(username)
    except Exception:
        pass

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [check_username(session, username) for username in USERNAMES_TO_CHECK]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
