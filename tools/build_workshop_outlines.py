"""Generate vector outlines and matching hit masks for the 1920x1080 workshop.

Paths trace the visible objects in bg_workshop.jpg. Run this script after editing
the paths; keep the bounds in sync with workshop_regions in hub_screens.rpy.
Only SVG assets are written; the background artwork is not modified.
"""

from pathlib import Path


REGIONS = {
    "sortie": ((493, 511, 302, 241), """
        M 523,565 L 645,528 Q 652,526 663,529 L 719,539
        L 726,631 L 774,681 Q 778,687 772,695
        L 623,746 Q 618,748 612,743 L 580,714 L 574,688
        L 538,675 Q 531,672 530,662 Z
    """),
    "repair": ((459, 190, 267, 214), """
        M 499,296 L 534,288 L 524,220 Q 527,217 533,220
        L 543,285 L 548,284 L 540,222 Q 546,218 551,221 L 558,282
        L 571,279 L 563,230 Q 568,228 572,231 L 579,279
        L 583,277 L 577,231 Q 583,228 588,231 L 594,276
        L 601,274 L 594,235 Q 598,232 603,235 L 610,273
        L 613,272 L 607,236 Q 612,232 616,236 L 622,272
        L 632,271 L 629,246 Q 633,242 638,246 L 641,272
        L 667,274 L 673,280 L 674,310 L 616,326
        L 618,354 L 613,357 L 610,328 L 587,335
        L 590,369 L 585,372 L 581,337 L 551,345
        L 557,386 L 552,389 L 545,347
        Q 531,350 530,340 L 528,330 L 506,326 L 499,317 Z
    """),
    "diary": ((20, 802, 280, 149), """
        M 26,887 L 126,817 L 286,829 Q 294,830 289,838
        L 279,848 L 293,869 L 249,903
        Q 244,892 227,893 Q 196,889 176,909
        Q 169,918 172,940 L 42,934 Q 27,934 25,919 Z
    """),
}


def main():
    output = Path(__file__).resolve().parents[1] / "game/images/ui/workshop"
    output.mkdir(parents=True, exist_ok=True)
    for name, ((x, y, width, height), path) in REGIONS.items():
        path = " ".join(path.split())
        header = (f'<svg xmlns="http://www.w3.org/2000/svg" '
                  f'width="{width}" height="{height}" '
                  f'viewBox="{x} {y} {width} {height}">\n')
        outline = (
            f'  <path d="{path}" fill="none" stroke="#14202a" '
            'stroke-opacity="0.5" stroke-width="5" stroke-linejoin="round"/>\n'
            f'  <path d="{path}" fill="none" stroke="#ffffff" '
            'stroke-width="2.5" stroke-linejoin="round"/>\n'
        )
        mask = f'  <path d="{path}" fill="#ffffff"/>\n'
        for suffix, content in (("outline", outline), ("mask", mask)):
            (output / f"{name}_{suffix}.svg").write_text(
                header + content + "</svg>\n", encoding="utf-8"
            )


if __name__ == "__main__":
    main()
