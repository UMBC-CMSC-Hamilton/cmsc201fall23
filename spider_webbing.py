"""
    spider webbing for the purpose of learning a bit about how to do the recursions in the project 3.

    The code I present is not the only way to do this kind of thing, but it's essentially what I want you to understand
        and be able to reproduce during the coding of the project.
"""

import random


def spider_web(web_map, starting_place, destination):
    """
        this is a helper function that sets the visited to false for all of the nodes in the spider web and then
        calls the spider web recursive function that does the search.
    :param web_map: this is the
    :param starting_place: the place where we start in the spider web
    :param destination: the destination we are trying to reach
    :return: the path that comes out of the actual searching recursive function
    """
    visited = {}
    for place in web_map:
        visited[place] = False

    return spider_web_rec(web_map, starting_place, destination, visited)


def spider_web_rec(web_map, starting_place, destination, visited):
    """
        This is the function that does the majority of the work here. The web_map is a dictionary of lists which
            has the nodes plus the

    :param web_map:
    :param starting_place: the name of the starting node
    :param destination: the name of the destination node
    :param visited: the visited dictionary, initially set to false but we'll set each node to true
    :return: the path if it exists, the path is a list of the nodes
    """
    path = []  # set the path to empty at first, this will contain the path from the current place that we start to the end.

    if starting_place == destination:  # if we've reached the end, then begin constructing the path from the back.
        return [destination]
    # setting the visited to true so we don't loop back.
    visited[starting_place] = True

    """
        here we need to loop through all of the places connected to the current node (which we consider the starting node)
            we use a for loop to scan through all of the possible destinations
        Then check if they're visited first before going.  You could also check once you get there which we do at the 
            top of the function, just for safety.  
        Finally we get the returned path, which is whatever the path is up to our current starting node.  If the path
            exists then that means that we've found a way to go.  If the path doesn't exist that means it was a dead
            end and we have to keep searching.  
        Thus, we check if path, meaning if it's not empty, or a dead end.  If it's not we return it.
            Remember that returning the path here exits the for loop and the function. Technically we could
            search for other paths, but as soon as we find the first path we exit.               
    """
    for next_place in web_map[starting_place]:
        if not visited[next_place]:
            path = spider_web_rec(web_map, next_place, destination, visited)
            if path:
                return [starting_place] + path

    visited[starting_place] = False
    # essentially this will return if no path is found, i.e. we still have  path = []
    return path


def make_spider_web(num_nodes, seed=0):
    """
        This code generates the spider web, technically you don't need to understand it in order to
            do the project, or this problem.
    """
    if seed:
        random.seed(seed)

    web_map = {}

    for i in range(1, num_nodes + 1):
        web_map[f'Node {i}'] = []

    for i in range(1, num_nodes + 1):
        sample = random.sample(list(range(i, num_nodes + 1)), random.randint(1, num_nodes - i + 1))
        for x in sample:
            if i != x:
                web_map[f'Node {i}'].append(f'Node {x}')
                web_map[f'Node {x}'].append(f'Node {i}')
    return web_map


if __name__ == '__main__':
    num_nodes, seed = [int(x) for x in input('Input num_nodes, seed: ').split(',')]
    the_web = make_spider_web(num_nodes, seed)
    print(the_web)
    path = spider_web(the_web, 'Node 1', f'Node {num_nodes}')
    print(path)
