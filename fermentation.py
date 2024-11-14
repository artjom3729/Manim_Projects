from manim import *
from chanim import *

myChemTemplate = TexTemplate(
                    tex_compiler="latex",   
                    output_format='.dvi',
                    preamble=r"""
                        \usepackage{amsmath}
                        \usepackage{amssymb}
                        \usepackage{chemfig}
                        \setchemfig{atom sep=2em,angle increment=45,bond offset=2pt,double bond sep=2pt}
                    """
                    )

npa = Tex(
        r"\chemfig{*6(-=(-(=[-2]O)-[:30]O(-[-2]H))-(-(=[2]O)-[:-30]O(-[2]H))=(-NO_2)-=)}",
        tex_template=myChemTemplate
        ).set_stroke(width=3)

print(npa)
print(npa[0])
print(npa[0][0])
print(npa[0][1])
print(npa[0][2])

class Fermentation(Scene):
    def construct(self):

        # Define the molecules involved in glycolysis
        glucose = Tex(
            r"\chemfig[cram width=2pt]{HO-[2,0.5,2]?<[7,0.7](-[2,0.5]OH)-[,,,,line width=2pt](-[6,0.5]OH)>[1,0.7](-[6,0.5]OH)-[3,0.7]O-[4]?(-[2,0.3]-[3,0.5]OH)}",
            tex_template=myChemTemplate
        ).scale(2).set_stroke(width=3)

        ATP = Tex(
            r"""\chemfig{O=[:49.5]P(-[:274.5,,,1]O^{-})(-[:132]O-[:192]P(-[:274.5,,,1]O^{-})(%
                -[:132]O-[:192]P(-[:132,,,2]^{-}O)(-[:192,,,2]^{-}O)=[:252]O)=[:229.5]O)-[:12]O%
                -[:312]>[:12]-[:318](<:[:264,,,1]OH)-[:30](<:[:336,,,1]OH)-[:102](-[:174]O%
                -[:246])<[:48]N-[:102]-[:30](-[:318]N=_[:246]-[:174]\phantom{N})=^[:90](%
                -[:30,,,1]NH_2)-[:150]N=^[:210]-[:270]N(=^[:330])}""",
            tex_template=myChemTemplate
        ).scale(2).set_stroke(width=3)

        phosphate = Tex(
            r"\chemfig{^{-}O-[:60,,2]P(=[:330]O)(-[:150,,,2]^{-}O)-[:60]O^{-}}",
            tex_template=myChemTemplate
        ).scale(2).set_stroke(width=3)

        npa = Tex(
            r"\chemfig{*6(-=(-(=[-2]O)-[:30]O(-[-2]H))-(-(=[2]O)-[:-30]O(-[2]H))=(-NO_2)-=)}",
            tex_template=myChemTemplate
        ).set_stroke(width=3)

        self.play(Write(npa))

        hydrazine = (
            Tex(
            r"\chemfig{N(-[3]H)(-[-3]H)-N(-[1]H)(-[-1]H)}",
            tex_template=myChemTemplate).set_stroke(width=3)
            .move_to(npa)
            .shift(2 * RIGHT)
            .scale(0.85)
        )

        self.play(
            npa.animate.shift(LEFT * 2),
            Write(hydrazine),
        )

        self.play(
            Rotate(hydrazine, angle=TAU / 4, run_time=0.5),
        )

        print(hydrazine)
        print(hydrazine[0])
        print(hydrazine[0][0])

        self.play(hydrazine.animate.shift(LEFT))
        self.play(
            Rotate(hydrazine[0][0], -PI / 2),
            Rotate(hydrazine[0][1], -PI / 2),
            Rotate(hydrazine[0][3], -PI / 2),
            Rotate(hydrazine[0][5], -PI / 2),
            Rotate(hydrazine[0][7], -PI / 2),
            Rotate(hydrazine[0][9], -PI / 2),
            Transform(
                hydrazine[0][8], hydrazine[0][10].copy().scale(1.25).shift(LEFT * 1.25)
            ),
            Transform(
                hydrazine[0][2], hydrazine[0][4].copy().scale(1.25).shift(LEFT * 1.25)
            ),
        )
        self.wait(2)

        water_grp_1 = VGroup(
            npa[0][16],
            npa[0][18],
            npa[0][19],
            hydrazine[0][7],
            hydrazine[0][8],
        )

        water_grp_2 = VGroup(
            npa[0][7],
            npa[0][9],
            npa[0][10],
            hydrazine[0][1],
            hydrazine[0][2],
        )
        self.play(FadeOut(water_grp_1, shift=UP), FadeOut(water_grp_2, shift=DOWN))

        hydrazine = VGroup(
            hydrazine[0][0],
            hydrazine[0][3],
            hydrazine[0][4],
            hydrazine[0][5],
            hydrazine[0][6],
            hydrazine[0][9],
            hydrazine[0][10],
        )

        self.play(hydrazine.animate.shift(LEFT * 1.5))

        self.wait()