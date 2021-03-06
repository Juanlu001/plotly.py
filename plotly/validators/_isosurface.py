import _plotly_utils.basevalidators


class IsosurfaceValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='isosurface', parent_name='', **kwargs):
        super(IsosurfaceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Isosurface'),
            data_docs=kwargs.pop(
                'data_docs', """
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            caps
                plotly.graph_objs.isosurface.Caps instance or
                dict with compatible properties
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                `value`) or the bounds set in `cmin` and `cmax`
                Defaults to `false` when `cmin` and `cmax` are
                set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as `value` and if
                set, `cmin` must be set as well.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as `value` and if
                set, `cmax` must be set as well.
            colorbar
                plotly.graph_objs.isosurface.ColorBar instance
                or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)', [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            contour
                plotly.graph_objs.isosurface.Contour instance
                or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            flatshading
                Determines whether or not normal smoothing is
                applied to the isosurfaces, creating
                isosurfaces with an angular, low-poly look via
                flat reflections.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                plotly.graph_objs.isosurface.Hoverlabel
                instance or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            isomax
                Sets the maximum boundary for iso-surface plot.
            isomin
                Sets the minimum boundary for iso-surface plot.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                plotly.graph_objs.isosurface.Lighting instance
                or dict with compatible properties
            lightposition
                plotly.graph_objs.isosurface.Lightposition
                instance or dict with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            slices
                plotly.graph_objs.isosurface.Slices instance or
                dict with compatible properties
            spaceframe
                plotly.graph_objs.isosurface.Spaceframe
                instance or dict with compatible properties
            stream
                plotly.graph_objs.isosurface.Stream instance or
                dict with compatible properties
            surface
                plotly.graph_objs.isosurface.Surface instance
                or dict with compatible properties
            text
                Sets the text elements associated with the
                vertices. If trace `hoverinfo` contains a
                "text" flag and "hovertext" is not set, these
                elements will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            uid
                Assign an id to this trace, Use this to provide
                object constancy between traces during
                animations and transitions.
            uirevision
                Controls persistence of some user-driven
                changes to the trace: `constraintrange` in
                `parcoords` traces, as well as some `editable:
                true` modifications such as `name` and
                `colorbar.title`. Defaults to
                `layout.uirevision`. Note that other user-
                driven trace attribute changes are controlled
                by `layout` attributes: `trace.visible` is
                controlled by `layout.legend.uirevision`,
                `selectedpoints` is controlled by
                `layout.selectionrevision`, and
                `colorbar.(x|y)` (accessible with `config:
                {editable: true}`) is controlled by
                `layout.editrevision`. Trace changes are
                tracked by `uid`, which only falls back on
                trace index if no `uid` is provided. So if your
                app can add/remove traces before the end of the
                `data` array, such that the same trace has a
                different index, you can still preserve user-
                driven changes if you give each trace a `uid`
                that stays with it as it moves.
            value
                Sets the 4th dimension (value) of the vertices.
            valuesrc
                Sets the source reference on plot.ly for  value
                .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the X coordinates of the vertices on X
                axis.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the Y coordinates of the vertices on Y
                axis.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the Z coordinates of the vertices on Z
                axis.
            zsrc
                Sets the source reference on plot.ly for  z .
"""
            ),
            **kwargs
        )
