import pandas as pd
import os
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

class DataWarehouseLoader:
    def __init__(self):
        cred = credentials.Certificate(r"eristaKey-CC2.json")
        firebase_admin.initialize_app(cred, {
            "storageBucket": "code-competence2.appspot.com"
        })
        self.bucket = storage.bucket()

    def load_data(self, file_path):
        df = pd.read_parquet(file_path)
        return df

    def transform_data(self, df_transactions, df_tickets, df_events, df_customer_feedback):
        merged_df = pd.merge(df_transactions, df_tickets, on='ticket_id', how='inner')
        merged_df = pd.merge(merged_df, df_events, on='event_id', how='inner')

        tickets_sold_per_event = merged_df.groupby('event_id')['quantity'].sum().reset_index()
        tickets_sold_per_event.columns = ['event_id', 'tickets_sold']

        revenue_per_event = merged_df.groupby('event_id')['total_amount'].sum().reset_index()

        if 'transaction_id' in df_customer_feedback.columns:
            feedback_analysis = pd.merge(df_customer_feedback, df_transactions, on='transaction_id', how='inner')
            avg_rating_per_event = feedback_analysis.groupby('feedback_id')['rating'].mean().reset_index()
        else:
            avg_rating_per_event = pd.DataFrame()

        return tickets_sold_per_event, revenue_per_event, avg_rating_per_event
    def save_to_warehouse(self, df, table_name):
        current_date = datetime.now().strftime('%Y/%m/%d')
        os.makedirs(current_date, exist_ok=True)

        file_name = f"{current_date}/{table_name}.parquet"
        blob = self.bucket.blob(file_name)
        df.to_parquet(file_name, index=False)
        blob.upload_from_filename(file_name)
        print(f"Upload Firebase Berhasil: {file_name}")

if __name__ == "__main__":
    loader = DataWarehouseLoader()

    events_df = loader.load_data('events.parquet')
    customers_df = loader.load_data('customers.parquet')
    tickets_df = loader.load_data('tickets.parquet')
    transactions_df = loader.load_data('transactions.parquet')
    customer_feedback_df = loader.load_data('customer_feedback.parquet')

    tickets_sold, revenue, avg_rating = loader.transform_data(transactions_df, tickets_df, events_df, customer_feedback_df)

    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(avg_rating, 'avg_rating_per_event')
