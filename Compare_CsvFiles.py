# try:
    #     with open(file1,"r") as f1 , open(file2,"r") as f2:
    #
    #         s1 = csv.reader(f1)
    #         s2 = csv.reader(f2)
    #
    #         column1 = next(s1)
    #         column2 = next(s2)
    #
    #         matching_columns = sorted([col for col in column1 if col.lower() in [c.lower() for c in column2]])
    #
    #         if matching_columns:
    #             print(f"matching columns in {file1} and {file2} : { ','.join(matching_columns)}")
    #         else:
    #             print(f"matching columns in {file1} and {file2} nat found." )
    #
    # except FileNotFoundError:
    #     print("file not found")
# def record_count(f):
#     # return len(f.splitlines())-1
#     with open(f, 'r') as csvfile:
#         first_line = csvfile.readline()  # Read and discard the header line (if present)
#         return len(csvfile.readlines()) - 1  # Count remaining lines excluding 1 for header
#
#
# file1 = "C:\\Users\\admin\\Downloads\\customers100.csv"
# file2 = "C:\\Users\\admin\\Downloads\\customers100.csv"
#
# record_count1 = record_count(file1)
# record_count2 = record_count(file2)
#
# print("record count in file1 :",record_count1)
# print("record count in file2 :",record_count2)
#
# for file1 in
# csv_file_comparision(file1,file2)

import pandas as pd
import logging


# import boto3
# from botocore.exceptions import ClientError

# Setup logging
logging.basicConfig(filename='comparison.log', level=logging.INFO)

class FileComparison:

    def read_file(file_path):
        try:
            # Read the file using pandas
            return pd.read_csv(file_path, sep=",")  # Use appropriate delimiter detection
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return None
        except Exception as e:
            logging.error(f"Error reading file {file_path}: {str(e)}")
            return None


    def compare_files(file1, file2):
        if file1 is None or file2 is None:
            logging.error("One or both input files are invalid.")
            return False

        try:
            # Compare columns
            columns_match = (read_file(file1).columns == read_file(file2).columns)

            # Compare record counts
            record_count_match = len(read_file(file1)) == len(read_file(file2))

            # Verify header and trailer records
            # Assuming header is the first row and trailer is the last row
            header_match = (read_file(file1).iloc[0] == read_file(file2).iloc[0])
            trailer_match = (read_file(file1).iloc[-1] == read_file(file2).iloc[-1])

            return {
                'columns_match': columns_match,
                'record_count_match': record_count_match,
                'header_match': header_match,
                'trailer_match': trailer_match
            }
        except Exception as e:
            logging.error(f"Error comparing files: {str(e)}")
            return False


    def generate_comparison_report(comparison_result):
        try:
            # Generate comparison report based on comparison result
            # You can format the report as CSV, JSON, or any other preferred format
            # Example CSV format:
            with open('comparison_report.csv', 'w') as report_file:
                report_file.write(compare_files(f1,f2))
                for key, value in comparison_result.items():
                    report_file.write(f"{key}: {value}\n")
            logging.info("Comparison report generated successfully.")
            return True
        except Exception as e:
            logging.error(f"Error generating comparison report: {str(e)}")
            return False

















#
# def upload_to_s3(file_path, bucket_name, object_name):
#     try:
#         # Upload file to Amazon S3 bucket
#         s3_client = boto3.client('s3')
#         response = s3_client.upload_file(file_path, bucket_name, object_name)
#         logging.info(f"Uploaded file {file_path} to S3 bucket {bucket_name}")
#         return True
#     except ClientError as e:
#         logging.error(f"Error uploading file to S3: {str(e)}")
#         return False
#     except Exception as e:
#         logging.error(f"Unexpected error uploading file to S3: {str(e)}")
#         return False






# def main():
#     # Main program logic
#     file1 = read_file('file1.csv')
#     file2 = read_file('file2.csv')
#
#     comparison_result = compare_files(file1, file2)
#
#     if comparison_result:
#         if generate_comparison_report(comparison_result):
#             # Upload report to S3
#             if upload_to_s3('comparison_report.csv', 'my-bucket', 'comparison_report.csv'):
#                 logging.info("Comparison report uploaded to S3 successfully.")
#             else:
#                 logging.error("Failed to upload comparison report to S3.")
#         else:
#             logging.error("Failed to generate comparison report.")
#     else:
#         logging.error("Comparison failed. Unable to generate report.")
#
#
# if _name_ == "_main_":
#     main()























