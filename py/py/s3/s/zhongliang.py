def weight_on_planets(years):
    if not isinstance(years, int) or years <= 0:
        raise ValueError("Years must be a positive integer.")

    initial_weight = 60  # 假设初始体重为60kg
    weight_increase_per_year = 0.5
    earth_gravity = 9.8
    moon_gravity = 1.62

    results = []
    for year in range(1, years + 1):
        weight = initial_weight + (year - 1) * weight_increase_per_year
        weight_earth = weight * earth_gravity
        weight_moon = weight * moon_gravity
        print(f"Year {year}: Earth Weight = {weight_earth:.2f} N, Moon Weight = {weight_moon:.2f} N")
        results.append((year, weight_earth, weight_moon))

    return results


# 输出未来10年的体重状况
weight_on_planets(10)
