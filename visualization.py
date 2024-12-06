import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def create_income_distribution_plot(processed_data_path, user_inputs, prediction):
    df = pd.read_csv(processed_data_path) # Load the processed data
    from preprocess_input import preprocess_input_data # Import the preprocess_input_data function

    # process the input data
    input_data = preprocess_input_data(
        age=user_inputs['age'],
        sex=user_inputs['sex'],
        education=user_inputs['education'],
        occupation=user_inputs['occupation'],
        race=user_inputs['race'],
        hours_worked=user_inputs['hours_worked']
    )

    processed_inputs = input_data.iloc[0].to_dict() # Extract processed input values

    # add education with input education value to the processed inputs
    processed_inputs['education'] = user_inputs['education']

    # define the variables
    variables = processed_inputs.keys()

    # Remove 'education-yr' from the visualization list
    variables = [var for var in variables if var != 'education-yr']

    # Initialize a list to store the percentage data
    percentage_data = {
        'Variable': [],
        '<=50K (%)': [],
        '>50K (%)': [],
        'Value': []
    }

    # Iterate over each variable and calculate percentages
    for var in variables:
        # for education, use education-yr for the calculation
        if var == 'education': 
            value = user_inputs['education'] 
            calc_var = 'education-yr'
            calc_value = processed_inputs[calc_var]
            subset = df[df[calc_var] == calc_value]
        else:
            value = processed_inputs[var]
            subset = df[df[var] == value]
        
        # total of values for each variable
        total = len(subset)
        # if no matching values
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
        percentage_data['Value'].append(value)

    # Create a DataFrame from the percentage data
    pct_df = pd.DataFrame(percentage_data)

    # Sort the values by the highest percentage of the predicted value
    pct_df = pct_df.sort_values(by=f'{prediction} (%)', ascending=True).reset_index(drop=True)

    # Melt the DataFrame
    pct_df_melted = pct_df.melt(id_vars=['Variable', 'Value'], value_vars=['<=50K (%)', '>50K (%)'],
                                var_name='Income', value_name='Percentage')

    # Create a stacked bar plot using Plotly Express
    fig = px.bar(
        pct_df_melted,
        x='Percentage',
        y='Variable',
        color='Income',
        orientation='h',  # Horizontal bars
        title="Income Distribution by Input Variables",
        labels={'Percentage': 'Percentage (%)', 'Variable': 'Variable'},
        color_discrete_map={'<=50K (%)': 'salmon', '>50K (%)': 'skyblue'},
        hover_data={'Variable': True, 'Value': True, 'Percentage': ':.1f'}
    )

    # Add percentage labels for each bar
    for i, row in pct_df_melted.iterrows():
        # Calculate the position for the label
        if row['Income'] == '<=50K (%)':
            x_position = row['Percentage'] / 2  # Center of the first bar
        else:
            x_position = 100 - (row['Percentage'] / 2)  # Center of the second bar
        
        # Determine font weight based on the predicted value
        # Bold the bars that match the prediction
        font_weight = "bold" if row['Income'] == f"{prediction} (%)" else "normal"

        # add percentage label to each bar
        fig.add_annotation(
            x=x_position,
            y=row['Variable'],  
            text=f"{row['Percentage']:.1f}%",
            showarrow=False,
            font=dict(size=10, color="black", weight=font_weight),
            xanchor='center',
            yanchor='middle',
        )

    return fig

    # # Set the style for the plot
    # sns.set_style("whitegrid")
    # # Initialize the matplotlib figure
    # fig, ax = plt.subplots(figsize=(10, 6))
    # # Set the positions and width for the bars
    # bar_width = 0.4
    # index = range(len(pct_df))

    # # Plot the bars directly next to each other
    # ax.barh(index, pct_df['<=50K (%)'], height=bar_width, color='skyblue', label='<=50K', align='edge')
    # ax.barh(index, pct_df['>50K (%)'], height=bar_width, color='salmon', label='>50K', align='edge', left=pct_df['<=50K (%)'])

    # # Set the y-ticks and labels
    # ax.set_yticks([i + bar_width / 2 for i in index])
    # ax.set_yticklabels(pct_df['Variable'])

    # # Set labels and title
    # ax.set_xlabel('Percentage (%)')
    # ax.set_title('Income Distribution by Input Variables')

    # # Add legend
    # ax.legend()

    # # Add percentage labels to the bars
    # for i in index:
    #     # Label for <=50K
    #     ax.text(pct_df['<=50K (%)'][i] / 2, i + bar_width/2, f"{pct_df['<=50K (%)'][i]:.1f}%", 
    #         va='center', ha='center', color='black', fontsize=9)
    
    #     # Label for >50K
    #     ax.text(pct_df['<=50K (%)'][i] + pct_df['>50K (%)'][i] / 2, i + bar_width / 2, f"{pct_df['>50K (%)'][i]:.1f}%", 
    #         va='center', ha='center', color='black', fontsize=9)

    # # Adjust layout for better fit
    # plt.tight_layout()
    
