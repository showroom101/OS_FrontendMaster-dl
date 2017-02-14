from spider import *


# APP: Spider Logic
# -----------------
browser_login()

# Fetch and save all courses
course_list = []
if not os.path.isfile(DATA_COURSE_LIST):
    save_course_list()
course_list = retrive_course_list()

time.sleep(5)

# Fetch and save all sections and subsections for each course
course_detailed_list = []
if not os.path.isfile(DATA_COURSE_DETAILED_LIST_CDN):
    save_course_detailed_list(course_list)
course_detailed_list = retrive_course_detailed_list()

# Fetch and save downloadable link for each video
save_downloadable_links(course_detailed_list)

# Download resources
course_detailed_list_cdn = retrive_downloadable_links()
download_courses(course_detailed_list_cdn)
