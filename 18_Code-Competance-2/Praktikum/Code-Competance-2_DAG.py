from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from Data_Ingestion import DataLakeBuilder  # Mengimpor kelas DataLakeBuilder dari modul Data_Ingestion
from Data_Transformation import DataWarehouseLoader  # Mengimpor kelas DataWarehouseLoader dari modul Data_Transformation

# Konfigurasi default untuk DAG
default_args = {
    'owner': 'ERISTA',  # Nama pemilik DAG
    'depends_on_past': False,  # Tidak tergantung pada eksekusi sebelumnya
    'start_date': days_ago(1),  # Mulai dari satu hari yang lalu
    'email_on_failure': False,  # Tidak mengirim email saat gagal
    'email_on_retry': False,  # Tidak mengirim email saat mencoba ulang
    'retries': 1,  # Mencoba ulang sekali jika gagal
}

# Membuat objek DAG dengan nama 'ERISTA-DAG'
dag = DAG('ERISTA-DAG-CC2', 
          description='DAG untuk Data Ingestion, Transformation, dan Loading ke Firebase Storage',
          default_args=default_args,
          schedule_interval=timedelta(1),  # Menjadwalkan DAG setiap hari
          start_date=datetime(2024, 5, 4))  # Mulai pada tanggal 4 Mei 2024

# Fungsi untuk menjalankan tugas pengambilan data
def data_ingestion_task():
    lake_builder = DataLakeBuilder()  # Membuat objek DataLakeBuilder
    csv_files = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']  # Daftar file CSV
    parquet_files = ['events.parquet', 'customers.parquet', 'tickets.parquet', 'transactions.parquet', 'customer_feedback.parquet']  # Daftar file Parquet

    for csv, parquet in zip(csv_files, parquet_files):  # Iterasi melalui daftar file CSV dan Parquet secara bersamaan
        df = lake_builder.read_csv_data(csv)  # Membaca data dari file CSV
        lake_builder.handle_missing_values(df)  # Menangani nilai yang hilang
        lake_builder.handle_duplicates(df)  # Menangani duplikat
        if csv == 'transactions.csv':  # Jika file CSV adalah 'transactions.csv'
            lake_builder.handle_outliers(df, 'total_amount')  # Menangani outlier untuk kolom 'total_amount'
        lake_builder.save_to_parquet(df, parquet)  # Menyimpan data ke file Parquet
        lake_builder.validate_data(parquet)  # Memvalidasi data

# Fungsi untuk menjalankan tugas transformasi data dan memuatnya ke penyimpanan
def data_transformation_task():
    warehouse_loader = DataWarehouseLoader()  # Membuat objek DataWarehouseLoader
    datasets = ['events', 'customers', 'tickets', 'transactions', 'customer_feedback']  # Daftar dataset
    metrics = ['tickets_sold_per_event', 'revenue_per_event', 'avg_rating_per_event']  # Daftar metrik

    for dataset, metric in zip(datasets, metrics):  # Iterasi melalui daftar dataset dan metrik secara bersamaan
        df = warehouse_loader.load_data(f'{dataset}.parquet')  # Memuat data dari file Parquet
        if dataset == 'transactions':  # Jika dataset adalah 'transactions'
            processed_data = warehouse_loader.transform_data(df, warehouse_loader.load_data('tickets.parquet'),
                                                            warehouse_loader.load_data('events.parquet'),
                                                            warehouse_loader.load_data('customer_feedback.parquet'))  # Melakukan transformasi data
            warehouse_loader.save_to_warehouse(processed_data, metric)  # Menyimpan data ke warehouse
        else:  # Untuk dataset lainnya
            warehouse_loader.save_to_warehouse(df, metric)  # Menyimpan data ke warehouse

# Membuat operator Python untuk tugas pengambilan data
ingestion_task = PythonOperator(
    task_id='data_ingestion',
    python_callable=data_ingestion_task,
    dag=dag)

# Membuat operator Python untuk tugas transformasi data
transformation_task = PythonOperator(
    task_id='data_transformation',
    python_callable=data_transformation_task,
    dag=dag)

# Mengatur dependensi antara tugas pengambilan data dan tugas transformasi data
ingestion_task >> transformation_task