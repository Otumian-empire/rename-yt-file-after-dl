import glob
import os
import sys


def main(playlist):
    # playlist = ""

    # all videos have some id that make it unique on youtube
    # write the ids into a file
    # if there is an error, update the yt_fmts by adding the missing
    # file format
    ids_file = "ids"
    ids_list = []
    video_playlist = []

    # youtube file formats
    yt_fmts = [
        'MOV', 'MPEG4', 'MP4', 'AVI', 'WMV', 'MPEGPS',
        'FLV', '3GPP', 'WebM', 'DNxHR', 'ProRes',
        'CineForm', 'HEVC', "MKV"
    ]

    # read the ids into a file
    # https://www.reddit.com/r/lifehacks/comments/4ko6od/request_get_a_list_of_urls_in_a_youtube_playlist/?utm_source=share&utm_medium=web2x&context=3
    os.system(f"youtube-dl --get-id {playlist} -i >> {ids_file}")

    with open(ids_file, "r") as ptr:
        ids_list = ptr.readlines()

    ids_list = [id.strip("\n") for id in ids_list]

    for fmt in yt_fmts:
        video_playlist.extend(glob.glob(f"*.{fmt.lower()}"))

    video_playlist = list(set(video_playlist))

    counter = 0

    for id_ in ids_list:
        for video_title in video_playlist:
            if video_title.find(id_) != -1:
                new_video_title = str(counter+1) + " " + video_title
                os.system(f"mv '{video_title}' '{new_video_title}'")
                counter += 1
                video_playlist.remove(video_title)

    os.system(f"rm {ids_file}")
    vids = glob.glob(f"*.{fmt.lower()}")

    for vid in vids:
        print(vid)

    print("Done")


if __name__ == "__main__":
    playlist = sys.argv[1]
    main(playlist)
