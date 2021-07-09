import requests
import re
from bookrags import urls
from bookrags.studypack import StudyPack

# Automatically navigate to the study guide page
# Query what pages there are


class BookRags:

    def __init__(self, username, password) -> None:
        self.__details = {
            'edEmailOrName': username,
            'edPW': password
        }
        self.__session = requests.Session()
        self.__login()

    def __login(self):
        ret = self.__session.post(
            urls.LOGIN_URL,
            data=self.__details)

    def is_logged_in(self):
        check = self.__session.get(
            urls.ACCOUNT_URL,
            allow_redirects=False)
        return len(check.text) > 1

    def logout(self):
        self.__session.get(urls.LOGOUT_URL)

    def get_title(self, link):
        page_text = self.__session.get(link).text
        page_title = re.search('<title>(.*?)</title>', page_text).group(1)
        return page_title

    def get_study_pack(self, link):
        """
        Returns all the pages for a study pack
        """
        page_text = self.__session.get(link)
        re.search(('<!-- BEGIN STUDY GUIDE BLOCK -->'
                   '(.*?)<!-- BEGIN STUDY GUIDE BLOCK -->'),
                  page_text)

    def get_pdf(self, link):
        """
        Gets the pdf link from the page
        """
        pass

    def get_word(self, link):
        """
        Get the word link from the page
        """
        pass


class StudyPack:
    pass