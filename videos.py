import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('USvideos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)


def my_max(dictionary):
    return_dict = {'channel': None, 'num_views_reactions': 0}
    # creating a sample dictionary
    # 'num_views_reactions' key captures the number of views/likes/dislikes

    for k, v in dictionary.items():
        ''' Find the maximum number of views/likes/dislikes '''
        if int(v) > return_dict['num_views_reactions']:
            return_dict['channel'] = k   # as key
            return_dict['num_views_reactions'] = int(v)   # as value
    return return_dict


def my_min(dictionary):
    return_dict = {'channel': None, 'num_views': float('Inf')}
    # creating a sample dictionary
    # 'num_views' key captures the number of views

    for k, v in dictionary.items():
        ''' Find the minimum number of views '''
        if int(v) < return_dict['num_views']:
            return_dict['channel'] = k
            return_dict['num_views'] = int(v)
        else:
            continue
    return return_dict


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None, 'most_pop_num_views': None,
                                              'least_pop_num_views': None}
    channel = {}
    for sub_dict in data[1:]:
        channel.setdefault(sub_dict['channel_title'], 0)                # assigning zero as a value to each corresponding 'channel_title' key
        channel[sub_dict['channel_title']] += int(sub_dict['views'])    # updating number of views (value) for a corresponding channel (key)

    most_pop_channel = my_max(channel)
    least_pop_channel = my_min(channel)
    ''' Assigning a value to each key in the above sample dictionary '''
    most_popular_and_least_popular_channel['most_popular_channel'] = most_pop_channel['channel']
    most_popular_and_least_popular_channel['most_pop_num_views'] = most_pop_channel['num_views_reactions']
    most_popular_and_least_popular_channel['least_popular_channel'] = least_pop_channel['channel']
    most_popular_and_least_popular_channel['least_pop_num_views'] = least_pop_channel['num_views']

    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None, 'num_dislikes': None}

    likes_channel = {}
    dislikes_channel = {}
    for sub_dict in data[1:]:
        likes_channel.setdefault(sub_dict['channel_title'], 0)              # assigning zero as a value to each corresponding 'channel_title' key
        likes_channel[sub_dict['channel_title']] += int(sub_dict['likes'])  # updating number of likes (value) for a corresponding channel (key)
        dislikes_channel.setdefault(sub_dict['channel_title'], 0)           # assigning zero as a value to each corresponding 'channel_title' key
        dislikes_channel[sub_dict['channel_title']] += int(sub_dict['dislikes']) # updating number of dislikes (value) for a corresponding channel (key)

    most_liked_channel = my_max(likes_channel)
    most_disliked_channel = my_max(dislikes_channel)
    ''' Assigning a value to each key in the above sample dictionary '''
    most_liked_and_disliked_channel['most_liked_channel'] = most_liked_channel['channel']
    most_liked_and_disliked_channel['num_likes'] = most_liked_channel['num_views_reactions']
    most_liked_and_disliked_channel['most_disliked_channel'] = most_disliked_channel['channel']
    most_liked_and_disliked_channel['num_dislikes'] = most_disliked_channel['num_views_reactions']

    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    #print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))
