# Import necessary libraries
import math                # Provides access to mathematical functions
import numpy as np         # NumPy library for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for plotting graphs
from scipy.stats import norm     # Import norm for normal distribution functions

# Define the black_scholes function to calculate option prices
def black_scholes(S, K, T, r, sigma, option_type='call', dividend_yield=0):
    """
    Calculate the Black-Scholes option price.

    Parameters:
    S (float): Current stock price
    K (float): Strike price of the option
    T (float): Time to maturity of the option in years
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying stock
    option_type (str): Type of option - 'call' or 'put'
    dividend_yield (float): Continuous dividend yield (default is 0)

    Returns:
    float: Calculated price of the option
    """
    # Calculate d1 and d2 using the Black-Scholes formula components
    d1 = (math.log(S / K) + (r - dividend_yield + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Calculate option price based on the type (call or put)
    if option_type == 'call':
        price = S * np.exp(-dividend_yield * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-dividend_yield * T) * norm.cdf(-d1)
    else:
        # Raise an error if the option type is neither call nor put
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return price

# Define a function to plot option prices against stock prices
def plot_option_price(S_range, K, T, r, sigma, option_type, dividend_yield):
    """
    Plot the option price against a range of stock prices.

    Parameters:
    S_range (np.array): Range of stock prices for plotting
    K (float): Strike price of the option
    T (float): Time to maturity of the option in years
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying stock
    option_type (str): Type of option - 'call' or 'put'
    dividend_yield (float): Continuous dividend yield

    This function does not return a value; it plots the graph directly.
    """
    # Calculate option prices for each stock price in the range
    prices = [black_scholes(S, K, T, r, sigma, option_type, dividend_yield) for S in S_range]

    # Set up the plot
    plt.figure(figsize=(10, 6))
    plt.plot(S_range, prices, label=f'{option_type.title()} Option Price')
    plt.title(f'{option_type.title()} Option Price vs Stock Price')
    plt.xlabel('Stock Price')
    plt.ylabel('Option Price')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage of the functions defined above
# Setting up parameters for the example
S_range = np.linspace(50, 150, 100)  # Range of stock prices
K = 100  # Strike price
T = 1    # Time to maturity (1 year)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2       # Stock volatility (20%)
dividend_yield = 0.02  # Dividend yield (2%)

# Plotting call and put option prices using the defined function
plot_option_price(S_range, K, T, r, sigma, 'call', dividend_yield)
plot_option_price(S_range, K, T, r, sigma, 'put', dividend_yield)
