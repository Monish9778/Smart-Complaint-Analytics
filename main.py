from src.data_ingestion import load_data
from src.preprocessing import preprocess_data
from src.analysis import complaint_summary
from src.modeling import cluster_complaints

DATA_PATH = "data/complaints.csv"

def main():
    df = load_data(DATA_PATH)
    df = preprocess_data(df)

    print("\nComplaint Summary:")
    print(complaint_summary(df))

    df['cluster'] = cluster_complaints(df['clean_text'])
    print("\nClustered Complaints:")
    print(df[['complaint_text', 'cluster']])

if __name__ == "__main__":
    main()
