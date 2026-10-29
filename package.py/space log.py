class CargoManifest:
    """Manages payload items destined for orbital insertion."""
    
    def __init__(self, target_orbit: str):
        self.target_orbit = target_orbit
        self.items = {}
        
    def add_item(self, item_name: str, weight_kg: float):
        """Adds a cargo item with its weight in kilograms."""
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero.")
        self.items[item_name] = self.items.get(item_name, 0) + weight_kg
        
    def get_total_weight(self) -> float:
        """Returns the total weight of the manifest."""
        return sum(self.items.values())
