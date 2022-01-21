from db_connection import Db_connection 

class Temperature:
    __db = Db_connection()
    def __init__(self) -> None:
        self.__get_input()
        self.__categorize_records()
    
    __output_line= "---------------------------------------------------------------------"
    def __get_input(self):
        no_of_days = int(input("How many days to record "))
        # records of the temperature taken
        temperature_records = []

        print("Please enter 5 days temperature readings")
        for i in range(no_of_days):
            temperature_records.append(int(input(f'Temperature day [{i+1}] = ')))
            
        self.temperature_record = temperature_records
        print("\n", self.__output_line)
        
        # inserting into db
        db= self.__db
        temp_vals =[tuple([x]) for x in temperature_records ]
        db.insert_many_records(temperatures=temp_vals)
            # if (type(i) == "int" and i > 0): 
        
    def __categorize_records(self):
        categorized_days = dict()
        for i in self.temperature_record:
            if (i > 85): categorized_days[i] = "very hot"
            elif (60 >i>= 85): categorized_days[i] = "pleasant day"
            else: categorized_days[i] = "very cold"
        self.categorized_days = categorized_days
    
    def output(self):
        print("Daily Temperature Report")
        print(self.__output_line)
        cnt=1
        for x,y in self.categorized_days.items():
            print(f'Temperature day [{cnt}] = {x} Celcius {y}')
            cnt+=1
        
if __name__ == "__main__":
    temp = Temperature()
    temp.output()

