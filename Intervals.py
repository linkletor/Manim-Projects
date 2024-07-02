from manim import*

class Interval(Scene):
    def construct(self):
        inequality = MathTex(r" \frac{2^x-2}{(x+1)^3} \geqslant 0")
        inequality.to_edge(UP,buff=1)
        solution = MathTex(r" \frac{x-1}{x+1} \geqslant 0")
        solution.next_to(inequality,DOWN)
        self.play(Write(inequality),run_time=3)
        self.wait()
        self.play(TransformFromCopy(inequality,solution))
        self.wait()

        arrow = Arrow(3*LEFT ,3*RIGHT, tip_length = 0.2,buff=0).set_stroke(YELLOW,2)
        dot_1 = Dot(LEFT , color=BLACK).set_stroke(YELLOW,2)
        dot_2 = Dot(RIGHT , 0.09, color = YELLOW).set_stroke(BLACK,2)
        number_line = VGroup(arrow , dot_1 ,dot_2).shift(DOWN)
        self.play(Create(number_line),run_time=3)
        self.wait()

        label = MathTex("-1", "1", "x")
        label[0].next_to(dot_1,DOWN)
        label[1].next_to(dot_2,DOWN)
        label[2].next_to(arrow,DOWN)
        label[2].align_to(arrow , RIGHT)
        signs = MathTex("+","-","+").arrange(buff=1.5)
        signs.next_to(arrow,UP,buff=0.15)
        self.play(FadeIn(label,shift = UP),lag_ration =0.5,run_time=2)
        self.wait()
        self.play(FadeIn(signs, shift=DOWN),lag_ration =0.5,run_time=2)
        self.wait()
        answer = Tex(r"Answer:$(-\infty;-1)"+r"\cup[1;+\infty]$",color = MAROON_B)
        answer.to_edge(DOWN,buff=1)
        self.play(Write(answer),run_time=3)
        self.wait(3)
        
