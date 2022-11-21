import os
import glob
import bs4

class TitleChanger:
    def __init__(self):
        print("Looking at Files in the directory: '{}'".format(os.getcwd()))
        self.title_dict = {'about.html': 'About Me',
                      'index.html': 'Adi Ravishankara',
                      'blog.html': 'Blog',
                      'projects.html': 'Projects',
                      'Blogs/first-web-app.html': 'First Web App'}
        self.files = self.list_files()
        for element in self.files:
            self.parse_html_file(element)

    def list_files(self):
        html_files = glob.glob('**/**.html', recursive=True)
        html_files = [file.replace('\\','/') for file in html_files]

        return html_files

    def parse_html_file(self, filename):
        soup = bs4.BeautifulSoup(open(filename, 'r', encoding='utf-8'), 'html.parser')
        st = soup.title
        ogst = st.string
        try:
            st.string = self.title_dict[filename]
            newst = st.string
            print('\nChanged title for {} from {} to {}'.format(filename, ogst, newst))
            with open(filename, 'wb') as f:
                f.write(soup.prettify('utf-8'))
        except KeyError:
            pass


if __name__ == '__main__':
    TitleChanger()
