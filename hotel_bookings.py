import pandas as pd
pd.set_option("display.max_columns", None)

hotel = pd.read_csv("data/hotel_bookings.csv")

print(hotel.shape)
hotel.info()
print(hotel.isnull().sum()[hotel.isnull().sum() > 0])
print(hotel["is_canceled"].value_counts(normalize=True))