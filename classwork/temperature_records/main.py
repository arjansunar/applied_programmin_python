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
        
    def __categorize_records(self):
        categorized_days = dict()
        no_of_categorized_day = {
            "hot": 0,
            "pleasant": 0,
            "cold": 0
        }
        for i in self.temperature_record:
            if (i >= 85): 
                categorized_days[i] = "very hot"
                no_of_categorized_day["hot"] += 1
            elif (i >= 60): 
                categorized_days[i] = "pleasant day"
                no_of_categorized_day["pleasant"] += 1
            else: 
                categorized_days[i] = "very cold"
                no_of_categorized_day["cold"] += 1
        self.categorized_days = categorized_days
        self.no_of_categorized_day = no_of_categorized_day
    
    def output(self):
        print("Daily Temperature Report")
        print(self.__output_line)
        cnt=1
        sum=0
        for x,y in self.categorized_days.items():
            print(f'Temperature day [{cnt}] = {x} Celcius {y}')
            sum += int(x)
            cnt+=1
        
        avg= int(sum / (cnt-1))
        print(f'\nThe average Temp for {cnt-1} days = {avg} Celcius')
        print(f'Number of hot days       = {self.no_of_categorized_day["hot"]} day/s')
        print(f'Number of pleasant days  = {self.no_of_categorized_day["pleasant"]} day/s')
        print(f'Number of cold days      = {self.no_of_categorized_day["cold"]} day/s')

        
        
if __name__ == "__main__":
    temp = Temperature()
    temp.output()

