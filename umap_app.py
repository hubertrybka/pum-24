from streamlit_drawable_canvas import st_canvas
import pandas as pd
import PIL
import streamlit as st
import seaborn as sns
import numpy as np
import pickle

# Load the data
umap_df = pd.read_csv('data/streamlit/umap.csv')

with open('data/streamlit/umap_mnist.pkl', 'rb') as f:
    umap = pickle.load(f)

# Create a canvas component

st.write("Draw a digit on the canvas below and see how it is transformed by UMAP!")

canvas_result = st_canvas(
    stroke_width=30,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=300,
    width=300,
    drawing_mode="freedraw"
)

if canvas_result.image_data is not None:
    image_data = canvas_result.image_data
    img = PIL.Image.fromarray(image_data.astype("uint8"))
    img_resized = img.resize((28, 28)).convert('L')
    img_vector = np.ones(28*28) - (np.array(img_resized).reshape(1, -1) / 255.0)

    img_umap = umap.transform(img_vector)

    sns.set_style('white')
    sns.set_context('notebook')

    custom_palette = sns.color_palette("mako", 10)
    custom_palette.append((1, 0, 0))

    img_umap_df = pd.DataFrame(img_umap[:,:2], columns=['DIM1', 'DIM2'], index=[0])
    img_umap_df['label'] = 10
    plot_df = pd.concat([umap_df, img_umap_df], axis=0, ignore_index=True)

    markers = [f"${i}$" for i in range(10)]
    markers.append('o')
    fig = sns.lmplot(data=plot_df,
                     x='DIM1',
                     y='DIM2',
                     hue='label',
                     fit_reg=False,
                     legend=False,
                     markers=markers,
                     palette=custom_palette,
                     height=8,
                     aspect=1.5,
                     scatter_kws={"s": 100}
                     )
    sns.despine(right=False, top=False)
    st.pyplot(fig)