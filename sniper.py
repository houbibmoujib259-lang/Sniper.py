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
    "_q_x9z", "_z_w7k", "_e_c3d", "_r_v4f", "_t_b5g", "_y_n6h", "_u_m7j", "_i_18k", "_o_p91", "_a_z1q",
    "_b_x9", "_z_q7", "_k_m3", "_v_w2", "_j_x5", "_n_p8", "_1_d4", "_s_h6", "_t_f1", "_r_m9_",
    # 3-character alphanumeric combinations (New batch) ew
    "b1c", "d2e", "f3g", "h4i", "j5k", "l6m", "n7o", "p8q", "r9s", "t0u",
    "v1w", "x2y", "z3a", "b4c", "d5e", "f6g", "h7i", "j8k", "l9m", "n0o",
    "p1q", "r2s", "t3u", "v4w", "x5y", "z6a", "b7c", "d8e", "f9g", "h0i",
    "j1k", "l2m", "n3o", "p4q", "r5s", "t6u", "v7w", "x8y", "z9a", "m1n",
    "k2l", "j3h", "h4g", "g5f", "f6d", "d7s", "s8a", "a9b", "b0c", "c1d",
    
    # 4-character alphanumeric combinations (New batch)
    "a1b2", "c3d4", "e5f6", "g7h8", "i9j0", "k1l2", "m3n4", "o5p6", "q7r8", "s9t0",
    "u1v2", "w3x4", "y5z6", "a7b8", "c9d0", "e1f2", "g3h4", "i5j6", "k7l8", "m9n0",
    "ab12", "cd34", "ef56", "gh78", "ij90", "kl12", "mn34", "op56", "qr78", "st90",
    "wx12", "yz34", "ba56", "dc78", "fe90", "hg12", "ji34", "lk56", "nm78", "po90",
    "1a2b", "3c4d", "5e6f", "7g8h", "9i0j", "2k1l", "4m3n", "6o5p", "8q7r", "0s9t",
    
    # Complex underscore and letter mixes
    "a_b1", "c_d2", "e_f3", "g_h4", "i_j5", "k_l6", "m_n7", "o_p8", "q_r9", "s_t0",
    "1_ab", "2_cd", "3_ef", "4_gh", "5_ij", "6_kl", "7_mn", "8_op", "9_qr", "0_st",
    "x_12", "y_34", "z_56", "a_78", "b_90", "c_21", "d_43", "e_65", "f_87", "g_09",
    "h_98", "i_76", "j_54", "k_32", "l_10", "m_24", "n_36", "o_48", "p_50", "q_62",
    
    # Extra short unique variations
    "x9_1", "z7_2", "k3_3", "v2_4", "j5_5", "p8_6", "d4_7", "h6_8", "f1_9", "m9_0",
    "1_9x", "2_7k", "3_3m", "4_2w", "5_5j", "6_8p", "7_4d", "8_6h", "9_1f", "0_9m",
    "ax_91", "sw_72", "dc_33", "fv_24", "gb_55", "hn_86", "jm_47", "kl_68", "lp_19", "qz_90",
    "9x_1a", "7k_2c", "3m_3e", "5f_4g", "8z_5i", "4l_6k", "2h_7m", "6p_8o", "1n_9q", "0c_0s",
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
