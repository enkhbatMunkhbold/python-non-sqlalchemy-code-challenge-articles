class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name') and len(name):
            self._name = name
        else:
            raise Exception

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author == self})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = list({magazine.category for magazine in self.magazines()})
        if len(areas):
            return areas
        else:
            return None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            raise Exception

    @classmethod
    def top_publisher(cls):
        publishings = {}
        for article in Article.all:
            if article.magazine not in publishings:
                publishings[article.magazine] = 1
            else:
                publishings[article.magazine] += 1        

        if len(publishings):
            return max(publishings, key=lambda k: publishings[k])
        else:
            return None
            

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if len(titles):
            return titles
        else:
            return None

    def contributing_authors(self):
        authors = []
        top_contributors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)
            else:
                top_contributors.append(article.author)
        if len(top_contributors):
            return top_contributors
        else:
            return None
