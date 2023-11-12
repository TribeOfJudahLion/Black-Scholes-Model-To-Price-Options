<br/>
<p align="center">
  <h3 align="center">Unlock Market Potential with Precision: The Black-Scholes Option Valuator</h3>

  <p align="center">
    Price with Confidence: Harness the Power of Black-Scholes for Smart Option Strategies
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Statement:

An investment analyst needs to understand the potential value of European options for a given stock to inform trading strategies for their clients. The stock is currently trading at $100 and is known for its stability, which suggests a lower volatility. However, the analyst wants to account for various scenarios where the stock price can range from $50 to $150 to see how it impacts the option values. The analyst is considering options with a strike price of $100 that will expire in one year. The current risk-free interest rate is 5%, and the stock has an annual dividend yield of 2%. The analyst requires a model that can calculate the price of both call and put options for the stock across the price range and visualize these prices to better communicate the findings with the clients.

### Solution:

We can use the provided Black-Scholes model to calculate the prices of European call and put options for the given stock. Here's how the solution would be structured using the provided Python code:

1. **Parameter Setup**: Set the current stock price `S` to $100, the strike price `K` also to $100, the time to maturity `T` to 1 year, the risk-free interest rate `r` to 5%, the volatility `sigma` (a measure of stability) to a conservative estimate of 20%, and the dividend yield to 2%.

2. **Price Calculation**:
   - Use the `black_scholes` function to calculate option prices for both call and put options.
   - The function calculates `d1` and `d2`, which are intermediaries based on the Black-Scholes formula, incorporating the time value of money and the probability factors for the stock price finishing in the money.
   - For the call option, the function evaluates the difference between the present value of buying the stock at the strike price (when beneficial) and the current stock price.
   - For the put option, it evaluates the difference between the strike price and the present value of the stock price (when beneficial).

3. **Visualization**:
   - Use the `plot_option_price` function to generate a graph plotting the calculated option prices across a range of stock prices from $50 to $150.
   - The graph provides a visual representation of how the option prices vary with the stock price, showing the value of the options at different potential future prices of the underlying stock.

### Execution:

By running the provided code with the specified parameters, the analyst would obtain two plots showing the call and put option prices against the stock price range.

1. **Call Option Plot**: This plot will show the analyst that as the stock price increases, the value of the call option also increases, particularly as it moves above the strike price of $100.

2. **Put Option Plot**: This plot will indicate that as the stock price decreases, the value of the put option increases, with the most significant gains as the stock price moves below the strike price.

### Conclusion:

The Black-Scholes model, as implemented in the provided Python code, allows the analyst to conclude that:

- The call option has higher value when the market expects the stock price to rise above the strike price, which would be beneficial for clients with a bullish outlook on the stock.
- The put option is more valuable when the market expects the stock price to fall below the strike price, useful for clients with a bearish outlook or those seeking to hedge against a drop in the stock price.

The analyst can now present these findings with the generated plots to provide a clear and visual explanation of the options' potential values under various market conditions.

The provided Python code is an implementation of the Black-Scholes model, an influential formula for the valuation of options. The code defines two primary functions, `black_scholes` and `plot_option_price`. Let's break down each component of the code for a comprehensive understanding.

### `black_scholes` Function

1. **Parameters**:
   - `S` (current stock price): The market price of the underlying asset (e.g., a stock).
   - `K` (strike price): The price at which the option can be exercised.
   - `T` (time to maturity): The time remaining until the option's expiration, expressed in years.
   - `r` (risk-free interest rate): The theoretical rate of return of an investment with zero risk, used to discount the option's payoff.
   - `sigma` (volatility): A measure of the amount of fluctuation in the price of the underlying asset.
   - `option_type`: Determines whether the option is a call or a put.
   - `dividend_yield`: The annual dividend rate of the underlying asset, expressed as a continuous yield.

2. **Black-Scholes Formula**:
   - The formula calculates two values, `d1` and `d2`, using the input parameters. These are intermediate variables used in the Black-Scholes formula.
   - For a call option, the price is calculated using `S * np.exp(-dividend_yield * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)`.
   - For a put option, the formula is `K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-dividend_yield * T) * norm.cdf(-d1)`.
   - `norm.cdf` is the cumulative distribution function of the standard normal distribution, used to model the probabilities of the underlying asset's price movements.

### `plot_option_price` Function

1. **Parameters**:
   - `S_range`: An array of stock prices for which the option price will be plotted.
   - `K`, `T`, `r`, `sigma`, `option_type`, `dividend_yield`: Same as in `black_scholes`.

2. **Plotting Logic**:
   - The function calculates the option price for each stock price in `S_range` using the `black_scholes` function.
   - It then plots these prices against the stock prices on a graph, with option price on the y-axis and stock price on the x-axis.

3. **Visualization**:
   - The graph helps visualize how the option price varies with the stock price, which is crucial for understanding the sensitivity of the option value to changes in the underlying asset's price.

### Example Usage

The code sets up a scenario with given values for `S_range`, `K`, `T`, `r`, `sigma`, and `dividend_yield`. It then calls `plot_option_price` for both a call and a put option, resulting in two graphs that show how the prices of these options vary with the stock price.

### Key Concepts

- **Call vs. Put Options**: Call options give the holder the right to buy the underlying asset at the strike price, while put options give the right to sell.
- **Impact of Parameters**: The model shows how option prices are sensitive to changes in parameters like the underlying asset's price, time to maturity, volatility, and the risk-free rate.
- **Dividend Yield**: The inclusion of dividend yield allows for a more realistic model, especially for assets that pay dividends.
- **Risk and Volatility**: The model's heavy reliance on volatility (`sigma`) highlights the importance of risk in option pricing.

This code provides a robust tool for visualizing and understanding option pricing dynamics according to the Black-Scholes model, a cornerstone of modern financial theory.

The provided Python code is an implementation of the Black-Scholes model, an influential formula for the valuation of options. The code defines two primary functions, `black_scholes` and `plot_option_price`. Let's break down each component of the code for a comprehensive understanding.

### `black_scholes` Function

1. **Parameters**:
   - `S` (current stock price): The market price of the underlying asset (e.g., a stock).
   - `K` (strike price): The price at which the option can be exercised.
   - `T` (time to maturity): The time remaining until the option's expiration, expressed in years.
   - `r` (risk-free interest rate): The theoretical rate of return of an investment with zero risk, used to discount the option's payoff.
   - `sigma` (volatility): A measure of the amount of fluctuation in the price of the underlying asset.
   - `option_type`: Determines whether the option is a call or a put.
   - `dividend_yield`: The annual dividend rate of the underlying asset, expressed as a continuous yield.

2. **Black-Scholes Formula**:
   - The formula calculates two values, `d1` and `d2`, using the input parameters. These are intermediate variables used in the Black-Scholes formula.
   - For a call option, the price is calculated using `S * np.exp(-dividend_yield * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)`.
   - For a put option, the formula is `K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-dividend_yield * T) * norm.cdf(-d1)`.
   - `norm.cdf` is the cumulative distribution function of the standard normal distribution, used to model the probabilities of the underlying asset's price movements.

### `plot_option_price` Function

1. **Parameters**:
   - `S_range`: An array of stock prices for which the option price will be plotted.
   - `K`, `T`, `r`, `sigma`, `option_type`, `dividend_yield`: Same as in `black_scholes`.

2. **Plotting Logic**:
   - The function calculates the option price for each stock price in `S_range` using the `black_scholes` function.
   - It then plots these prices against the stock prices on a graph, with option price on the y-axis and stock price on the x-axis.

3. **Visualization**:
   - The graph helps visualize how the option price varies with the stock price, which is crucial for understanding the sensitivity of the option value to changes in the underlying asset's price.

### Example Usage

The code sets up a scenario with given values for `S_range`, `K`, `T`, `r`, `sigma`, and `dividend_yield`. It then calls `plot_option_price` for both a call and a put option, resulting in two graphs that show how the prices of these options vary with the stock price.

### Key Concepts

- **Call vs. Put Options**: Call options give the holder the right to buy the underlying asset at the strike price, while put options give the right to sell.
- **Impact of Parameters**: The model shows how option prices are sensitive to changes in parameters like the underlying asset's price, time to maturity, volatility, and the risk-free rate.
- **Dividend Yield**: The inclusion of dividend yield allows for a more realistic model, especially for assets that pay dividends.
- **Risk and Volatility**: The model's heavy reliance on volatility (`sigma`) highlights the importance of risk in option pricing.

This code provides a robust tool for visualizing and understanding option pricing dynamics according to the Black-Scholes model, a cornerstone of modern financial theory.

The output results are two graphs generated by the `plot_option_price` function from the Python code provided. These graphs plot the prices of call and put options, respectively, against varying stock prices within a specified range.

### Call Option Price vs. Stock Price Graph

The first graph shows the relationship between the call option price and the stock price. This relationship is generally positive and nonlinear:

- When the stock price is significantly below the strike price (left side of the graph), the call option price is low because the likelihood of the option being exercised profitably is small.
- As the stock price increases, the call option price also rises, reflecting the increased probability that the option will be "in the money" (where the stock price is above the strike price).
- Near and beyond the strike price, the slope of the curve increases sharply, indicating a greater sensitivity of the option price to changes in the stock price. This is because as the stock price moves above the strike price, the option has intrinsic value equal to the difference between the stock price and the strike price.
- Far above the strike price, the option price continues to increase but at a steadier rate as the option is deep "in the money," and its price starts to move dollar for dollar with the stock price.

### Put Option Price vs. Stock Price Graph

The second graph illustrates the relationship between the put option price and the stock price. This relationship is generally negative:

- When the stock price is high (right side of the graph), the put option price is low because the chance of the option being exercised profitably is small; the market does not expect the stock price to fall below the strike price.
- As the stock price decreases, the put option price increases because the likelihood of the option being "in the money" (where the stock price is below the strike price) is higher.
- The most significant increase in the put option price happens as the stock price approaches the strike price from the right. This is where the option starts to gain intrinsic value, which is the difference between the strike price and the lower stock price.
- When the stock price is significantly below the strike price (left side of the graph), the put option price increases at a slower rate, reflecting that the option is deep "in the money," and like the call option, the put option price will start to move dollar for dollar with the stock price but in the opposite direction.

### Key Observations:

- **Call options** tend to increase in value as the underlying asset's price increases.
- **Put options** increase in value as the underlying asset's price decreases.
- The value of both call and put options is not linearly related to the stock price. It is affected by the option's "moneyness" (relation of stock price to strike price), time to expiration, volatility of the underlying asset, risk-free interest rate, and dividends.
- The slope of these graphs at any point is related to the "Delta" of the option, which is a measure of the rate of change of the option price with respect to the price of the underlying asset.

The graphs provide a visual representation of how the value of options moves with the price of the underlying asset, which is a fundamental concept in options trading and financial theory.

## Built With

This project is built with a mix of mathematical computation and visualization libraries in Python. Below are the details of each component:

- **Python**: A high-level, interpreted programming language known for its ease of readability and extensive libraries. We've utilized Python 3 due to its modern features and community support.

- **Math**: A built-in Python module providing mathematical functions. This project uses it to perform operations such as logarithms and square roots which are integral to the Black-Scholes formula.

- **NumPy**: An open-source Python library that's the cornerstone for numerical computation in Python. It provides support for arrays (which are more efficient than Python lists for large data), as well as a host of functions to perform operations on these arrays. In our project, it's used for its array handling capabilities and the `np.exp` function for calculating exponentials.

- **Matplotlib**: A plotting library for Python and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications. In this project, Matplotlib's `pyplot` module is used to visualize the option pricing as a function of the stock price.

- **SciPy**: An open-source Python library used for scientific and technical computing. This project uses the `stats` module from SciPy, particularly `norm.cdf`, which provides the cumulative distribution function for a normal distribution, crucial for calculating probabilities in the Black-Scholes model.

- **Black-Scholes Function**: A custom-defined Python function that calculates the price of a European option (either call or put) using the Black-Scholes formula, taking into account the time value of money through the risk-free rate, and adjusting for dividends with the dividend yield.

- **Option Price Plotting Function**: Another custom Python function that generates a plot of option prices over a range of underlying asset prices. This visual output aids in understanding how option prices vary with the underlying asset price.

These components are combined into a cohesive codebase that can calculate and display the price of financial options using the Black-Scholes model, which is a fundamental model in financial economics.

#### Dependencies

To run this project, the following Python packages must be installed:

- NumPy (for numerical computations)
- Matplotlib (for data visualization)
- SciPy (for scientific computations, particularly the `norm` module)

You can install these dependencies using `pip`:

```bash
pip install numpy matplotlib scipy
```

#### Installation

To utilize this project, clone the repo or download the source code. Ensure you have Python and the dependencies installed. Execute the script in a Python environment, and the plots will be displayed showing the calculated option prices.

---

This "Built With" section provides a clear, detailed overview of the technologies and libraries used in the project, suitable for inclusion in a GitHub repository's README.md to inform users and contributors about the project's technical stack.Here are a few examples.

## Getting Started

This section will guide you through setting up your local environment to run the Option Pricing application using the Black-Scholes model.

#### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- Pip (Python package installer)

#### Installation

1. **Clone the repository** or download the source files to your local machine.

   If you have git installed, you can clone the repository using the following command:

   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   ```
   
   Alternatively, download the zip file from the GitHub repository page and extract it on your local machine.

2. **Set up a virtual environment** (optional but recommended):

   Navigate to the project directory and create a virtual environment:

   ```sh
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```sh
     source venv/bin/activate
     ```

3. **Install the required packages**:

   Install all dependencies using `pip`:

   ```sh
   pip install numpy matplotlib scipy
   ```

#### Running the Application

After installation, you can run the application to plot the option prices.

1. **Start your Python interpreter**:

   Ensure your virtual environment is activated, and start the Python interpreter:

   ```sh
   python
   ```

2. **Run the script**:

   You can either import the functions and use them in the Python interpreter or run the script if it's saved in a `.py` file:

   - If running in the interpreter, import the functions and run them directly:

     ```python
     from your_script_name import plot_option_price

     # Set your parameters
     S_range = np.linspace(50, 150, 100)
     K = 100
     T = 1
     r = 0.05
     sigma = 0.2
     dividend_yield = 0.02

     # Plot the option prices
     plot_option_price(S_range, K, T, r, sigma, 'call', dividend_yield)
     plot_option_price(S_range, K, T, r, sigma, 'put', dividend_yield)
     ```

   - If running as a script, navigate to the script's directory and run:

     ```sh
     python your_script_name.py
     ```

   Replace `your_script_name` with the actual name of your Python script.

3. **View the output**:

   The application will generate and display the plots for call and put option prices against the stock price range. These plots will appear in new windows.

#### Troubleshooting

- If you encounter any issues with package versions, refer to the package documentation for compatibility information.
- Ensure all commands are run in the project's root directory and the virtual environment (if used) is activated.

#### Next Steps

Once you have the application running, you can modify the parameters within the script to model different scenarios or expand the functionality by integrating more features such as time-to-expiration impacts or different volatility measures.

## Roadmap

See the [open issues](https://github.com//Black-Scholes-Model-To-Price-Options/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Black-Scholes-Model-To-Price-Options/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Black-Scholes-Model-To-Price-Options/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Black-Scholes-Model-To-Price-Options/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion/) - **

## Acknowledgements

* []()
* []()
* []()
