# Copyright 2024 rxzheng
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'qwfpjl1234'
insta_password = 'Linux#1234'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  geckodriver_path=r"/opt/homebrew/bin/geckodriver")

with smart_run(session):
    # general settings
    #session.set_relationship_bounds(enabled=True,
          #                         max_followers=4590,
           #                         min_followers=45,
            #                        min_following=77)

   # session.set_dont_include(["friend1", "friend2", "friend3"])
   # session.set_dont_like(["pizza", "#store"])

    # activities

    session.follow_user_followers(['qwfpjl1234'], amount=800,
                                  randomize=False, interact=False)



