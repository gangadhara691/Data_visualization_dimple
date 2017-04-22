    // Copyright: 2015 AlignAlytics
    // License: "https://github.com/PMSI-AlignAlytics/dimple/blob/master/MIT-LICENSE.txt"
    // Source: /src/methods/_drawMarkers.js
    dimple._postDrawHandling = function (series, updated, removed, duration) {
        // Run after transition methods
        if (duration === 0) {
            updated.each(function (d, i) {
                if (series.afterDraw) {
                    series.afterDraw(this, d, i);
                }
            });
            removed.remove();
        } else {
            updated.on("end", function (d, i) {
                if (series.afterDraw) {
                    series.afterDraw(this, d, i);
                }
            });
            removed.call(function () {
                if (series.shapes) {
                    series.shapes.exit().remove();
                }
            });
        }
    };
