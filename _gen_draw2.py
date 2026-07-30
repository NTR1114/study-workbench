# -*- coding: utf-8 -*-
# 生成绘画学院：7 门专业课程（素描/人物/服装/建筑/动物/风景/色彩原创）
# 每门 8 章，每章含专业 SVG 教学图解 + 案例 + 4 练习 + B站视频
import json, urllib.parse

def url(kw):
    return "https://search.bilibili.com/all?keyword=" + urllib.parse.quote(kw)

# ---------- SVG 图解库 ----------
def svg(viewbox, inner, cls="dv-svg"):
    return '<svg class="%s" viewBox="%s" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (cls, viewbox, inner)

# 铅笔硬度条
def s_pencil():
    bars = [("HB","#9e9e9e"),("2B","#6d6d6d"),("4B","#4a4a4a"),("6B","#2b2b2b"),("8B","#141414")]
    g = ""
    for i,(t,c) in enumerate(bars):
        x = 10 + i*48
        g += '<rect x="%d" y="40" width="38" height="70" rx="5" fill="%s"/>' % (x,c)
        g += '<text x="%d" y="125" font-size="13" text-anchor="middle" fill="#555">%s</text>' % (x+19,t)
        g += '<text x="%d" y="30" font-size="11" text-anchor="middle" fill="#888">%s</text>' % (x+19,["硬·浅","","","","软·深"][i])
    return svg("0 0 250 140", g + '<text x="125" y="142" font-size="11" text-anchor="middle" fill="#999">硬度↑ 黑度↓：B 越多越软越黑</text>')

# 人体头身比例
def s_figure(heads=8, gender='m'):
    w = 230; h = 380
    lines = ""
    for i in range(1, heads+1):
        y = 40 + (340/heads)*i
        lines += '<line x1="20" y1="%.1f" x2="180" y2="%.1f" stroke="#e2e6ee"/>' % (y,y)
        lines += '<text x="186" y="%.1f" font-size="11" fill="#aaa">%d头</text>' % (y+3,i)
    # 简化人形
    cx = 100
    if gender=='m':
        torso = '<path d="M84 80 L116 80 L122 200 L78 200 Z" fill="#bcdffb" stroke="#7fb8da"/>'
        hips = '<path d="M80 200 L120 200 L114 250 L86 250 Z" fill="#ffd9b0" stroke="#caa472"/>'
    else:
        torso = '<path d="M86 80 L114 80 L110 200 L90 200 Z" fill="#fbcfe8" stroke="#e08bbf"/>'
        hips = '<path d="M80 200 L120 200 L126 252 L74 252 Z" fill="#ffd9b0" stroke="#caa472"/>'
    body = '<circle cx="%d" cy="58" r="18" fill="#ffd9b0" stroke="#caa472"/>' % cx
    body += torso + hips
    body += '<rect x="86" y="252" width="12" height="78" rx="6" fill="#ffd9b0" stroke="#caa472"/><rect x="102" y="252" width="12" height="78" rx="6" fill="#ffd9b0" stroke="#caa472"/>'
    body += '<rect x="74" y="252" width="44" height="13" rx="6" fill="#90caf9" stroke="#5b9bd5"/>'
    return svg("0 0 260 %d"%(h), lines + body + '<text x="20" y="18" font-size="12" fill="#888">%d 头身 · %s</text>'%(heads,{'m':'男性(肩宽胯窄)','f':'女性(肩窄胯宽)'}.get(gender,'标准')))

# 头部的三庭五眼
def s_head():
    g = '<ellipse cx="130" cy="100" rx="66" ry="88" fill="#fff3e6" stroke="#caa472"/>'
    g += '<line x1="64" y1="55" x2="196" y2="55" stroke="#e0567a" stroke-dasharray="3 3"/>'
    g += '<line x1="64" y1="100" x2="196" y2="100" stroke="#e0567a" stroke-dasharray="3 3"/>'
    g += '<line x1="64" y1="148" x2="196" y2="148" stroke="#e0567a" stroke-dasharray="3 3"/>'
    for x in (64,99,130,161,196):
        g += '<line x1="%d" y1="14" x2="%d" y2="186" stroke="#2f7fd0" stroke-dasharray="2 3"/>'%(x,x)
    g += '<text x="204" y="58" font-size="11" fill="#c0392b">三庭</text><text x="204" y="103" font-size="11" fill="#c0392b">三庭</text><text x="204" y="151" font-size="11" fill="#c0392b">三庭</text>'
    g += '<text x="6" y="12" font-size="11" fill="#1565c0">五眼</text>'
    return svg("0 0 260 200", g)

# 眼睛构造
def s_eye():
    g = '<path d="M18 60 Q100 12 182 60 Q100 108 18 60 Z" fill="#fff" stroke="#333" stroke-width="2"/>'
    g += '<circle cx="100" cy="60" r="30" fill="#4a90d9"/><circle cx="100" cy="60" r="13" fill="#222"/><circle cx="92" cy="52" r="4" fill="#fff"/>'
    g += '<path d="M30 42 Q100 6 170 42" fill="none" stroke="#7a5230" stroke-width="3"/>'
    g += '<path d="M30 80 Q100 110 170 80" fill="none" stroke="#9c6b4a" stroke-width="2"/>'
    g += '<text x="6" y="120" font-size="11" fill="#888">上眼睑(眉)→ 眼球 → 瞳孔 → 高光点</text>'
    return svg("0 0 200 130", g)

# 手部构造
def s_hand():
    g = '<rect x="62" y="92" width="78" height="86" rx="14" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<rect x="64" y="32" width="16" height="68" rx="8" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<rect x="84" y="20" width="16" height="80" rx="8" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<rect x="104" y="28" width="16" height="72" rx="8" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<rect x="124" y="44" width="15" height="56" rx="8" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<rect x="40" y="104" width="18" height="54" rx="9" fill="#ffe0bd" stroke="#caa472" transform="rotate(-35 49 131)"/>'
    g += '<line x1="101" y1="92" x2="101" y2="178" stroke="#e0b48a" stroke-dasharray="3 3"/>'
    g += '<text x="6" y="186" font-size="11" fill="#888">先画「手套」大块，再分五指（中指最长）</text>'
    return svg("0 0 200 196", g)

# 足构造
def s_foot():
    g = '<path d="M40 150 Q40 90 110 90 L160 90 Q180 90 180 110 L178 140 Q176 160 150 160 L60 160 Q40 160 40 150 Z" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<rect x="46" y="158" width="22" height="16" rx="6" fill="#ffd0a8" stroke="#caa472"/><rect x="70" y="160" width="18" height="15" rx="5" fill="#ffd0a8" stroke="#caa472"/><rect x="90" y="160" width="18" height="14" rx="5" fill="#ffd0a8" stroke="#caa472"/><rect x="110" y="158" width="20" height="14" rx="5" fill="#ffd0a8" stroke="#caa472"/><rect x="132" y="154" width="22" height="14" rx="5" fill="#ffd0a8" stroke="#caa472"/>'
    g += '<text x="6" y="190" font-size="11" fill="#888">脚≈楔形块+脚趾；大脚趾粗短</text>'
    return svg("0 0 210 198", g)

# 体块骨架
def s_mannequin():
    g = '<circle cx="100" cy="36" r="16" fill="#ffd9b0" stroke="#caa472"/>'
    g += '<line x1="100" y1="52" x2="100" y2="150" stroke="#444" stroke-width="3"/>'
    g += '<path d="M70 70 L130 70 L138 150 L62 150 Z" fill="#cdeffd" stroke="#7fb8da" stroke-width="2"/>'
    g += '<path d="M74 150 L126 150 L120 200 L80 200 Z" fill="#d9c2f0" stroke="#9b7bcf" stroke-width="2"/>'
    g += '<line x1="62" y1="150" x2="34" y2="240" stroke="#444" stroke-width="3"/><line x1="138" y1="150" x2="166" y2="240" stroke="#444" stroke-width="3"/>'
    g += '<line x1="88" y1="72" x2="40" y2="120" stroke="#444" stroke-width="3"/><line x1="112" y1="72" x2="160" y2="120" stroke="#444" stroke-width="3"/>'
    g += '<text x="6" y="262" font-size="11" fill="#888">头(球) → 脊柱 → 胸腔块 → 骨盆块 → 四肢</text>'
    return svg("0 0 200 270", g)

# 肌肉躯干
def s_muscle():
    g = '<path d="M70 50 Q100 40 130 50 L132 120 Q100 132 68 120 Z" fill="#e8a87a" stroke="#b56b3a"/>'
    g += '<path d="M74 56 Q100 64 126 56" fill="none" stroke="#b56b3a" stroke-width="2"/>'
    g += '<path d="M76 120 Q100 134 124 120 L120 170 Q100 180 80 170 Z" fill="#e8a87a" stroke="#b56b3a"/>'
    g += '<path d="M82 70 L82 118" stroke="#b56b3a" stroke-width="2"/><path d="M100 66 L100 126" stroke="#b56b3a" stroke-width="2"/><path d="M118 70 L118 118" stroke="#b56b3a" stroke-width="2"/>'
    g += '<text x="6" y="195" font-size="11" fill="#888">胸大肌 · 腹直肌 · 前锯肌；线条随体积走</text>'
    return svg("0 0 200 205", g)

# 动作线
def s_gesture():
    g = '<path d="M40 182 Q110 70 180 44" fill="none" stroke="#e0567a" stroke-width="2" stroke-dasharray="6 4"/>'
    g += '<circle cx="150" cy="52" r="11" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<line x1="150" y1="63" x2="122" y2="112" stroke="#666" stroke-width="3"/><line x1="122" y1="112" x2="96" y2="176" stroke="#666" stroke-width="3"/><line x1="122" y1="112" x2="150" y2="176" stroke="#666" stroke-width="3"/>'
    g += '<line x1="135" y1="82" x2="176" y2="72" stroke="#666" stroke-width="3"/><line x1="135" y1="82" x2="102" y2="66" stroke="#666" stroke-width="3"/>'
    g += '<text x="6" y="198" font-size="11" fill="#888">红色虚线 = 动作线(C/S形)，决定动势</text>'
    return svg("0 0 220 204", g)

# 衣褶类型
def s_drapery():
    g = ""
    # 管状褶
    g += '<path d="M20 20 Q40 60 20 100 Q40 140 20 180" fill="none" stroke="#7a5230" stroke-width="3"/>'
    g += '<path d="M40 20 Q60 60 40 100 Q60 140 40 180" fill="none" stroke="#7a5230" stroke-width="3"/>'
    g += '<text x="20" y="196" font-size="10" fill="#888">管状(垂坠)</text>'
    # 之字褶
    g += '<path d="M90 20 L110 60 L90 100 L110 140 L90 180" fill="none" stroke="#7a5230" stroke-width="3"/>'
    g += '<text x="84" y="196" font-size="10" fill="#888">之字(弯折)</text>'
    # 螺旋褶
    g += '<path d="M150 20 Q190 50 160 90 Q130 130 175 180" fill="none" stroke="#7a5230" stroke-width="3"/>'
    g += '<path d="M165 20 Q205 50 175 90 Q145 130 190 180" fill="none" stroke="#7a5230" stroke-width="3"/>'
    g += '<text x="150" y="196" font-size="10" fill="#888">螺旋(扭绞)</text>'
    return svg("0 0 250 205", g)

# 五大调球体
def s_value():
    g = '<circle cx="100" cy="100" r="76" fill="#bbb"/>'
    g += '<path d="M100 24 A76 76 0 0 1 100 176 Z" fill="#777"/>'
    g += '<ellipse cx="78" cy="70" rx="22" ry="16" fill="#eee"/>'  # 高光
    g += '<path d="M100 176 A76 76 0 0 0 150 130 Q120 160 100 176 Z" fill="#ddd"/>'  # 反光
    g += '<path d="M100 176 A76 76 0 0 1 150 130" fill="none" stroke="#555" stroke-width="3"/>'  # 明暗交界线
    labels = [("高光","70,52"),("亮部","40,110"),("明暗交界线","150,128"),("反光","120,168"),("投影","170,150")]
    for t,xy in labels:
        x,y = (int(v) for v in xy.split(","))
        g += '<text x="%d" y="%d" font-size="10" fill="#333">%s</text>'%(x,y,t)
    return svg("0 0 200 200", g)

# 一点透视房间
def s_p1():
    g = '<rect x="20" y="20" width="200" height="160" fill="#fafafa" stroke="#333"/>'
    g += '<circle cx="120" cy="95" r="3" fill="#e0567a"/>'  # VP
    for x in (60,100,160,200):
        g += '<line x1="%d" y1="20" x2="120" y2="95" stroke="#bbb"/>'%(x,)
        g += '<line x1="%d" y1="180" x2="120" y2="95" stroke="#bbb"/>'%(x,)
    g += '<line x1="20" y1="95" x2="220" y2="95" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<text x="20" y="195" font-size="11" fill="#888">所有平行线→同一灭点(红)</text>'
    return svg("0 0 240 205", g)

# 两点透视建筑
def s_p2():
    g = '<rect x="20" y="20" width="220" height="170" fill="#fafafa" stroke="#333"/>'
    g += '<circle cx="30" cy="180" r="3" fill="#e0567a"/><circle cx="220" cy="180" r="3" fill="#e0567a"/>'
    # 建筑体
    g += '<path d="M95 60 L150 50 L150 150 L95 160 Z" fill="#cdeffd" stroke="#333"/>'
    g += '<path d="M150 50 L205 60 L205 150 L150 150 Z" fill="#a9d8f5" stroke="#333"/>'
    g += '<path d="M95 60 L150 50 L205 60 L150 70 Z" fill="#e7f4ff" stroke="#333"/>'
    g += '<line x1="95" y1="60" x2="30" y2="180" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<line x1="150" y1="70" x2="30" y2="180" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<line x1="150" y1="50" x2="220" y2="180" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<line x1="205" y1="60" x2="220" y2="180" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<text x="20" y="200" font-size="11" fill="#888">两灭点(红)，竖线保持垂直</text>'
    return svg("0 0 240 210", g)

# 三点透视
def s_p3():
    g = '<rect x="20" y="20" width="220" height="170" fill="#fafafa" stroke="#333"/>'
    g += '<circle cx="30" cy="185" r="3" fill="#e0567a"/><circle cx="225" cy="185" r="3" fill="#e0567a"/><circle cx="125" cy="10" r="3" fill="#e0567a"/>'
    g += '<path d="M95 70 L150 62 L150 140 L95 148 Z" fill="#cdeffd" stroke="#333"/>'
    g += '<path d="M150 62 L200 72 L200 140 L150 140 Z" fill="#a9d8f5" stroke="#333"/>'
    g += '<path d="M95 70 L150 62 L200 72 L150 80 Z" fill="#e7f4ff" stroke="#333"/>'
    g += '<line x1="150" y1="80" x2="125" y2="10" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<line x1="95" y1="70" x2="30" y2="185" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<line x1="200" y1="72" x2="225" y2="185" stroke="#e0567a" stroke-dasharray="4 3"/>'
    g += '<text x="20" y="200" font-size="11" fill="#888">三灭点：仰视/鸟瞰，竖线也消失</text>'
    return svg("0 0 240 210", g)

# 平面图
def s_plan():
    g = '<rect x="20" y="20" width="200" height="160" fill="#fff" stroke="#333"/>'
    g += '<rect x="20" y="20" width="120" height="90" fill="none" stroke="#333"/><rect x="140" y="20" width="80" height="60" fill="none" stroke="#333"/>'
    g += '<rect x="20" y="110" width="80" height="70" fill="none" stroke="#333"/><rect x="100" y="110" width="120" height="70" fill="none" stroke="#333"/>'
    g += '<path d="M140 50 A14 14 0 0 1 154 64" fill="none" stroke="#888" stroke-dasharray="3 2"/>'
    g += '<text x="55" y="70" font-size="11" fill="#888">客厅</text><text x="165" y="55" font-size="10" fill="#888">卧</text><text x="50" y="150" font-size="10" fill="#888">厨</text><text x="150" y="150" font-size="10" fill="#888">卫</text>'
    g += '<text x="20" y="195" font-size="11" fill="#888">平面：俯视隔墙；门弧线表开向</text>'
    return svg("0 0 240 205", g)

# 立面图
def s_elev():
    g = '<rect x="40" y="30" width="160" height="150" fill="#fff" stroke="#333"/>'
    for i in range(3):
        y = 55 + i*40
        g += '<line x1="40" y1="%d" x2="200" y2="%d" stroke="#bbb"/>'%(y,y)
    for r in range(4):
        x = 60 + r*40
        g += '<rect x="%d" y="60" width="24" height="30" fill="#cdeffd" stroke="#333"/><rect x="%d" y="110" width="24" height="30" fill="#cdeffd" stroke="#333"/>'%(x,x)
    g += '<line x1="20" y1="180" x2="220" y2="180" stroke="#333" stroke-width="3"/>'
    g += '<text x="20" y="198" font-size="11" fill="#888">立面：正视图，窗/门按真实尺寸</text>'
    return svg("0 0 240 210", g)

# 时装人体 9 头
def s_croquis():
    cx = 100
    g = '<line x1="20" y1="40" x2="180" y2="40" stroke="#eee"/>'
    for i in range(1,10):
        y = 40 + (340/9)*i
        g += '<line x1="20" y1="%.1f" x2="180" y2="%.1f" stroke="#eee"/>'%(y,y)
        g += '<text x="186" y="%.1f" font-size="10" fill="#bbb">%d</text>'%(y+3,i)
    g += '<circle cx="%d" cy="56" r="13" fill="#ffe0bd" stroke="#caa472"/>'%(cx,)
    g += '<path d="M88 70 L112 70 L116 175 L84 175 Z" fill="#f3c6dd" stroke="#d98cb8"/>'
    g += '<path d="M84 175 L116 175 L122 235 L78 235 Z" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<rect x="90" y="235" width="9" height="95" rx="4" fill="#ffe0bd" stroke="#caa472"/><rect x="101" y="235" width="9" height="95" rx="4" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<path d="M84 80 L55 120" stroke="#666" stroke-width="4"/><path d="M116 80 L145 120" stroke="#666" stroke-width="4"/>'
    g += '<text x="20" y="18" font-size="11" fill="#888">9 头身时装比例：颈长、肩窄、腿占近半</text>'
    return svg("0 0 240 390", g)

# 款式图（T恤平面）
def s_flat():
    g = '<path d="M70 50 L100 38 L130 50 L150 70 L135 85 L128 75 L128 170 L72 170 L72 75 L65 85 L50 70 Z" fill="#fff" stroke="#333" stroke-width="2"/>'
    g += '<line x1="72" y1="75" x2="128" y2="75" stroke="#333" stroke-dasharray="3 3"/>'
    g += '<text x="100" y="195" font-size="11" text-anchor="middle" fill="#888">款式图(Technical Flat)：平铺、对称、无透视</text>'
    return svg("0 0 200 205", g)

# 面料质感
def s_textile():
    g = '<rect x="10" y="20" width="60" height="60" rx="6" fill="#e0e0e0"/>'
    for i in range(6):
        for j in range(6):
            g += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#9e9e9e" stroke-width="1"/>'%(16+i*9,26+j*9,16+i*9,35+j*9)
    g += '<text x="40" y="96" font-size="10" text-anchor="middle" fill="#666">针织纹</text>'
    g += '<rect x="82" y="20" width="60" height="60" rx="6" fill="#3e2723"/>'
    g += '<path d="M90 30 Q110 50 130 30 M90 50 Q110 70 130 50 M90 70 Q110 90 130 70" stroke="#6d4030" fill="none" stroke-width="2"/>'
    g += '<text x="112" y="96" font-size="10" text-anchor="middle" fill="#666">皮革</text>'
    g += '<rect x="154" y="20" width="60" height="60" rx="6" fill="#fce4ec"/>'
    g += '<path d="M160 40 Q180 30 200 40 M160 55 Q180 45 200 55 M160 70 Q180 60 200 70" stroke="#f48fb1" fill="none" stroke-width="1.5" opacity="0.8"/>'
    g += '<text x="184" y="96" font-size="10" text-anchor="middle" fill="#666">薄纱</text>'
    g += '<text x="110" y="118" font-size="11" text-anchor="middle" fill="#999">用排线/笔触/透明度区分材质</text>'
    return svg("0 0 224 122", g)

# 色环
def s_wheel(n=12):
    import colorsys
    g = '<circle cx="100" cy="100" r="36" fill="#fff" stroke="#ccc"/><text x="100" y="104" font-size="11" text-anchor="middle" fill="#666">色环</text>'
    for i in range(n):
        ang = 2*3.14159*i/n - 3.14159/2
        x = 100 + 64*__import__('math').cos(ang); y = 100 + 64*__import__('math').sin(ang)
        r,g_,b = colorsys.hsv_to_rgb(i/n,0.65,0.85)
        col = "#%02x%02x%02x"%(int(r*255),int(g_*255),int(b*255))
        g += '<circle cx="%.1f" cy="%.1f" r="15" fill="%s"/>'%(x,y,col)
    return svg("0 0 200 200", g)

# 配色方案
def s_schemes():
    sw = lambda x,y,c: '<rect x="%d" y="%d" width="40" height="24" rx="5" fill="%s"/>'%(x,y,c)
    g = '<text x="6" y="22" font-size="11" fill="#555">单色</text>'+sw(56,8,"#1565c0")+sw(104,8,"#1e88e5")+sw(152,8,"#42a5f5")+sw(200,8,"#90caf9")
    g += '<text x="6" y="56" font-size="11" fill="#555">邻近</text>'+sw(56,42,"#1e88e5")+sw(104,42,"#42a5f5")+sw(152,42,"#4dd0e1")+sw(200,42,"#26c6da")
    g += '<text x="6" y="90" font-size="11" fill="#555">互补</text>'+sw(56,76,"#fb8c00")+sw(104,76,"#ffb74d")+sw(152,76,"#1565c0")+sw(200,76,"#42a5f5")
    g += '<text x="6" y="124" font-size="11" fill="#555">三角</text>'+sw(56,110,"#e53935")+sw(104,110,"#fdd835")+sw(152,110,"#1e88e5")+sw(200,110,"#90caf9")
    g += '<text x="6" y="158" font-size="11" fill="#999">60-30-10：主60% 辅30% 点缀10%</text>'
    return svg("0 0 256 168", g)

# 明度阶
def s_value_scale():
    g = ""
    for i in range(9):
        v = 255 - i*28
        g += '<rect x="%d" y="30" width="24" height="80" fill="rgb(%d,%d,%d)"/>'%(10+i*25,v,v,v)
    g += '<text x="6" y="130" font-size="11" fill="#888">明度阶：左亮→右暗，控制画面节奏</text>'
    return svg("0 0 235 140", g)

# 树构造
def s_tree():
    g = '<path d="M92 190 L92 120" stroke="#7a5230" stroke-width="10"/>'
    g += '<path d="M92 150 L70 130 M92 160 L114 140" stroke="#7a5230" stroke-width="5"/>'
    g += '<circle cx="92" cy="80" r="42" fill="#7cb342"/><circle cx="58" cy="100" r="30" fill="#8bc34a"/><circle cx="126" cy="100" r="30" fill="#689f38"/>'
    g += '<text x="6" y="200" font-size="11" fill="#888">树干定势 → 三团叶块塑体积</text>'
    return svg("0 0 190 210", g)

# 山峦层次
def s_mountain():
    g = '<rect x="0" y="120" width="240" height="80" fill="#e3f2fd"/>'
    g += '<path d="M0 160 L60 90 L120 150 L180 80 L240 150 L240 200 L0 200 Z" fill="#90a4ae" opacity="0.5"/>'
    g += '<path d="M0 175 L50 120 L110 165 L170 115 L240 170 L240 200 L0 200 Z" fill="#546e7a" opacity="0.7"/>'
    g += '<path d="M0 190 L40 155 L100 185 L160 150 L240 188 L240 200 L0 200 Z" fill="#37474f"/>'
    g += '<text x="6" y="18" font-size="11" fill="#888">远山淡(大气透视) → 近山浓</text>'
    return svg("0 0 240 205", g)

# 静物
def s_still():
    g = '<ellipse cx="80" cy="170" rx="40" ry="10" fill="#000" opacity="0.12"/><ellipse cx="160" cy="175" rx="30" ry="8" fill="#000" opacity="0.12"/>'
    g += '<rect x="60" y="90" width="40" height="80" rx="6" fill="#cfd8dc" stroke="#90a4ae"/>'
    g += '<path d="M60 90 Q80 70 100 90 Z" fill="#b0bec5" stroke="#90a4ae"/>'
    g += '<circle cx="160" cy="130" r="32" fill="#ffcc80" stroke="#ef9a4d"/>'
    g += '<rect x="125" y="150" width="70" height="25" rx="3" fill="#a1887f" stroke="#795548"/>'
    g += '<text x="6" y="200" font-size="11" fill="#888">组合练习：瓶+球+盒，练比例与光影</text>'
    return svg("0 0 220 210", g)

# 光影球（时间）
def s_light_time():
    g = '<circle cx="80" cy="100" r="60" fill="#ffe082"/>'
    g += '<path d="M80 40 A60 60 0 0 1 80 160 Z" fill="#ffb300" opacity="0.5"/>'
    g += '<ellipse cx="60" cy="78" rx="16" ry="11" fill="#fff" opacity="0.8"/>'
    g += '<circle cx="175" cy="100" r="60" fill="#5c6bc0"/>'
    g += '<path d="M175 40 A60 60 0 0 0 175 160 Z" fill="#3949ab" opacity="0.6"/>'
    g += '<text x="20" y="195" font-size="11" fill="#888">暖光(晨/昏) ←→ 冷光(正午/夜)</text>'
    return svg("0 0 260 205", g)

# 动物骨架（四足）
def s_quadskeleton():
    g = '<ellipse cx="100" cy="90" rx="60" ry="34" fill="#fff" stroke="#333"/>'
    g += '<circle cx="180" cy="70" r="18" fill="#fff" stroke="#333"/>'
    g += '<line x1="180" y1="70" x2="200" y2="60" stroke="#333"/><line x1="195" y1="70" x2="210" y2="82" stroke="#333"/><line x1="178" y1="58" x2="188" y2="50" stroke="#333"/><line x1="178" y1="82" x2="190" y2="90" stroke="#333"/>'
    g += '<line x1="100" y1="120" x2="60" y2="180" stroke="#333" stroke-width="3"/><line x1="100" y1="120" x2="100" y2="180" stroke="#333" stroke-width="3"/><line x1="120" y1="120" x2="150" y2="180" stroke="#333" stroke-width="3"/><line x1="120" y1="120" x2="180" y2="170" stroke="#333" stroke-width="3"/>'
    g += '<text x="6" y="200" font-size="11" fill="#888">脊柱(筒)→ 四肢(柱)；前肩/后臀两段</text>'
    return svg("0 0 220 210", g)

# 猫狗构造
def s_catdog():
    g = '<ellipse cx="100" cy="100" rx="55" ry="30" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<circle cx="160" cy="78" r="20" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<path d="M148 62 L142 44 L156 58 Z" fill="#ffe0bd" stroke="#caa472"/><path d="M172 62 L180 44 L166 58 Z" fill="#ffe0bd" stroke="#caa472"/>'
    g += '<line x1="60" y1="120" x2="45" y2="165" stroke="#caa472" stroke-width="4"/><line x1="80" y1="122" x2="78" y2="168" stroke="#caa472" stroke-width="4"/><line x1="120" y1="122" x2="125" y2="168" stroke="#caa472" stroke-width="4"/><line x1="140" y1="120" x2="152" y2="165" stroke="#caa472" stroke-width="4"/>'
    g += '<path d="M160 58 Q200 60 205 95" fill="none" stroke="#caa472" stroke-width="3"/>'
    g += '<text x="6" y="195" font-size="11" fill="#888">先用「香肠团」定大形，再加耳/尾</text>'
    return svg("0 0 220 205", g)

# 马比例
def s_horse():
    g = '<rect x="20" y="60" width="200" height="70" rx="14" fill="#e0c0a0" stroke="#a07850"/>'
    g += '<rect x="20" y="100" width="200" height="6" fill="#a07850" opacity="0.4"/>'
    g += '<circle cx="210" cy="78" r="22" fill="#e0c0a0" stroke="#a07850"/>'
    g += '<line x1="60" y1="130" x2="55" y2="180" stroke="#a07850" stroke-width="5"/><line x1="90" y1="130" x2="95" y2="180" stroke="#a07850" stroke-width="5"/><line x1="150" y1="130" x2="145" y2="180" stroke="#a07850" stroke-width="5"/><line x1="180" y1="130" x2="190" y2="180" stroke="#a07850" stroke-width="5"/>'
    g += '<line x1="20" y1="95" x2="20" y2="127" stroke="#d32f2f" stroke-width="2" stroke-dasharray="3 2"/><line x1="120" y1="60" x2="120" y2="130" stroke="#d32f2f" stroke-width="2" stroke-dasharray="3 2"/>'
    g += '<text x="6" y="200" font-size="11" fill="#888">身长≈头长×2.5；肩/臀为两大块</text>'
    return svg("0 0 240 210", g)

# 鸟构造
def s_bird():
    g = '<ellipse cx="110" cy="110" rx="55" ry="38" fill="#fff" stroke="#333"/>'
    g += '<circle cx="60" cy="95" r="18" fill="#fff" stroke="#333"/>'
    g += '<path d="M42 95 L26 90 L42 100 Z" fill="#f9a825" stroke="#333"/>'
    g += '<path d="M110 72 Q170 50 200 80 Q160 95 110 95 Z" fill="#fff" stroke="#333"/>'
    g += '<path d="M80 145 Q110 165 145 145" fill="none" stroke="#333" stroke-width="2"/>'
    g += '<text x="6" y="200" font-size="11" fill="#888">鸟=两枚蛋(身+头)+楔形翼；轻量流线</text>'
    return svg("0 0 220 210", g)

# 皮毛笔触
def s_fur():
    g = ""
    for i in range(8):
        y = 30 + i*18
        g += '<path d="M20 %d q20 -8 40 0 q20 8 40 0" fill="none" stroke="#8d6e63" stroke-width="2"/>'%(y,)
    g += '<text x="6" y="12" font-size="11" fill="#888">短毛：顺生长方向排短弧线</text>'
    g += '<text x="120" y="200" font-size="11" fill="#888">羽毛：叠瓦状分层</text>'
    for i in range(6):
        y = 150 + i*8
        g += '<path d="M140 %d l50 -6" stroke="#5c6bc0" stroke-width="2"/>'%(y,)
    return svg("0 0 220 210", g)

# 三分构图
def s_thirds():
    g = '<rect x="20" y="20" width="200" height="150" fill="#f0f4f8" stroke="#333"/>'
    for x in (87,153):
        g += '<line x1="%d" y1="20" x2="%d" y2="170" stroke="#e0567a" stroke-dasharray="4 3"/>'%(x,x)
    for y in (75,125):
        g += '<line x1="20" y1="%d" x2="220" y2="%d" stroke="#e0567a" stroke-dasharray="4 3"/>'%(y,y)
    for (x,y) in [(87,75),(153,75),(87,125),(153,125)]:
        g += '<circle cx="%d" cy="%d" r="5" fill="#e0567a"/>'%(x,y)
    g += '<rect x="40" y="120" width="34" height="40" fill="#42a5f5"/>'
    g += '<text x="120" y="195" font-size="11" fill="#888">主体放交叉点(红)最舒服</text>'
    return svg("0 0 240 205", g)

# 灵感板
def s_mood():
    cols = ["#e57373","#ffb74d","#fff176","#81c784","#64b5f6","#ba68c8"]
    g = ""
    for i in range(6):
        x = 10 + (i%3)*72; y = 10 + (i//3)*70
        g += '<rect x="%d" y="%d" width="62" height="58" rx="4" fill="%s"/>'%(x,y,cols[i])
    g += '<text x="6" y="160" font-size="11" fill="#888">灵感板：汇集色彩/图片/情绪，定调性</text>'
    return svg("0 0 236 170", g)

# 工作流
def s_workflow():
    steps = ["缩略图","线稿","铺色","光影","细化","成稿"]
    g = ""
    for i,s in enumerate(steps):
        x = 8 + i*38
        g += '<rect x="%d" y="40" width="32" height="40" rx="6" fill="#e3f2fd" stroke="#1976d2"/>'%(x,)
        g += '<text x="%d" y="63" font-size="9" text-anchor="middle" fill="#1565c0">%s</text>'%(x+16,s)
        if i<5: g += '<path d="M%d 60 L%d 60" stroke="#1976d2" stroke-width="2" marker-end="url(#ar)"/>'%(x+32,x+38)
    g += '<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="#1976d2"/></marker></defs>'
    g += '<text x="6" y="105" font-size="11" fill="#888">从草图到成稿的迭代工作流</text>'
    return svg("0 0 248 115", g)

# 负空间
def s_negative():
    g = '<path d="M40 160 Q60 60 100 50 Q140 60 160 160 Z" fill="#fff" stroke="#333"/>'
    g += '<path d="M70 160 Q85 90 100 85 Q115 90 130 160 Z" fill="#333"/>'
    g += '<text x="6" y="190" font-size="11" fill="#888">看「空隙(黑)」的形状，更容易抓准轮廓</text>'
    return svg("0 0 200 200", g)

# 作品集
def s_portfolio():
    g = '<rect x="20" y="30" width="55" height="75" rx="3" fill="#fff" stroke="#333"/><rect x="90" y="20" width="55" height="85" rx="3" fill="#fff" stroke="#333"/><rect x="160" y="35" width="55" height="70" rx="3" fill="#fff" stroke="#333"/>'
    g += '<path d="M30 95 L65 60 M30 60 L65 95" stroke="#bbb"/><rect x="100" y="40" width="35" height="20" fill="#ffcc80"/><circle cx="188" cy="70" r="14" fill="#90caf9"/>'
    g += '<text x="6" y="130" font-size="11" fill="#888">作品集：精选 12-20 张，体现完整能力</text>'
    return svg("0 0 230 140", g)

# 字体工具小图：服装 T 台 pose
def s_pose():
    cx = 100
    g='<circle cx="%d" cy="34" r="10" fill="#ffe0bd" stroke="#caa472"/>'%(cx,)
    g+='<line x1="100" y1="44" x2="100" y2="110" stroke="#666" stroke-width="3"/>'
    g+='<path d="M100 60 Q130 70 140 110" fill="none" stroke="#666" stroke-width="3"/><path d="M100 60 Q70 78 64 120" fill="none" stroke="#666" stroke-width="3"/>'
    g+='<line x1="100" y1="110" x2="78" y2="175" stroke="#666" stroke-width="3"/><line x1="100" y1="110" x2="124" y2="175" stroke="#666" stroke-width="3"/>'
    g+='<text x="6" y="195" font-size="11" fill="#888">时装站姿：一腿承重、胯偏移、肩微倾</text>'
    return svg("0 0 200 205", g)

S = dict(pencil=s_pencil, figure=s_figure, head=s_head, eye=s_eye, hand=s_hand, foot=s_foot,
         mannequin=s_mannequin, muscle=s_muscle, gesture=s_gesture, drapery=s_drapery, value=s_value,
         p1=s_p1, p2=s_p2, p3=s_p3, plan=s_plan, elev=s_elev, croquis=s_croquis, flat=s_flat,
         textile=s_textile, wheel=s_wheel, schemes=s_schemes, vscale=s_value_scale, tree=s_tree,
         mountain=s_mountain, still=s_still, light=s_light_time, quadskeleton=s_quadskeleton,
         catdog=s_catdog, horse=s_horse, bird=s_bird, fur=s_fur, thirds=s_thirds, mood=s_mood,
         workflow=s_workflow, negative=s_negative, portfolio=s_portfolio, pose=s_pose)

# ---------- 内容组装工具 ----------
def sec(h, b):
    return {"h": h, "b": b}
def case(t, b):
    return {"title": t, "b": b}
def pq(q, opts, ans, explain):
    return {"q": q, "options": opts, "answer": ans, "explain": explain}
def vid(t, kw):
    return {"title": t, "platform": "哔哩哔哩", "url": url(kw)}

COURSES = []

def add_course(cid, name, emoji, color, intro, chapters):
    COURSES.append({
        "id": cid, "name": name, "emoji": emoji, "color": color,
        "intro": intro,
        "syllabus": [c["title"] for c in chapters],
        "chapters": chapters
    })

def ch(title, lv, sections, cs, practices, v):
    return {"title": title, "lv": lv, "sections": sections, "caseStudy": cs, "practice": practices, "video": v}

# ============================================================
# 课程1：素描与造型基础
# ============================================================
c1 = []
c1.append(ch("第1章 工具与材料体系", "小白", [
    sec("1.1 铅笔的硬度系统", "<p>铅笔用<strong>H/B 标号</strong>：H 偏硬、色浅，适合打稿；B 偏软、色深，适合明暗。常用 HB/2B/4B/6B 组合即可覆盖打稿到深暗部，专业素描还会用到炭笔与色粉。</p>"+S["pencil"]()),
    sec("1.2 纸张与橡皮", "<p>纸张按<strong>纹理</strong>分：细纹纸适合钢笔/彩铅，粗纹纸适合炭笔/素描。橡皮分硬橡皮(擦净)与可塑橡皮(减淡、提亮高光)。备一本速写本，随手记录。</p>"),
    sec("1.3 削笔与执笔", "<p>长笔尖适合排线；削出楔形面可画宽窄变化的线。打稿用「写握」，排线与长线用<strong>悬腕</strong>以手臂带动，线才连贯稳定。</p>")],
    case("案例：为什么总是画不深", "<p>只用 HB 当然深不下去。深暗部要用 4B/6B 叠加，并配合可塑橡皮提反光，黑白拉得开，体积才出得来。</p>"),
    [pq("B 数越大表示？",["越硬越浅","越软越黑","越细","越短"],1,"B 越多笔芯越软、颜色越深。"),
     pq("悬腕排线的作用是？",["只画小字","线条更稳更连贯","省力","好看"],1,"手臂带动比手指动更稳。"),
     pq("可塑橡皮常用于？",["全擦掉","减淡/提亮高光","粘纸","画黑"],1,"可塑橡皮可按压减淡，做高光。"),
     pq("粗纹纸适合？",["钢笔","炭笔/素描","印章","打印"],1,"粗纹承载炭粉，附着力强。")],
    vid("素描工具 铅笔硬度 纸张 新手入门","素描工具 铅笔 纸张 新手入门")))

c1.append(ch("第2章 控笔与线条语言", "小白", [
    sec("2.1 线条的轻重", "<p>线不只是「勾边」。通过<strong>起笔轻—行笔重—收笔轻</strong>做出虚实，物体才有前后与体积。轮廓线近实远虚，结构线轻而准。</p>"),
    sec("2.2 排线塑造明暗", "<p>排线是素描的「像素」：平行线叠出灰调，交叉线加深，<strong>疏密</strong>控制深浅。保持线条方向一致、不回笔，画面才干净。</p>"),
    sec("2.3 轮廓线与结构线", "<p>轮廓线描述外边界；结构线(中线、对称线)帮助定位内部。先结构后轮廓，比例不易崩。</p>")],
    case("案例：线条抖、不连贯", "<p>多因盯笔尖、手指发紧。做「看终点、一口气画长线」练习 20 条；排线时手放松、用小臂节奏。</p>"),
    [pq("排线主要用来？",["装饰","表现明暗灰调","签名","裁纸"],1,"排线叠出不同灰度。"),
     pq("近处轮廓应？",["更虚","更实","消失","变彩色"],0,"近实远虚才有空间。"),
     pq("结构线的作用是？",["好看的边","辅助定位比例","代替明暗","上色"],1,"先结构后轮廓更稳。"),
     pq("行笔节奏建议？",["起轻行重收轻","全程一样重","越画越轻","随机"],0,"轻重变化做出虚实。")],
    vid("控笔训练 排线 线条 素描基础","控笔 排线 素描基础 线条训练")))

c1.append(ch("第3章 几何概括：万物皆可拆", "小白", [
    sec("3.1 四大基本形", "<p><strong>球、方、柱、锥</strong>是一切形体的积木。头=球，躯干=柱/方，杯=柱+椭圆，房=方。先抓基本形再上细节。</p>"),
    sec("3.2 体块组装法", "<p>把对象想成几个几何体「拼」起来：先定最大块，再叠小块。例如人物=球(头)+方(胸腔)+方(盆骨)+柱(四肢)。</p>"),
    sec("3.3 30 秒草图", "<p>限时抓大形、禁细节，训练概括力。这是画得快又准的秘密武器，每天 5 张。</p>"+S["mannequin"]())],
    case("案例：杯子画不像", "<p>直接描花纹必败。先当圆柱：中轴定对称→上下椭圆→连侧面，体积对了花纹自然贴得上。</p>"),
    [pq("四大基本形是？",["点线面体","球方柱锥","红黄蓝绿","春夏秋冬"],1,"球方柱锥可组合万物。"),
     pq("画人的简化思路？",["先画脸","球+方+柱拼块","先画鞋","先上色"],1,"几何体拼出大形。"),
     pq("30秒草图训练？",["上色","概括大形","签名","裁纸"],1,"限时抓形练概括。"),
     pq("为什么先基本形？",["偷懒","比例稳、好叠细节","不好看","规定"],1,"大形定准细节才好加。")],
    vid("几何体概括 素描 概括能力","几何体概括 素描 形体结构")))

c1.append(ch("第4章 明暗与五大调", "进阶", [
    sec("4.1 光与体积", "<p>光让平面产生体积。受光面亮、背光面暗，转折处最暗。理解光向，是画「立体」的第一步。</p>"),
    sec("4.2 五大调子", "<p><strong>高光、亮部、明暗交界线、反光、投影</strong>。其中明暗交界线(受光转背光的棱)最深，反光是环境光回弹，别画成死黑。</p>"+S["value"]()),
    sec("4.3 用排线做灰阶", "<p>由亮到暗逐层排线叠加，过渡才自然。亮部留白、暗部加密，中间调靠疏密控制。</p>")],
    case("案例：球画成饼", "<p>只分了黑白两块。补上「明暗交界线+反光+投影渐变」，球体立刻鼓起来。</p>"),
    [pq("五大调不包括？",["高光","反光","轮廓线","明暗交界线"],2,"轮廓线非调子。"),
     pq("最深的是？",["高光","亮部","明暗交界线","投影"],2,"转折棱最深。"),
     pq("反光来自？",["太阳","环境回弹光","想象","笔太软"],1,"环境光反射回来。"),
     pq("中间调靠？",["留白","排线疏密","涂黑","橡皮"],1,"疏密控制灰度。")],
    vid("素描五大调 明暗 球体光影","素描 五大调 明暗 光影")))

c1.append(ch("第5章 透视基础：一点透视", "进阶", [
    sec("5.1 灭点与地平线", "<p>平行线条向远处汇聚于<strong>灭点(VP)</strong>，所有 VP 都在地平线上。人眼高度决定地平线位置。</p>"),
    sec("5.2 一点透视", "<p>物体正面平行于画面时，纵深线全部汇向<strong>同一个 VP</strong>。适合画房间、走廊、街道。</p>"+S["p1"]()),
    sec("5.3 应用：画一个房间", "<p>先定地平线与 VP，再画近处方框，把四角连向 VP 即得地面与天花，家具按比例缩进。</p>")],
    case("案例：地板穿帮", "<p>地砖线没汇向 VP。所有纵深线必须严格交于同一灭点，否则空间错乱。</p>"),
    [pq("灭点都在？",["天上","地平线上","画面外","任意"],1,"VP 全在地平线。"),
     pq("一点透视特征？",["两个VP","一个VP","无VP","曲线VP"],1,"一点=单灭点。"),
     pq("适合画？",["人脸","房间/走廊","云","手"],1,"纵深平行场景。"),
     pq("地平线由什么定？",["天气","视点高度","笔","纸"],1,"眼高即地平线。")],
    vid("一点透视 房间 室内 素描透视","一点透视 室内 素描")))

c1.append(ch("第6章 两点与三点透视", "进阶", [
    sec("6.1 两点透视", "<p>物体转角正对画面、两组面都倾斜时，出现<strong>左右两个 VP</strong>，竖线保持垂直。常用于建筑外观、产品。</p>"+S["p2"]()),
    sec("6.2 三点透视", "<p>仰视高楼或鸟瞰城市时加<strong>第三个 VP</strong>(上或下)，竖线也向它汇聚，气势更强。</p>"+S["p3"]()),
    sec("6.3 视锥与变形", "<p>物体偏离视线中心过远会变形。把主体放在视锥(约 60°)内，透视才舒服。</p>")],
    case("案例：楼歪了", "<p>竖线也斜了就是误用三点。普通外观用两点，竖线务必垂直。</p>"),
    [pq("两点透视有？",["0 VP","1 VP","2 VP","3 VP"],2,"两灭点+垂直竖线。"),
     pq("三点透视竖线？",["垂直","也向第3 VP 汇聚","消失","变弯"],1,"仰/俯时竖线汇聚。"),
     pq("适合高楼仰视的是？",["一点","两点","三点","无"],2,"三点显高耸。"),
     pq("视锥作用是？",["好看","避免边缘变形","省事","上色"],1,"中心区透视更真。")],
    vid("两点透视 三点透视 建筑 透视画法","两点透视 三点透视 建筑透视")))

c1.append(ch("第7章 结构素描与观察方法", "专业", [
    sec("7.1 测量与比例", "<p>用铅笔当尺：伸直手臂、闭一眼，量对象各段比例，再移到纸上。比「凭感觉」准得多。</p>"),
    sec("7.2 负空间观察", "<p>不盯物体本身，而看它<strong>周围的空隙形状</strong>。空隙好画、且能反证轮廓是否准。</p>"+S["negative"]()),
    sec("7.3 比较与校对", "<p>时刻比较：这段比那段长多少？这条线斜率对吗？画完退远看整体，错误会自己跳出来。</p>")],
    case("案例：总是画长", "<p>没测量导致局部膨胀。每次定完大框再细分，并用负空间校验外轮廓。</p>"),
    [pq("铅笔当尺是为了？",["好玩","测比例","签名","裁纸"],1,"量化比例防走形。"),
     pq("负空间指？",["背景色","物体间空隙形状","阴影","高光"],1,"看空隙反证轮廓。"),
     pq("校对应？",["只看局部","退远看整体","闭眼","问人"],1,"远观见整体错。"),
     pq("结构素描重？",["颜色","形与比例","笔触","尺寸"],1,"结构优先于明暗。")],
    vid("结构素描 观察方法 负空间 测量","结构素描 观察方法 负空间")))

c1.append(ch("第8章 从素描到速写：快速表达", "专业", [
    sec("8.1 速写是什么", "<p>速写是在<strong>短时间</strong>内抓神态、动态与本质的素描。几秒到几分钟，重神轻形。</p>"),
    sec("8.2 动态速写", "<p>先画动作线(脊柱曲线)→ 体块 → 细节。抓「势」比抓「像」更重要。</p>"+S["gesture"]()),
    sec("8.3 日常训练法", "<p>随身本画路人、咖啡杯、街景。每天 10 张小速写，半年手眼大进。这也为后续人物/场景打底。</p>")],
    case("案例：速写僵硬", "<p>太想画准每根线。放松、用整条手臂画长线，先求势再补形。</p>"),
    [pq("速写重？",["细抠","神态与动态","上色","尺寸"],1,"短时间抓神。"),
     pq("动态速写先画？",["脸","动作线","鞋","背景"],1,"动作线定势。"),
     pq("练习频率？",["一年一次","每天多张","周末猛画","不画"],1,"高频短练最有效。"),
     pq("速写与素描关系？",["无关","速写是快素描","相反","替代"],1,"速写是限时素描。")],
    vid("速写 动态速写 日常练习 人物速写","速写 动态速写 人物速写 练习")))

add_course("sketch","素描与造型基础","✏️","#455a64",
    "一切画种的根基：从工具、线条、几何概括，到明暗五大调、一点/两点/三点透视、结构观察与速写。把造型底子打牢，人物/服装/建筑/动物都受益。", c1)

# ============================================================
# 课程2：人物绘画
# ============================================================
c2 = []
c2.append(ch("第1章 人体比例体系", "小白", [
    sec("1.1 头身比", "<p>以一头高为单位量全身。成人约 <strong>7.5–8 头身</strong>，儿童 4–5，Q 版 2–3。先定头身，人就不畸长畸短。</p>"+S["figure"](8,'m')),
    sec("1.2 分段位置", "<p>肩≈2头宽，腰≈1头，肘在 2.5 头，手腕 3.5 头，膝在 6 头，脚底 8 头。打基准线再填形。</p>"),
    sec("1.3 男女与年龄差异", "<p>男肩宽胯窄(倒三角)，女肩窄胯宽(正三角)；儿童头大四肢短。先定体型再放比例。</p>"+S["figure"](8,'f'))],
    case("案例：腿显短", "<p>胯(4头)到脚(8头)腿占约4头，远比想象长。把膝明确放 6 头即可纠正。</p>"),
    [pq("成人常见头身？",["3","5","7.5–8","12"],2,"成人约 7.5–8 头。"),
     pq("膝约在？",["2头","4头","6头","8头"],2,"膝在 6 头处。"),
     pq("男性体型？",["倒三角","正三角","方","圆"],0,"男肩宽胯窄。"),
     pq("画人先？",["画脸","定头身基准再填形","画鞋","上色"],1,"先骨架后细节。")],
    vid("人体比例 头身比 人物绘画","人体比例 头身比 人物绘画教程")))

c2.append(ch("第2章 骨骼与体块：胸腔/骨盆/头", "进阶", [
    sec("2.1 三段式体块", "<p>人体可抽象为<strong>头(球)、胸腔(倒梯形块)、骨盆(块)</strong>，由脊柱串起。这是「火柴人→真人」的关键。</p>"+S["mannequin"]()),
    sec("2.2 脊柱与扭动", "<p>脊柱是 S 形弹簧，肩胯可反向扭动( Contrapposto )。扭动让站姿有呼吸感。</p>"),
    sec("2.3 用体块定姿态", "<p>先摆两块(胸腔/骨盆)的朝向与夹角，再连四肢。姿态对了，动作自然。</p>")],
    case("案例：人像木偶", "<p>两块平行无扭动。让肩胯微转、重心偏一脚，立刻活。</p>"),
    [pq("人体核心三块？",["头胸盆","手脚手","发眼嘴","鞋裤衣"],0,"头/胸腔/骨盆。"),
     pq("Contrapposto 指？",["平站","肩胯反向扭动","躺","跳"],1,"经典对立平衡。"),
     pq("脊柱形状？",["直线","S形弹簧","圆","无"],1,"S 形可扭动。"),
     pq("定姿态先摆？",["手指","胸腔与骨盆块","头发","鞋"],1,"两大块定势。")],
    vid("人体体块 骨骼 胸腔骨盆 人物结构","人体体块 胸腔 骨盆 人物结构")))

c2.append(ch("第3章 肌肉结构与体积", "进阶", [
    sec("3.1 主要肌群", "<p>正面看：胸大肌、腹直肌、前锯肌；背面：背阔、斜方、臀大肌。理解走向，体积与衣下结构才准。</p>"+S["muscle"]()),
    sec("3.2 体积的明暗", "<p>肌肉是圆体，按五大调上明暗。胸、大腿等圆柱面亮部偏一侧，交界线随形体走。</p>"),
    sec("3.3 男女性别差异", "<p>男肌明显、棱角；女脂肪丰、过渡柔。不必画出每块肌肉，但要知道它们在哪。</p>")],
    case("案例：胸像平", "<p>没按圆柱体打调子。把胸腔当圆柱，亮侧/暗侧分明，体积鼓起。</p>"),
    [pq("正面主要肌群含？",["胸大肌","三头肌","比目鱼","咬肌"],0,"胸大肌在正面。"),
     pq("肌肉按什么上明暗？",["平面","圆体五大调","随机","颜色"],1,"肌是圆体。"),
     pq("女性特征？",["棱角硬","过渡柔","肌肉夸张","无脂肪"],1,"女性脂肪多更柔。"),
     pq("画衣下身体？",["不用管","要知道肌肉位置","全平","只画线"],1,"知结构衣才贴。")],
    vid("人体肌肉 结构 体积 素描人物","人体肌肉 结构 体积 素描")))

c2.append(ch("第4章 头部结构与三庭五眼", "小白", [
    sec("4.1 三庭", "<p>发际→眉、眉→鼻底、鼻底→下巴，三段<strong>等长</strong>。这是正面头像的竖标尺。</p>"+S["head"]()),
    sec("4.2 五眼", "<p>脸宽≈<strong>5 个眼宽</strong>：眼间距=1眼，左右各 1 眼+半眼。横向定位五官。</p>"),
    sec("4.3 角度变化", "<p>3/4 侧脸时五眼压缩、近大远小；俯仰时三庭透视缩短。结构是恒定的，只是透视变。</p>")],
    case("案例：脸显宽", "<p>眼间距画太大。收紧到「一眼宽」，并按三庭等分，脸立刻标准。</p>"),
    [pq("三庭指？",["三种鼻","竖分三等","三眼","三耳"],1,"发际-眉-鼻-下巴三等。"),
     pq("五眼指？",["2眼","5眼宽","10眼","1眼"],1,"脸宽≈5眼宽。"),
     pq("侧脸五眼？",["不变","近大远小压缩","消失","变长"],1,"透视压缩。"),
     pq("俯视时？",["三庭拉长","三庭透视缩短","不变","消失"],1,"俯仰改变三庭透视。")],
    vid("三庭五眼 头部结构 五官位置","三庭五眼 头部结构 头像")))

c2.append(ch("第5章 五官精细画法", "进阶", [
    sec("5.1 眼睛", "<p>眼非两点，是杏仁框+眼球+瞳孔+<strong>高光</strong>。上眼睑带弧、有眉，高光让眼有神。</p>"+S["eye"]()),
    sec("5.2 鼻与嘴", "<p>鼻=梯形块+鼻孔，侧面更立体；嘴先定闭合线再分上下唇，注意嘴随脸转动的椭圆透视。</p>"),
    sec("5.3 耳", "<p>耳位于眉线与鼻底线之间，形如「?」。侧面耳是重要体积标志。</p>")],
    case("案例：死鱼眼", "<p>只画黑瞳无高光、上睑平直。加白高光+有弧度的上睑，眼神即活。</p>"),
    [pq("让眼有神靠？",["大瞳","高光+弧上睑","涂黑","睫毛"],1,"高光与弧线关键。"),
     pq("耳约在？",["头顶","眉-鼻底间","下巴","颈"],1,"眉到鼻底之间。"),
     pq("嘴先定？",["颜色","闭合线","大小","光"],1,"先闭合线再分唇。"),
     pq("鼻侧面更？",["平","立体","小","无"],1,"侧面鼻体积强。")],
    vid("五官画法 眼睛 鼻子 嘴巴 耳朵 详细","五官画法 眼睛 鼻子 嘴巴 耳朵 教程")))

c2.append(ch("第6章 手与足的构造", "专业", [
    sec("6.1 手=27块骨", "<p>手难在多变。先画<strong>「手套」大块</strong>定整体，再把五指当圆柱安上，别先抠指甲。</p>"+S["hand"]()),
    sec("6.2 手指关系", "<p>中指最长，无名指略短，食近无名，小指到大鱼际。指根落一条弧线；指节有粗细变化。</p>"),
    sec("6.3 足", "<p>足≈楔形块+脚趾，侧面先画鞋形再补趾；正面脚比想象宽，大趾粗短。</p>"+S["foot"]())],
    case("案例：手像鸡爪", "<p>五指同长同直。让中指最长、指根落弧线、指节有粗细，立刻像人手。每天画 5 种姿态。</p>"),
    [pq("画手第一步？",["指甲","手套块再分指","血管","戒指"],1,"先大块后细节。"),
     pq("最长的是？",["小指","食指","中指","拇指"],2,"中指最长。"),
     pq("指根落？",["直线","弧线","圆","随机"],1,"指根在弧线上。"),
     pq("练手方法？",["一年一次","每天多姿态","只左手","不画"],1,"高频多姿态突破。")],
    vid("手的结构 画法 足 素描","手的结构 画法 足 素描教程")))

c2.append(ch("第7章 动态与重心：动作线", "进阶", [
    sec("7.1 动作线", "<p>一条贯穿头到胯的 <strong>C/S 形曲线</strong>决定动势。先画它，人就有了姿势。</p>"+S["gesture"]()),
    sec("7.2 重心转移", "<p>自然站立常<strong>一脚承重</strong>、另一脚放松；走跑身体前倾、四肢交替；坐以胯为支点。</p>"),
    sec("7.3 衣褶随结构", "<p>褶皱出现在关节弯曲与受力点(肩/胯/膝)。只画「该有」的几条，画面才干净。</p>"+S["drapery"]())],
    case("案例：站如晾衣杆", "<p>身体直筒。让重心偏移、肩胯微扭(一高一低)，加 S 形动作线即有呼吸。</p>"),
    [pq("动势由？",["头发","动作线","鞋","背景"],1,"动作线定势。"),
     pq("站立重心常？",["两脚均","一脚承重","头顶","无"],1,"一脚承重更自然。"),
     pq("衣褶多在？",["平处","关节与受力点","发","天"],1,"关节受力处生褶。"),
     pq("画动态先？",["脸","动作线","鞋","色"],1,"动作线起手。")],
    vid("人体动态 动作线 重心 衣褶","人体动态 动作线 重心 衣褶")))

c2.append(ch("第8章 人体光影与衣褶深入", "专业", [
    sec("8.1 光下的身体", "<p>身体是多个圆柱/球组合，统一光源下亮部朝光、暗部背光，交界线沿形体转折。</p>"),
    sec("8.2 衣褶类型", "<p><strong>管状褶</strong>(垂坠)、<strong>之字褶</strong>(弯折)、<strong>螺旋褶</strong>(扭绞)。按布料与动作选类型。</p>"+S["drapery"]()),
    sec("8.3 从写生到创作", "<p>掌握结构后，可凭想象摆 Pose、设计服装。人物绘画与服装设计在此交汇。</p>")],
    case("案例：衣像乱线", "<p>满身碎线。先想受力点，只画 3–5 条主褶，其余留白，衣才干净有质感。</p>"),
    [pq("身体可看作？",["平面","圆柱球组合","线","点"],1,"多体积组合。"),
     pq("垂坠产生？",["之字褶","管状褶","螺旋","无"],0,"重力垂坠成管状。"),
     pq("扭绞产生？",["管状","之字","螺旋褶","无"],2,"扭转成螺旋。"),
     pq("结构扎实后可？",["只能临摹","凭想象创作","停","只写生"],1,"结构→创作。")],
    vid("人体光影 衣褶深入 人物创作","人体光影 衣褶 人物绘画 进阶")))

add_course("figure","人物绘画","👤","#c2185b",
    """从比例、骨骼体块、肌肉体积，到头部三庭五眼、五官、手足、动态重心与衣褶光影。系统学完可从「画准人」走向「凭想象设计人物」。

涵盖：头身比、胸腔/骨盆/脊柱、主要肌群、三庭五眼、眼睛/鼻/嘴/耳、手的27骨构造、动作线与重心、五大调在人体上的应用。""", c2)

# ============================================================
# 课程3：服装设计
# ============================================================
c3 = []
c3.append(ch("第1章 时装画人体：9头身 Croquis", "小白", [
    sec("1.1 时装比例", "<p>时装画为了修长美感，常用 <strong>9 头身甚至 10 头身</strong>，颈长、肩窄、腿占近半身。这是行业「理想化」标准。</p>"+S["croquis"]()),
    sec("1.2 与真人比例区别", "<p>真人 7.5–8 头；时装画拉长腿、缩小头与手，强调服装而非解剖真实。</p>"),
    sec("1.3 建立自己的 Croquis", "<p>画一个标准 9 头身模板，反复描摹(Object tracing)，形成个人基底，套不同衣服。</p>")],
    case("案例：画得像真人模特", "<p>用了 8 头。把腿再拉长、头再缩小到 9 头，立刻有时装感。</p>"),
    [pq("时装画常用？",["6头","9头身","12头","4头"],1,"9–10 头为美。"),
     pq("与真人比？",["相同","腿更长头更小","更短","无差"],1,"拉长腿缩小头。"),
     pq("Croquis 是？",["一种布","标准人体模板","软件","鞋"],1,"可反复描的基底。"),
     pq("重点突出？",["解剖","服装","骨头","肌肉"],1,"时装画重衣非解剖。")],
    vid("时装画 9头身 croquis 服装人体","时装画 9头身 croquis 服装人体")))

c3.append(ch("第2章 重心与动态 Pose", "进阶", [
    sec("2.1 时装站姿", "<p>经典 Pose：一腿承重、胯偏移、肩微倾、手自然扶腰或垂落，显高显瘦。</p>"+S["pose"]()),
    sec("2.2 行走与转身", "<p>行走时重心前移、四肢交替；转身用肩胯扭动增加动感，适合展示服装全貌。</p>"),
    sec("2.3 手部与表情", "<p>手可扮「兰花指」或插袋；脸常简化、表情淡，避免抢服装。配饰(包/帽)补全故事。</p>")],
    case("案例：Pose 僵硬", "<p>两腿对称直立。让一脚承重、胯上提、肩下压，S 形一出来就松弛高级。</p>"),
    [pq("时装站姿要点？",["两腿并","一腿承重胯偏移","躺","跳"],1,"承重+偏移。"),
     pq("脸在时装画中？",["夸张","简化淡表情","哭泣","大笑"],1,"别抢服装。"),
     pq("转身靠？",["手","肩胯扭动","脚","发"],1,"扭动增动感。"),
     pq("手可？",["不用","扮姿/插袋","藏起","涂黑"],1,"手助姿态。")],
    vid("时装画 pose 动态 服装模特姿态","时装画 pose 动态 模特 姿态")))

c3.append(ch("第3章 人体局部时装化处理", "进阶", [
    sec("3.1 颈肩修饰", "<p>颈画细长、锁骨明显；肩削窄(比真人更瘦)，显衣服肩线利落。</p>"),
    sec("3.2 腿与手", "<p>腿拉长、脚踝细；手可适度美化但保留结构，避免「鸡爪」。</p>"+S["hand"]()),
    sec("3.3 风格化脸", "<p>可走写实、也可极简符号脸，统一于个人画风。重点是和服装调性一致。</p>")],
    case("案例：肩太宽显壮", "<p>照搬真人宽肩。收窄肩、拉长颈，服装立刻精致。</p>"),
    [pq("时装肩应？",["更宽","削窄","同真人","方"],1,"窄肩利落。"),
     pq("颈处理？",["粗短","细长","无","黑"],1,"细长显精致。"),
     pq("手避免？",["结构","鸡爪感","美化","简化"],1,"别画成鸡爪。"),
     pq("脸与服装？",["无关","调性一致","越夸张越好","隐藏"],1,"风格统一。")],
    vid("时装画 人体局部 美化 服装人体","时装画 人体 局部 美化")))

c3.append(ch("第4章 服装平面结构图（款式图）", "专业", [
    sec("4.1 什么是款式图", "<p>款式图(Technical Flat)是<strong>平铺、对称、无透视</strong>的服装工程图，供打版与生产。与效果图互补。</p>"+S["flat"]()),
    sec("4.2 画法要点", "<p>用直尺感的直线、明确缝合线/口袋/门襟；左右对称可只画一半镜像。标注工艺细节。</p>"),
    sec("4.3 系列化表达", "<p>一套系列用统一人体模板画多款 flat，便于看整体搭配与品类结构。</p>")],
    case("案例：款式图像效果图", "<p>加了透视与动态。款式图必须平、准、可量产，回归平面对称。</p>"),
    [pq("款式图特征？",["透视","平铺对称无透视","动态","彩色"],1,"工程平面图。"),
     pq("用途是？",["欣赏","打版生产","签名","装饰"],1,"给工厂看。"),
     pq("可只画？",["全动态","一半镜像","一只袖","无"],1,"对称可半画。"),
     pq("与效果图关系？",["替代","互补","无关","相反"],1,"一美一工互补。")],
    vid("服装款式图 平面图 technical flat 画法","服装款式图 平面图 technical flat")))

c3.append(ch("第5章 面料与质感表现", "专业", [
    sec("5.1 材质即笔触", "<p>不同面料用不同<strong>笔触/排线/透明度</strong>：针织用细密交叉，皮革用高光与深纹，薄纱用半透明叠层。</p>"+S["textile"]()),
    sec("5.2 垂坠与挺括", "<p>雪纺垂坠出柔和管褶；西装挺括用硬折线；毛衣蓬松用短弧笔触。先判断再下笔。</p>"),
    sec("5.3 图案与肌理", "<p>格纹、条纹、印花要随身体转折变形(包覆在体积上)，否则像贴纸。</p>")],
    case("案例：纱裙像塑料", "<p>涂成实心。改半透明叠加+边缘虚化，薄纱感立现。</p>"),
    [pq("薄纱用？",["实心","半透明叠加","黑","金"],1,"透明叠出纱感。"),
     pq("皮革重？",["细线","高光与深纹","无","灰"],1,"高光深纹。"),
     pq("图案应？",["平贴","随体积变形","随机","消失"],1,"包覆在形体上。"),
     pq("毛衣用？",["直线","短弧笔触","点","方"],1,"短弧显蓬松。")],
    vid("服装面料 质感表现 针织 皮革 薄纱 绘画","服装面料 质感 针织 皮革 薄纱 绘画")))

c3.append(ch("第6章 图案与印花设计基础", "进阶", [
    sec("6.1 二方/四方连续", "<p>图案靠<strong>重复</strong>成纹：二方连续(条带)、四方连续(面料满铺)。理解平接/错接避免接缝。</p>"),
    sec("6.2 纹样与风格", "<p>花草、几何、民族、复古各有语汇。纹样要与品牌调性、服装版型匹配。</p>"),
    sec("6.3 数码印花", "<p>现代用 PS/AI 制版喷印，可小批量。手绘纹样扫描后也可转数码。</p>")],
    case("案例：印花显乱", "<p>元素大小不一、无节奏。统一单元+规律重复，纹样立刻高级。</p>"),
    [pq("面料满铺用？",["独幅","四方连续","点","线"],1,"四方连续。"),
     pq("条带用？",["四方","二方连续","无","圆"],1,"二方连续。"),
     pq("纹样要？",["随意","与调性匹配","越多越好","消失"],1,"契合品牌。"),
     pq("现代印花多？",["手绣","数码喷印","贴纸","油画"],1,"数码为主。")],
    vid("服装图案 印花设计 连续纹样","服装图案 印花设计 连续纹样")))

c3.append(ch("第7章 色彩企划与系列开发", "专业", [
    sec("7.1 色彩故事(Color Story)", "<p>一个系列先定<strong>主色+辅色+点缀</strong>的色板，贯穿所有款式，形成统一调性。</p>"+S["schemes"]()),
    sec("7.2 系列结构", "<p>系列含主打款、搭配款、延续款，数量与品类有节奏(如 6–12 套)。主题先行再落地。</p>"),
    sec("7.3 从灵感板到企划", "<p>用灵感板(Moodboard)汇集图片/色彩/情绪，提炼主题与色板，再开发款式。</p>"+S["mood"]())],
    case("案例：系列像杂货铺", "<p>每件各用一色。回到统一色板(主60%辅30%点缀10%)，系列才成「组」。</p>"),
    [pq("色彩故事含？",["一色","主辅点缀","无序","黑"],1,"主辅点三色板。"),
     pq("系列需？",["一件","主题与节奏","随机","无"],1,"主题统领。"),
     pq("灵感板作用？",["装饰","提炼主题色板","签名","卖"],1,"定调性。"),
     pq("主色占比约？",["10%","60%","100%","0"],1,"60-30-10 法则。")],
    vid("服装色彩企划 系列开发 灵感板 moodboard","服装色彩企划 系列开发 灵感板")))

c3.append(ch("第8章 从灵感板到作品集（独立设计路径）", "大师", [
    sec("8.1 设计流程", "<p>调研→灵感板→色彩/面料企划→款式图→效果图→打版样衣→拍摄。专业设计师走完整闭环。</p>"+S["workflow"]()),
    sec("8.2 技术包(Tech Pack)", "<p>给工厂的「说明书」：尺寸表、工艺、面料、图。能写 Tech Pack 才算独立设计师。</p>"),
    sec("8.3 作品集与品牌", "<p>精选 12–20 张成体系作品，体现调研→设计→成品。可进一步做个人品牌/工作室。</p>"+S["portfolio"]())],
    case("案例：只会画不会做", "<p>效果图漂亮但工厂做不出。补齐款式图+Tech Pack，设计才可落地量产。</p>"),
    [pq("独立设计师要会？",["只画","设计+技术包落地","只拍照","只卖"],1,"设计到落地。"),
     pq("Tech Pack 给？",["客户","工厂","自己","无"],1,"工厂生产依据。"),
     pq("作品集数量？",["1张","12–20张体系","100张乱","0"],1,"精而体系。"),
     pq("完整流程终点是？",["画图","样衣/拍摄","灵感","板"],1,"成品落地。")],
    vid("服装设计流程 tech pack 作品集 独立设计师","服装设计 流程 tech pack 作品集 设计师")))

add_course("fashion","服装设计","👗","#8e24aa",
    """从 9 头身时装人体、动态 Pose、局部美化，到款式图(Technical Flat)、面料质感、印花、色彩企划与系列开发，最终走到灵感板→Tech Pack→作品集的独立设计闭环。

涵盖：Croquis 模板、承重站姿、颈肩腿修饰、平面结构图、针织/皮革/薄纱笔触、连续纹样、Color Story、Moodboard、技术包与作品集。""", c3)

# ============================================================
# 课程4：建筑绘画
# ============================================================
c4 = []
c4.append(ch("第1章 透视原理与灭点", "小白", [
    sec("1.1 透视三要素", "<p><strong>灭点(VP)、地平线、视锥</strong>。平行纵线汇于 VP，VP 在地平线；人眼高度=地平线高度。</p>"),
    sec("1.2 一点/两点/三点", "<p>正面平行画面=一点；转角为两点；仰/俯加三点。选对类型，建筑才站得稳。</p>"+S["p1"]()),
    sec("1.3 常用视高", "<p>人视(站高)最亲切；鸟瞰看布局；虫视显宏伟。先定视高再起稿。</p>")],
    case("案例：楼飘空", "<p>没定地平线。先画地平线、放 VP，建筑「落地」才真实。</p>"),
    [pq("VP 在？",["天上","地平线","外","任意"],1,"VP 在地平线。"),
     pq("转角建筑用？",["一点","两点","无","曲线"],1,"两点透视。"),
     pq("地平线=？",["天气","视点高","笔","纸"],1,"眼高即地平。"),
     pq("显宏伟用？",["人视","虫视/三点仰","平","无"],1,"仰视三点显高。")],
    vid("建筑透视 灭点 地平线 原理","建筑透视 灭点 地平线 原理")))

c4.append(ch("第2章 一点透视：室内与街道", "进阶", [
    sec("2.1 室内一点", "<p>房间正面平行画面，地面/天花/墙脚线全汇向中心 VP。家具按近大远小缩进。</p>"+S["p1"]()),
    sec("2.2 街道与廊道", "<p>两侧建筑、路灯、地砖线汇向远方 VP，强烈的纵深引导。</p>"),
    sec("2.3 常见错误", "<p>近处物体也歪、VP 不统一。保持单一 VP、竖线垂直即可避免。</p>")],
    case("案例：地砖穿帮", "<p>砖线没汇 VP。所有纵深线严格交于一点，地面才平。</p>"),
    [pq("室内一点特征？",["两VP","一VP中心","无","曲线"],1,"中心单 VP。"),
     pq("家具缩进靠？",["随机","近大远小","颜色","笔"],1,"透视缩进。"),
     pq("街道引导靠？",["云","线汇VP","人","树"],1,"纵深线引导。"),
     pq("近处竖线应？",["斜","垂直","弯","无"],0,"竖线垂直。")],
    vid("一点透视 室内 街道 建筑画法","一点透视 室内 街道 建筑")))

c4.append(ch("第3章 两点透视：建筑外观", "进阶", [
    sec("3.1 转角外观", "<p>建筑转角正对画面，左右两 VP，竖线垂直。最常用、最稳的外观透视。</p>"+S["p2"]()),
    sec("3.2 起稿步骤", "<p>定地平线→放两 VP→画最近竖棱→连 VP 定各面→加窗门。先框后填。</p>"),
    sec("3.3 控制变形", "<p>主体放视锥中心，避免边缘拉伸；VP 别太近，否则透视夸张失真。</p>")],
    case("案例：楼像要倒", "<p>竖线也斜了。两点透视竖线必须垂直，只两组面倾斜。</p>"),
    [pq("两点竖线？",["斜","垂直","弯","无"],1,"竖线垂直。"),
     pq("起稿先？",["窗","地平线+VP","树","云"],1,"先定 VP。"),
     pq("VP 太近会？",["更准","夸张失真","无影响","变平"],1,"过近失真。"),
     pq("最常用外观是？",["一点","两点","三点","无"],1,"两点最常用。")],
    vid("两点透视 建筑外观 画法 步骤","两点透视 建筑外观 画法")))

c4.append(ch("第4章 三点透视：仰视与鸟瞰", "专业", [
    sec("4.1 何时用三点", "<p>画<strong>高楼仰视</strong>或<strong>城市鸟瞰</strong>时，竖线也向第三 VP 汇聚，强化高度/深度。</p>"+S["p3"]()),
    sec("4.2 仰视构图", "<p>第三 VP 在上方，楼向天收拢，显巍峨；常用于地标、教堂。</p>"),
    sec("4.3 鸟瞰构图", "<p>第三 VP 在下方，城市向地展开，适合规划/场景设计。</p>")],
    case("案例：仰视楼仍平", "<p>只用了两点。加顶部第三 VP 让竖线收拢，高度感立刻出来。</p>"),
    [pq("三点用于？",["平房","高楼仰/鸟瞰","桌","云"],1,"强化高度深度。"),
     pq("仰视第三VP在？",["下","上","中","外"],1,"上方收拢。"),
     pq("鸟瞰第三VP在？",["上","下","中","外"],1,"下方展开。"),
     pq("三点比两点多？",["一面","一个竖VP","无","一笔"],1,"多竖线灭点。")],
    vid("三点透视 仰视 鸟瞰 建筑","三点透视 仰视 鸟瞰 建筑")))

c4.append(ch("第5章 平立剖面图基础（建筑师语言）", "专业", [
    sec("5.1 平面图(Plan)", "<p>俯视切屋顶，看隔墙、房间、门开向。是空间设计的「地图」。</p>"+S["plan"]()),
    sec("5.2 立面图(Elevation)", "<p>正视图，按真实尺寸画门窗、材质分隔。多个立面表达四向外观。</p>"+S["elev"]()),
    sec("5.3 剖面图(Section)", "<p>假想切开看内部层高、楼梯、结构。平立剖三者互相印证。</p>")],
    case("案例：画了效果图却说不清空间", "<p>补一张平面，房间关系、动线立刻清晰，也便于和团队沟通。</p>"),
    [pq("平面是？",["正面","俯视隔墙图","剖面","透视图"],1,"俯视空间图。"),
     pq("立面是？",["俯视","正视图","剖面","平面"],1,"正视图。"),
     pq("门弧线表示？",["装饰","开向","尺寸","材质"],1,"开启方向。"),
     pq("三者关系？",["无关","互相印证","替代","随机"],1,"平立剖互补。")],
    vid("建筑平面图 立面图 剖面图 基础","建筑 平面图 立面图 剖面图 基础")))

c4.append(ch("第6章 建筑细部：门窗与材质", "进阶", [
    sec("6.1 门窗构造", "<p>窗有框、扇、玻璃反射；门有门套、五金。细部决定「像不像建筑」。</p>"),
    sec("6.2 材质表现", "<p>砖用错缝排线、石材用斑驳、玻璃用竖向高光带。用<strong>排线方向</strong>区分材质。</p>"),
    sec("6.3 阴影与体积", "<p>统一光源下，凸出部受光、凹进部背光；投影方向一致，建筑才立体。</p>")],
    case("案例：墙像纸板", "<p>没材质没阴影。加砖缝排线+统一投影，墙立刻有厚度与质感。</p>"),
    [pq("窗含？",["只有玻璃","框扇玻璃","无","云"],0,"框+扇+玻璃。"),
     pq("材质靠？",["颜色","排线方向","随机","尺寸"],1,"线向区分。"),
     pq("投影应？",["乱","方向一致","无","彩"],1,"统一光源。"),
     pq("细部作用？",["无关","决定真实感","装饰","省事"],1,"细节定真实。")],
    vid("建筑细部 门窗 材质 排线","建筑细部 门窗 材质 表现")))

c4.append(ch("第7章 马克笔与淡彩建筑表现", "专业", [
    sec("7.1 马克笔上色", "<p>先浅铺大面、再叠深、留高光；用笔要<strong>快、顺形体</strong>，避免反复涂抹出脏边。</p>"),
    sec("7.2 淡彩(Watercolor)", "<p>湿画法做天空与玻璃，干画做墙体；水彩通透适合清新建筑速写。</p>"),
    sec("7.3 配景与人", "<p>树、车、人物作比例尺与生机，但别抢主体。远配景概括、近配景略细。</p>")],
    case("案例：马克笔出脏边", "<p>反复叠涂。改「一笔到位+快速运笔+留白」，干净利落。</p>"),
    [pq("马克笔要点？",["慢涂","快顺形体留高光","多遍","黑"],1,"快而准。"),
     pq("淡彩适合？",["厚重","清新通透","金属","夜景"],1,"水彩通透。"),
     pq("配景作用？",["抢戏","比例尺与生机","无关","删除"],1,"给尺度与生气。"),
     pq("远配景应？",["最细","最概括","最艳","最大"],1,"远概近细。")],
    vid("马克笔 建筑表现 淡彩 上色","马克笔 建筑表现 淡彩 上色")))

c4.append(ch("第8章 城市速写与场景取舍", "大师", [
    sec("8.1 选景与取景", "<p>先框选有意思的视角(转角、光影、对比)，舍掉杂乱。速写重「感受」非全录。</p>"),
    sec("8.2 快速流程", "<p>定透视框→抓大体积→上材质→点配景人物。限时 10–20 分钟一张。</p>"+S["workflow"]()),
    sec("8.3 个人城市志", "<p>坚持画本地街巷，积累成册，既是练习也是作品。可发展为插画/绘本方向。</p>")],
    case("案例：速写像照片堆", "<p>啥都画。学会取舍：留主建筑与光，删电线杆丛林，画面才高级。</p>"),
    [pq("速写重？",["全录","感受与取舍","尺寸","颜色"],1,"取舍去杂。"),
     pq("先定？",["窗","透视框","树","云"],1,"先透视框。"),
     pq("限时训练？",["一天","10–20分/张","不","一年"],1,"短时高效。"),
     pq("城市志是？",["作业","作品积累","垃圾","无关"],1,"练且成作。")],
    vid("城市速写 建筑场景 取景 教程","城市速写 建筑 场景 取景")))

add_course("arch","建筑绘画","🏛️","#00695c",
    """从透视原理、一点/两点/三点透视，到建筑师语言(平立剖面)、细部材质、马克笔淡彩表现，最终走到城市速写与场景取舍。

涵盖：灭点/地平线/视锥、室内与街道一点透视、建筑外观两点透视、仰视鸟瞰三点透视、平面/立面/剖面、砖石玻璃材质排线、马克笔与淡彩上色、城市速写取景。""", c4)

# ============================================================
# 课程5：动物绘画
# ============================================================
c5 = []
c5.append(ch("第1章 动物结构与比较解剖", "小白", [
    sec("1.1 动物≠人", "<p>动物多为<strong>四足水平脊柱</strong>，胸腔与骨盆两大块横置，肩游离、胯连脊柱。先理解再画。</p>"+S["quadskeleton"]()),
    sec("1.2 与人体对照", "<p>同是「头+胸腔+骨盆+四肢」，但动物水平排布、四肢更柱状。可用人体知识迁移。</p>"),
    sec("1.3 简化积木法", "<p>把动物想成「长筒(身)+球(头)+四柱(腿)」，先抓大动态再补细节。</p>")],
    case("案例：狗像站着的熊", "<p>用了直立思维。把身体放平、四腿着地，比例立刻对。</p>"),
    [pq("动物脊柱？",["垂直","水平","圆","无"],1,"水平四足。"),
     pq("两大块是？",["头手","胸腔骨盆","耳尾","鞋"],1,"胸腔+骨盆。"),
     pq("与人体可？",["无关","迁移知识","相反","替代"],1,"结构可迁移。"),
     pq("简化法用？",["细毛","筒+球+柱","点","线"],1,"积木概括。")],
    vid("动物结构 比较解剖 四足 绘画","动物结构 比较解剖 四足 绘画")))

c5.append(ch("第2章 四足动物骨架与体块", "进阶", [
    sec("2.1 脊柱双段", "<p>脊柱分<strong>胸椎段(固定、承重背)</strong>与<strong>腰椎段(灵活)</strong>；前肢连肩(可动)，后肢连胯(有力)。</p>"),
    sec("2.2 体块组装", "<p>胸腔块(前)、骨盆块(后)由背连线，四肢为柱。奔跑时背可弓可伸。</p>"+S["quadskeleton"]()),
    sec("2.3 比例因种而异", "<p>长腿鹿、短腿鼩；长身鼬、圆身熊。先量各段比例再画。</p>")],
    case("案例：腿装反了", "<p>前腿接到胯。记住：前肩后胯，前肢更灵活、后肢更壮。</p>"),
    [pq("前肢连？",["胯","肩(游离)","头","尾"],1,"前肩可动。"),
     pq("后肢连？",["肩","胯(有力)","耳","鼻"],1,"后胯发力。"),
     pq("背分？",["一段","胸腰两段","三段","无"],1,"胸固定腰灵活。"),
     pq("画前先？",["毛","量各段比例","眼","色"],1,"比例优先。")],
    vid("四足动物 骨架 体块 画法","四足动物 骨架 体块 画法")))

c5.append(ch("第3章 猫与狗的画法", "进阶", [
    sec("3.1 先用「香肠团」", "<p>身体=椭圆团，头=圆，加三角耳与长尾，四肢短柱。先大形再特征。</p>"+S["catdog"]()),
    sec("3.2 猫狗差异", "<p>猫脸短圆、耳大、身柔韧；狗吻长、耳多样、身因种差异大。抓「种征」。</p>"),
    sec("3.3 动态猫狗", "<p>猫喜蜷、扑、弓背；狗喜立、奔、摇。用动作线抓神态。</p>")],
    case("案例：猫狗分不清", "<p>都画成长吻。猫缩吻放大眼、狗拉长吻，种征就出来了。</p>"),
    [pq("起手用？",["毛","香肠团","眼","爪"],1,"团块定形。"),
     pq("猫特征？",["长吻","短圆脸大耳","垂耳必","无"],1,"猫短圆。"),
     pq("狗特征？",["无耳","吻较长种异","圆如猫","无尾"],1,"狗吻长种多。"),
     pq("种征指？",["毛色","品种特征","大小","性别"],1,"辨识关键点。")],
    vid("猫 狗 画法 结构 宠物绘画","猫 狗 画法 结构 宠物")))

c5.append(ch("第4章 马的 proportions 与运动", "专业", [
    sec("4.1 马的身体比例", "<p>身长≈<strong>头长×2.5</strong>；颈长、胸深、臀圆。肩与臀为两大块，腿细长有力。</p>"+S["horse"]()),
    sec("4.2 站立与奔腾", "<p>立姿三肢承重；奔腾四蹄离地分「收」与「展」两态，用动作线定大形。</p>"),
    sec("4.3 鬃毛与尾", "<p>鬃沿颈曲线、尾随动势飘。用流畅长笔触，显力量与速度。</p>")],
    case("案例：马身太短", "<p>身长只 1.5 头。拉长到 2.5 头、拉长颈，马感立刻出来。</p>"),
    [pq("马身长≈？",["1头","2.5头","5头","0.5头"],1,"身长2.5头。"),
     pq("两大块？",["头腹","肩臀","耳腿","尾颈"],1,"肩+臀。"),
     pq("奔腾四蹄？",["全着地","有离地态","无","少"],1,"有收展离地。"),
     pq("鬃尾用？",["短点","流畅长笔触","方","无"],1,"长笔触显速。")],
    vid("马 画法 比例 运动 绘画","马 画法 比例 运动 绘画")))

c5.append(ch("第5章 鸟类：蛋形构造与羽毛", "进阶", [
    sec("5.1 两枚蛋", "<p>鸟=身(大蛋)+头(小蛋)由颈连，翼为楔形附于身侧。轻量流线是关键。</p>"+S["bird"]()),
    sec("5.2 羽毛分层", "<p>飞羽(长、叠瓦)、绒羽(蓬松)、尾羽(舵)。分层画才真实。水禽与猛禽形态差异大。</p>"),
    sec("5.3 飞行姿态", "<p>滑翔展翼成直线，拍翼成 M 形。身体略前倾，显空气动力。</p>")],
    case("案例：鸟像气球", "<p>身圆无方向。加明显颈连头、楔形翼，流线感出来。</p>"),
    [pq("鸟身构？",["方","两枚蛋+楔翼","三角","线"],1,"蛋形组合。"),
     pq("飞羽特征？",["圆","长叠瓦","无","点"],1,"长且叠。"),
     pq("滑翔翼？",["M形","直线展开","卷","无"],1,"直线滑翔。"),
     pq("颈作用？",["无","连头显向","装饰","重"],1,"颈连头定向。")],
    vid("鸟类 画法 结构 羽毛 绘画","鸟类 画法 结构 羽毛 绘画")))

c5.append(ch("第6章 皮毛与质感表现", "专业", [
    sec("6.1 短毛笔触", "<p>顺毛发生长方向画<strong>短弧线</strong>，疏密表明暗；长毛用流畅长线分组。</p>"+S["fur"]()),
    sec("6.2 鳞片与羽", "<p>爬行/鱼类用叠瓦鳞纹；羽毛用分层弧线。质感=笔触语言。</p>"),
    sec("6.3 湿件与干件", "<p>鼻头湿润用高光点；角/蹄用硬高光。区分「干湿」提升真实。</p>")],
    case("案例：毛像刷子", "<p>凌乱短竖。改顺向分组弧线、按体积疏密，毛才服帖。</p>"),
    [pq("短毛用？",["竖线","顺向短弧","点","方"],1,"顺向弧线。"),
     pq("鳞片用？",["直线","叠瓦纹","点","无"],1,"叠瓦。"),
     pq("湿鼻用？",["无","高光点","黑","灰"],1,"湿件高光。"),
     pq("质感=？",["颜色","笔触语言","尺寸","随机"],1,"笔触即质感。")],
    vid("动物皮毛 质感 鳞片 羽毛 表现","动物皮毛 质感 鳞片 羽毛 表现")))

c5.append(ch("第7章 动态与运动线（奔跑/飞翔）", "专业", [
    sec("7.1 动物动作线", "<p>同人物，用脊背曲线定动势。四足奔跑有「伸-腾-收」循环。</p>"+S["gesture"]()),
    sec("7.2 连续动作", "<p>画一组连续帧(如猫扑)，理解关节顺序，动画/插画都受益。</p>"),
    sec("7.3 生态与习性", "<p>懂习性(猫偷袭、马易受惊)才能让姿态可信，而非摆拍。</p>")],
    case("案例：奔鹿像站鹿", "<p>四腿并拢。拉开「前后对角伸展」，腾空感即出。</p>"),
    [pq("四足奔有？",["一站","伸腾收循环","无","躺"],1,"连续循环。"),
     pq("动作线定？",["尺寸","动势","颜色","毛"],1,"脊背曲线。"),
     pq("连续帧助？",["装饰","理解关节顺序","省事","无关"],1,"懂顺序。"),
     pq("姿态可信靠？",["想象","习性","随机","颜色"],1,"习性真实。")],
    vid("动物动态 奔跑 飞翔 运动线","动物动态 奔跑 飞翔 运动线")))

c5.append(ch("第8章 动物拟人化与角色设计", "大师", [
    sec("8.1 拟人比例", "<p>把动物套用<strong>二/三头身 Q 版</strong>或人形比例，保留种征(耳、尾、毛色)即可爱角色。</p>"),
    sec("8.2 性格外化", "<p>圆脸显萌、尖脸显狡；姿态与配色传达性格。参考人物绘画的表情系统。</p>"),
    sec("8.3 从写生到 IP", "<p>先写实打底，再做风格化，发展出可商用的动物 IP/吉祥物。</p>"+S["mood"]())],
    case("案例：拟人却不可爱", "<p>用了写实头身。降到 2–3 头身、放大眼耳，萌感立现。</p>"),
    [pq("Q版动物约？",["8头","2–3头身","5头","1头"],1,"低头身萌。"),
     pq("萌感靠？",["写实","圆脸大眼耳","尖脸","灰"],1,"圆+大特征。"),
     pq("性格靠？",["随机","脸型姿态配色","尺寸","毛"],1,"外化性格。"),
     pq("IP 路径？",["只写生","写实→风格化→IP","只照片","不画"],1,"写实打底再风格。")],
    vid("动物拟人 角色设计 Q版 吉祥物 IP","动物拟人 角色设计 Q版 吉祥物")))

add_course("animal","动物绘画","🐾","#ef6c00",
    """从比较解剖、四足骨架体块，到猫狗、马、鸟的构造，再到皮毛/鳞片/羽毛质感、奔跑飞翔运动线与动物拟人角色设计。

涵盖：水平脊柱与胸腔骨盆块、前肩后胯、香肠团起手、马身2.5头长、鸟两蛋一楔翼、顺向短弧毛笔触、伸腾收运动循环、Q版拟人IP。""", c5)

# ============================================================
# 课程6：风景·场景·插画
# ============================================================
c6 = []
c6.append(ch("第1章 自然元素：树/石/水", "小白", [
    sec("1.1 树的画法", "<p>先定树干势，再堆<strong>三团叶块</strong>塑体积，而非描每片叶。针叶用放射、阔叶用团块。</p>"+S["tree"]()),
    sec("1.2 石头与岩", "<p>石分三面(受光/侧光/背光)，硬边+体量；水用水平/倒影笔触表静动。</p>"),
    sec("1.3 水与倒影", "<p>静水拉长倒影、断笔；流水用平行短线示流向。水的「轻」靠留白。</p>")],
    case("案例：树像棉花糖", "<p>只画一团。加树干方向+三叶块明暗，树立刻立住。</p>"),
    [pq("树叶先？",["每片","三团块","每针","无"],1,"团块塑形。"),
     pq("石分？",["一面","三面","无","圆"],1,"三面体积。"),
     pq("静水用？",["乱线","拉长倒影","黑","方"],1,"倒影。"),
     pq("水的轻靠？",["重涂","留白","黑","金"],1,"留白显轻。")],
    vid("风景 树 石头 水 画法","风景 树 石头 水 画法")))

c6.append(ch("第2章 天空与大气透视", "进阶", [
    sec("2.1 天空与云", "<p>云非棉花而是一团体积，用上亮下暗的软笔触；天空自上而下微变冷。</p>"),
    sec("2.2 大气透视", "<p>远处物体<strong>变淡、变冷、对比降</strong>，因空气尘埃。这是「深远」的秘密。</p>"+S["mountain"]()),
    sec("2.3 空气感", "<p>用降低饱和+提亮远层，制造空间。近实远虚人人懂，但要主动用。</p>")],
    case("案例：远山和近山一样重", "<p>没大气透视。把远山减淡降温，深度立刻拉开。</p>"),
    [pq("云是？",["棉花","体积团","线","点"],1,"体积。"),
     pq("远物应？",["更艳","更淡更冷","更黑","更大"],1,"淡冷降对比。"),
     pq("大气透视因？",["笔","空气尘埃","纸","天"],1,"空气介质。"),
     pq("深度靠？",["重涂","近实远虚+淡冷","随机","彩"],1,"主动用透视。")],
    vid("天空 云 大气透视 风景","天空 云 大气透视 风景")))

c6.append(ch("第3章 山脉与远景层次", "进阶", [
    sec("3.1 层叠山脉", "<p>用<strong>多层三角形</strong>由远及近，远层淡、近层浓，形成纵深。</p>"+S["mountain"]()),
    sec("3.2 近中远三段", "<p>构图分前/中/远景：中景为主、前景框图、远景衬空间。三段齐全才丰富。</p>"),
     sec("3.3 留白与雾", "<p>层间留白/薄雾分隔，避免糊成一团；雾也是「呼吸」。</p>")],
    case("案例：山糊一片", "<p>没分层没留白。拉开三层+雾带，山峦错落有致。</p>"),
    [pq("山脉用？",["圆","多层三角","方","线"],1,"三角层叠。"),
     pq("构图三段？",["一段","前中远","无","单"],1,"前中远。"),
     pq("层间用？",["黑","留白/薄雾","金","彩"],1,"雾分隔。"),
     pq("中景是？",["陪衬","主体","删除","无"],1,"中景为主。")],
    vid("山脉 远景 层次 风景构图","山脉 远景 层次 风景")))

c6.append(ch("第4章 室内与道具（静物）", "进阶", [
    sec("4.1 静物组合", "<p>选 2–3 件明暗/高低对比的物体，构成三角形稳定构图。</p>"+S["still"]()),
    sec("4.2 室内空间", "<p>用一点/两点透视画房间，家具依透视缩进，光影统一。</p>"),
    sec("4.3 道具叙事", "<p>一杯咖啡、一本书即可暗示「人刚离开」，场景会讲故事。</p>")],
    case("案例：静物散", "<p>物体各放各。用三角构图+统一光，画面立刻聚拢。</p>"),
    [pq("静物宜？",["多而乱","2–3件对比","无","一"],1,"少而对比。"),
     pq("构图用？",["线","三角稳定","圆","方"],1,"三角。"),
     pq("室内靠？",["随机","透视+统一光","黑","无"],1,"透视光。"),
     pq("道具可？",["无关","叙事","删除","装饰"],1,"暗示故事。")],
    vid("静物 室内 道具 素描 水彩","静物 室内 道具 素描 水彩")))

c6.append(ch("第5章 光影与时间（晨/午/黄昏）", "专业", [
    sec("5.1 光的色温", "<p>晨昏光<strong>暖(橙红)</strong>、正午光硬白、阴天光冷柔。光决定画面情绪。</p>"+S["light"]()),
    sec("5.2 长影与短影", "<p>低角度(晨昏)影长、戏剧；高角度(正午)影短、平。用影长表时间。</p>"),
    sec("5.3 统一光源", "<p>全画面只有一个主光方向，暗部统一、投影同向，才可信。</p>")],
    case("案例：光像两个太阳", "<p>物体各照各的。统一到一个主光向，画面才和谐。</p>"),
    [pq("黄昏光？",["冷","暖橙红","白","黑"],1,"暖。"),
     pq("晨昏影？",["短","长而戏剧","无","方"],1,"长影。"),
     pq("应统一？",["多光源","单主光","随机","无"],1,"单主光。"),
     pq("光决定？",["尺寸","情绪","笔","纸"],1,"情绪。")],
    vid("光影 时间 晨昏 正午 风景光","光影 时间 晨昏 正午 风景光")))

c6.append(ch("第6章 场景设计与世界观（插画）", "专业", [
    sec("6.1 什么是场景设计", "<p>为故事/游戏构建<strong>可信空间</strong>：地形、建筑、植被、气候统一于世界观。</p>"),
    sec("6.2 从 brief 到草图", "<p>先读需求(时代/风格/情绪)，缩略图探索多方案，再选一深入。</p>"+S["workflow"]()),
    sec("6.3 细节密度", "<p>视觉中心细、边缘概；用细节引导视线，而非平均用力。</p>")],
    case("案例：场景像贴图", "<p>元素堆砌无逻辑。先定世界观(废土?童话?)，所有元素服务它。</p>"),
    [pq("场景设计重？",["单物","可信空间+世界观","尺寸","笔"],1,"世界观统一。"),
     pq("先读？",["笔","brief需求","天","纸"],1,"需求先行。"),
     pq("细节应？",["平均","中心细边缘概","全细","全概"],1,"中心密。"),
     pq("缩略图用于？",["成品","探索方案","签名","装饰"],1,"多方案探索。")],
    vid("场景设计 世界观 环境 插画","场景设计 世界观 环境 插画")))

c6.append(ch("第7章 叙事构图与镜头感", "专业", [
    sec("7.1 三分与引导", "<p>主体放三分交叉点，用路/河/视线作<strong>引导线</strong>把观者带进故事。</p>"+S["thirds"]()),
    sec("7.2 镜头语言", "<p>近景(特写情绪)、中景(动作)、远景(环境气势)。像导演一样选「机位」。</p>"),
    sec("7.3 对比与焦点", "<p>大小/冷暖/虚实对比制造焦点；一处最清晰，其余让位。</p>")],
    case("案例：画面没重点", "<p>处处都细。制造一处最强对比作焦点，其余弱化，故事感出来。</p>"),
    [pq("主体放？",["中心","三分交叉点","角","外"],1,"交叉点。"),
     pq("引导线作用？",["装饰","引视线入戏","填","无"],1,"引导。"),
     pq("远景表？",["情绪","环境气势","特写","无"],1,"大环境。"),
     pq("焦点应？",["多处","一处最强","无","全"],1,"单焦点。")],
    vid("叙事构图 镜头感 插画构图","叙事构图 镜头感 插画")))

c6.append(ch("第8章 从草图到成稿的工作流", "大师", [
    sec("8.1 标准工作流", "<p>缩略图→精草→线稿→铺色→光影→细化→成稿。每步都可回看。</p>"+S["workflow"]()),
    sec("8.2 图层与迭代", "<p>数字绘画分层(线/色/光)便于改；传统则先浅后深、由整体到局部。</p>"),
    sec("8.3 建立场景库", "<p>积累树/石/建筑模块，组合成新场景，效率与一致性兼得。</p>")],
    case("案例：一上来就抠细节", "<p>没大形就细化，结果整体崩。回缩略图重定构图再推进。</p>"),
    [pq("第一步？",["细节","缩略图","色","签名"],1,"缩略图。"),
     pq("数字绘画宜？",["单图层","分层迭代","无","黑"],1,"分层好改。"),
     pq("场景库作用？",["无关","复用提效","删除","装饰"],1,"模块复用。"),
     pq("细化顺序？",["先局部","整体到局部","随机","后"],1,"整体优先。")],
    vid("插画工作流 从草图到成稿 场景","插画工作流 草图 成稿 场景")))

add_course("scene","风景·场景·插画","🌄","#1565c0",
    """从自然元素(树/石/水)、天空大气透视、山脉层次、室内静物，到光影时间、场景设计与世界观、叙事构图与从草图到成稿的工作流。

涵盖：三团叶块树法、大气透视远近淡冷、前中远三段、静物三角构图、晨昏暖光、环境/游戏场景设计、三分引导线镜头感、标准插画工作流。""", c6)

# ============================================================
# 课程7：色彩·构图·原创设计（大师路径）
# ============================================================
c7 = []
c7.append(ch("第1章 色彩科学：色相/明度/纯度", "小白", [
    sec("1.1 色彩三属性", "<p><strong>色相</strong>(什么色)、<strong>明度</strong>(明暗)、<strong>纯度</strong>(鲜艳度)。三者独立，是调色的三维坐标。</p>"+S["wheel"]()),
    sec("1.2 孟塞尔体系", "<p>专业用孟塞尔(色相/明度/彩度)描述颜色，比「红一点」精确，便于沟通与复现。</p>"),
    sec("1.3 屏幕与颜料", "<p>屏幕 RGB(加色)、印刷/颜料 CMYK(减色)。数字绘画要懂二者差异防偏色。</p>")],
    case("案例：说不清要什么红", "<p>用「色相红、明度中、纯度高」替代「亮红」，沟通与调色都准。</p>"),
    [pq("三属性是？",["红黄蓝","色相明度纯度","深浅","冷暖"],1,"H/V/C。"),
     pq("孟塞尔用于？",["装饰","精确描述颜色","签名","玩"],1,"精确沟通。"),
     pq("屏幕用？",["CMYK","RGB加色","无","黑"],1,"RGB。"),
     pq("颜料用？",["RGB","CMYK减色","无","白"],1,"减色。")],
    vid("色彩三属性 色相 明度 纯度 色彩科学","色彩三属性 色相 明度 纯度")))

c7.append(ch("第2章 色环与配色系统", "进阶", [
    sec("2.1 12 色环", "<p>三原→间→复色排成环。<strong>相邻邻近、相对互补</strong>，关系一目了然。</p>"+S["wheel"]()),
    sec("2.2 四套配色", "<p>单色(同色深浅)、邻近(相邻)、互补(对角最跳)、三角(等边三点平衡)。</p>"+S["schemes"]()),
    sec("2.3 60-30-10", "<p>主色60%、辅色30%、点缀10%。这套比例几乎不出错，是专业底色板。</p>")],
    case("案例：画面太花", "<p>七八个高饱和互打。收为「一主一辅一点缀、降其余饱和」，立刻高级。</p>"),
    [pq("色环相对色？",["邻近","互补","同色","无"],1,"互补最跳。"),
     pq("最平衡活泼？",["单色","三角色","灰","黑"],1,"三角。"),
     pq("60-30-10 指？",["笔","主次点缀比","时","步"],1,"面积比。"),
     pq("降饱和作用？",["更花","更和谐","更亮","无"],1,"降噪提级。")],
    vid("色环 配色系统 单色 邻近 互补 三角","色环 配色系统 邻近 互补 三角")))

c7.append(ch("第3章 光与色彩：固/源/环境色", "进阶", [
    sec("3.1 三色叠加", "<p>物体色=固有色 × 光源色 ± 环境色反射。写实色彩是三者互动，而非平涂固有色。</p>"+S["light"]()),
    sec("3.2 环境色反射", "<p>红墙边的白瓷会染红；水面反天蓝。注意邻近大色对暗部的影响。</p>"),
    sec("3.3 冷暖对比", "<p>受光偏暖、背光的暗部偏冷(或反之)，冷暖对比让色彩「活」。</p>")],
    case("案例：暗部死黑", "<p>暗部填纯黑。改「固有色+环境冷色」，暗部也有色彩呼吸。</p>"),
    [pq("物体色=？",["固有色","固有色×光源±环境","黑","白"],1,"三者互动。"),
     pq("红墙边白瓷？",["仍白","染红","黑","灰"],1,"环境反射。"),
     pq("暗部宜？",["纯黑","带环境冷色","金","无"],1,"暗部有彩。"),
     pq("冷暖对比让？",["平","色彩活","乱","无"],1,"活。")],
    vid("光与色彩 固有色 光源色 环境色","光与色彩 固有色 光源色 环境色")))

c7.append(ch("第4章 构图法则：三分/引导线/对比", "进阶", [
    sec("4.1 三分法", "<p>横竖各两线分九格，主体放<strong>交叉点</strong>最舒服，避免死板居中。</p>"+S["thirds"]()),
    sec("4.2 引导线", "<p>路、河、视线把观者目光引向主体，是「讲故事」的隐形手。</p>"),
    sec("4.3 对比制造焦点", "<p>大小、明暗、冷暖、虚实对比集中处即焦点；一处最强，其余让步。</p>")],
    case("案例：主体居中显呆", "<p>移到三分点、加一条引导线，画面立刻有呼吸与方向。</p>"),
    [pq("三分法分？",["两格","九格","一格","圆"],1,"九宫格。"),
     pq("引导线引向？",["边框","主体","外","无"],1,"引主体。"),
     pq("焦点靠？",["平均","对比集中","随机","无"],1,"对比聚焦。"),
     pq("最强焦点应？",["多处","一处","无","全"],1,"单点最强。")],
    vid("构图法则 三分法 引导线 对比","构图法则 三分法 引导线 对比")))

c7.append(ch("第5章 画面节奏与留白", "专业", [
    sec("5.1 视觉节奏", "<p>用<strong>重复/渐变/对比</strong>制造节奏，像音乐的节拍，引导视线游走。</p>"+S["vscale"]()),
    sec("5.2 留白的力量", "<p>空白不是「没画」，是呼吸与想象。东方绘画尤重计白当黑。</p>"),
    sec("5.3 疏密关系", "<p>密处精彩、疏处透气；疏可走马、密不透风，张弛有度。</p>")],
    case("案例：画面喘不过气", "<p>塞满。大胆留白+一处密，反而更高级有想象。</p>"),
    [pq("节奏靠？",["随机","重复渐变对比","黑","无"],1,"节奏元素。"),
     pq("留白是？",["没画","呼吸与想象","错","空"],1,"计白当黑。"),
     pq("疏密应？",["全密","疏密有致","全疏","无"],1,"张弛。"),
     pq("密处应？",["无","精彩","空","黑"],1,"密处精。")],
    vid("画面节奏 留白 疏密 构图","画面节奏 留白 疏密 构图")))

c7.append(ch("第6章 建立个人风格的方法", "专业", [
    sec("6.1 风格从何来", "<p>风格=你反复做的选择总和(线、色、题材、笔触)。不是硬想，是积累后的显现。</p>"),
    sec("6.2 刻意混搭", "<p>临摹多位喜欢的大师，提取元素<strong>混搭重组</strong>，长出自己的语言。</p>"+S["mood"]()),
    sec("6.3 限制即风格", "<p>自我设限(只用三色、只画线稿)反而催生鲜明风格。约束激发创造力。</p>")],
    case("案例：总在模仿别人", "<p>临摹完不重组。做「A的构图+B的色+C的线」混搭练习，风格才发芽。</p>"),
    [pq("风格是？",["一天悟","选择总和","买笔","抄一次"],1,"长期选择。"),
     pq("混搭指？",["全抄","提取重组","不临","随机"],1,"重组生风格。"),
     pq("限制作用？",["束缚","催生鲜明风格","无用","坏"],1,"约束创风格。"),
     pq("风格可？",["硬想","积累显现","买","借"],1,"自然显现。")],
    vid("个人画风 建立风格 混搭 方法","个人画风 建立风格 方法")))

c7.append(ch("第7章 原创设计流程：从 brief 到成品", "大师", [
    sec("7.1 接 brief", "<p>明确目标、受众、用途、调性。设计是「解决问题」，不是自嗨。</p>"),
    sec("7.2 调研与概念", "<p>收集参考、提炼关键词、画 mindmap，形成可落地的设计概念。</p>"+S["workflow"]()),
    sec("7.3 迭代与交付", "<p>多方案→选优→细化→自检(达标？)。专业交付含说明与多尺寸。</p>")],
    case("案例：设计自嗨不符需求", "<p>没读 brief。回到「用户要什么」，所有视觉服务目标，才算好设计。</p>"),
    [pq("设计是？",["自嗨","解决问题","玩","抄"],1,"解决问题。"),
     pq("先？",["画","读brief定目标","色","笔"],1,"需求先行。"),
     pq("概念来自？",["随机","调研提炼","梦","无"],1,"调研提炼。"),
     pq("交付含？",["只图","说明+多尺寸","签名","无"],1,"完整交付。")],
    vid("原创设计流程 brief 到成品 设计思维","原创设计流程 brief 成品 设计思维")))

c7.append(ch("第8章 作品集与持续精进（成为独立设计师）", "大师", [
    sec("8.1 作品集即名片", "<p>精选 12–20 张体系作品，体现「调研→设计→成品」能力，比数量重要。</p>"+S["portfolio"]()),
    sec("8.2 持续精进系统", "<p>每日速写+每周创作+每月复盘；建立参考库与练习计划，量变质变。</p>"),
    sec("8.3 独立之路", "<p>可接约稿、做个人品牌、开课、出周边。把绘画从爱好变成可持续的创造力。</p>")],
    case("案例：学了很多却接不到活", "<p>缺体系作品集。整理成「主题系列+过程稿」，客户一眼看到你的能力边界。</p>"),
    [pq("作品集重？",["数量","体系与过程","随机","无"],1,"体系。"),
     pq("精进靠？",["一天","日练周作月复盘","不练","随机"],1,"系统积累。"),
     pq("独立可？",["只画","约稿/品牌/周边","停","无"],1,"多元变现。"),
     pq("过程稿作用？",["无用","显能力边界","删","藏"],1,"证明能力。")],
    vid("作品集 持续精进 独立设计师 绘画变现","作品集 持续精进 独立设计师 绘画")))

add_course("master","色彩·构图·原创设计","🎨","#d32f2f",
    """大师收官课：从色彩科学(色相/明度/纯度、孟塞尔、RGB/CMYK)、配色系统、光与色彩互动，到构图法则、画面节奏与留白、个人风格建立，最终走到原创设计流程与作品集，完成「从小白到独立设计师」的闭环。

涵盖：12色环、单色/邻近/互补/三角配色、固有色×光源色±环境色、三分法引导线、疏密留白、混搭生风格、brief→成品设计流程、作品集与持续精进系统。""", c7)

# ---------- 输出 ----------
out = "window.DRAW_COURSES = " + json.dumps(COURSES, ensure_ascii=False, indent=1) + ";\n"
with open("data/draw_courses.js","w",encoding="utf-8") as f:
    f.write(out)
total_ch = sum(len(c["chapters"]) for c in COURSES)
print("课程数:", len(COURSES), " 总章数:", total_ch, " 字节:", len(out))
for c in COURSES:
    print(" -", c["emoji"], c["name"], "章:", len(c["chapters"]))
