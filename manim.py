from manim import*

class Fermat(Scene): 
    def construct(self):  
        # Однобуквенные заглавные переменные — двойное нарушение.
        # Но если очень хочется — можно. 

        # Основные объекты
        A = Dot(3 * UL)
        B = Dot(2 * UR + RIGHT)
        P = Dot(LEFT)        
        line = Line(4 * LEFT, 4 * RIGHT).set_stroke(BLUE, 2)               
        AP = always_redraw(lambda:
            Line(A.get_center(), P.get_center())
        )
        BP = always_redraw(lambda:
            Line(B.get_center(), P.get_center())
        )
        # Симметричные точки и отрезки
        A_sym = Dot(3 * DL)
        line_sym = DashedLine(A_sym, A)
        right_angle = RightAngle(line, line_sym, 0.3)  
        right_angle.set_stroke(BLUE, 2)  
        AP_sym = always_redraw(lambda:
            Line(A_sym.get_center(), P.get_center())
        ) 
        # Лейблы
        label = MathTex("A", "B", "l", "A'").scale(0.75)
        label[0].next_to(A, UL, buff=0.1)
        label[1].next_to(B, UR, buff=0.1)
        label[2].next_to(4 * RIGHT, UL, buff=0.1)  
        label[3].next_to(A_sym, DL, buff=0.1)        
        label_P = always_redraw(
            lambda: MathTex("P")
                .scale(0.75)
                .next_to(P, UP, buff=0.15)
        )  
        # Анимация задачи
        self.play(
            AnimationGroup(
                Create(line),
                GrowFromCenter(A),
                GrowFromCenter(B),
                lag_ratio=1
            )
        )
        self.play(
            Create(AP),
            Create(BP),
            Create(P),
            run_time=3
        )
        self.play(
            Write(label[:-1]),
            GrowFromCenter(label_P),
            run_time=2
        )
        self.wait()
        self.play(
            P.animate.shift(3 * RIGHT),
            rate_func=there_and_back,
            run_time=6
        )
        self.wait()   
        
        # Симметричные построения
        self.play(
            AnimationGroup(
                Create(line_sym),
                GrowFromCenter(A_sym),
                GrowFromCenter(label[-1]),
                Create(right_angle),
                lag_ratio=0.2,
                run_time=2
            )
        )        
        self.play(Create(AP_sym), run_time=1.5)
        self.play(
            P.animate.shift(3 * RIGHT),            
            rate_func=there_and_back,
            run_time=6
        )
        self.wait()

        # Ответ
        shortest_way = Line(A_sym.get_center(), 
            B.get_center()).set_stroke(YELLOW, 3)
        self.play(Create(shortest_way), run_time=2)
        self.play(P.animate.shift(1.6 * RIGHT), run_time=3)
        self.wait(3)