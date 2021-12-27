from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

PATH = 'C:\Program Files (x86)\chromedriver.exe'
MAX_GENERATIONS = 3

GOOGLE = "https://www.google.com"
SEARCH_XPATH = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"


def get_relative(name, relative_type):
    relative_name = None
    if (name):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(PATH, options=option)
        driver.get(GOOGLE)
        search = driver.find_element_by_xpath(SEARCH_XPATH)
        search.send_keys(f"{name} {relative_type}")
        search.send_keys(Keys.RETURN)
        try:
            relative_elem = driver.find_element_by_class_name('FLP8od')
            relative_name = relative_elem.text
        except:
            pass
        driver.close()
    return relative_name


class Person:
    def __init__(self, name, max_generations=1, gen=1):
        if (name == ''):
            name = None
        self.name = name
        self.gen = gen
        if gen < max_generations and name != None:
            self.mother = Person(get_relative(
                name, "mother"), max_generations, gen + 1)
            self.father = Person(get_relative(
                name, "father"), max_generations, gen + 1)
        else:
            self.mother = None
            self.father = None


class FamilyTree:
    def __init__(self, name, generations):
        self.root = Person(name, generations)
        self.generations = generations

    @staticmethod
    def generate_JSON_tree(person):
        tree = {'father': 'None', 'person': 'None',
                'generation': 'None', 'mother': 'None'}
        if(person):
            tree['father'] = FamilyTree.generate_JSON_tree(person.father)
            tree['person'] = person.name
            tree['generation'] = person.gen
            tree['mother'] = FamilyTree.generate_JSON_tree(person.mother)
        return tree

    def generate_JSON_file(self):
        json_tree = FamilyTree.generate_JSON_tree(self.root)
        with open(f"JSONFamilyTrees/{self.root.name}_{self.generations}Gen_Family_Tree.json", "w+") as fp:
            json.dump(json_tree, fp)

    @staticmethod
    def print_family(person):
        if (person):
            FamilyTree.print_family(person.father)
            print(f"Gen: {person.gen}, Name: {person.name}")
            FamilyTree.print_family(person.mother)

    def print_family_tree(self):
        FamilyTree.print_family(self.root)


def main():
    tree = FamilyTree("Cristiano Ronaldo", MAX_GENERATIONS)
    tree.print_family_tree()


if __name__ == '__main__':
    main()
