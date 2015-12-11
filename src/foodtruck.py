from httplib2 import Http
from bs4 import BeautifulSoup


class FoodTruckFiesta:
    soup = None

    def __init__(self):
        h = Http()
        resp, content = h.request("http://foodtruckfiesta.com/dc-food-truck-list/")
        self.soup = BeautifulSoup(content, 'html5lib')

    def get_truck_list(self, location="DC - Metro Center"):

        list_start = None
        for h2 in self.soup.find_all('h2'):
            if h2.text.find(location) != -1:
                list_start = h2
                break
        if list_start is None:
            return None

        links = []

        next_elm = list_start.next_sibling
        while next_elm.name != 'h2':
            if hasattr(next_elm, 'descendants') and next_elm.descendants is not None:
                links = links + [d for d in next_elm.descendants if d.name == 'a']
            next_elm = next_elm.next_sibling


        def remove_style(link):
            for d in link.descendants:
                try:
                    d['style'] = ''
                except Exception:
                    pass
            return link
        links = map(remove_style, links)
        return links
