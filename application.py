{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "19563c4c-89ad-4d32-9564-df782f25c1dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "aeb052cf-02d1-4545-898e-b12a2407728b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"C:\\Project\\spotify_millsongdata.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dc1f36d4-e285-410d-af7f-db16a1afc032",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>link</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Ahe's My Kind Of Girl</td>\n",
       "      <td>/a/abba/ahes+my+kind+of+girl_20598417.html</td>\n",
       "      <td>Look at her face, it's a wonderful face  \\r\\nA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Andante, Andante</td>\n",
       "      <td>/a/abba/andante+andante_20002708.html</td>\n",
       "      <td>Take it easy with me, please  \\r\\nTouch me gen...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>As Good As New</td>\n",
       "      <td>/a/abba/as+good+as+new_20003033.html</td>\n",
       "      <td>I'll never know why I had to go  \\r\\nWhy I had...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Bang</td>\n",
       "      <td>/a/abba/bang_20598415.html</td>\n",
       "      <td>Making somebody happy is a question of give an...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Bang-A-Boomerang</td>\n",
       "      <td>/a/abba/bang+a+boomerang_20002668.html</td>\n",
       "      <td>Making somebody happy is a question of give an...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  artist                   song                                        link  \\\n",
       "0   ABBA  Ahe's My Kind Of Girl  /a/abba/ahes+my+kind+of+girl_20598417.html   \n",
       "1   ABBA       Andante, Andante       /a/abba/andante+andante_20002708.html   \n",
       "2   ABBA         As Good As New        /a/abba/as+good+as+new_20003033.html   \n",
       "3   ABBA                   Bang                  /a/abba/bang_20598415.html   \n",
       "4   ABBA       Bang-A-Boomerang      /a/abba/bang+a+boomerang_20002668.html   \n",
       "\n",
       "                                                text  \n",
       "0  Look at her face, it's a wonderful face  \\r\\nA...  \n",
       "1  Take it easy with me, please  \\r\\nTouch me gen...  \n",
       "2  I'll never know why I had to go  \\r\\nWhy I had...  \n",
       "3  Making somebody happy is a question of give an...  \n",
       "4  Making somebody happy is a question of give an...  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1a2f2b56-b702-4f2e-a363-4a391feb58f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>link</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>57645</th>\n",
       "      <td>Ziggy Marley</td>\n",
       "      <td>Good Old Days</td>\n",
       "      <td>/z/ziggy+marley/good+old+days_10198588.html</td>\n",
       "      <td>Irie days come on play  \\r\\nLet the angels fly...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57646</th>\n",
       "      <td>Ziggy Marley</td>\n",
       "      <td>Hand To Mouth</td>\n",
       "      <td>/z/ziggy+marley/hand+to+mouth_20531167.html</td>\n",
       "      <td>Power to the workers  \\r\\nMore power  \\r\\nPowe...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57647</th>\n",
       "      <td>Zwan</td>\n",
       "      <td>Come With Me</td>\n",
       "      <td>/z/zwan/come+with+me_20148981.html</td>\n",
       "      <td>all you need  \\r\\nis something i'll believe  \\...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57648</th>\n",
       "      <td>Zwan</td>\n",
       "      <td>Desire</td>\n",
       "      <td>/z/zwan/desire_20148986.html</td>\n",
       "      <td>northern star  \\r\\nam i frightened  \\r\\nwhere ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57649</th>\n",
       "      <td>Zwan</td>\n",
       "      <td>Heartsong</td>\n",
       "      <td>/z/zwan/heartsong_20148991.html</td>\n",
       "      <td>come in  \\r\\nmake yourself at home  \\r\\ni'm a ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             artist           song  \\\n",
       "57645  Ziggy Marley  Good Old Days   \n",
       "57646  Ziggy Marley  Hand To Mouth   \n",
       "57647          Zwan   Come With Me   \n",
       "57648          Zwan         Desire   \n",
       "57649          Zwan      Heartsong   \n",
       "\n",
       "                                              link  \\\n",
       "57645  /z/ziggy+marley/good+old+days_10198588.html   \n",
       "57646  /z/ziggy+marley/hand+to+mouth_20531167.html   \n",
       "57647           /z/zwan/come+with+me_20148981.html   \n",
       "57648                 /z/zwan/desire_20148986.html   \n",
       "57649              /z/zwan/heartsong_20148991.html   \n",
       "\n",
       "                                                    text  \n",
       "57645  Irie days come on play  \\r\\nLet the angels fly...  \n",
       "57646  Power to the workers  \\r\\nMore power  \\r\\nPowe...  \n",
       "57647  all you need  \\r\\nis something i'll believe  \\...  \n",
       "57648  northern star  \\r\\nam i frightened  \\r\\nwhere ...  \n",
       "57649  come in  \\r\\nmake yourself at home  \\r\\ni'm a ...  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "31bfbbee-6af8-48bd-bee5-9e9b617cb752",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(57650, 4)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ece56e5d-7bbd-470b-a1ca-be4a6bf63bfe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "artist    0\n",
       "song      0\n",
       "link      0\n",
       "text      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1d0b4941-028e-4ad1-832b-6ee4e14dae79",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df.sample(5000).drop('link',axis=1).reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0260e15f-f423-4542-9cd6-0f59dde42b1a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>America</td>\n",
       "      <td>Mad Dog</td>\n",
       "      <td>Through the darkness I see you again  \\r\\nWatc...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>R. Kelly</td>\n",
       "      <td>Raindrops</td>\n",
       "      <td>Can you hear the sounds of the love angels cal...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Vince Gill</td>\n",
       "      <td>From Where I Stand</td>\n",
       "      <td>Oh, I'm drawn to you  \\r\\nLike a burnin' flame...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Willie Nelson</td>\n",
       "      <td>Everybody's Talkin'</td>\n",
       "      <td>Everybody's talkin' 'bout me  \\r\\nI don't hear...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>The Beatles</td>\n",
       "      <td>I Want To Hold Your Hand</td>\n",
       "      <td>Oh yeah I tell you somethin'  \\r\\nI think you'...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Yeng Constantino</td>\n",
       "      <td>Hawak Kamay</td>\n",
       "      <td>Minsan madarama mo kay bigat ng problema  \\r\\n...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Rainbow</td>\n",
       "      <td>Lost In Hollywood</td>\n",
       "      <td>Got to get a message through  \\r\\n'Cause I thi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Justin Timberlake</td>\n",
       "      <td>Hootnanny</td>\n",
       "      <td>I could go number one ten times  \\r\\nPretty gi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Toto</td>\n",
       "      <td>Manuela Run</td>\n",
       "      <td>Don't look now, you better watch that sword th...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Vybz Kartel</td>\n",
       "      <td>Wine Pon Me</td>\n",
       "      <td>Jah know  \\r\\nBaby a whe' yuh wan from me  \\r\\...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              artist                      song  \\\n",
       "0            America                   Mad Dog   \n",
       "1           R. Kelly                 Raindrops   \n",
       "2         Vince Gill        From Where I Stand   \n",
       "3      Willie Nelson       Everybody's Talkin'   \n",
       "4        The Beatles  I Want To Hold Your Hand   \n",
       "5   Yeng Constantino               Hawak Kamay   \n",
       "6            Rainbow         Lost In Hollywood   \n",
       "7  Justin Timberlake                 Hootnanny   \n",
       "8               Toto               Manuela Run   \n",
       "9        Vybz Kartel               Wine Pon Me   \n",
       "\n",
       "                                                text  \n",
       "0  Through the darkness I see you again  \\r\\nWatc...  \n",
       "1  Can you hear the sounds of the love angels cal...  \n",
       "2  Oh, I'm drawn to you  \\r\\nLike a burnin' flame...  \n",
       "3  Everybody's talkin' 'bout me  \\r\\nI don't hear...  \n",
       "4  Oh yeah I tell you somethin'  \\r\\nI think you'...  \n",
       "5  Minsan madarama mo kay bigat ng problema  \\r\\n...  \n",
       "6  Got to get a message through  \\r\\n'Cause I thi...  \n",
       "7  I could go number one ten times  \\r\\nPretty gi...  \n",
       "8  Don't look now, you better watch that sword th...  \n",
       "9  Jah know  \\r\\nBaby a whe' yuh wan from me  \\r\\...  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "861a9cfd-f096-4015-a450-128012f7e1cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Through the darkness I see you again  \\r\\nWatch my temperature rise  \\r\\nCan't believe my eyes, don't tell me  \\r\\nI've had way too much tonight  \\r\\n  \\r\\nDrank the potion stronger than me  \\r\\nGot me all confused  \\r\\nWhy you so amused, don't tell me  \\r\\nYou've had way too much tonight  \\r\\n  \\r\\nPlease don't tell me no  \\r\\nGod, I miss you so  \\r\\nOne thing you should know  \\r\\nGod, I love you so, oh  \\r\\n  \\r\\nHad way too much tonight  \\r\\nI'm a mad dog at times like these  \\r\\nDon't know where to turn  \\r\\nAin't the time to learn my lesson  \\r\\nI've had way too much tonight  \\r\\n  \\r\\nAin't the time to learn my lesson  \\r\\nI've had way too much to-  \\r\\nReally too much to-  \\r\\nI've had way too much tonight  \\r\\nAlright  \\r\\n  \\r\\nI've had way too much to-  \\r\\nReally too much to-  \\r\\nI've had way too much tonight\\r\\n\\r\\n\""
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['text'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a1277ebd-6077-41da-8f02-e2fc47aceb34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5000, 3)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "eec2fde2-f235-4272-89b9-5a4fb1bcc45c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to C:\\Users\\BHAVANA\n",
      "[nltk_data]     R\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "ps=PorterStemmer()\n",
    "nltk.download('punkt')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d180bdb2-7c6d-4635-a110-528a24d8c807",
   "metadata": {},
   "outputs": [],
   "source": [
    "def token(txt):\n",
    "    token=nltk.word_tokenize(txt)\n",
    "    b = [ps.stem(w) for w in token]\n",
    "    return \" \".join(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c1c3909c-cb6e-4744-ab57-0a8e3df54b36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'you are beauti , beauti'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "token(\"you are beautiful,beauty\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a3274e3c-db49-4800-bd9a-f6c6eeb1a31f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       through the dark i see you again watch my temp...\n",
       "1       can you hear the sound of the love angel call ...\n",
       "2       oh , i 'm drawn to you like a burnin ' flame b...\n",
       "3       everybodi 's talkin ' 'bout me i do n't hear a...\n",
       "4       oh yeah i tell you somethin ' i think you 'll ...\n",
       "                              ...                        \n",
       "4995    i come to you with strang fire i make an offer...\n",
       "4996    they 've been spend most their live live in a ...\n",
       "4997    kon ik het hem maar aan zijn verstand brengen ...\n",
       "4998    black boy employ selassi we kiss , we defin wh...\n",
       "4999    all you hoe , be cryin ' for these bitch all y...\n",
       "Name: text, Length: 5000, dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['text'].apply(lambda x: token(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d8842201-5764-4465-be6e-44a239b8fc01",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a14eec1f-926a-46d0-92de-f99ba5c463fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "tfid=TfidfVectorizer(analyzer='word',stop_words='english')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5c4b5acb-d059-425c-8c82-151ef8697aa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix=tfid.fit_transform(df['text'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6497795c-2a85-4665-aa47-5ba391ffc02e",
   "metadata": {},
   "outputs": [],
   "source": [
    "similar=cosine_similarity(matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e73af1ed-951c-4263-ada1-e84f3af3a5a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.        , 0.01958795, 0.0237412 , ..., 0.        , 0.02867203,\n",
       "       0.03334202])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "similar[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9065e1b4-87c0-4209-887f-085b4b231c36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['song']=='Mad Dog'].index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80c03392-73ac-4622-8e49-2fdc3a1ec417",
   "metadata": {},
   "source": [
    "Recommender Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a0955905-e461-4011-8ab3-803f349b1f18",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recommender(song_name):\n",
    "    idx=df[df['song']==song_name].index[0]\n",
    "    distance=sorted(list(enumerate(similar[idx])),reverse=True ,key=lambda x:x[1])\n",
    "    song=[]\n",
    "    for s_id in distance[1:5]:\n",
    "        song.append(df.iloc[s_id[0]].song)\n",
    "    return song"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "4d4db5d2-43ce-4716-89ac-39fede262e7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['I Just Want To Have Something To Do',\n",
       " 'Again Tonight',\n",
       " 'Tonight',\n",
       " 'Time Of Our Life']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recommender('Mad Dog')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "761291ba-6849-4849-b8e1-bc3649a46aca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['The Closer You Get',\n",
       " \"It's The Falling In Love\",\n",
       " \"Don't Be Bashful Little Girl\",\n",
       " 'Rain Your Love Down']"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recommender('Raindrops')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "a135e45d-5332-43ee-9ff1-7fab71181e4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f68d65c3-3edf-4615-9c0f-4770106bd6c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(similar,open(\"similarity.pkl\",\"wb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "85a3f2d7-c88b-4509-9aa6-06e9dc12d034",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(df,open(\"df.pkl\",\"wb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "991c3f31-96d9-4160-8417-c51313d36e7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "## Music Recommender System"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "330e93d47c374b3c9f2c0362b8d2e8a4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Type or select a song from the dropdown', options=('Mad Dog', 'Raindrops', 'From Where I…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-06-15 22:21:22.053 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\BHAVANA R\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import streamlit as st\n",
    "from streamlit_jupyter import StreamlitPatcher, tqdm\n",
    "StreamlitPatcher().jupyter() \n",
    "\n",
    "import pickle\n",
    "pickle.dump(similar,open('similarity.pkl','wb'))\n",
    "pickle.dump(df,open('df.pkl','wb'))\n",
    "\n",
    "import spotipy\n",
    "from spotipy.oauth2 import SpotifyClientCredentials\n",
    "\n",
    "CLIENT_ID = \"21858c73f9314eb9878c53baf752506c\"\n",
    "CLIENT_SECRET = \"9e087a03d84d4e09b7357a5e8a843fe0\"\n",
    "\n",
    "# Initialize the Spotify client\n",
    "client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)\n",
    "sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)\n",
    "\n",
    "def get_song_album_cover_url(song_name, artist_name):\n",
    "    search_query = f\"track:{song_name} artist:{artist_name}\"\n",
    "    results = sp.search(q=search_query, type=\"track\")\n",
    "\n",
    "    if results and results[\"tracks\"][\"items\"]:\n",
    "        track = results[\"tracks\"][\"items\"][0]\n",
    "        album_cover_url = track[\"album\"][\"images\"][0][\"url\"]\n",
    "        print(album_cover_url)\n",
    "        return album_cover_url\n",
    "    else:\n",
    "        return \"https://i.postimg.cc/0QNxYz4V/social.png\"\n",
    "\n",
    "def recommend(song):\n",
    "    index = music[music['song'] == song].index[0]\n",
    "    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])\n",
    "    recommended_music_names = []\n",
    "    recommended_music_posters = []\n",
    "    for i in distances[1:6]:\n",
    "        # fetch the movie poster\n",
    "        artist = music.iloc[i[0]].artist\n",
    "        print(artist)\n",
    "        print(music.iloc[i[0]].song)\n",
    "        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))\n",
    "        recommended_music_names.append(music.iloc[i[0]].song)\n",
    "\n",
    "    return recommended_music_names,recommended_music_posters\n",
    "\n",
    "st.header('Music Recommender System')\n",
    "music = pickle.load(open('df.pkl','rb'))\n",
    "similar = pickle.load(open('similarity.pkl','rb'))\n",
    "\n",
    "music_list = music['song'].values\n",
    "selected_music = st.selectbox(\n",
    "    \"Type or select a song from the dropdown\",\n",
    "    music_list\n",
    ")\n",
    "\n",
    "if st.button('Show Recommendation'):\n",
    "    recommended_music_names,recommended_music_posters = recommend(selected_movie)\n",
    "    col1, col2, col3, col4, col5= st.columns(5)\n",
    "    with col1:\n",
    "        st.text(recommended_music_names[0])\n",
    "        st.image(recommended_music_posters[0])\n",
    "    with col2:\n",
    "        st.text(recommended_music_names[1])\n",
    "        st.image(recommended_music_posters[1])\n",
    "\n",
    "    with col3:\n",
    "        st.text(recommended_music_names[2])\n",
    "        st.image(recommended_music_posters[2])\n",
    "    with col4:\n",
    "        st.text(recommended_music_names[3])\n",
    "        st.image(recommended_music_posters[3])\n",
    "    with col5:\n",
    "        st.text(recommended_music_names[4])\n",
    "        st.image(recommended_music_posters[4])\n",
    "\n",
    " \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6d370a1-5303-4a08-bcf5-659babc46ff9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
