import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
calculate_roofing_material_cost():
    try:
        # Input the total roof area in square feet
        roof_area = float(input("Enter the total roof area in square feet: "))

        # Waste factors (can be adjusted if needed)
        shingle_waste_factor = 0.10  # 10% waste for shingles
        underlayment_waste_factor = 0.05  # 5% waste for underlayment

        # Shingles
        cost_per_square = float(input("Enter the cost per square (100 sq ft) of shingles: "))
        total_shingle_area = roof_area * (1 + shingle_waste_factor)
        number_of_squares = total_shingle_area / 100
        total_shingle_cost = number_of_squares * cost_per_square

        # Starter Shingles
        perimeter_length = float(input("Enter the total length of eaves and rakes (in linear feet): "))
        cost_per_linear_foot_starter = float(input("Enter the cost per linear foot of starter shingles: "))
        total_starter_cost = perimeter_length * cost_per_linear_foot_starter

        # Ice & Water Shield
        valley_length = float(input("Enter the total length of valleys (in linear feet): "))
        ice_water_shield_width = 3  # Assuming 3-foot-wide rolls
        ice_water_shield_area = valley_length * ice_water_shield_width
        cost_per_square_ice_water = float(input("Enter the cost per square (100 sq ft) of ice & water shield: "))
        total_ice_water_cost = (ice_water_shield_area / 100) * cost_per_square_ice_water

        # Underlayment
        cost_per_square_underlayment = float(input("Enter the cost per square (100 sq ft) of underlayment: "))
        total_underlayment_area = roof_area * (1 + underlayment_waste_factor)
        total_underlayment_cost = (total_underlayment_area / 100) * cost_per_square_underlayment

        # Ridge Shingles
        ridge_length = float(input("Enter the total length of ridges and hips (in linear feet): "))
        cost_per_linear_foot_ridge = float(input("Enter the cost per linear foot of ridge shingles: "))
        total_ridge_cost = ridge_length * cost_per_linear_foot_ridge

        # Cobra Vents
        cost_per_linear_foot_cobra = float(input("Enter the cost per linear foot of cobra vents: "))
        total_cobra_vent_cost = ridge_length * cost_per_linear_foot_cobra

        # O'Hagin Vents
        number_of_ohagin_vents = int(input("Enter the number of O'Hagin vents needed: "))
        cost_per_ohagin_vent = float(input("Enter the cost per O'Hagin vent: "))
        total_ohagin_vent_cost = number_of_ohagin_vents * cost_per_ohagin_vent

        # Flashings
        number_of_flashings = int(input("Enter the number of flashings needed: "))
        cost_per_flashing = float(input("Enter the cost per flashing: "))
        total_flashing_cost = number_of_flashings * cost_per_flashing

        # Gutters
        gutter_length = float(input("Enter the total length of gutters (in linear feet): "))
        cost_per_linear_foot_gutter = float(input("Enter the cost per linear foot of gutters: "))
        total_gutter_cost = gutter_length * cost_per_linear_foot_gutter

        # Edge Metal
        cost_per_linear_foot_edge_metal = float(input("Enter the cost per linear foot of edge metal: "))
        total_edge_metal_cost = perimeter_length * cost_per_linear_foot_edge_metal

        # Paint
        number_of_paint_cans = int(input("Enter the number of paint cans needed: "))
        cost_per_paint_can = float(input("Enter the cost per paint can: "))
        total_paint_cost = number_of_paint_cans * cost_per_paint_can

        # Gutter Guards
        cost_per_linear_foot_gutter_guard = float(input("Enter the cost per linear foot of gutter guards: "))
        total_gutter_guard_cost = gutter_length * cost_per_linear_foot_gutter_guard

        # Metal Valleys
        cost_per_linear_foot_valley = float(input("Enter the cost per linear foot of metal valleys: "))
        total_valley_cost = valley_length * cost_per_linear_foot_valley

        # Calculate total cost
        total_material_cost = (
            total_shingle_cost +
            total_starter_cost +
            total_ice_water_cost +
            total_underlayment_cost +
            total_ridge_cost +
            total_cobra_vent_cost +
            total_ohagin_vent_cost +
            total_flashing_cost +
            total_gutter_cost +
            total_edge_metal_cost +
            total_paint_cost +
            total_gutter_guard_cost +
            total_valley_cost
        )

        # Display the breakdown of costs
        print("\n--- Material Cost Breakdown ---")
        print(f"Shingles: ${total_shingle_cost:.2f}")
        print(f"Starter Shingles: ${total_starter_cost:.2f}")
        print(f"Ice & Water Shield: ${total_ice_water_cost:.2f}")
        print(f"Underlayment: ${total_underlayment_cost:.2f}")
        print(f"Ridge Shingles: ${total_ridge_cost:.2f}")
        print(f"Cobra Vents: ${total_cobra_vent_cost:.2f}")
        print(f"O'Hagin Vents: ${total_ohagin_vent_cost:.2f}")
        print(f"Flashings: ${total_flashing_cost:.2f}")
        print(f"Gutters: ${total_gutter_cost:.2f}")
        print(f"Edge Metal: ${total_edge_metal_cost:.2f}")
        print(f"Paint: ${total_paint_cost:.2f}")
        print(f"Gutter Guards: ${total_gutter_guard_cost:.2f}")
        print(f"Metal Valleys: ${total_valley_cost:.2f}")
        print(f"\nTotal Material Cost: ${total_material_cost:.2f}")

    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_roofing_material_cost()
