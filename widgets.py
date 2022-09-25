import pygame, arrow
from gui_settings import *


class Widget(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs.get("id")
        self.text_string = kwargs.get("text")
        self.text = None
        self.color = kwargs.get("color")
        self.rect = kwargs.get("rect")
        self.name = kwargs.get("name")
        self.selected = False
        self.handler = kwargs.get("handler")

        if self.id is None:
            self.id = 0
        if self.rect is None:
            self.image = pygame.Surface((8, 8))
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.Surface((self.rect.width, self.rect.height))

        if self.color is None:
            self.color = COLOR_WIDGET
        if self.text_string is None:
            self.text_string = ""

        self.image.fill(self.color)

        # Text is rendered in reference to Widget.Rect so it needs to come after Rect changes
        self.font_name = "freesansbold.ttf"
        self.font_size = 8
        self.font = pygame.font.Font(self.font_name, self.font_size)
        if self.text_string:
            self.text = self.font.render(self.text_string, True, COLOR_TEXT, None)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = self.rect.center

    def draw(self, surface: 'pygame surface'):
        if self.selected:
            self.image.fill(COLOR_SELECTED)
        else:
            self.image.fill(self.color)
        surface.blit(self.image, self.rect.topleft)
        if self.text:
            surface.blit(self.text, self.text_rect)

    def click(self):
        pass

    def update_text(self, text_string=None, font_name=None, font_size=None, color=None, max_font_size=96,
                    width_buffer=0, height_buffer=0, x_offset=0, y_offset=0):
        new_color = COLOR_TEXT
        if text_string:
            self.text_string = text_string
        if font_size:
            self.font_size = font_size
        if font_name:
            self.font_name = font_name
        if color:
            new_color = color
        self.font = pygame.font.Font(self.font_name, self.font_size)
        # if self.text_string:
        self.text = self.font.render(self.text_string, True, new_color, None)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
        self.text_rect.x += x_offset
        self.text_rect.y += y_offset

        # If font_size unspecified, maximize
        if font_size:
            return
        # self.update_text(font_size=max_font_size)
        # if self.text_string:
        test_font = pygame.font.Font(self.font_name, max_font_size)
        text = test_font.render(self.text_string, True, new_color, None)
        text_rect = text.get_rect()
        text_width = test_font.size(self.text_string)[0]
        text_height = test_font.size(self.text_string)[1]
        available_width = self.rect.width - width_buffer - x_offset
        available_height = self.rect.height - height_buffer - y_offset
        j = 0
        while (text_width >= available_width) or (text_height >= available_height):
            j += 2
            test_font = pygame.font.Font(self.font_name, max_font_size - j)
            text = test_font.render(self.text_string, True, new_color, None)
            text_rect = text.get_rect()
            text_width = test_font.size(self.text_string)[0]
            text_height = test_font.size(self.text_string)[1]
            available_width = self.rect.width - width_buffer - x_offset
            available_height = self.rect.height - height_buffer - y_offset
        self.font_size = max_font_size - j
        self.__update_text(text_string=text_string, font_name=font_name, font_size=self.font_size, color=color,
                           max_font_size=max_font_size, width_buffer=width_buffer, height_buffer=height_buffer,
                           x_offset=x_offset, y_offset=y_offset)

    # https://stackoverflow.com/questions/6846829/override-recursive-method-in-python
    # something to do with it being a recursive AND overwritten method
    __update_text = update_text


class Node(Widget):
    def __init__(self, graph=None, **kwargs):
        super().__init__(text="Default", **kwargs)
        self.graph = graph

        # Get kwargs
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.area = kwargs.get("area")
        self.settings_required = kwargs.get("settings_required")
        self.items = kwargs.get("items")

        # Assign default values if no kwargs
        if self.id is None:
            self.id = 0
        if self.name is None:
            self.name = "Default"
        if self.area is None:
            self.area = "Default"
        if self.settings_required is None:
            self.settings_required = []
        if self.items is None:
            self.items = 0

        # update Text
        self.text_string = str(self.id)
        self.text = self.font.render(self.text_string, True, COLOR_TEXT, None)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def update(self):
        pass

    def delete(self):
        pass

    def add_edge(self, other_node, **kwargs):
        pass


# Depreciated

# class Edge(Widget):
#     def __init__(self, graph=None, **kwargs):
#         super().__init__(**kwargs)
#         self.graph = graph
#
#         self.weight = kwargs.get("weight")
#         self.nodes = kwargs.get("nodes")
#
#         if self.weight is None:
#             self.weight = 1
#
#         if self.nodes:
#             self.start_pos = self.nodes[0].rect.center
#             self.end_pos = self.nodes[1].rect.center
#
#             self.rect.centerx = (self.nodes[0].rect.centerx + self.nodes[1].rect.centerx) / 2
#             self.rect.centery = (self.nodes[0].rect.centery + self.nodes[1].rect.centery) / 2
#
#     def draw(self, surface):
#         super().draw(surface)
#
#         if self.nodes:
#             self.start_pos = self.nodes[0].rect.center
#             self.end_pos = self.nodes[1].rect.center
#             self.rect.centerx = (self.nodes[0].rect.centerx + self.nodes[1].rect.centerx) / 2
#             self.rect.centery = (self.nodes[0].rect.centery + self.nodes[1].rect.centery) / 2
#             # pygame.draw.line(surface, COLOR_EDGE, self.start_pos, self.end_pos)
#             a = pygame.Vector2(self.start_pos)
#             b = pygame.Vector2(self.end_pos)
#             # print(math.acos(a*b/(a.magnitude() * b.magnitude())))
#             arrow.draw_arrow(surface, a, b, COLOR_EDGE, 2, 10, 10)
#             # arrow.draw_arrow(screen, pygame.Vector2(self.start_pos), pygame.Vector2(x, y), COLOR_EDGE, 2, 10, 10)
#
#     def delete(self):
#         print("Deleting ", self, self.id)
#         self.handler.remove_widget(self)


# class Edge(Widget):
#     def __init__(self, start_pos, end_pos, weight=1, color=COLOR_EDGE, **kwargs):
#         super().__init__(**kwargs)
#         self.weight = weight
#         self.color = color
#         self.body_width = kwargs.get("body_width")
#         self.head_width = kwargs.get("head_width")
#         self.head_height = kwargs.get("head_height")
#         self.start_pos = pygame.Vector2(start_pos)
#         self.end_pos = pygame.Vector2(end_pos)
#
#     def update(self):
#         pass
#
#     def draw(self, surface):
#         arrow.draw_arrow(surface, self.start_pos, self.end_pos, self.color)


class Button(Widget):
    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        self.parent = parent
        assert type(self.parent) == WidgetManager, "Parent should be WidgetManager instance"
        self.font = pygame.font.Font('freesansbold.ttf', 24)

    def update(self):
        pass


class ModeButton(Button):
    def __init__(self, parent, mode, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.mode = mode
        assert self.mode in self.parent.mode_list, "mode needs to be in WidgetManager.mode_list"
        self.font = pygame.font.Font('freesansbold.ttf', 24)

    def click(self):
        self.parent.change_mode(self.mode)


class Textbox(Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        assert type(self.parent) == WidgetManager, "Parent should be WidgetManager instance"
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.label_text = kwargs.get("label_text")
        if not self.label_text:
            self.label_text = "Default:"
        print(self.label_text)
        self.label = self.font.render(self.label_text, True, COLOR_TEXT, None)
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center

    def update(self):
        pass

    def click(self):
        self.selected = True
        self.parent.selected_widgets.append(self)

    def update_text(self, text_string=None, font_name=None, font_size=None, color=None, max_font_size=96,
                    width_buffer=0, height_buffer=0, x_offset=0, y_offset=0):
        # print(self.font_size)
        super(Button, self).update_text(width_buffer=60, y_offset=16)
        self.label_rect = self.label.get_rect()
        self.label_rect.left = self.rect.left
        self.label_rect.top = self.rect.top

    def draw(self, surface):
        super(Button, self).draw(surface)
        surface.blit(self.label, self.label_rect)


class WidgetManager(object):
    def __init__(self, surface):
        self.widget_list = []
        self.button_list = []
        self.edge_list = []
        self.graph = None
        self.surface = surface
        self.id_count = 0

        # widget types
        self.widget_types = ["node", "button"]

        # Widget attributes
        self.widget_attributes = [
            "text",
            "color",
            "rect"
        ]

        # Which widgets are currently selected
        self.selected_widgets = []

        self.mode_list = [
            "create node",
            "create edge",
            "edit",
            "delete",
            "move"
        ]

        self.mode = "create node"

        # Text in bottom right corner displaying current mode
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.text = self.font.render(self.mode, True, COLOR_TEXT, None)
        self.text_rect = self.text.get_rect()
        self.text_box = pygame.Surface((self.text_rect.width, self.text_rect.height))
        self.text_box_rect = self.text_box.get_rect()
        self.change_mode(self.mode)

        # Create Edge Line variables
        self.start_pos = []

    def change_mode(self, new_mode):
        self.mode = new_mode
        # Stop Create Edge line from rendering
        self.start_pos = []
        # Update text in lower right corner
        self.text = self.font.render(self.mode, True, COLOR_TEXT, None)
        self.text_rect = self.text.get_rect()
        self.text_rect.x = SCREEN_WIDTH - self.text_rect.width
        self.text_rect.y = SCREEN_HEIGHT - self.text_rect.height
        self.text_box = pygame.Surface((self.text_rect.width, self.text_rect.height))
        self.text_box_rect = self.text_box.get_rect()
        self.text_box_rect.x = SCREEN_WIDTH - self.text_box_rect.width
        self.text_box_rect.y = SCREEN_HEIGHT - self.text_box_rect.height
        self.text_box.fill(COLOR_WIDGET)

    def draw(self, surface=None):
        if surface is None:
            surface = self.surface
        for widget in self.widget_list:
            widget.draw(surface)
        for edge in self.edge_list:
            arrow.draw_arrow(surface, edge[0], edge[1], color=COLOR_EDGE)

        # Draw line when creating edge
        if self.start_pos:
            pygame.draw.line(surface, COLOR_EDGE, self.start_pos, pygame.mouse.get_pos())

        # Draw Mode Textbox
        surface.blit(self.text_box, self.text_box_rect)
        surface.blit(self.text, self.text_rect)

    def update(self):
        for widget in self.widget_list:
            widget.update()

        self.update_edges()

        match self.mode:
            case "move":
                mouse_pos = pygame.mouse.get_pos()

                for widget in self.selected_widgets:
                    widget.rect.centerx = mouse_pos[0]
                    widget.rect.centery = mouse_pos[1]
                    widget.text_rect.centerx = mouse_pos[0]
                    widget.text_rect.centery = mouse_pos[1]

    def remove_widget(self, widget):
        self.widget_list.remove(widget)
        # widget.delete()

    def add_widget(self, widget_type, **kwargs):
        id = self.id_count
        widget = None
        if not isinstance(widget_type, str):
            print(widget_type, "is not a string.")
            return
        match widget_type.lower():
            case "node":
                self.create_node(id=id, **kwargs)
                self.id_count += 1
            case "edge":
                # self.create_edge(id=id, **kwargs)
                # self.id_count += 1
                print("Widget Manager method add_widget Not implemented for create edge")
                pass
            case "button":
                widget = Button(id=id, parent=self, **kwargs)
                self.button_list.append(widget)
                self.update_buttons()
                self.id_count += 1
                print("Button created")
            case "textbox":
                widget = Textbox(id=id, parent=self, **kwargs)
                self.button_list.append(widget)
                self.update_buttons()
                self.id_count += 1
                print("Textbox created")
            case "mode button":
                mode = kwargs.get("mode")
                if mode:
                    del kwargs["mode"]
                    widget = ModeButton(id=id, parent=self, mode=mode, **kwargs)
                    self.button_list.append(widget)
                    self.update_buttons()
                    print("Mode Button Created: ", mode)
                    self.id_count += 1
            case unknown_command:
                print(unknown_command, " does not match any widget types.")
                return
        if widget:
            self.widget_list.append(widget)
        # for widget in self.widget_list:
        #     print(widget.id)

    def create_node(self, **kwargs):
        new_node = Node(graph=self.graph, **kwargs)
        self.graph.add_node(new_node, **kwargs)
        self.widget_list.append(new_node)

    def create_edge(self, node0, node1, **kwargs):
        self.graph.add_edge(node0, node1, **kwargs)
        node0.add_edge(node1, **kwargs)

        directed = kwargs.get("directed")
        if directed:
            return
        node1.add_edge(node0, **kwargs)

    def add_edge(self, node, weight=1, directed=True):
        # Only select Nodes
        if type(node) is not Node:
            return
        # First Node clicked, add to selected and get start_pos for edge drawing
        if len(self.selected_widgets) == 0:
            self.selected_widgets.append(node)
            self.start_pos = [node.rect.centerx, node.rect.centery]
        # Second Node clicked, add to selected, create edge, update nodes edges, clear selected widgets
        if len(self.selected_widgets) == 1:
            if node not in self.selected_widgets:
                self.selected_widgets.append(node)
                self.create_edge(self.selected_widgets[0], self.selected_widgets[1], weight=weight, directed=directed)
                self.clear_selected_widgets()

    def get_clicked(self, mouse_pos):
        return [s for s in self.widget_list if s.rect.collidepoint(mouse_pos)]

    def update_buttons(self):
        # Grab all buttons and sort them by ID
        dic = {}
        for button in self.button_list:
            dic[button] = button.id
        dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
        sorted_buttons = dic.keys()

        # Move and Reshape each button to fill the buffer zone, in ID order
        n = len(sorted_buttons)
        width = BUFFER_WIDTH / n
        height = BUFFER_HEIGHT
        for i, button in enumerate(sorted_buttons):
            l = i * width
            t = 0
            w = width - 8
            h = height
            button.image = pygame.Surface((w, h))
            button.rect = pygame.Rect(l, t, w, h)
            button.image.fill(button.color)
            # maximize font size based on size of button
            button.update_text()
            # if button.text_string:
            #     text_width = button.font.size(button.text_string)[0]
            #     j = 0
            #     while text_width >= w:
            #         j += 2
            #         button.update_text(font_size=96-j)
            #         text_width = button.font.size(button.text_string)[0]

    def left_click(self):
        mouse_pos = pygame.mouse.get_pos()

        # Perform Click method on each widget clicked on, Unselecting any buttons not clicked
        clicked_widgets = self.get_clicked(mouse_pos)
        for button in self.button_list:
            button.selected = False
            if button in self.selected_widgets:
                self.selected_widgets.remove(button)
        for widget in clicked_widgets:
            widget.click()


        # Perform functions based on Mode
        match self.mode:
            case "create node":
                # Create new node, unless clicking on existing widget
                if not clicked_widgets:
                    self.add_widget("node", color=COLOR_NODE,
                                    rect=pygame.Rect(mouse_pos[0] - 16, mouse_pos[1] - 16, 32, 32))
            case "edit":
                pass
            case "create edge":
                # Clicking on Node creates edge, clicking anything else clears selected_widgets
                if len(clicked_widgets):
                    for widget in clicked_widgets:
                        if type(widget) == Node:
                            self.add_edge(widget)
                        else:
                            self.clear_selected_widgets()
                else:
                    self.clear_selected_widgets()
            case "move":
                # Selects widget to move
                if len(clicked_widgets):
                    for widget in clicked_widgets:
                        if type(widget) == Node:
                            self.selected_widgets = [widget]
                        else:
                            self.clear_selected_widgets()
                else:
                    self.clear_selected_widgets()

            case "delete":
                for widget in clicked_widgets:
                    # Deleting Node, delete the node itself, and all edges connected to it
                    if type(widget) == Node:

                        # Undirected
                        edges = self.graph.edges([widget])
                        # directed
                        # edges = nx.edges(self.graph, [widget])

                        for edge in list(edges):
                            self.graph.remove_edge(edge[0], edge[1])

                        # Todo same thing with edges do with neighbors edges for directed graph case

                        self.graph.remove_node(widget)
                        self.remove_widget(widget)

    def left_click_release(self):
        mouse_pos = pygame.mouse.get_pos()

        match self.mode:
            case "move":
                self.selected_widgets = []

    def clear_selected_widgets(self):
        self.selected_widgets = []
        self.start_pos = []

    def update_edges(self):
        self.edge_list = []
        for edge in self.graph.edges.data():
            start_pos = pygame.Vector2(edge[0].rect.centerx, edge[0].rect.centery)
            end_pos = pygame.Vector2(edge[1].rect.centerx, edge[1].rect.centery)
            self.edge_list.append([start_pos, end_pos])

    def test(self):
        self.update_edges()

    def keydown(self, event):
        for widget in self.selected_widgets:
            if True:  # if type(widget) is not Edge:
                if event.key == pygame.K_RETURN:
                    self.selected_widgets = []
                elif event.key == pygame.K_BACKSPACE:
                    widget.text_string = widget.text_string[:-1]
                else:
                    widget.text_string += event.unicode
                widget.update_text()
