import math
from circleCollider import *


class CollisionChecker:
    def circleCircleCheckCollsion(self,circle1: CircleCollider, circle2: CircleCollider) -> bool:
        distance = math.sqrt(math.pow((circle1.x - circle2.x),2) + math.pow((circle1.y - circle2.y),2))
        radiusSum = circle1.radius + circle2.radius
        if distance <= radiusSum:
            return True
        else:
            return False
        
    def circleCircleResolve(self,c1: CircleCollider, c2: CircleCollider):
        distanceX = c1.x - c2.x
        distanceY = c1.y - c2.y
        radiusSum = c1.radius + c2.radius
        length = math.sqrt(distanceX*distanceX + distanceY * distanceY)
        unitX = distanceX / length
        unitY = distanceY / length

        c1.x = c2.x + (radiusSum ) * unitX
        c1.y = c2.y + (radiusSum ) * unitY
         