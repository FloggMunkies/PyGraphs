import json, operator

ops = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt
}


def cmp(arg1, op, arg2):
    operation = ops.get(op)
    return operation(arg1, arg2)


class json_handler:
    def __init__(self, file, init_dict):
        self.file = file
        self.init_dict = init_dict

    def overwrite_json(self, new_data):
        with open(self.file, "w") as outfile:
            json.dump(new_data, outfile)

    def reset_json(self):
        self.overwrite_json(self.init_dict)

    def append_json(self, new_dict):
        data = self.get_json()

        # convert data to list if not
        if type(data) is dict:
            data = [data]

        # append new item to data list
        data.append(new_dict)

        # write list to file
        with open(self.file, "w") as outfile:
            json.dump(data, outfile)

    def add_node_blank(self):
        index = self.get_node_total()
        new_node = self.init_dict
        for key in new_node:
            new_node[key] = ""
        new_node["node"] = index
        self.append_json(new_node)

    def add_node(self, **kwargs):
        index = self.get_node_total()
        self.add_node_blank()
        self.edit_node(index, **kwargs)

    def get_json(self):
        return json.load(open(self.file))

    def get_node(self, node):
        return self.get_json()[node]

    def get_node_total(self):
        data = self.get_json()
        if type(data) is dict:
            return 1
        return len(data)

    def edit_node(self, node, **kwargs):
        """
        Copies node dict and edits it, then copies the json list, and overwrites the specific node dict,
        and overwrites the json  file
        :param node: index of which node you are editing (Integer)
        :param kwargs: new dictionary key, value pairs
        :return:
        """
        node_data = self.get_node(node)
        for key, value in kwargs.items():
            if key in self.init_dict.keys():
                node_data[key] = value
            else:
                print("WARNING: ", key, " is not in ", self.init_dict.keys())

        json_data = self.get_json()
        json_data[node] = node_data
        self.overwrite_json(json_data)

    def save_json(self, filename):
        data = self.get_json()
        with open(filename, "w") as outfile:
            json.dump(data, outfile)

    def load_json(self, filename):
        self.overwrite_json(json.load(open(filename)))

    def print_node(self, node, labels=True, *args):
        node_data = self.get_node(node)
        temp = []
        if not args:
            args = list(self.init_dict.keys())
        for arg in args:
            if arg in self.init_dict.keys():
                if labels:
                    temp.append([arg, node_data[arg]])
                else:
                    temp.append(node_data[arg])
        print(temp)

    def print_nodes_filtered(self, labels=True, *args, **kwargs):
        data = self.get_json()
        for node_dict in data:
            if all(cmp(node_dict[k], "==", v) for k, v in kwargs.items()):
                print(node_dict)

    def get_nodes_filtered(self, labels=True, print_flag=False, **kwargs):
        data = self.get_json()
        temp = []
        for node_dict in data:
            if all(cmp(node_dict[k], "==", v) for k, v in kwargs.items()):
                temp.append(node_dict)
                if print_flag:
                    print(node_dict)
        return temp

    def mass_edit_nodes(self, labels=True, *args, **kwargs):
        node_list = self.get_nodes_filtered(labels=labels, print_flag=True, **kwargs)
        try:
            node_id = int(input("Which node to edit? "))
        except ValueError:
            node_id = -1
        index = self.find(node_list, "node", node_id)
        while index > 0:
            k = input(list(self.init_dict.keys()))
            while k not in self.init_dict.keys():
                k = input(list(self.init_dict.keys()))
            v = input(str(node_list[index][k]) + " : ")
            new_data = {k: v}
            self.edit_node(node_id, **new_data)
            self.print_node(node_id)
            node_list = self.get_nodes_filtered(labels=labels, print_flag=True, **kwargs)
            try:
                node_id = int(input("Which node to edit? "))
            except ValueError:
                node_id = -1
            index = self.find(node_list, "node", node_id)

    def find(self, lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1




# class Graph:
#     def __init__(self):
#         self.node_list = []
#         self.node_dict = {}
#         self.adj_list = {}
#
#     def add_node(self, node, name):
#         if node not in self.node_list:
#             self.node_list.append(node)
#             self.node_dict[node] = name
#         else:
#             print("Node ", node, " already exists!")
#
#     def add_edge(self, node1, node2, weight):
#         temp = []
#         if node1 in self.node_list and node2 in self.node_list:
#             if node1 not in self.adj_list:
#                 temp.append([node2, weight])
#                 self.adj_list[node1] = temp
#
#             elif node1 in self.adj_list:
#                 temp.extend(self.adj_list[node1])
#                 temp.append([node2, weight])
#                 self.adj_list[node1] = temp
#
#         else:
#             print("Nodes don't exist!")
#
#     def print_adj(self, verbose=False):
#         if verbose:
#             for node in self.adj_list:
#                 temp = []
#                 for edge in self.adj_list[node]:
#                     temp.append([edge[0], self.node_dict[edge[0]], edge[1]])
#                 print(node, " ", self.node_dict[node], " ---> ", temp)
#         else:
#             for node in self.adj_list:
#                 print(node, " ---> ", self.adj_list[node])

init_node_dict = {
    "node": 0,
    "name": "Test",
    "area": "Test",
    "open": False,
    "items": 0,
    "items_collected": 0,
    "edges": []
}

foo = json_handler("test.json", init_node_dict)
foo.load_json("saved_map.json")
# foo.mass_edit_nodes(False, area="Central Plaza")

# TODO
# Use filtered print to correct mistakes with wrong area assignments
# Add edges


# for node in foo.get_json():
#     print(node)
#     x = input("name: ")
#     if x:
#         foo.edit_node(node["node"], name=x)
#     else:
#         print("No Changes")

# Adds area
# for i in range(52):
#     if i <= 11:
#         foo.add_node(area="Main Gate")
#     if 11 < i <= 21:
#         foo.add_node(area="Central Plaza")
#     if 21 < i <= 32:
#         foo.add_node(area="Below Plaza")
#     if 32 < i <= 34:
#         foo.add_node(area="Forever Forest Entrance")
#     if 34 < i <= 39:
#         foo.add_node(area="Train Station")
#     if 39 < i <= 45:
#         foo.add_node(area="Residential Area")
#     if 45 < i <= 52:
#         foo.add_node(area="Harbor")

# Create Graph
#
# graph = Graph()
#
# # Adding nodes
# graph.add_node(0, "Outside Toad Town")
# graph.add_node(1, "Main Gate")
# graph.add_node(2, "Mario's House")
# graph.add_node(3, "Central Plaza")
# graph.add_node(4, "Castle Ruins")
# # Adding edges
# graph.add_edge(0, 1, 1)
# graph.add_edge(1, 0, 1)
# graph.add_edge(1, 2, 1)
# graph.add_edge(2, 1, 1)
# graph.add_edge(1, 3, 1)
# graph.add_edge(3, 1, 1)
# graph.add_edge(3, 4, 1)
# graph.add_edge(4, 3, 1)
#
#
# # Printing the graph
# graph.print_adj(verbose=True)
#
# # Printing the adjacency list
# print(graph.adj_list)

# with open("game_map.json", "r") as openfile:
#     json_object = json.load(openfile)
#
# for node in json_object:
#     print(node["node"], " ", node["area"], " ---> ", node["edges"])
#
# with open("check_map.json", "r") as openfile:
#     json_object = json.load(openfile)
#
# for node in json_object:
#     print(node["node"], " ", node["name"], " ---> ", node["edges"])
