from webscrape import scrape_data
from split_text import split_into_sentences
from create_video import create_video


# Get title and description from random post
title_string, description_string = scrape_data("AmItheAsshole")

# Split post description into list of sentences
sentence_list = split_into_sentences(description_string)

# Add title string beginning of sentence list
sentence_list.insert(0, title_string)

# Create video from sentence list
create_video(sentence_list)