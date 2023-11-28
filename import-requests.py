import requests 

class CatFactsAPI:
    def __init__(self):
        self.api_url = "https://catfact.ninja/breeds"

    def get_cat_breed_by_index(self, n):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Check for request errors

            data = response.json()
            
            # Check if 'data' is present in the response
            if 'data' in data:
                cat_breeds = data['data']
                
                # Check if the index is within the range of available cat breeds
                if 1 <= n <= len(cat_breeds):
                    return cat_breeds[n - 1]['breed']
                else:
                    return f"Error: Index out of range. There are {len(cat_breeds)} cat breeds available."
            else:
                return "Error: 'data' field not found in API response."

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

# Example usage:
cat_facts_api = CatFactsAPI()
breed_index = 7  # Replace with the desired index
result = cat_facts_api.get_cat_breed_by_index(breed_index)

# Print the result
if result:
    print(f"The {breed_index}th cat breed is: {result}")
else:
    print("Failed to retrieve cat breed information.")
