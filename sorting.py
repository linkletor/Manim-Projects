from manim import *

class BubbleSort(Scene):
    def construct(self):
        # Create a list of numbers to sort
        numbers = [4, 2, 7, 1, 5, 3]
        
        # Create rectangles to represent the numbers
        rectangles = VGroup(*[Rectangle(height=num, width=0.5, fill_opacity=0.8, color=BLUE) for num in numbers])
        rectangles.arrange(RIGHT, buff=0.2)
        
        # Add labels to the rectangles
        labels = VGroup(*[Text(str(num)).move_to(rect) for num, rect in zip(numbers, rectangles)])
        
        # Add the entire group to the scene
        self.play(Create(rectangles), Write(labels))
        
        # Bubble sort animation
        for i in range(len(numbers)):
            for j in range(len(numbers) - i - 1):
                # Highlight the two rectangles being compared
                self.play(rectangles[j].animate.set_color(RED), rectangles[j+1].animate.set_color(RED))
                
                if numbers[j] > numbers[j+1]:
                    # Swap the numbers
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    
                    # Animate the swap
                    self.play(
                        rectangles[j].animate.move_to(rectangles[j+1]),
                        rectangles[j+1].animate.move_to(rectangles[j]),
                        labels[j].animate.move_to(rectangles[j+1]),
                        labels[j+1].animate.move_to(rectangles[j])
                    )
                    
                    # Update the rectangles and labels groups
                    rectangles[j], rectangles[j+1] = rectangles[j+1], rectangles[j]
                    labels[j], labels[j+1] = labels[j+1], labels[j]
                
                # Reset the color of the compared rectangles
                self.play(rectangles[j].animate.set_color(BLUE), rectangles[j+1].animate.set_color(BLUE))
        
        # Final animation to show the sorted list
        self.play(rectangles.animate.set_color(GREEN))
        self.wait(2)
        