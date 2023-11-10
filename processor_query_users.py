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
user_query = """SELECT users.username, users.trust_level, user_stats.topics_entered, user_stats.time_read, 
                user_stats.days_visited, user_stats.posts_read_count, user_stats.likes_given, user_stats.likes_received,
                user_stats.new_since, user_stats.post_count, user_stats.topic_count, user_custom_fields.value AS user_custom_field,
                posts.like_count, posts.score, posts.reads, posts.word_count, posts.image_upload_id,
                topics.title AS topic, categories.name AS category, categories.description AS category_description, 
                tags.name AS tag, given_daily_likes.given_date, posts.raw AS post, topics.archetype
                FROM users
                JOIN posts ON users.id = posts.user_id
                JOIN user_stats ON user_stats.user_id = users.id
                JOIN user_badges ON user_badges.user_id = users.id
                JOIN user_custom_fields ON user_custom_fields.user_id = users.id
                JOIN topics ON topics.id = posts.topic_id
                JOIN categories ON categories.topic_id = topics.id
                JOIN category_tag_stats ON category_tag_stats.category_id = categories.id
                JOIN tags ON category_tag_stats.tag_id = tags.id
                JOIN given_daily_likes ON given_daily_likes.user_id = users.id
                GROUP BY users.username, users.trust_level, user_stats.topics_entered, user_stats.time_read, 
                user_stats.days_visited, user_stats.posts_read_count, user_stats.likes_given, user_stats.likes_received,
                user_stats.new_since, user_stats.post_count, user_stats.topic_count, user_custom_fields.value,
                posts.like_count, posts.score, posts.reads, posts.word_count, posts.image_upload_id,
                topics.title, categories.name, categories.description,
                tags.name, given_daily_likes.given_date, posts.raw,topics.archetype;
            """
## Ejecutar Query
user_df = pd.read_sql(user_query,engine)

# Convertir a formato csv y exportar la data
user_df.to_csv('dataset_users.csv', index=False, encoding='UTF-8')

# Imprimir la cantidad de registros recibidos de la consulta
print('Registros users: ', len(user_df))


