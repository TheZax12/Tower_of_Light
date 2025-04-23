import pygame

from log.LogObserver import LogObserver
from entities.player.Player import Player
from entities.player.Inventory import Inventory

from UI.Colors import *


class LogPanel(LogObserver):
    
    def __init__(self, x, y, width, height, title_font, message_font):
        self.rect = pygame.Rect(x, y, width, height)
        self.message_font = message_font
        self.line_height = self.message_font.get_height() + 4

        self.title_font = title_font
        self.title_font.set_bold(True)
        self.title_height = self.title_font.get_height()
        
        self.logs = []

        self.background_color = background_color
        self.text_color = (0, 0, 0)
        self.border_color = border_color
        
        self.scroll_offset = 0 
        self.last_scroll_time = pygame.time.get_ticks()
        self.fade_delay = 2000
        self.fade_duration = 1000
        self.fade_min = 50
        self.dragging_scrollbar = False
        self.scrollbar_drag_offset = 0
        self.header_section_height = 0

    def update_log(self, log_event: str):
        wrapped_lines = self.wrap_text(log_event, self.rect.width - 20)
        self.logs.extend(wrapped_lines)

        self.scroll_offset = 0

    def wrap_text(self, text, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " "
            if self.message_font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        
        return lines
    
    def log_scrolling(self, events):
        transcript_title_height = self.title_font.get_height() + 15
        transcript_area_start_y_abs = self.rect.top + self.header_section_height + transcript_title_height
        available_height_for_lines = self.rect.bottom - transcript_area_start_y_abs - 5

        if available_height_for_lines < self.line_height:
            visible_lines = 0
            scrollbar_height = 0
            max_scroll_transcript = 0
        else:
            visible_lines = available_height_for_lines // self.line_height
            scrollbar_height = available_height_for_lines
            max_scroll_transcript = max(0, len(self.logs) - visible_lines)

        scrollbar_width = 10
        scrollbar_x = self.rect.right - scrollbar_width - 2
        scrollbar_y_abs = transcript_area_start_y_abs

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if max_scroll_transcript > 0 and scrollbar_height > 0:
                        thumb_height = max(20, (visible_lines / len(self.logs)) * scrollbar_height) if len(self.logs) > 0 else scrollbar_height
                        current_scroll_transcript = max(0, min(self.scroll_offset, max_scroll_transcript))
                        fraction = 1 - (current_scroll_transcript / max_scroll_transcript) if max_scroll_transcript > 0 else 1
                        thumb_y_abs = scrollbar_y_abs + (fraction * (scrollbar_height - thumb_height))
                        thumb_rect = pygame.Rect(scrollbar_x, thumb_y_abs, scrollbar_width, thumb_height)

                        if thumb_rect.collidepoint(mouse_x, mouse_y):
                            self.dragging_scrollbar = True
                            self.scrollbar_drag_offset = mouse_y - thumb_y_abs
                            self.last_scroll_time = pygame.time.get_ticks()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging_scrollbar = False
                    
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging_scrollbar and max_scroll_transcript > 0 and scrollbar_height > 0:
                    mouse_y = event.pos[1]
                    thumb_height = max(20, (visible_lines / len(self.logs)) * scrollbar_height) if len(self.logs) > 0 else scrollbar_height
                    
                    new_thumb_y_abs = mouse_y - self.scrollbar_drag_offset
                    new_thumb_y_abs = max(scrollbar_y_abs, min(new_thumb_y_abs, scrollbar_y_abs + scrollbar_height - thumb_height))
                    
                    new_thumb_y_rel = new_thumb_y_abs - scrollbar_y_abs
                    
                    track_movable_height = scrollbar_height - thumb_height
                    fraction = new_thumb_y_rel / track_movable_height if track_movable_height > 0 else 0
                    
                    self.scroll_offset = int((1 - fraction) * max_scroll_transcript)
                    self.scroll_offset = max(0, min(self.scroll_offset, max_scroll_transcript))
                    self.last_scroll_time = pygame.time.get_ticks()

            elif event.type == pygame.MOUSEWHEEL:
                scroll_amount = event.y * 3
                self.scroll_offset += scroll_amount
                self.scroll_offset = max(0, min(self.scroll_offset, max_scroll_transcript))
                self.last_scroll_time = pygame.time.get_ticks()

    def render_transcript(self, display_surface: pygame.Surface, y_offset: int):
        script_title = "~ ~ ~ ~ ~ ~ ~ TRANSCRIPT ~ ~ ~ ~ ~ ~ ~"
        transcript_title_surface = self.title_font.render(script_title, True, self.text_color)
        transcript_title_x = self.rect.left + (self.rect.width - transcript_title_surface.get_width()) // 2
        transcript_title_y = self.rect.top + y_offset + 5
        display_surface.blit(transcript_title_surface, (transcript_title_x, transcript_title_y))
        title_section_height = transcript_title_surface.get_height() + 5
        
        transcript_lines_start_y = self.rect.top + y_offset + title_section_height
        available_height_for_lines = self.rect.bottom - transcript_lines_start_y - 5

        if available_height_for_lines < self.line_height:
            return

        visible_lines = available_height_for_lines // self.line_height
        start = max(0, len(self.logs) - visible_lines - self.scroll_offset)
        end = start + visible_lines

        scrollbar_width = 10
        scrollbar_x = self.rect.right - scrollbar_width - 2
        scrollbar_y = transcript_lines_start_y
        scrollbar_height = available_height_for_lines
        track_color = (200, 200, 200)
        thumb_color = (100, 100, 100)
        
        current_time = pygame.time.get_ticks()
        time_since_scroll = current_time - self.last_scroll_time
        if time_since_scroll < self.fade_delay:
            alpha = 255
        elif time_since_scroll < self.fade_delay + self.fade_duration:
            alpha = max(self.fade_min, int(255 * (1 - (time_since_scroll - self.fade_delay) / self.fade_duration)))
        else:
            alpha = self.fade_min

        if alpha > 0:
            scrollbar_surf = pygame.Surface((scrollbar_width, scrollbar_height), pygame.SRCALPHA)
            scrollbar_surf.fill((*track_color, alpha))
            total_lines = len(self.logs)

            max_scroll_transcript = max(0, total_lines - visible_lines) 
            current_scroll_transcript = max(0, min(self.scroll_offset, max_scroll_transcript))

            if total_lines > visible_lines:
                thumb_height = max(20, (visible_lines / total_lines) * scrollbar_height)
                fraction = 1 - (current_scroll_transcript / max_scroll_transcript) if max_scroll_transcript > 0 else 1 
                thumb_y_rel = fraction * (scrollbar_height - thumb_height)
                pygame.draw.rect(scrollbar_surf, (*thumb_color, alpha),
                                 (0, thumb_y_rel, scrollbar_width, thumb_height))
            display_surface.blit(scrollbar_surf, (scrollbar_x, scrollbar_y))
        
        y = transcript_lines_start_y
        for line in self.logs[start:end]:
            text_surface = self.message_font.render(line, True, self.text_color)
            display_surface.blit(text_surface, (self.rect.left + 10, y))
            y += self.line_height

    def render_player_stats(self, display_surface: pygame.Surface, player: Player) -> int:
        stats_title = "~ ~ ~ ~ ~ ~ PLAYER STATS ~ ~ ~ ~ ~ ~"
        title_surface = self.title_font.render(stats_title, True, self.text_color)
        title_x = self.rect.left + (self.rect.width - title_surface.get_width()) // 2
        title_y = self.rect.top + 5
        display_surface.blit(title_surface, (title_x, title_y))
        
        stats_string = player.player_stats()
        stats_lines = []
        if isinstance(stats_string, str):
            stats_lines = stats_string.strip().split('\n')
        else:
            stats_lines = ["Stats unavailable"]

        current_y = title_y + title_surface.get_height() + 5

        for line in stats_lines:
            stats_surface = self.message_font.render(line, True, self.text_color)
            stats_x = self.rect.left + 10
            display_surface.blit(stats_surface, (stats_x, current_y))
            line_height = self.message_font.get_linesize() 
            current_y += line_height

        return current_y + 5
    
    def render_inventory_contents(self, display_surface: pygame.Surface, inventory: Inventory, start_y: int) -> int:
        inventory_title = "~ ~ ~ ~ ~ ~ ~ INVENTORY ~ ~ ~ ~ ~ ~ ~"
        title_surface = self.title_font.render(inventory_title, True, self.text_color)
        title_x = self.rect.left + (self.rect.width - title_surface.get_width()) // 2
        title_y = start_y
        display_surface.blit(title_surface, (title_x, title_y))

        inventory_string = inventory.inventory_contents()
        inventory_lines = []
        if isinstance(inventory_string, str):
            inventory_lines = inventory_string.strip().split('\n')
        else:
            inventory_lines = ["Inventory unavailable"]

        current_y = title_y + title_surface.get_height() + 5

        for line in inventory_lines:
            inventory_surface = self.message_font.render(line, True, self.text_color)
            inventory_x = self.rect.left + 10
            display_surface.blit(inventory_surface, (inventory_x, current_y))
            line_height = self.message_font.get_linesize()
            current_y += line_height

        return current_y + 5

    def draw(self, display_surface: pygame.Surface, player: Player, inventory: Inventory):
        pygame.draw.rect(display_surface, self.background_color, self.rect)
        pygame.draw.rect(display_surface, self.border_color, self.rect, 1)
        
        stats_end_y = self.render_player_stats(display_surface, player)
        inventory_end_y = self.render_inventory_contents(display_surface, inventory, stats_end_y)
        
        self.header_section_height = inventory_end_y - self.rect.top

        self.render_transcript(display_surface, y_offset=self.header_section_height)