import os

html_content = """<!DOCTYPE html>
<html lang="ko" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>nick19850906-debug | EPIC Bento Workstation</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&family=Outfit:wght@300;400;600;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #03050a;
            --bento-bg: rgba(18, 22, 33, 0.45);
            --bento-border: rgba(255, 255, 255, 0.08);
            --bento-border-hover: rgba(255, 255, 255, 0.18);
            --text-main: #f8fafc;
            --text-muted: #8b9bb4;
            --accent-cyan: #00e5ff;
            --accent-purple: #9d4edd;
            --accent-pink: #ff2a6d;
            --accent-green: #00ff87;
            --accent-orange: #ff9f0a;
            --glass-shine: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, transparent 40%);
        }

        [data-theme="light"] {
            --bg-base: #f0f4f9;
            --bento-bg: rgba(255, 255, 255, 0.65);
            --bento-border: rgba(0, 0, 0, 0.08);
            --bento-border-hover: rgba(0, 0, 0, 0.2);
            --text-main: #0f172a;
            --text-muted: #64748b;
            --accent-cyan: #0284c7;
            --accent-purple: #7e22ce;
            --accent-pink: #be123c;
            --accent-green: #15803d;
            --accent-orange: #c2410c;
            --glass-shine: linear-gradient(135deg, rgba(255,255,255,0.8) 0%, transparent 40%);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-base);
            color: var(--text-main);
            min-height: 100vh;
            overflow-x: hidden;
            transition: background-color 0.4s ease, color 0.4s ease;
        }

        /* Canvases */
        #auroraCanvas, #fireworksCanvas {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
        }
        #auroraCanvas { z-index: 0; opacity: 0.9; }
        #fireworksCanvas { z-index: 999; }
        #cursorSpotlight {
            position: fixed; top: 0; left: 0;
            width: 500px; height: 500px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(0, 229, 255, 0.08) 0%, rgba(157, 78, 221, 0.05) 40%, transparent 70%);
            pointer-events: none; z-index: 1;
            transform: translate(-50%, -50%);
            mix-blend-mode: screen;
        }

        /* Layout */
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            grid-auto-rows: minmax(100px, auto);
            gap: 1.5rem;
            max-width: 1300px;
            margin: 3rem auto;
            padding: 0 2rem;
            position: relative;
            z-index: 10;
        }

        @keyframes fadeUp {
            0% { opacity: 0; transform: translateY(40px) scale(0.97); }
            100% { opacity: 1; transform: translateY(0) scale(1); }
        }

        /* Bento Cards */
        .bento-card {
            background: var(--bento-bg);
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            border: 1px solid var(--bento-border);
            border-radius: 32px;
            padding: 2.2rem;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.3);
            transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), border-color 0.4s ease, box-shadow 0.4s ease;
            animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
        }
        
        .bento-card:nth-child(1) { animation-delay: 0.05s; }
        .bento-card:nth-child(2) { animation-delay: 0.1s; }
        .bento-card:nth-child(3) { animation-delay: 0.15s; }
        .bento-card:nth-child(4) { animation-delay: 0.2s; }
        .bento-card:nth-child(5) { animation-delay: 0.25s; }
        .bento-card:nth-child(6) { animation-delay: 0.3s; }

        .bento-card::before {
            content: ''; position: absolute; inset: 0;
            background: var(--glass-shine); pointer-events: none; border-radius: inherit; z-index: 1;
        }

        .bento-card > * { position: relative; z-index: 2; }

        .bento-card:hover {
            transform: translateY(-8px);
            border-color: var(--bento-border-hover);
            box-shadow: 0 20px 50px -10px rgba(0,0,0,0.5);
        }

        /* Sizes */
        .hero-card { grid-column: span 8; grid-row: span 2; justify-content: center; background: linear-gradient(145deg, var(--bento-bg), rgba(0, 229, 255, 0.05)); }
        .status-card { grid-column: span 4; grid-row: span 2; align-items: center; justify-content: center; text-align: center; }
        .metrics-card { grid-column: span 5; grid-row: span 3; }
        .cli-card { grid-column: span 7; grid-row: span 3; padding: 0; }
        .tech-card { grid-column: span 6; grid-row: span 2; }
        .cheer-card { grid-column: span 6; grid-row: span 2; align-items: center; justify-content: center; text-align: center; background: radial-gradient(circle at center, rgba(157, 78, 221, 0.1) 0%, var(--bento-bg) 100%); }

        @media (max-width: 1024px) {
            .hero-card { grid-column: span 12; grid-row: span 2; }
            .status-card { grid-column: span 12; grid-row: span 1; flex-direction: row; justify-content: space-between; padding: 1.5rem 2.2rem; }
            .metrics-card { grid-column: span 12; }
            .cli-card { grid-column: span 12; grid-row: span 4; }
            .tech-card { grid-column: span 12; }
            .cheer-card { grid-column: span 12; }
        }

        /* Typography & Components */
        .badge {
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: rgba(0, 229, 255, 0.12); border: 1px solid rgba(0, 229, 255, 0.3);
            color: var(--accent-cyan); padding: 0.4rem 1rem; border-radius: 99px;
            font-size: 0.82rem; font-weight: 700; letter-spacing: 0.05em; font-family: 'Fira Code', monospace;
            margin-bottom: 1.2rem; align-self: flex-start;
        }
        
        .hero-card h1 {
            font-size: 2.8rem; font-weight: 900; line-height: 1.1; margin-bottom: 1rem; letter-spacing: -0.03em;
            background: linear-gradient(90deg, #fff, var(--accent-cyan)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .hero-card p { color: var(--text-muted); font-size: 1.15rem; line-height: 1.6; max-width: 90%; }

        /* Status Profile */
        .profile-ring {
            width: 90px; height: 90px; border-radius: 50%;
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-purple));
            display: flex; align-items: center; justify-content: center;
            font-size: 2rem; font-weight: 900; color: #fff; margin-bottom: 1rem;
            box-shadow: 0 0 30px rgba(0, 229, 255, 0.4);
            animation: float 4s ease-in-out infinite;
        }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
        
        .status-card h3 { font-size: 1.4rem; font-weight: 800; margin-bottom: 0.3rem; }
        .status-card p { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem; }
        
        .theme-btn {
            background: rgba(255,255,255,0.05); border: 1px solid var(--bento-border);
            color: var(--text-main); border-radius: 16px; padding: 0.7rem 1.4rem;
            cursor: pointer; font-size: 0.95rem; font-weight: 600; display: inline-flex; align-items: center; gap: 0.5rem;
            transition: all 0.3s ease;
        }
        .theme-btn:hover { background: rgba(255,255,255,0.1); border-color: var(--accent-cyan); transform: scale(1.05); }

        /* Metrics */
        .card-title {
            display: flex; align-items: center; gap: 0.75rem; font-size: 1.25rem; font-weight: 800; margin-bottom: 1.8rem;
        }
        .card-icon {
            width: 42px; height: 42px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;
            background: rgba(255,255,255,0.05); box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1);
        }

        .metric-row { margin-bottom: 1.4rem; }
        .metric-head { display: flex; justify-content: space-between; font-size: 0.9rem; margin-bottom: 0.5rem; font-weight: 600; }
        .metric-head span:first-child { color: var(--text-muted); }
        .metric-head span:last-child { color: var(--text-main); font-family: 'Fira Code', monospace; }
        
        .progress-bar { width: 100%; height: 8px; background: rgba(0,0,0,0.3); border-radius: 99px; overflow: hidden; position: relative; }
        .progress-fill { height: 100%; border-radius: 99px; position: absolute; left: 0; top: 0; }
        .progress-fill::after {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            animation: shine 2s infinite linear;
        }
        @keyframes shine { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }

        /* Tech Stack */
        .tech-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.8rem; }
        .tech-item {
            background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1rem;
            display: flex; flex-direction: column; align-items: center; gap: 0.5rem; transition: all 0.3s ease; text-align: center;
        }
        .tech-item:hover {
            background: rgba(0,229,255,0.05); border-color: var(--accent-cyan); transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,229,255,0.1);
        }
        .tech-item .emoji { font-size: 1.6rem; }
        .tech-item .name { font-size: 0.85rem; font-weight: 600; }
        .tech-item .sub { font-size: 0.7rem; color: var(--text-muted); font-family: 'Fira Code', monospace;}

        /* CLI Terminal Full Bleed */
        .cli-card .card-title { padding: 2rem 2rem 0; margin-bottom: 1.5rem; }
        .terminal-container {
            background: #050811; border-top: 1px solid rgba(255,255,255,0.1);
            height: 100%; display: flex; flex-direction: column;
        }
        .term-header {
            display: flex; align-items: center; justify-content: space-between; padding: 1rem 1.5rem; background: #0a0f1d; border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .mac-dots { display: flex; gap: 0.5rem; }
        .mac-dots div { width: 12px; height: 12px; border-radius: 50%; }
        .tabs { display: flex; gap: 0.5rem; overflow-x: auto; padding: 0 1.5rem 1rem; background: #0a0f1d; }
        .tab-trigger {
            background: rgba(255,255,255,0.05); border: 1px solid transparent; color: var(--text-muted);
            padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.8rem; font-family: 'Fira Code', monospace; cursor: pointer; transition: all 0.2s;
        }
        .tab-trigger.active, .tab-trigger:hover { background: rgba(0,229,255,0.1); color: var(--accent-cyan); border-color: rgba(0,229,255,0.3); }
        .term-body { padding: 1.5rem; font-family: 'Fira Code', monospace; font-size: 0.9rem; color: #cbd5e1; line-height: 1.6; overflow-y: auto; flex: 1; white-space: pre-wrap; }
        
        /* Cheer Card */
        .cheer-card h2 { font-size: 1.8rem; font-weight: 900; margin-bottom: 0.5rem; background: linear-gradient(90deg, var(--accent-purple), var(--accent-pink)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .cheer-card p { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.5; }
        .btn-epic {
            background: linear-gradient(90deg, var(--accent-purple), var(--accent-pink)); border: none; color: white; padding: 1rem 2rem; border-radius: 20px;
            font-size: 1.1rem; font-weight: 800; cursor: pointer; box-shadow: 0 10px 30px rgba(191,90,242,0.4); transition: all 0.3s ease;
        }
        .btn-epic:hover { transform: scale(1.05) translateY(-3px); box-shadow: 0 15px 40px rgba(255,42,109,0.6); }

        /* Toast */
        #toastBanner {
            position: fixed; bottom: 40px; left: 50%; transform: translate(-50%, 100px);
            background: rgba(0,0,0,0.8); backdrop-filter: blur(20px); border: 1px solid var(--accent-cyan); color: #fff;
            padding: 1rem 2rem; border-radius: 99px; font-weight: 700; font-size: 0.95rem; box-shadow: 0 10px 30px rgba(0,229,255,0.3);
            z-index: 1000; opacity: 0; transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); pointer-events: none;
        }
        #toastBanner.show { transform: translate(-50%, 0); opacity: 1; }

        footer { text-align: center; padding: 2rem; color: var(--text-muted); font-size: 0.85rem; position: relative; z-index: 10; }
        footer strong { color: var(--text-main); }
    </style>
</head>
<body>
    <canvas id="auroraCanvas"></canvas>
    <canvas id="fireworksCanvas"></canvas>
    <div id="cursorSpotlight"></div>
    <div id="toastBanner"><span id="toastMessage"></span></div>

    <main class="bento-grid">
        <!-- Hero Card -->
        <article class="bento-card hero-card">
            <div class="badge">🔥 ORBSTACK VIRTUALIZATION</div>
            <h1>Developer Workstation<br>Infrastructure Live.</h1>
            <p>성공적으로 커스텀 NGINX 이미지가 빌드되고 컨테이너가 배포되었습니다. Linux CLI, Git, 그리고 Docker 인프라 세팅 검증을 완료한 대시보드입니다.</p>
        </article>

        <!-- Status Profile Card -->
        <article class="bento-card status-card">
            <div class="profile-ring">RM</div>
            <h3>nick19850906</h3>
            <p>루키마리너 2기</p>
            <button class="theme-btn" onclick="toggleTheme()"><span class="icon">🌙</span> 테마 변경</button>
        </article>

        <!-- Metrics Card -->
        <article class="bento-card metrics-card">
            <div class="card-title">
                <div class="card-icon" style="color: var(--accent-cyan);">📊</div>
                <span>컨테이너 실측 데이터</span>
            </div>
            
            <div class="metric-row">
                <div class="metric-head"><span>웹 엔진 최적화</span><span>62.4 MB</span></div>
                <div class="progress-bar"><div class="progress-fill" style="width: 85%; background: var(--accent-cyan);"></div></div>
            </div>
            <div class="metric-row">
                <div class="metric-head"><span>포트 매핑 상태</span><span>:8080 → :80</span></div>
                <div class="progress-bar"><div class="progress-fill" style="width: 100%; background: var(--accent-purple);"></div></div>
            </div>
            <div class="metric-row">
                <div class="metric-head"><span>바인드 마운트</span><span>app/ 연결됨</span></div>
                <div class="progress-bar"><div class="progress-fill" style="width: 100%; background: var(--accent-green);"></div></div>
            </div>
            <div class="metric-row">
                <div class="metric-head"><span>볼륨 영속성</span><span>redis-data 유지</span></div>
                <div class="progress-bar"><div class="progress-fill" style="width: 90%; background: var(--accent-orange);"></div></div>
            </div>
        </article>

        <!-- CLI Terminal Card -->
        <article class="bento-card cli-card">
            <div class="card-title">
                <div class="card-icon" style="color: var(--accent-green);">💻</div>
                <span>인터랙티브 검증 콘솔</span>
            </div>
            <div class="terminal-container">
                <div class="term-header">
                    <div class="mac-dots">
                        <div style="background: #ff5f56;"></div><div style="background: #ffbd2e;"></div><div style="background: #27c93f;"></div>
                    </div>
                    <span style="font-size:0.75rem; color:var(--text-muted); font-family: monospace;">bash - 80x24</span>
                </div>
                <div class="tabs">
                    <button class="tab-trigger active" onclick="switchCliTab('docker', this)">docker ps -a</button>
                    <button class="tab-trigger" onclick="switchCliTab('curl', this)">curl localhost</button>
                    <button class="tab-trigger" onclick="switchCliTab('git', this)">git push</button>
                </div>
                <div class="term-body" id="cliScreen">
<span style="color:var(--accent-green)">dev@macbook ~ %</span> <span style="color:var(--accent-cyan)">docker ps -a</span>
CONTAINER ID   IMAGE               STATUS         PORTS                  NAMES
a1b2c3d4e5f6   my-custom-web:1.0   Up 2 hours     0.0.0.0:8080->80/tcp   my-web-8080
f6e5d4c3b2a1   nginx:alpine        Up 3 hours     0.0.0.0:8081->80/tcp   my-web-bind
                </div>
            </div>
        </article>

        <!-- Tech Stack Card -->
        <article class="bento-card tech-card">
            <div class="card-title">
                <div class="card-icon" style="color: var(--accent-pink);">⚡</div>
                <span>핵심 인프라 스택</span>
            </div>
            <div class="tech-grid">
                <div class="tech-item"><span class="emoji">🐧</span><span class="name">Linux CLI</span><span class="sub">Z Shell</span></div>
                <div class="tech-item"><span class="emoji">🐳</span><span class="name">Docker</span><span class="sub">v26.0.0</span></div>
                <div class="tech-item"><span class="emoji">🚀</span><span class="name">OrbStack</span><span class="sub">No Sudo</span></div>
                <div class="tech-item"><span class="emoji">🐙</span><span class="name">Git</span><span class="sub">GitHub</span></div>
            </div>
        </article>

        <!-- Cheer Card -->
        <article class="bento-card cheer-card">
            <h2>미션 완수 달성!</h2>
            <p>모든 개발 환경 세팅과 검증이 끝났습니다.<br>이제 완벽한 작업실에서 코딩을 시작하세요.</p>
            <button class="btn-epic" onclick="fireEpicFireworksAnimation()">🎉 EPIC 폭죽 터뜨리기</button>
        </article>
    </main>

    <footer>
        <p>© 2026 <strong>nick19850906-debug</strong>. All rights reserved | Rookie Mariner 2nd Gen</p>
    </footer>

    <script>
        // 1. Spotlight Cursor Follower
        const spotlight = document.getElementById('cursorSpotlight');
        window.addEventListener('mousemove', (e) => {
            spotlight.style.left = e.clientX + 'px';
            spotlight.style.top = e.clientY + 'px';
        });

        // 2. Theme Toggle
        function toggleTheme() {
            const html = document.documentElement;
            const cur = html.getAttribute('data-theme');
            const next = cur === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', next);
            document.querySelector('.theme-btn .icon').innerText = next === 'dark' ? '🌙' : '☀️';
            showToast(next === 'dark' ? '🌙 다크 모드로 전환되었습니다.' : '☀️ 라이트 모드로 전환되었습니다.');
        }

        // 3. Interactive CLI Tab Switcher
        function switchCliTab(type, btn) {
            document.querySelectorAll('.tab-trigger').forEach(b => b.classList.remove('active'));
            if(btn) btn.classList.add('active');
            const screen = document.getElementById('cliScreen');
            let log = '';
            if(type === 'docker') {
                log = `<span style="color:var(--accent-green)">dev@macbook ~ %</span> <span style="color:var(--accent-cyan)">docker ps -a</span>\n` +
                      `CONTAINER ID   IMAGE               STATUS         PORTS                  NAMES\n` +
                      `a1b2c3d4e5f6   my-custom-web:1.0   Up 2 hours     0.0.0.0:8080->80/tcp   my-web-8080\n` +
                      `f6e5d4c3b2a1   nginx:alpine        Up 3 hours     0.0.0.0:8081->80/tcp   my-web-bind`;
            } else if(type === 'curl') {
                log = `<span style="color:var(--accent-green)">dev@macbook ~ %</span> <span style="color:var(--accent-cyan)">curl -i http://localhost:8080</span>\n` +
                      `HTTP/1.1 200 OK\nServer: nginx/1.25.4\nDate: ${new Date().toUTCString()}\nContent-Type: text/html\n\n[200 OK Response Received Successfully!]`;
            } else if(type === 'git') {
                log = `<span style="color:var(--accent-green)">dev@macbook ~ %</span> <span style="color:var(--accent-cyan)">git push origin main</span>\n` +
                      `Enumerating objects: 12, done.\nCounting objects: 100% (12/12), done.\nWriting objects: 100% (12/12)\nTo https://github.com/nick19850906-debug/scratch.git\n * [new branch]      main -> main`;
            }
            screen.innerHTML = log;
        }

        // 4. Dynamic Aurora Canvas
        const auroraCanvas = document.getElementById('auroraCanvas');
        const auroraCtx = auroraCanvas.getContext('2d');
        function resizeAurora() { auroraCanvas.width = window.innerWidth; auroraCanvas.height = window.innerHeight; }
        window.addEventListener('resize', resizeAurora);
        resizeAurora();
        let auroraStep = 0;
        function drawAuroraWaves() {
            auroraCtx.clearRect(0, 0, auroraCanvas.width, auroraCanvas.height);
            auroraStep += 0.005;
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            const color1 = isDark ? 'rgba(0, 229, 255, 0.05)' : 'rgba(2, 132, 199, 0.04)';
            const color2 = isDark ? 'rgba(157, 78, 221, 0.05)' : 'rgba(147, 51, 234, 0.04)';
            auroraCtx.beginPath(); auroraCtx.fillStyle = color1; auroraCtx.moveTo(0, auroraCanvas.height * 0.4);
            for(let x = 0; x <= auroraCanvas.width; x += 20) {
                const y = Math.sin(x * 0.003 + auroraStep) * 80 + Math.cos(x * 0.002 + auroraStep * 0.8) * 40 + auroraCanvas.height * 0.4;
                auroraCtx.lineTo(x, y);
            }
            auroraCtx.lineTo(auroraCanvas.width, auroraCanvas.height); auroraCtx.lineTo(0, auroraCanvas.height); auroraCtx.fill();
            auroraCtx.beginPath(); auroraCtx.fillStyle = color2; auroraCtx.moveTo(0, auroraCanvas.height * 0.6);
            for(let x = 0; x <= auroraCanvas.width; x += 20) {
                const y = Math.cos(x * 0.004 - auroraStep * 1.2) * 90 + Math.sin(x * 0.0015 + auroraStep) * 60 + auroraCanvas.height * 0.6;
                auroraCtx.lineTo(x, y);
            }
            auroraCtx.lineTo(auroraCanvas.width, auroraCanvas.height); auroraCtx.lineTo(0, auroraCanvas.height); auroraCtx.fill();
            requestAnimationFrame(drawAuroraWaves);
        }
        drawAuroraWaves();

        // 5. 3D Tilt & Glow
        document.querySelectorAll('.bento-card').forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left, y = e.clientY - rect.top;
                const rx = (rect.height/2 - y) / 30, ry = (x - rect.width/2) / 30;
                card.style.transform = `perspective(1200px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-8px)`;
                let glow = card.querySelector('.mouse-glow');
                if(!glow) {
                    glow = document.createElement('div'); glow.className = 'mouse-glow';
                    glow.style.cssText = 'position:absolute; width:200px; height:200px; background:radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%); border-radius:50%; pointer-events:none; mix-blend-mode:overlay; z-index:0;';
                    card.appendChild(glow);
                }
                glow.style.left = (x - 100) + 'px'; glow.style.top = (y - 100) + 'px';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = `perspective(1200px) rotateX(0deg) rotateY(0deg) translateY(0px)`;
                const glow = card.querySelector('.mouse-glow'); if(glow) glow.remove();
            });
        });

        // 6. Fireworks Engine
        const fwCanvas = document.getElementById('fireworksCanvas');
        const fwCtx = fwCanvas.getContext('2d');
        let fwParticles = [];
        function resizeFireworks() { fwCanvas.width = window.innerWidth; fwCanvas.height = window.innerHeight; }
        window.addEventListener('resize', resizeFireworks); resizeFireworks();
        class SparkParticle {
            constructor(x, y, color) {
                this.x = x; this.y = y; this.color = color;
                const angle = Math.random() * Math.PI * 2, speed = Math.random() * 9 + 2;
                this.vx = Math.cos(angle) * speed; this.vy = Math.sin(angle) * speed;
                this.alpha = 1; this.friction = 0.95; this.gravity = 0.12;
                this.decay = Math.random() * 0.02 + 0.012; this.size = Math.random() * 3.5 + 1.5;
            }
            update() { this.vx *= this.friction; this.vy *= this.friction; this.vy += this.gravity; this.x += this.vx; this.y += this.vy; this.alpha -= this.decay; }
            draw() {
                fwCtx.save(); fwCtx.globalAlpha = Math.max(0, this.alpha); fwCtx.fillStyle = this.color;
                fwCtx.shadowBlur = 12; fwCtx.shadowColor = this.color; fwCtx.beginPath();
                fwCtx.arc(this.x, this.y, this.size, 0, Math.PI * 2); fwCtx.fill(); fwCtx.restore();
            }
        }
        function createExplosion(x, y) {
            const colors = ['#00e5ff', '#9d4edd', '#ff2a6d', '#00ff87', '#ff9f0a', '#ffffff', '#ffd700'];
            for(let i = 0; i < 80; i++) fwParticles.push(new SparkParticle(x, y, colors[Math.floor(Math.random() * colors.length)]));
        }
        function animateFireworks() {
            fwCtx.clearRect(0, 0, fwCanvas.width, fwCanvas.height);
            for(let i = fwParticles.length - 1; i >= 0; i--) {
                const p = fwParticles[i]; p.update(); p.draw();
                if(p.alpha <= 0) fwParticles.splice(i, 1);
            }
            requestAnimationFrame(animateFireworks);
        }
        animateFireworks();
        function fireEpicFireworksAnimation() {
            showToast('🎆 벤토 박스 UI 완성 축하 폭죽이 폭발합니다! 🔥');
            for(let i = 0; i < 9; i++) {
                setTimeout(() => {
                    const x = Math.random() * (window.innerWidth * 0.8) + (window.innerWidth * 0.1);
                    const y = Math.random() * (window.innerHeight * 0.6) + (window.innerHeight * 0.1);
                    createExplosion(x, y);
                }, i * 200);
            }
        }

        // Toast
        function showToast(msg) {
            const toast = document.getElementById('toastBanner');
            document.getElementById('toastMessage').innerText = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 3000);
        }
    </script>
</body>
</html>
"""

with open("app/index.html", "w") as f:
    f.write(html_content)

print("Successfully rewrote app/index.html")
