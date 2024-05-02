from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Menentukan default arguments untuk DAG
default_args = {
    'owner': 'erista',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Mendefinisikan DAG dengan nama 'dag_1' dan default arguments
dag = DAG(
    '17_prio1_no-1', default_args=default_args, schedule_interval=None)

# Task 1: Menampilkan pesan salam dari Airflow
greetings_task = BashOperator(
    task_id='say_hello',  # Nama task
    bash_command='echo "Hello from Airflow"',  # Command bash yang akan dieksekusi
    dag=dag)  # Menambahkan task ke dalam DAG

# Task 2: Membuat direktori 'about_us'
about_directory_task = BashOperator(
    task_id='create_about_us_directory',  # Nama task
    bash_command='mkdir -p about_us',  # Command bash untuk membuat direktori
    dag=dag)  # Menambahkan task ke dalam DAG

# Task 3: Membuat direktori 'our_works'
works_directory_task = BashOperator(
    task_id='create_our_works_directory',  # Nama task
    bash_command='mkdir -p our_works',  # Command bash untuk membuat direktori
    dag=dag)  # Menambahkan task ke dalam DAG

# Task 4: Membuat file 'about.txt' di dalam direktori 'about_us'
about_file_task = BashOperator(
    task_id='create_about_us_about_file',  # Nama task
    bash_command='mkdir -p about_us && touch about_us/about.txt',  # Command bash untuk membuat file
    dag=dag)  # Menambahkan task ke dalam DAG

# Task 5: Membuat file 'works.txt' di dalam direktori 'our_works'
works_file_task = BashOperator(
    task_id='create_our_works_works_file',  # Nama task
    bash_command='mkdir -p our_works && touch our_works/works.txt',  # Command bash untuk membuat file
    dag=dag)  # Menambahkan task ke dalam DAG

# Task 6: Menampilkan pesan bahwa proses sudah selesai
completion_message_task = BashOperator(
    task_id='print_completion_message',  # Nama task
    bash_command='echo "Process completed"',  # Command bash untuk menampilkan pesan
    dag=dag)  # Menambahkan task ke dalam DAG

# Mendefinisikan dependency antar task
greetings_task >> about_directory_task
greetings_task >> works_directory_task
about_directory_task >> about_file_task
works_directory_task >> works_file_task
about_file_task >> completion_message_task
works_file_task >> completion_message_task