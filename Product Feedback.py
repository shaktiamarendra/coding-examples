"""
Python program that takes product feedback as input, 
processes it, and allows ordering products based on their feedback scores.

Features:
Supports adding feedback for products.

Orders products by feedback score.

Displays products in sorted order (ascending or descending)."""

class ProductFeedback:
    def __init__(self):
        self.feedback_data = {}

    def add_feedback(self, product_name: str, score: float):
        """Adds or updates feedback score for a product."""
        if product_name in self.feedback_data:
            self.feedback_data[product_name].append(score)
        else:
            self.feedback_data[product_name] = [score]
    
    def get_ordered_products(self, descending=True):
        """Returns products ordered by average feedback score, then alphabetically."""
        sorted_products = sorted(
            self.feedback_data.items(), #.items() converts dictionary into a list of tuples where each tuple has the format: ("product_name", [list_of_feedback_scores]).This is needed as Sorting a dictionary directly is not possible because dictionaries don't have a built-in sorting method.The .items() method converts a dictionary into a list of (key, value) tuples, which allows sorting based on custom criteria
            # This function takes an item from self.feedback_data.items(), e.g., ("Laptop", [4.5, 4.0]). item[1] refers to the list of feedback scores. sum(item[1]) / len(item[1]) computes the average feedback score for the product.Using -sum() ensures his ensures highest feedback scores come first, while still using alphabetical ordering in case of ties.
            key=lambda item: (-sum(item[1]) / len(item[1]), item[0]) if descending 
                            else (sum(item[1]) / len(item[1]), item[0])
        )
        # Convert back to a dictionary (maintains order in Python 3.7+)
        return dict(sorted_products)

    def display_products(self, descending=True):
        """Prints the sorted dictionary of feedback."""
        sorted_feedback = self.get_ordered_products(descending)
        print("\nProducts ordered by feedback score (then alphabetically if tied):")
        for product, scores in sorted_feedback.items():
            avg_score = sum(scores) / len(scores)
            print(f"{product}: {avg_score:.2f} (Based on {len(scores)} reviews)")

# Example Usage:
if __name__ == "__main__":
    pf = ProductFeedback()
    
    # Asking feedback from user
    while True:
        # Taking input from user
        user_input = input("Enter product name and feedback (or type 'Enough' to stop): ").rsplit(maxsplit=1) #rsplit is used to take care of whitespaces in the product names
        
        # Check for exit condition
        if user_input[0].strip().lower() == "enough":
            break
        
        if len(user_input) < 2:
           print("Invalid input! Please enter the product name followed by a numerical feedback score.")
        else:
           prod, feedback = user_input[0], user_input[1]
        try:
           feedback = float(feedback)
           print(f"Product: {prod}, Feedback: {feedback}")
        except ValueError:
           print("Invalid feedback score! Please enter a number.")
    # Add the user-entered details in dictionary
        pf.add_feedback(prod, feedback) 

    # Adding feedback
    pf.add_feedback("TV Channels", 4.5)
    pf.add_feedback("TV Channels", 3.4)
    pf.add_feedback("OTT", 4)
    pf.add_feedback("OTT", 2.8)
    pf.add_feedback("Smartphone", 4.8)
    pf.add_feedback("Smartphone", 4.7)
    pf.add_feedback("Headphones", 5.4)
    pf.add_feedback("Headphones", 4.1)

    # Display products sorted by feedback
    pf.display_products(descending=True)
