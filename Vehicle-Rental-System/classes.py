class VehicleRentalSystem:
  def val(self):
    with open("vehicles.txt","r") as file:
      data= file.readlines()
      lastline=data[-1]
      x=lastline.strip().split("|")
      return (int(x[0])+1)
    
  def view_vehicle(self):
      with open("vehicles.txt","r") as file:
        data=file.readlines()
        for lines in data:
          x=lines.strip().split('|')
          print(f"Vehicle Id: {x[0]}")
          print(f"Vehicle Type: {x[1]}")
          print(f"Brand: {x[2]}")
          print(f"Model: {x[3]}")
          print(f"Price(per-day): {x[4]}")
          print(f"Availabilty: {x[5]}")
          print()
          
          
  def search_vehicle(self,search):
    with open("vehicles.txt","r") as file:
      data=file.readlines()
      found=False
      for lines in data:
        x=lines.strip().split('|')
        if search.upper()==x[0].upper() or search.upper()==x[3].upper():
          print(f"\nVehicle Id: {x[0]}")
          print(f"Vehicle Type: {x[1]}")
          print(f"Brand: {x[2]}")
          print(f"Model: {x[3]}")
          print(f"Price(per-day): {x[4]}")
          print(f"Availabilty: {x[5]}")
          print()
          found=True
      if found==False:
        print("\nNo such vehicle in the directory")
        
        
      










class Vehicle:
  def __init__(self,vehicle_id,vehicle_type,brand,model,price_per_day,available):
    self.vehicle_id=vehicle_id
    self.vehicle_type=vehicle_type
    self.brand=brand
    self.model=model
    self.price_per_day=price_per_day
    self.available=available
    
  def display_details(self):
    print(f"\nVehicle id: {self.vehicle_id}")
    print(f"Vehicle Type: {self.vehicle_type}")
    print(f"Brand: {self.brand}")
    print(f"Model: {self.model}")
    print(f"Price(per-day) :{self.price_per_day}")
    print(f"Availability :{self.available}")
    
  def add_vehicle(self):
    string="\n"+str(self.vehicle_id)+"|"+self.vehicle_type+"|"+self.brand+"|"+self.model+"|"+str(self.price_per_day)+"|"+str(self.available)
    with open("vehicles.txt","a") as file:
      file.write(string)
      
      
  