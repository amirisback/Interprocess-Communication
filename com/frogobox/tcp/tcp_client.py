# import library socket karena akan menggunakan IPC socket
import socket
from com.frogobox.base.config import *

# definisikan tujuan IP server
SERVER_ADDRESS = BASE_CONFIG_IP_ADDRESS

# definisikan port dari server yang akan terhubung
SERVICE_PORT = BASE_CONFIG_PORT

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER = BASE_CONFIG_BUFFER

# definisikan pesan yang akan disampaikan
MESSAGE = 'TCP ' + MESSAGE_REQUEST

# buat socket TCP
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
tcpClient.connect((SERVER_ADDRESS, SERVICE_PORT))

# kirim pesan ke server, pesan bebas, dan ditambahkan nama anggota kelompok
tcpClient.send(MESSAGE.encode())

# terima pesan dari server
data = tcpClient.recv(BUFFER)

# tampilkan pesan/reply dari server
print('Received', data.decode())

# tutup koneksi
tcpClient.close()
