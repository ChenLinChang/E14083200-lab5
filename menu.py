import pygame
import os
import math

MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
SELL_IMAGE=pygame.image.load(os.path.join("images","sell.png"))
UPGRADE_IMAGE=pygame.image.load(os.path.join("images","upgrade.png"))

Menu_size=(200,230)
upgrade_size=(70,50)
sell_size=(40,40)

class UpgradeMenu:
    def __init__(self, x, y):
        self.menu = pygame.transform.scale(MENU_IMAGE, Menu_size)
        self.upgrade = pygame.transform.scale(UPGRADE_IMAGE, upgrade_size)
        self.sell = pygame.transform.scale(SELL_IMAGE, sell_size)

        self.rect = self.menu.get_rect()
        self.rect_upgrade = self.upgrade.get_rect()
        self.rect_sell = self.sell.get_rect()

        self.rect.center = (x, y)
        self.rect_upgrade.center = (x, y - 85)
        self.rect_sell.center = (x, y + 85)

        self.__buttons = [Button(UPGRADE_IMAGE,"upgrade",self.rect.centerx,self.rect.centery-85),Button(SELL_IMAGE,"sell",self.rect.centerx,self.rect.centery+85)]
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu,self.rect)
        # draw button
        win.blit(self.upgrade,self.rect_upgrade) #畫出upgrade
        win.blit(self.sell, self.rect_sell) #畫出sell

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """

        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """

        return True if self.rect.collidepoint(x, y) else False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






