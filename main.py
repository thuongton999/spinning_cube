import pygame
import matrices
import settings

pygame.init()


WIDTH, HEIGHT = 300, 300
scale = 300
angle = 0
distance = 5
speed = 0.02

frame = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPINNING CUBE")
pygame.mouse.set_visible(False)

def connectPoints(index, points, screen, color, size=2):
  point1 = points[index[0]]
  point2 = points[index[1]]
  pygame.draw.line(screen, color, (point1[0], point1[1]), (point2[0], point2[1]), size)
    

class Cube():
  def __init__(self):
    self.showPoints = True
    self.showEdges = True

    self.points = [
      [[-1], [-1], [1]],
      [[1], [-1], [1]],
      [[1], [1], [1]],
      [[-1], [1], [1]],
      [[-1], [-1], [-1]],
      [[1], [-1], [-1]],
      [[1], [1], [-1]],
      [[-1], [1], [-1]]
    ]

  def renderCube(self, screen, position, angle, distance, scale):
    rotationX = matrices.rotationX(angle)
    rotationY = matrices.rotationY(angle)
    rotationZ = matrices.rotationZ(angle)

    renderedPoints = [0]*len(self.points)
    index = 0
    for point in self.points:
      rotated2D = matrices.matrixMultiplication(rotationX, point)
      rotated2D = matrices.matrixMultiplication(rotationY, rotated2D)
      rotated2D = matrices.matrixMultiplication(rotationZ, rotated2D)

      z = 1/(distance - rotated2D[2][0])

      renderedMatrix = [[z, 0, 0], [0, z, 0]]
      rendered2D = matrices.matrixMultiplication(renderedMatrix, rotated2D)

      x = int(rendered2D[0][0] * scale) + position[0]
      y = int(rendered2D[1][0] * scale) + position[1]
      renderedPoints[index] = [x, y]

      index += 1
      if self.showPoints:
        pygame.draw.circle(screen, settings.colors["DARKGREY"], (x, y), 3)

    if self.showEdges:
      for m in range(4):
        connectPoints([m, (m+1)%4], renderedPoints, screen, settings.colors["DARKGREY"])
        connectPoints([m+4, (m+1)%4 + 4], renderedPoints, screen, settings.colors["DARKGREY"])
        connectPoints([m, m+4], renderedPoints, screen, settings.colors["DARKGREY"])

if __name__ == "__main__":
  cube = Cube()
  spinning = True
  while spinning:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        spinning = False

    screen.fill(settings.colors["VERYLIGHTGREY"])

    cube.renderCube(screen, [WIDTH // 2, HEIGHT // 2], angle, distance, scale)

    angle += speed

    pygame.display.update()
    frame.tick(FPS)
