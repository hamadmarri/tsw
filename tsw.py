import time
import threading
import sys
import tty

running = True
ms = 0

print("s - stop\t p - pause/resume")


def start_time():
	global ms
	while (running):
		time.sleep(0.093)
		ms += 93
		print("\b" * 100, end='', flush=True)
		s = ms // 1000
		_ms = ms % 1000
		m = s // 60
		s = s % 60
		h = m // 60
		m = m % 60
		print('{:02}:'.format(h), end='', flush=True)
		print('{:02}:'.format(m), end='', flush=True)
		print('{:02}:'.format(s), end='', flush=True)
		print('{:03}'.format(_ms), end='', flush=True)



t = threading.Thread(target=start_time)
t.start()


tty.setcbreak(sys.stdin)
while True:
	try:
		i = sys.stdin.read(1)[0]
	except:
		i = "s"

	if i == "s":
		running = False
		t.join()
		print("\n\nstopwatch stopped")
		break
	elif i == "p" and running:
		running = False
		t.join()
		print(" paused")
	elif i == "p" and not running:
		running = True
		t = threading.Thread(target=start_time)
		t.start()



