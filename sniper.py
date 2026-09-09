import os
import aiohttp
import asyncio

SESSION_ID = os.getenv("TIKTOK_SESSION_ID")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

USERNAMES_TO_CHECK = [
    "x_9q", "z_7k", "k_3m", "v_2w", "j_5x", "p_8n", "d_4l", "h_6s", "f_1t", "m_9r",
    "q_2z", "w_5k", "x_8j", "c_3v", "b_7h", "n_4f", "l_6d", "t_1p", "s_9m", "r_2x",
    "9xx2", "7kk7", "3mm3", "5ff5", "8zz8", "4ll4", "2hh2", "6pp6", "1nn1", "0cc0",
    "qax9", "zsw7", "edc3", "rfv4", "tgb5", "yhn6", "ujm7", "ikl8", "olp9", "aqz1",
    "bx_9", "zq_7", "km_3", "vw_2", "jx_5", "np_8", "ld_4", "sh_6", "tf_1", "rm_9",
    "qz_2", "kw_5", "jx_8", "vc_3", "hb_7", "fn_4", "dl_6", "pt_1", "ms_9", "xr_2",
    "x7z9", "k3m8", "j5l7", "v2w6", "b1n5", "h4t4", "f6r3", "d9s2", "p8q1", "m2c0",
    "z_x_9", "m_k_8", "l_j_7", "w_v_6", "n_b_5", "t_h_4", "r_f_3", "s_d_2", "q_p_1", "c_m_0",
    "v9_x", "k7_z", "m3_k", "w2_v", "x5_j", "n8_p", "l4_d", "s6_h", "t1_f", "r9_m",
    "z2_q", "k5_w", "j8_x", "v3_c", "h7_b", "f4_n", "d6_l", "p1_t", "m9_s", "x2_r",
    "2xx9", "7kk3", "3mm7", "5ff2", "8zz4", "4ll8", "2hh0", "6pp1", "1nn6", "0cc5",
    "ax9q", "sw7z", "dc3e", "fv4r", "gb5t", "hn6y", "jm7u", "kl8i", "lp9o", "qz1a",
    "9x_xq", "7k_kk", "3m_mm", "5f_ff", "8z_zz", "4l_ll", "2h_hh", "6p_pp", "1n_nn", "0c_cc",
    "x9_qz", "z7_wk", "k3_mj", "v2_xw", "j5_nc", "p8_dh", "d4_sf", "h6_rt", "f1_mp", "m9_zq",
    "q2_wx", "w5_jc", "x8_vb", "c3_bh", "b7_fn", "n4_dl", "l6_tp", "t1_ms", "s9_rx", "r2_9x",
    "xx92", "kk77", "mm33", "ff55", "zz88", "ll44", "hh22", "pp66", "nn11", "cc00",
    "x9qz", "z7wk", "k3mj", "v2xw", "j5nc", "p8dh", "d4sf", "h6rt", "f1mp", "m9zq",
    "q2wx", "w5jc", "x8vb", "c3bh", "b7fn", "n4dl", "l6tp", "t1ms", "s9rx", "r29x",
    "q_x9z", "z_w7k", "e_c3d", "r_v4f", "t_b5g", "y_n6h", "u_m7j", "i_l8k", "o_p9l", "a_z1q",
    "b_x9_", "z_q7_", "k_m3_", "v_w2_", "j_x5_", "n_p8_", "l_d4_", "s_h6_", "t_f1_", "r_m9_"
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
