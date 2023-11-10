import os
from sqlalchemy.engine import URL
import pandas as pd
from sqlalchemy.engine import create_engine
from dotenv import load_dotenv

load_dotenv()

# Acceder a las variables de entorno
db_host = os.getenv('POSTGRES_HOST')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_port = os.getenv('POSTGRES_PORT')
db_database = os.getenv('POSTGRES_DATABASE')



## Conection to DB
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}",  pool_size=20)

## String query
post_query = """SELECT posts.id, posts.raw, posts.post_number, posts.like_count, posts.score, posts.cooked, posts.reads, posts.word_count, posts.image_upload_id,
                post_action_types.name_key AS post_action_type, topics.title AS topic, topics.views, topics.posts_count, topics.archetype,topics.excerpt,
                categories.name AS category, categories.description AS category_description, category_search_data.raw_data AS category_search_data, tags.name AS tag
                FROM posts
                LEFT JOIN topics ON topics.id = posts.topic_id
                LEFT JOIN post_actions ON post_actions.post_id = posts.id
                LEFT JOIN post_action_types ON post_action_types.id = post_actions.post_action_type_id
                LEFT JOIN categories ON categories.topic_id = topics.id
                LEFT JOIN category_search_data ON category_search_data.category_id = categories.id
                LEFT JOIN category_tag_stats ON category_tag_stats.category_id = categories.id
                LEFT JOIN tags ON category_tag_stats.tag_id = tags.id;
            """
## Query
post_df = pd.read_sql(post_query,engine)
## Opciones para almacenar resultado
post_df.to_csv('dataset_posts.csv', index=False, encoding='UTF-8')

print('Registros posts: ', len(post_df))


