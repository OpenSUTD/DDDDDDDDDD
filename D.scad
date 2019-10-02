// Basic intro to OpenSCAD :)

linear_extrude(2)
    for (i=[0:9])
        translate([10*i,10*sin(i*40)])
            text("D", valign="center");