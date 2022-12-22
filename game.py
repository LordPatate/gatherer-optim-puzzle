import pygame
from asyncio import sleep, create_task, run

import const
from ai import AI
from stuff import Hero, Item
from utils import dist

pygame.init()

window = pygame.display.set_mode((const.WINDOW_W, const.WINDOW_H))
window.fill(const.WHITE)

heroSpr = pygame.Surface((const.HERO_W, const.HERO_H))
heroSpr.fill(const.BLUE)

itemSpr = pygame.Surface((const.ITEM_W, const.ITEM_H))
itemSpr.fill(const.RED)


origin = ((const.WINDOW_W - const.HERO_W) / 2,
          (const.WINDOW_H - const.HERO_H) / 2)
hero = Hero(origin)
world = Item.generate(const.ITEM_AMOUNT)


async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        task = create_task(sleep(0.01))

        pygame.draw.rect(window, const.WHITE, pygame.Rect(
            hero.pos, (const.HERO_W, const.HERO_H)))
        for item in world:
            pygame.draw.rect(window, const.WHITE, pygame.Rect(
                item.pos, (const.ITEM_W, const.ITEM_H)))

        # UPDATE
        action = AI.update(hero, world)
        if action.actionType == action.MOVE:
            hero.toward(action.dest)
        elif action.actionType == action.PICK:
            hero.pick(world)
        elif action.actionType == action.DROP:
            hero.bag.clear()

        for item in hero.bag:
            if dist(item.pos, hero.pos) >= const.LEASH_LENGTH:
                item.toward(hero.pos)

        # BLITTING
        window.blit(heroSpr, hero.pos)
        for item in world:
            window.blit(itemSpr, item.pos)

        pygame.display.flip()
        await task

run(main())

pygame.display.quit()
