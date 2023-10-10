from mindee import Client
from mindee.documents import TypeReceiptV5
import os
from time import process_time

class receiptTextExtractor:

    def __init__(self) -> None:
        self.mindee_client = Client(api_key = "e8f28efeb479898af6759c78a5a8f333")
        self.inventory = {"cabinet": [], "fridge": [] }
        self.temporary_inventory_list = []
        
    def receipt_photo_upload_extract(self, photo_file_path): 
        self.receipt_photo = self.mindee_client.doc_from_path(photo_file_path)

        result = self.receipt_photo.parse(TypeReceiptV5)
        #print( vars( result.document))

        for item in result.document.line_items:
            print ( item.description)

            # insert a processor for the food item

            self.temporary_inventory_list.append(item.description)



class Text_Interpreter:

    def __init__( self):
        pass

    def autocorrect_spelling( self):
        pass

    def filter_ingredients( self):
        pass




if __name__ == "__main__":

    print("hello")
    receipt_reader = receiptTextExtractor()

  #  for receipt_photo in 
   # print (os.path.abspath(os.path.join(os.getcwd(), os.pardir))) 
 #   print(os.path.join(os.getcwd(), "receipts"))

    receipt_directory_path = os.path.join(os.getcwd(), "receipts")
    receipt_directory_list =  os.listdir(os.path.join(os.getcwd(), "receipts"))

    t1_seconds_start = process_time()

    for receipt_photo in receipt_directory_list:
    
        upload_receipt_photo = receipt_reader.receipt_photo_upload_extract(photo_file_path= os.path.join( receipt_directory_path, receipt_photo))

    t1_seconds_end = process_time()
    print("Elapsed tim during the whole program in seconds:", t1_seconds_end - t1_seconds_start)
    print ( receipt_reader.temporary_inventory_list)

