import csv
import pandas as pd

from Utilities.logger import logGenerator



class FileComparison:

    log = logGenerator.loggen()

    file1 = None
    file2 = None
    file_location = "C:\\Users\\admin\\Documents\\file_report.txt"


    def __init__(self, f1, f2):
        self.file1 = f1
        self.file2 = f2

    def matching_column(self):
        self.log.info("matching column method started...")

        try:
            with open(self.file1, 'r') as df1, open(self.file2, 'r') as df2:
                f1 = pd.read_csv(df1,nrows=1)
                f2 = pd.read_csv(df2,nrows=1)
                matching_columns = [col for col in f1 if col in f2]
                my_list = [f1,f2,matching_columns]

                self.log.info("matching column list return by function")
                return my_list

        except FileNotFoundError:
            self.log.error(f"the error is file not found")
            print("File Not Found.........")
        except Exception as e:
            self.log.error(f"the error is {e}")
            print(f"Error is {e}")
        finally:
            self.log.info("matching column method successfully return list")


    def detect_delimiter(self):
        self.log.info("detect_delimiter method started....")

        try:
            common_delimiter = [",", "\t", ";"]
            delimiter_present_file1 = []
            delimiter_present_file2 = []

            with open(self.file1, 'r') as df1, open(self.file2, 'r') as df2:
                file1 = df1.read()
                file2 = df2.read()

                for delimiter in common_delimiter:
                    if delimiter in file1:
                        delimiter_present_file1.append(delimiter)

                for delimiter in common_delimiter:
                    if delimiter in file2:
                        delimiter_present_file2.append(delimiter)
                delimiter_list = [delimiter_present_file1, delimiter_present_file2]

                return delimiter_list

        except Exception as e:
            self.log.error(f"the error is {e}")
            print(f"exception is  : {e}")

    def compare_records(self):
        self.log.info("compare_records method started....")
        try:
            with open(self.file1, 'r') as df1, open(self.file2, 'r') as df2:
                file1 = len(df1.readlines())
                file2 = len(df2.readlines())

                records_list = [file1,file2]
                return records_list


        except Exception as e:
            self.log.error(f"the error is {e}")
            print(f"Error is : {e}")

    def header_trailer_validation(self):
        self.log.info("header_trailer_validation method started....")
        try:

            with open(self.file1, 'r') as df1, open(self.file2, 'r') as df2:
                file1 = df1.readlines()
                file2 = df2.readlines()

                header_file1 = file1[0].strip()
                header_file2 = file2[0].strip()

                trailer_file1 = file1[-1].strip()
                trailer_file2 = file2[-1].strip()

                header_status = "Header Record Aligned" if header_file1 == header_file2 else "Header Mismatch In Both Files"
                trailer_status = "Trailer Record Aligned" if trailer_file1 == trailer_file2 else "Trailer is Mismatching"
                status_list = [header_status, trailer_status]
                return status_list
                # if header_file1 != header_file2:
                #     return "Header Mismatch In Both Files"
                # else:
                #     return "Header Record Aligned"
                #
                # if trailer_file1 != trailer_file2:
                #     return "Trailer is Mismatching"
                # else:
                #     return "Trailer Record Aligned"

        except Exception as e:
            self.log.error(f"the error is {e}")
            print(f"Error Occure : {e}")

    def detail_report(self):
        self.log.info("detail_report method Started....")
        try:
            data = {
                'records_file1' : self.compare_records()[0],
                'records_fil2' :  self.compare_records()[1],
                'matching_columns' : self.matching_column()[2],
                'delimiter in file1' : self.detect_delimiter()[0],
                'delimiter in file2' : self.detect_delimiter()[1],
                'header status' : self.header_trailer_validation()[0],
                'trailer status' : self.header_trailer_validation()[1]
            }

            with open(self.file_location, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
            self.log.info(f"Report Generated Successfully..")
            print("Report generated successfully !!!")

        except Exception as e:
            self.log.error(f"the error is {e}")
            print("error is :",e)



f1 = "C:\\Users\\admin\\Documents\\file1.txt"
f2 = "C:\\Users\\admin\\Documents\\file2.txt"

# outliers book read
compare = FileComparison(f1, f2)
# print(compare.detail_report())
# print(compare.detect_delimiter())






