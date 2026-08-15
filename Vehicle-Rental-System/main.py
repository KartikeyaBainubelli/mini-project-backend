from classes import VehicleId
from classes import Vehicle


while True:
  print("----- VEHICLE RENTAL SYSTEM -----")
  print()
  print("1. Add Vehicle")
  print("2. View Vehicles")
  print("3. Search Vehicle")
  print("4. Rent Vehicle")
  print("5. Return Vehicle")
  print("6. Update Vehicle")
  print("7. Delete Vehicle")
  print("8. Calculate Rental Cost")
  print("9. Exit")
  print()
  
  try:
    choice=int(input("Enter your choice from (1-9):"))
    
    match choice:
      
      case 1:
        vehicle_id=VehicleId.val()
        vehicle_type=input("\nEnter the type of vehicle: ")
        brand=input("Enter the brand of the vehicle: ")
        model=input("Enter the model of the vehicle: ")
        price=int(input("Enter the price per day:"))
        Vehicle.add_vehicle(vehicle_id,vehicle_type,brand,model,price,True)
        
        
      # case 2:
      #   print(200)
        
      # case 3:
      #   print(300)
        
      # case 4:
      #   print(400)
      #   value=int(input("Enter the number of days you want to rent: "))
        
      # case 5:
      #   print(500)
        
      # case 6:
      #   print(600)
        
      # case 7:
      #   print(700)
        
      # case 8:
      #   print(800)
        
      case 9:
        break
        
      case _:
        print("\nInvalid number")
  except ValueError:
    print("\nEnter valid input")
    