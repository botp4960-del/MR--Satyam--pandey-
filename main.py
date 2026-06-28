from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        
        # Safely convert time to integer, use a default if it fails
        try:
            time_interval = int(request.form.get('time'))
        except (ValueError, TypeError):
            time_interval = 5 # Default to 5 seconds if input is invalid

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode('utf-8').splitlines()

        # The message sending logic remains as per your original request to ensure functionality
        while True:
            try:
                for message1 in messages:
                    # Construct the API URL for the Facebook Graph API to send a message
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    
                    # Send the POST request
                    response = requests.post(api_url, data=parameters, headers=headers)
                    
                    # Check response status
                    if response.status_code == 200:
                        print(f"Message sent successfully. Status: 200 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    else:
                        print(f"Failed to send message. Status: {response.status_code}. Response: {response.text}")
                    
                    # Wait for the specified interval
                    time.sleep(time_interval)
            
            except Exception as e:
                # General error handling
                print(f"An error occurred: {e}")
                time.sleep(30) # Wait longer before retrying on error


    # Cyberpunk themed HTML/CSS
    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NEURAL MESSAGE TERMINAL</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    body {
      background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
      font-family: 'Rajdhani', sans-serif;
      color: #00f3ff;
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }
    
    body::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: 
        radial-gradient(circle at 20% 80%, rgba(0, 243, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 0, 128, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(0, 255, 191, 0.05) 0%, transparent 50%);
      pointer-events: none;
    }
    
    .cyber-container {
      max-width: 400px;
      background: rgba(10, 15, 30, 0.9);
      backdrop-filter: blur(10px);
      border-radius: 0;
      border: 1px solid #00f3ff;
      padding: 30px;
      margin: 40px auto;
      position: relative;
      box-shadow: 
        0 0 20px rgba(0, 243, 255, 0.3),
        inset 0 0 20px rgba(0, 243, 255, 0.1);
    }
    
    .cyber-container::before {
      content: '';
      position: absolute;
      top: -2px;
      left: -2px;
      right: -2px;
      bottom: -2px;
      background: linear-gradient(45deg, #00f3ff, #ff0080, #00ffbf, #00f3ff);
      z-index: -1;
      animation: borderGlow 3s linear infinite;
    }
    
    @keyframes borderGlow {
      0% { filter: hue-rotate(0deg); }
      100% { filter: hue-rotate(360deg); }
    }
    
    .cyber-header {
      text-align: center;
      margin-bottom: 30px;
      font-family: 'Orbitron', monospace;
      font-weight: 900;
      font-size: 1.8rem;
      color: #00f3ff;
      text-shadow: 0 0 10px rgba(0, 243, 255, 0.7);
      letter-spacing: 2px;
      position: relative;
    }
    
    .cyber-header::after {
      content: '';
      display: block;
      width: 100%;
      height: 2px;
      background: linear-gradient(90deg, transparent, #00f3ff, transparent);
      margin-top: 10px;
    }
    
    .matrix-rain {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: -1;
      opacity: 0.1;
    }
    
    .cyber-input {
      background: rgba(0, 0, 0, 0.7);
      border: 1px solid #00f3ff;
      border-radius: 0;
      color: #00ffbf;
      font-family: 'Rajdhani', sans-serif;
      font-weight: 600;
      padding: 12px 15px;
      margin-bottom: 20px;
      transition: all 0.3s ease;
    }
    
    .cyber-input:focus {
      background: rgba(0, 20, 30, 0.9);
      border-color: #ff0080;
      box-shadow: 0 0 15px rgba(255, 0, 128, 0.5);
      color: #ffffff;
      outline: none;
    }
    
    .cyber-label {
      color: #00ffbf;
      font-weight: 600;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-size: 0.9rem;
    }
    
    .cyber-btn {
      background: linear-gradient(45deg, #00f3ff, #00ffbf);
      border: none;
      border-radius: 0;
      color: #0c0c0c;
      font-family: 'Orbitron', monospace;
      font-weight: 700;
      padding: 15px;
      margin-top: 20px;
      text-transform: uppercase;
      letter-spacing: 2px;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }
    
    .cyber-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(0, 243, 255, 0.4);
      color: #0c0c0c;
    }
    
    .cyber-btn::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
      transition: 0.5s;
    }
    
    .cyber-btn:hover::before {
      left: 100%;
    }
    
    .terminal-text {
      font-family: 'Courier New', monospace;
      color: #00ff00;
      background: rgba(0, 0, 0, 0.8);
      border: 1px solid #00ff00;
      padding: 15px;
      margin-top: 20px;
      font-size: 0.8rem;
      line-height: 1.4;
    }
    
    .cyber-footer {
      text-align: center;
      margin-top: 30px;
      color: #ff0080;
      font-family: 'Orbitron', monospace;
    }
    
    .neon-text {
      color: #00f3ff;
      text-shadow: 0 0 5px #00f3ff, 0 0 10px #00f3ff;
      animation: neonPulse 2s infinite;
    }
    
    @keyframes neonPulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.7; }
    }
    
    .hacker-text {
      background: linear-gradient(45deg, #00f3ff, #ff0080, #00ffbf);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 700;
    }
    
    .glitch {
      position: relative;
      display: inline-block;
    }
    
    .glitch::before,
    .glitch::after {
      content: attr(data-text);
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }
    
    .glitch::before {
      left: 2px;
      text-shadow: -2px 0 #ff0080;
      clip: rect(44px, 450px, 56px, 0);
      animation: glitch-anim 5s infinite linear alternate-reverse;
    }
    
    .glitch::after {
      left: -2px;
      text-shadow: -2px 0 #00ffbf;
      clip: rect(44px, 450px, 56px, 0);
      animation: glitch-anim2 5s infinite linear alternate-reverse;
    }
    
    @keyframes glitch-anim {
      0% { clip: rect(42px, 9999px, 44px, 0); }
      5% { clip: rect(12px, 9999px, 59px, 0); }
      10% { clip: rect(48px, 9999px, 29px, 0); }
      15% { clip: rect(42px, 9999px, 73px, 0); }
      20% { clip: rect(63px, 9999px, 27px, 0); }
      25% { clip: rect(34px, 9999px, 55px, 0); }
      30% { clip: rect(86px, 9999px, 73px, 0); }
      35% { clip: rect(20px, 9999px, 20px, 0); }
      40% { clip: rect(26px, 9999px, 60px, 0); }
      45% { clip: rect(25px, 9999px, 66px, 0); }
      50% { clip: rect(57px, 9999px, 98px, 0); }
      55% { clip: rect(5px, 9999px, 46px, 0); }
      60% { clip: rect(82px, 9999px, 31px, 0); }
      65% { clip: rect(54px, 9999px, 27px, 0); }
      70% { clip: rect(28px, 9999px, 99px, 0); }
      75% { clip: rect(45px, 9999px, 69px, 0); }
      80% { clip: rect(23px, 9999px, 85px, 0); }
      85% { clip: rect(54px, 9999px, 84px, 0); }
      90% { clip: rect(45px, 9999px, 47px, 0); }
      95% { clip: rect(37px, 9999px, 20px, 0); }
      100% { clip: rect(4px, 9999px, 91px, 0); }
    }
    
    @keyframes glitch-anim2 {
      0% { clip: rect(65px, 9999px, 100px, 0); }
      5% { clip: rect(52px, 9999px, 74px, 0); }
      10% { clip: rect(79px, 9999px, 85px, 0); }
      15% { clip: rect(75px, 9999px, 5px, 0); }
      20% { clip: rect(67px, 9999px, 61px, 0); }
      25% { clip: rect(14px, 9999px, 79px, 0); }
      30% { clip: rect(1px, 9999px, 66px, 0); }
      35% { clip: rect(86px, 9999px, 30px, 0); }
      40% { clip: rect(23px, 9999px, 98px, 0); }
      45% { clip: rect(85px, 9999px, 72px, 0); }
      50% { clip: rect(71px, 9999px, 75px, 0); }
      55% { clip: rect(2px, 9999px, 48px, 0); }
      60% { clip: rect(30px, 9999px, 16px, 0); }
      65% { clip: rect(59px, 9999px, 50px, 0); }
      70% { clip: rect(41px, 9999px, 62px, 0); }
      75% { clip: rect(2px, 9999px, 82px, 0); }
      80% { clip: rect(47px, 9999px, 73px, 0); }
      85% { clip: rect(3px, 9999px, 27px, 0); }
      90% { clip: rect(26px, 9999px, 55px, 0); }
      95% { clip: rect(42px, 9999px, 97px, 0); }
      100% { clip: rect(38px, 9999px, 49px, 0); }
    }
  </style>
</head>
<body>
  <canvas class="matrix-rain" id="matrixRain"></canvas>

  <div class="cyber-container">
    <div class="cyber-header">
      <span class="glitch" data-text="NEURAL MESSAGE TERMINAL">NEURAL MESSAGE TERMINAL</span>
    </div>
    
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken" class="cyber-label">ACCESS TOKEN</label>
        <input type="text" class="form-control cyber-input" id="accessToken" name="accessToken" required placeholder="ENTER SECURITY CLEARANCE">
      </div>
      <div class="mb-3">
        <label for="threadId" class="cyber-label">CONVERSATION ID</label>
        <input type="text" class="form-control cyber-input" id="threadId" name="threadId" required placeholder="TARGET IDENTIFICATION">
      </div>
      <div class="mb-3">
        <label for="kidx" class="cyber-label">SENDER IDENTITY</label>
        <input type="text" class="form-control cyber-input" id="kidx" name="kidx" required placeholder="OPERATIVE DESIGNATION">
      </div>
      <div class="mb-3">
        <label for="txtFile" class="cyber-label">MESSAGE DATABASE</label>
        <input type="file" class="form-control cyber-input" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time" class="cyber-label">TRANSMISSION INTERVAL</label>
        <input type="number" class="form-control cyber-input" id="time" name="time" value="5" required placeholder="SECONDS BETWEEN PULSES">
      </div>
      <button type="submit" class="btn cyber-btn w-100">
        INITIATE MESSAGE STREAM
      </button>
    </form>
    
    <div class="terminal-text">
      <div>> SYSTEM STATUS: <span class="neon-text">ONLINE</span></div>
      <div>> SECURITY PROTOCOL: <span class="neon-text">ACTIVE</span></div>
      <div>> READY FOR NEURAL TRANSMISSION</div>
    </div>
    
    <footer class="cyber-footer">
      <p class="mb-1">SYSTEM OPERATOR: <span class="hacker-text">WALEED</span></p>
      <p class="mb-0">NEURAL INTERFACE ACTIVE</p>
    </footer>
  </div>

  <script>
    // Matrix Rain Effect
    const canvas = document.getElementById('matrixRain');
    const ctx = canvas.getContext('2d');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const chars = '01010101010101010101010101010101';
    const charArray = chars.split('');
    
    const font_size = 12;
    const columns = canvas.width / font_size;
    
    const drops = [];
    
    for(let x = 0; x < columns; x++)
        drops[x] = 1;
    
    function drawMatrix() {
        ctx.fillStyle = 'rgba(10, 15, 30, 0.04)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.fillStyle = '#00f3ff';
        ctx.font = font_size + 'px monospace';
        
        for(let i = 0; i < drops.length; i++) {
            const text = charArray[Math.floor(Math.random() * charArray.length)];
            ctx.fillText(text, i * font_size, drops[i] * font_size);
            
            if(drops[i] * font_size > canvas.height && Math.random() > 0.975)
                drops[i] = 0;
            
            drops[i]++;
        }
    }
    
    setInterval(drawMatrix, 35);
    
    window.addEventListener('resize', function() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
    
    // Cyber input effects
    document.querySelectorAll('.cyber-input').forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.style.transform = 'translateX(5px)';
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.style.transform = 'translateX(0)';
        });
    });
  </script>
</body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)