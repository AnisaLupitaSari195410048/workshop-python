#Start CockroachDB menggunakan Cockroach Tanpa server(beta)
#cloning repo GitHub kode sampel:

'''
git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
'''

#Instal driver psycopg2

'''
pip install psycopg2-binary
'''

#Jalankan kode

#setel pada DATABASE_URLvariabel lingkungan ke string koneksi ke cluster CockroachDB Cloud:
'''
export DATABASE_URL="{connection-string}"
'''

'''
cd hello-world-python-psycopg2
'''

'''
python example.py
'''

#Start CockroachDB menggunakan cluster lokal
#jalankan perintah
'''
cockroach start-single-node --advertise-addr 'localhost' --insecure
'''

#perhatikan informasi koneksi pada shell SQL:
'''
CockroachDB node starting at 2021-08-30 17:25:30.06524 +0000 UTC (took 4.3s)
build:               CCL v21.1.6 @ 2021/07/20 15:33:43 (go1.15.11)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257?sslmode=disable
'''