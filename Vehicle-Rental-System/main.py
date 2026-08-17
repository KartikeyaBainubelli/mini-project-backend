from classes import VehicleRentalSystem
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
        veho=VehicleRentalSystem()
        vehicle_id=veho.val()
        vehicle_type=input("\nEnter the type of vehicle: ")
        brand=input("Enter the brand of the vehicle: ")
        model=input("Enter the model of the vehicle: ")
        price=int(input("Enter the price per day:"))
        vehi=Vehicle(vehicle_id,vehicle_type,brand,model,price,True)
        vehi.add_vehicle()
        
        
      case 2:
        vehw=VehicleRentalSystem()
        vehw.view_vehicle()
        
      case 3:
        search=input("Enter vehicle id or model :")
        vehw=VehicleRentalSystem()
        vehw.search_vehicle(search)
        
      # case 4:
      #   print(400)
      #   value=i
        
      # case 5:
      #   print(500)
        
      case 6:
        vehicle_id=input("\nEnter the id of the vehicle you want to update")
        vehicle_type=input("Update- type of vehicle: ")
        brand=input("Update- brand of the vehicle: ")
        model=input("Update- model of the vehicle: ")
        price=input("Update- price per day: ")
        available=input("Update- Availability of vehicle: ")
        vehi=Vehicle(vehicle_id,vehicle_type,brand,model,price,available)
        vehi.update_vehicle()
        
      case 7:
        vehicle_id=input("enter vehicle_id to delete the vehicle data: ")
        vehi=VehicleRentalSystem()
        vehi.delete_vehicle(vehicle_id)
        
      # case 8:
      #   print(800)
        
      case 9:
        break
        
      case _:
        print("\nInvalid number")
  except ValueError:
    print("\nEnter valid input")
    