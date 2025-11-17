import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page configuration
st.set_page_config(page_title="Flight Pricing Calculator", page_icon="✈️", layout="wide")

# Title and description
st.title("✈️ Flight Seat Pricing Model")
st.markdown("**Adjust the factors below to see how they affect seat pricing and revenue**")

# Pricing calculation function
def calculate_price(base_fare, days_until_departure, seats_filled, total_seats, 
                   flight_duration, season_multiplier, competitor_price, demand_index):
    """
    Calculate flight seat price based on multiple factors
    """
    # 1. Start with base fare
    price = base_fare
    
    # 2. Time-based pricing (dynamic pricing based on booking window)
    if days_until_departure <= 7:
        # Last week surge
        time_multiplier = 1.5 + (7 - days_until_departure) * 0.1
    elif days_until_departure <= 21:
        # Medium advance booking
        time_multiplier = 1.2 + (21 - days_until_departure) * 0.02
    else:
        # Early bird discount
        time_multiplier = 1.0 - (days_until_departure - 21) * 0.005
    
    price *= max(0.8, time_multiplier)  # Floor at 80% of base
    
    # 3. Capacity-based pricing (yield management)
    occupancy_rate = (seats_filled / total_seats) * 100
    
    if occupancy_rate < 50:
        capacity_multiplier = 0.9  # Discount for low occupancy
    elif occupancy_rate < 70:
        capacity_multiplier = 1.0 + (occupancy_rate - 50) * 0.01
    else:
        capacity_multiplier = 1.2 + (occupancy_rate - 70) * 0.02
    
    price *= capacity_multiplier
    
    # 4. Flight duration pricing
    price += flight_duration * 25  # Add $25 per hour
    
    # 5. Seasonal demand multiplier
    price *= season_multiplier
    
    # 6. Competitive pricing adjustment
    competitive_diff = (price - competitor_price) / competitor_price
    if competitive_diff > 0.15:
        price *= 0.95  # Lower price if 15% above competitors
    
    # 7. Overall demand index
    price *= demand_index
    
    # 8. Minimum price floor (operational costs)
    min_price = base_fare * 0.6
    price = max(min_price, price)
    
    return round(price, 2)

# Create three columns for the main metrics
col1, col2, col3 = st.columns(3)

# Sidebar for all input sliders
st.sidebar.header("📊 Pricing Factors")

# Input sliders
base_fare = st.sidebar.slider("💵 Base Fare ($)", 100, 500, 200, 10)
days_until_departure = st.sidebar.slider("📅 Days Until Departure", 1, 90, 30, 1)
total_seats = st.sidebar.slider("✈️ Total Seats (Capacity)", 50, 400, 180, 10)
seats_filled = st.sidebar.slider("👥 Seats Filled", 0, total_seats, 50, 1)
flight_duration = st.sidebar.slider("⏱️ Flight Duration (hours)", 1.0, 15.0, 3.0, 0.5)
season_multiplier = st.sidebar.slider("🌡️ Seasonal Demand Multiplier", 0.7, 1.8, 1.0, 0.1)
competitor_price = st.sidebar.slider("🏢 Competitor Average Price ($)", 100, 600, 250, 10)
demand_index = st.sidebar.slider("📈 Overall Demand Index", 0.5, 2.0, 1.0, 0.1)

# Calculate price and metrics
final_price = calculate_price(base_fare, days_until_departure, seats_filled, total_seats,
                              flight_duration, season_multiplier, competitor_price, demand_index)
occupancy_rate = (seats_filled / total_seats) * 100
current_revenue = final_price * seats_filled
potential_max_revenue = final_price * total_seats

# Display main metrics
with col1:
    st.metric("💰 Current Seat Price", f"${final_price:,.2f}")

with col2:
    st.metric("📊 Occupancy Rate", f"{occupancy_rate:.1f}%")

with col3:
    st.metric("💵 Current Revenue", f"${current_revenue:,.2f}")

st.divider()

# Additional info
col4, col5 = st.columns(2)

with col4:
    st.metric("🎯 Potential Max Revenue (if full)", f"${potential_max_revenue:,.2f}")

with col5:
    profit_margin = ((final_price - base_fare) / base_fare) * 100
    st.metric("📈 Profit Margin", f"{profit_margin:.1f}%")

st.divider()

# Formula explanation
with st.expander("📖 Pricing Formula Breakdown"):
    st.markdown("""
    ### How the Price is Calculated:
    
    1. **Base Fare:** Starting price covering operational costs
    
    2. **Time Multiplier:** 
       - 45+ days: Early bird discounts (up to 20% off)
       - 21-44 days: Normal pricing
       - 7-20 days: Gradual increase
       - 0-7 days: Last-minute surge (up to 50% premium)
    
    3. **Capacity Pricing (Yield Management):**
       - < 50% full: 10% discount to fill seats
       - 50-70% full: Gradual price increase
       - > 70% full: Sharp increase (scarcity pricing)
    
    4. **Duration Fee:** +$25 per flight hour
    
    5. **Seasonal Adjustment:** Peak/off-season multiplier
    
    6. **Competitive Adjustment:** -5% if priced >15% above competitors
    
    7. **Demand Index:** Overall market demand multiplier
    
    8. **Price Floor:** Minimum 60% of base fare to cover costs
    """)

# Visualization section
st.divider()
st.subheader("📊 Price Sensitivity Analysis")

# Create tabs for different visualizations
tab1, tab2, tab3 = st.tabs(["Days Until Departure", "Occupancy Rate", "Demand Impact"])

with tab1:
    # Price vs Days Until Departure
    days_range = np.arange(1, 91)
    prices_by_days = [calculate_price(base_fare, d, seats_filled, total_seats,
                                     flight_duration, season_multiplier, 
                                     competitor_price, demand_index) for d in days_range]
    
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(days_range, prices_by_days, linewidth=2, color='#4CAF50')
    ax1.axvline(x=days_until_departure, color='red', linestyle='--', label='Current')
    ax1.set_xlabel('Days Until Departure', fontsize=12)
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.set_title('Price vs Booking Window', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    st.pyplot(fig1)
    
    st.info("💡 Notice how prices drop for early bookings and surge as departure approaches!")

with tab2:
    # Price vs Occupancy Rate
    occupancy_range = np.arange(0, total_seats + 1)
    prices_by_occupancy = [calculate_price(base_fare, days_until_departure, s, total_seats,
                                          flight_duration, season_multiplier,
                                          competitor_price, demand_index) for s in occupancy_range]
    
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(occupancy_range, prices_by_occupancy, linewidth=2, color='#2196F3')
    ax2.axvline(x=seats_filled, color='red', linestyle='--', label='Current')
    ax2.set_xlabel('Seats Filled', fontsize=12)
    ax2.set_ylabel('Price ($)', fontsize=12)
    ax2.set_title('Price vs Occupancy (Yield Management)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    st.pyplot(fig2)
    
    st.info("💡 Prices increase sharply above 70% capacity - classic yield management!")

with tab3:
    # Revenue vs Demand Index
    demand_range = np.linspace(0.5, 2.0, 50)
    revenue_by_demand = [calculate_price(base_fare, days_until_departure, seats_filled, total_seats,
                                        flight_duration, season_multiplier,
                                        competitor_price, d) * seats_filled for d in demand_range]
    
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(demand_range, revenue_by_demand, linewidth=2, color='#FF9800')
    ax3.axvline(x=demand_index, color='red', linestyle='--', label='Current')
    ax3.set_xlabel('Demand Index', fontsize=12)
    ax3.set_ylabel('Revenue ($)', fontsize=12)
    ax3.set_title('Revenue vs Market Demand', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    st.pyplot(fig3)
    
    st.info("💡 Higher demand = higher revenue potential. Monitor market conditions!")

# Footer
st.markdown("---")
st.markdown("**💼 Business Insights:** Use this model to optimize pricing strategy based on real-time factors!")