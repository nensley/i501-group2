import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_income_distribution_plot(processed_data_path, user_inputs):
    df = pd.read_csv(processed_data_path) # Load the processed data
    from preprocess_input import preprocess_input_data # Import the preprocess_input_data function

    input_data = preprocess_input_data(
        age=user_inputs['age'],
        sex=user_inputs['sex'],
        education=user_inputs['education'],
        occupation=user_inputs['occupation'],
        race=user_inputs['race'],
        hours_worked=user_inputs['hours_worked']
    )

    
    processed_inputs = input_data.iloc[0].to_dict() # Extract processed input values

    variables = processed_inputs.keys() # Define the variables to visualize

    # Initialize a list to store the percentage data
    percentage_data = {
        'Variable': [],
        '<=50K (%)': [],
        '>50K (%)': []
    }

    # Iterate over each variable and calculate percentages
    for var in variables:
        value = processed_inputs[var]
        subset = df[df[var] == value]
        total = len(subset)
        if total == 0:
            # Avoid division by zero
            pct_less_equal = 0
            pct_greater = 0
        else:
            count_less_equal = len(subset[subset['income'] == '<=50K'])
            count_greater = len(subset[subset['income'] == '>50K'])
            pct_less_equal = (count_less_equal / total) * 100
            pct_greater = (count_greater / total) * 100
        
        percentage_data['Variable'].append(var.replace('-', ' ').title())
        percentage_data['<=50K (%)'].append(pct_less_equal)
        percentage_data['>50K (%)'].append(pct_greater)

    # Create a DataFrame from the percentage data
    pct_df = pd.DataFrame(percentage_data)

    # Set the style for the plot
    sns.set_style("whitegrid")
    # Initialize the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Set the positions and width for the bars
    bar_width = 0.4
    index = range(len(pct_df))

    # Plot the bars
    ax.barh([i + bar_width for i in index], pct_df['<=50K (%)'], height=bar_width, color='skyblue', label='<=50K')
    ax.barh(index, pct_df['>50K (%)'], height=bar_width, color='salmon', label='>50K')

    # Set the y-ticks and labels
    ax.set_yticks([i + bar_width / 2 for i in index])
    ax.set_yticklabels(pct_df['Variable'])

    # Set labels and title
    ax.set_xlabel('Percentage (%)')
    ax.set_title('Income Distribution by Input Variables')

    # Add legend
    ax.legend()

    # Add percentage labels to the bars
    for i in index:
        ax.text(pct_df['<=50K (%)'][i] + 1, i + bar_width, f"{pct_df['<=50K (%)'][i]:.1f}%", va='center', color='black', fontsize=9)
        ax.text(pct_df['>50K (%)'][i] + 1, i, f"{pct_df['>50K (%)'][i]:.1f}%", va='center', color='black', fontsize=9)

    # Adjust layout for better fit
    plt.tight_layout()

    return fig
