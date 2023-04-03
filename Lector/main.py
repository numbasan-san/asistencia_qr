
from kivymd.app import MDApp
from kivy.lang import Builder
from pyzbar.pyzbar import ZBarSymbol
from kivymd.uix.snackbar import Snackbar
import pandas as pd
import numpy as np
import datetime

KV = """

#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
MDBoxLayout:
	orientation:'vertical'
	ZBarCam:
		id:zbarcam
		code_types:ZBarSymbol.QRCODE.value,ZBarSymbol.EAN13.value
		on_symbols:app.on_symbols(*args)
		

"""

nombres = []
matriculas = []
fecha = ''
hora = ''
count = '0'

class my_app(MDApp):
	"""docstring for my_app"""

	def build(self):
		self.root = Builder.load_string(KV)

	def on_symbols(self, instance, symbols):
		if not symbols == "":
			for symbol in symbols:				
				# print(f'Your QR is: {symbol.data.decode()}')
				Snackbar(
					text = f'Estudiante: {symbol.data.decode()}.',
					md_bg_color = 'green',
					font_size = 25
				).open()
				valores = symbol.data.decode().split(",")
				if not (valores[0] in nombres) and not (valores[1] in matriculas):
					nombres.append(valores[0])
					matriculas.append(valores[1])
					ahora = datetime.datetime.now()
					fecha = ahora.strftime('%d/%m/%Y')
					hora = ahora.strftime('%H:%M:%S')

				data = {
					'nombre': nombres,
					'matricula': matriculas,
					'fecha': fecha,
					'hora': hora
				}
				df = pd.DataFrame(data)

				df.to_excel(f'asistencia.xlsx')

				excel = pd.read_excel('asistencia.xlsx')
				count = str(len(excel))
				print(count)

if __name__ == '__main__':
	my_app().run()

"""
from kivy import *
from kivy.app import App
from kivy.uix import *

'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera
from kivy.lang import Builder
import numpy as np
import cv2


Builder.load_file("main.kv")

class AndroidCamera(Camera):
    camera_resolution = (640, 480)
    counter = 0


    def _camera_loaded(self, *largs):
        self.texture = Texture.create(size=np.flip(self.camera_resolution), colorfmt='rgb')
        self.texture_size = list(self.texture.size)

    def on_tex(self, *l):
        if self._camera._buffer is None:
            return None
        frame = self.frame_from_buf()

        self.frame_to_screen(frame)
        super(Camera, self).on_tex(*l)

    def frame_from_buf(self):
        w, h = self.resolution
        frame = np.frombuffer(self._camera._buffer.tostring(), 'uint8').reshape((h + h // 2, w))
        frame_bgr = cv2.cvtColor(frame, 93)
        return np.rot90(frame_bgr, 3)

    def frame_to_screen(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(frame_rgb, str(self.counter), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        self.counter += 1
        flipped = np.flip(frame_rgb, 0)
        buf = flipped.tostring()
        self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

class MyLayout(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()

'''
from kivy import *
from kivy.app import App
from kivy.uix import *
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.camera import Camera


'''
class mainApp(App):
	def build(self):
		pass

mainApp().run()

'''
class miCamara(App):
	'''docstring for Camara'''
	def build(self):
		rl = RelativeLayout()
		cam = AndroidCamera(resolution = (320, 240), size = (500, 300), pos = (0, 0), play = True )
		rl.add_widget(cam)
		return rl
miCamara().run()
"""
