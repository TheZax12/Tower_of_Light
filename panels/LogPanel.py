import pygame

from log.LogObserver import LogObserver

from UI.Colors import *


class LogPanel(LogObserver):
    
    def __init__(self, x, y, width, height, title_font, message_font):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = message_font
        self.line_height = self.font.get_height() + 4

        self.title_text = "~~~~~~~ TRANSCRIPT ~~~~~~~"
        self.title_font = title_font
        self.title_font.set_bold(True)
        self.title_height = self.title_font.get_height() + 4
        
        self.logs = []
        self.scroll_offset = 0

        self.background_color = background_color
        self.text_color = (0, 0, 0)
        self.border_color = border_color

        self.last_scroll_time = pygame.time.get_ticks()
        self.fade_delay = 2000
        self.fade_duration = 1000
        self.fade_min = 50
        self.dragging_scrollbar = False
        self.scrollbar_drag_offset = 0

    def update_log(self, log_event: str):
        wrapped_lines = self.wrap_text(log_event, self.rect.width - 20)
        self.logs.extend(wrapped_lines)

        if self.scroll_offset == 0:
            self.scroll_offset = 0

    def wrap_text(self, text, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " "
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        
        return lines
    
    def max_scroll(self):
        visible_lines = (self.rect.height - self.title_height) // self.line_height
        return max(0, len(self.logs) - visible_lines)

    def log_scrolling(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    scrollbar_width = 10
                    scrollbar_x = self.rect.right - scrollbar_width - 2
                    scrollbar_y = self.rect.top + self.title_height + 5
                    scrollbar_height = self.rect.height - self.title_height - 10
                    visible_lines = (self.rect.height - self.title_height - 5) // self.line_height
                    total_lines = len(self.logs)
                    if total_lines > visible_lines:
                        thumb_height = max(20, (visible_lines / total_lines) * scrollbar_height)
                        max_scroll_value = self.max_scroll()
                        fraction = 1 - (self.scroll_offset / max_scroll_value) if max_scroll_value > 0 else 1
                        thumb_y = fraction * (scrollbar_height - thumb_height)
                        thumb_rect = pygame.Rect(scrollbar_x, scrollbar_y + thumb_y, scrollbar_width, thumb_height)
                        if thumb_rect.collidepoint(mouse_x, mouse_y):
                            self.dragging_scrollbar = True
                            self.scrollbar_drag_offset = mouse_y - (scrollbar_y + thumb_y)
                            self.last_scroll_time = pygame.time.get_ticks()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging_scrollbar = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging_scrollbar:
                    mouse_y = event.pos[1]
                    scrollbar_y = self.rect.top + self.title_height + 5
                    scrollbar_height = self.rect.height - self.title_height - 10
                    visible_lines = (self.rect.height - self.title_height - 5) // self.line_height
                    total_lines = len(self.logs)
                    if total_lines > visible_lines:
                        max_scroll_value = self.max_scroll()
                        thumb_height = max(20, (visible_lines / total_lines) * scrollbar_height)
                        new_thumb_y = mouse_y - self.scrollbar_drag_offset - scrollbar_y
                        new_thumb_y = max(0, min(new_thumb_y, scrollbar_height - thumb_height))
                        fraction = new_thumb_y / (scrollbar_height - thumb_height)
                        self.scroll_offset = int((1 - fraction) * max_scroll_value)
                        self.last_scroll_time = pygame.time.get_ticks()
            elif event.type == pygame.MOUSEWHEEL:
                self.scroll_offset += event.y
                self.scroll_offset = max(0, min(self.scroll_offset, self.max_scroll()))
                self.last_scroll_time = pygame.time.get_ticks()
    
    def draw(self, display_surface: pygame.Surface):
        pygame.draw.rect(display_surface, self.background_color, self.rect)
        pygame.draw.rect(display_surface, self.border_color, self.rect, 1)

        title_surface = self.title_font.render(self.title_text, True, self.text_color)
        title_x = self.rect.left + (self.rect.width - title_surface.get_width()) // 2
        title_y = self.rect.top + 5
        display_surface.blit(title_surface, (title_x, title_y))

        visible_lines = (self.rect.height - self.title_height - 5) // self.line_height
        start = max(0, len(self.logs) - visible_lines - self.scroll_offset)
        end = start + visible_lines

        scrollbar_width = 10
        scrollbar_x = self.rect.right - scrollbar_width - 2
        scrollbar_y = self.rect.top + self.title_height + 5
        scrollbar_height = self.rect.height - self.title_height - 10
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
            if total_lines > visible_lines:
                thumb_height = max(20, (visible_lines / total_lines) * scrollbar_height)
                max_scroll_value = self.max_scroll()
                fraction = 1 - (self.scroll_offset / max_scroll_value) if max_scroll_value > 0 else 1
                thumb_y = fraction * (scrollbar_height - thumb_height)
                pygame.draw.rect(scrollbar_surf, (*thumb_color, alpha),
                                 (0, thumb_y, scrollbar_width, thumb_height))
            display_surface.blit(scrollbar_surf, (scrollbar_x, scrollbar_y))

        y = self.rect.top + self.title_height + 5
        for line in self.logs[start:end]:
            text_surface = self.font.render(line, True, self.text_color)
            display_surface.blit(text_surface, (self.rect.left + 10, y))
            y += self.line_height
