import pygame
import colors


def main_menu_handler(self):
    if self.buttons[0].state == "pressed":
        self.delete_objects()
        self.last_platform_height = 0

        self.create_jumper()
        self.create_plato()
        self.first_platforms_layer()
        self.create_stats_trackers()

        self.game_over = False
        self.game_state = "Play"
        return

    # Settings
    if self.buttons[1].state == "pressed":
        self.delete_objects()

        self.create_menu_settings()

        self.game_state = "Menu_settings"

    # Exit
    if self.buttons[2].state == "pressed":
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        return


def playing_game_handler(self):
    if self.jumper.game_over:
        self.jumper.game_over = False
        # action
        self.game_lost()
        self.game_lost_time = self.time + 0
        self.game_over = True

    if not self.game_over:
        plat_was_jumped = 0
        plat = self.jumper.collision_check(self.platforms)
        if plat is not None:
            plat.color = colors.RED1
            plat_was_jumped = 1
        height_dif = self.camera_chasing()

        self.update_points(height_dif, plat_was_jumped)

        if self.tracking_platform.top >= 0:
            self.another_platforms()
    else:
        self.game_lost_pause()


def menu_settings_handler(self):
    # Sound
    if self.buttons[0].state == "pressed":
        pass

    # Difficulty
    if self.buttons[1].state == "pressed":
        pass

    # Back
    if self.buttons[2].state == "pressed":
        self.delete_objects()

        self.create_menu()

        self.game_state = "Menu_main"