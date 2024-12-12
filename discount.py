
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
     
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
       
        return price


def advanced_discount_calculator():
    while True:
        try:
         
            original_price = float(input("Enter the original price of the item: $"))
            discount_percentage = float(input("Enter the discount percentage: "))
            
            
            if original_price < 0 or discount_percentage < 0:
                print("Price and discount percentage must be non-negative.")
                continue
            
          
            final_price = calculate_discount(original_price, discount_percentage)
            
          
            print("\n--- Discount Details ---")
            print(f"Original Price: ${original_price:.2f}")
            print(f"Discount Percentage: {discount_percentage}%")
            print(f"Final Price: ${final_price:.2f}")
            
           
            another = input("\nCalculate another discount? (yes/no): ").lower()
            if another != 'yes':
                break
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")


class DiscountCalculator:
    def __init__(self):
        self.discount_history = []
    
    def calculate_discount(self, price, discount_percent):
       
        if price < 0 or discount_percent < 0:
            raise ValueError("Price and discount must be non-negative")
        
        discount_percent = min(discount_percent, 100)
        
        
        if discount_percent >= 20:
            discount_amount = price * (discount_percent / 100)
            final_price = price - discount_amount
       
            result = {
                "original_price": price,
                "discount_percent": discount_percent,
                "discount_amount": discount_amount,
                "final_price": final_price
            }
            
            self.discount_history.append(result)
            return result
        
        return {"original_price": price, "final_price": price}
    
    def display_history(self):
        """Display discount calculation history"""
        print("\n--- Discount Calculation History ---")
        for idx, entry in enumerate(self.discount_history, 1):
            print(f"\nCalculation {idx}:")
            print(f"Original Price: ${entry['original_price']:.2f}")
            print(f"Discount: {entry.get('discount_percent', 0)}%")
            print(f"Final Price: ${entry['final_price']:.2f}")


def main():
   
    print("\n--- Simple Discount Calculator ---")
    original_price = float(input("Enter the original price: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount_percentage)
    print(f"\nFinal Price: ${final_price:.2f}")

    
    print("\n--- Advanced Discount Calculator ---")
    advanced_discount_calculator()

    
    print("\n--- Object-Oriented Discount Calculator ---")
    calculator = DiscountCalculator()
    
    while True:
        try:
            price = float(input("Enter product price: $"))
            discount = float(input("Enter discount percentage: "))
            
            result = calculator.calculate_discount(price, discount)
            
            print("\n--- Discount Result ---")
            print(f"Original Price: ${result['original_price']:.2f}")
            print(f"Discount: {result.get('discount_percent', 0)}%")
            print(f"Final Price: ${result['final_price']:.2f}")
            
            view_history = input("\nView calculation history? (yes/no): ").lower()
            if view_history == 'yes':
                calculator.display_history()
            
            another = input("\nCalculate another discount? (yes/no): ").lower()
            if another != 'yes':
                break
        
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()