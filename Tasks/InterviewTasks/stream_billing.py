from datetime import datetime, timedelta
from typing import List


def convert_duration_str_to_seconds(duration_string: str) -> int:
    """
    Convert a string provided in "hh:mm:ss" format into a integer representing the duration in seconds

    :param duration_string:     String, representing time in "hh:mm:ss" format
    :return:                    Integer, representing the duration in seconds
    """
    duration_str = duration_string.split(",")[0]
    duration_datetime = datetime.strptime(duration_str, "%H:%M:%S").time()
    duration_timedelta = timedelta(hours=duration_datetime.hour, minutes=duration_datetime.minute,
                                   seconds=duration_datetime.second)
    duration_integer = int(duration_timedelta.seconds)
    return duration_integer


def get_longest_stream_id(log_string: List[str]) -> str:
    """
    Return stream ID with the longest total time of all activities

    :param log_string:          List of Strings, representing log of streams in "hh:mm:ss, nnn-nn-nnnn" format,
                                where "nnn-nn-nnnn" is the stream ID and "hh:mm:ss" is the duration of that stream
    :return:                    String, representing the stream ID with the longest total time of all activities
    """
    streams_dictionary = {}
    for stream in log_string:
        duration = convert_duration_str_to_seconds(stream.split(",")[0])
        stream_id = stream.split(",")[1]
        if stream_id in streams_dictionary:
            streams_dictionary[stream_id] += duration
        else:
            streams_dictionary[stream_id] = duration
    longest_duration = 0
    longest_stream_id = ''
    for stream_id, duration in streams_dictionary.items():
        if duration > longest_duration:
            longest_duration = duration
            longest_stream_id = stream_id
    return longest_stream_id


def get_stream_price(duration: int) -> int:
    """
    Return the price for a stream with the provided duration

    :param duration:            Integer, representing the duration of a stream in seconds
    :return:                    Integer, representing the price for a stream with the provided duration
    """
    if duration < 180:
        price = duration * 4
    elif duration % 60 == 0:
        price = (duration // 60) * 225
    else:
        price = (duration // 60 + 1) * 225
    return price


if __name__ == '__main__':
    S = ["00:01:25,123-45-6789", "00:03:01,987-65-4321", "00:03:00,123-45-6789"]
    longest_stream_id = get_longest_stream_id(S)
    total_price = 0
    for stream in S:
        duration = convert_duration_str_to_seconds(stream.split(",")[0])
        stream_id = stream.split(",")[1]
        if stream_id == longest_stream_id:
            print(f'{stream_id=}')
            stream_price = get_stream_price(duration) // 2
            print(f'{stream_price=}')
        else:
            print(f'{stream_id=}')
            stream_price = get_stream_price(duration)
            print(f'{stream_price=}')
        total_price += stream_price
    print(f'{longest_stream_id=}')
    print(f'{total_price=}')
