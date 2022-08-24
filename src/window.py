import pygame

from dataclasses import dataclass, field

@dataclass
class Window:
    screen: pygame.Surface = field(
        init = False
    )
    
    width: int = field(
        default = 800
    )
    
    height: int = field(
        default = 800
    )
    
    caption: str = field(
        default = "N BODY SIMULATION"
    )
    
    def __post_init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.main_font = pygame.font.SysFont("arial", 25)
        self.lost_font = pygame.font.SysFont("arial", 50)
        pygame.display.set_caption(self.caption)
   
    def render_pixels(self, resource: pygame.image, position: tuple[float, float]) -> None:
        self.screen.blit(resource, position)
        
    def render_text(
        self,
        text: str, 
        position: tuple, 
        font: pygame.font.SysFont, 
        centre: bool = False
    ) -> None:
        text_surface = font.render(text, True, (255., 255., 255.))
        if centre:
            position = (
                position[0] - text_surface.get_width() >> 1, 
                position[1] - text_surface.get_height() >> 1
            )
        self.screen.blit(text_surface, position)
        
        