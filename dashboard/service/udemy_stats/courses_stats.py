# Importing analysis libraries
import pandas as pd 
import os  # For file paths

# Importing charting libraries
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go


data_folder_path = os.path.join(
    os.path.dirname(__file__), "../../../data/"
)

csv_file_path = os.path.normpath(
    data_folder_path + "courses_numerical_categorical_data.csv"
)


def load_courses(from_csv):
    print("Reading JSON input")

    courses = pd.read_csv(csv_file_path)
    courses.sort_values(
        by='num_subscribers',
        ascending=False,
        inplace=True
    )

    print("Finished loading data from csv")
    return courses


def plot_scatter(courses):
    print("Preparing scatter plot")
    fig = px.scatter(
        courses,
        y="num_subscribers",
        x="udemy_id",
        hover_data=courses.columns,
        render_mode='webgl'
    )
    fig_html = pio.to_html(fig, full_html=False)
    print("Finished creating scatter plot")
    return fig_html


courses = load_courses(from_csv=csv_file_path)
plot = plot_scatter(courses)