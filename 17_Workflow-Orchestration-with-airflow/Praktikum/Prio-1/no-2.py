from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from random import sample

default_args = {
    'owner': 'ERISTA',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 9),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_2', default_args=default_args, schedule_interval=timedelta(days=1))  # Perubahan: Frekuensi jadwal diubah menjadi harian

# Fungsi untuk menghasilkan bilangan acak dengan rentang yang berbeda
def generate_random_numbers():
    numbers = sample(range(10, 101), 50)  # Perubahan: Menghasilkan 50 bilangan acak antara 10 dan 100
    return numbers

# Fungsi untuk menghitung jumlah total bilangan dengan cara yang sedikit berbeda
def calculate_sum(ti):
    numbers = ti.xcom_pull(task_ids='generate_random_numbers')
    total = sum(numbers)
    ti.xcom_push(key='sum_of_numbers', value=total)

# Fungsi untuk menampilkan hasil pengecekan jumlah bilangan yang berbeda
def check_even_sum(ti):
    total = ti.xcom_pull(key='sum_of_numbers')
    result = 'Jumlah Bilangan Genap' if total % 2 == 0 else 'Jumlah Bilangan Ganjil'  # Perubahan: Penyampaian hasil yang lebih umum
    print(result)

# Task untuk menghasilkan bilangan acak dengan nama task yang lebih deskriptif
t1 = PythonOperator(
    task_id='generate_random_numbers_task',  # Perubahan: Nama task yang lebih deskriptif
    python_callable=generate_random_numbers,
    provide_context=True,
    dag=dag)

# Task untuk menghitung jumlah total bilangan dengan nama task yang lebih deskriptif
t2 = PythonOperator(
    task_id='calculate_total_sum_task',  # Perubahan: Nama task yang lebih deskriptif
    python_callable=calculate_sum,
    provide_context=True,
    dag=dag)

# Task untuk menampilkan hasil pengecekan jumlah bilangan dengan nama task yang lebih deskriptif
t3 = PythonOperator(
    task_id='check_total_sum_task',  # Perubahan: Nama task yang lebih deskriptif
    python_callable=check_even_sum,
    provide_context=True,
    dag=dag)

# Mendefinisikan dependency antar task
t1 >> t2 >> t3